import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    pool = await database.connect()
    await database.migrate(pool)
    yield
    await database.close()


app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    rows = await database.pool.fetch(
        "SELECT id, title, completed, created_at FROM todos ORDER BY created_at DESC"
    )
    todos = [dict(row) for row in rows]
    return templates.TemplateResponse("home.html", {"request": request, "todos": todos})


@app.post("/todos", response_class=HTMLResponse)
async def create_todo(request: Request, title: str = Form(...)):
    row = await database.pool.fetchrow(
        "INSERT INTO todos (title) VALUES ($1) RETURNING id, title, completed, created_at",
        title,
    )
    todo = dict(row)
    return templates.TemplateResponse(
        "todo_item.html", {"request": request, "todo": todo}, status_code=201
    )


@app.patch("/todos/{todo_id}/toggle", response_class=HTMLResponse)
async def toggle_todo(request: Request, todo_id: int):
    row = await database.pool.fetchrow(
        "UPDATE todos SET completed = NOT completed WHERE id = $1 RETURNING id, title, completed, created_at",
        todo_id,
    )
    if not row:
        return HTMLResponse(status_code=404, content="Not found")
    todo = dict(row)
    return templates.TemplateResponse("todo_item.html", {"request": request, "todo": todo})


@app.delete("/todos/{todo_id}", response_class=HTMLResponse)
async def delete_todo(todo_id: int):
    await database.pool.execute("DELETE FROM todos WHERE id = $1", todo_id)
    return HTMLResponse(status_code=200, content="")


@app.get("/health")
async def health_check():
    try:
        await database.pool.execute("SELECT 1")
        return JSONResponse({"status": "healthy"})
    except Exception as e:
        return JSONResponse({"status": "unhealthy", "error": str(e)}, status_code=503)


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8080"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
