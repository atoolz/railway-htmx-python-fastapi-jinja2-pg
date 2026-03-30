<p align="center">
  <img src="assets/banner.png" alt="HTMX + FastAPI + PostgreSQL Railway Template" width="100%">
</p>

<p align="center">
  <strong>Production-ready HTMX starter with Python, FastAPI, Jinja2, and PostgreSQL. One-click deploy to Railway.</strong>
</p>

<p align="center">
  <a href="https://railway.com/deploy/htmx-fastapi-jinja2-postgres">
    <img src="https://railway.com/button.svg" alt="Deploy on Railway">
  </a>
</p>

<p align="center">
  <a href="https://github.com/atoolz/railway-htmx-python-fastapi-jinja2-pg/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/atoolz/railway-htmx-python-fastapi-jinja2-pg?style=flat-square&color=00c9a7" alt="License">
  </a>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square" alt="Python 3.12">
  <img src="https://img.shields.io/badge/HTMX-2.0.7-3366CC?style=flat-square" alt="HTMX 2.0.7">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square" alt="FastAPI 0.115">
  <img src="https://img.shields.io/badge/PostgreSQL-16-336791?style=flat-square" alt="PostgreSQL">
</p>

<br>

## Deploy and Host HTMX + FastAPI + PostgreSQL Starter on Railway

HTMX + FastAPI + PostgreSQL Starter is a production-ready template for building hypermedia-driven web applications. It combines HTMX for dynamic interactions without JavaScript, Python with FastAPI and Jinja2 for server-side rendering, and PostgreSQL for persistent storage. Deploy in one click and start building.

### About Hosting HTMX + FastAPI + PostgreSQL Starter

The template deploys as a Python application built via multi-stage Dockerfile. It connects to a PostgreSQL instance over Railway's private network using asyncpg with connection pooling. Database migrations run automatically on startup, creating the required tables without manual SQL. The application reads `DATABASE_URL` from environment variables and listens on the port assigned by Railway. A health check endpoint at `/health` pings the database and returns status, ensuring Railway can verify deployments before routing traffic. Tailwind CSS and HTMX load via CDN, so there is no frontend build step.

### Common Use Cases

- Rapid prototyping of server-rendered web apps that need dynamic interactions without the complexity of React, Vue, or other JavaScript frameworks
- Building internal tools, admin panels, and CRUD dashboards where Python's ecosystem and FastAPI's async performance matter but a full SPA is overkill
- Learning HTMX patterns (hx-get, hx-post, hx-swap, hx-target) with a working reference application backed by a real database

### Dependencies for Hosting

- A Railway PostgreSQL database instance (added via the Railway dashboard or CLI)
- The `DATABASE_URL` environment variable set to `${{Postgres.DATABASE_URL}}` on the web service

#### Deployment Dependencies

- [HTMX documentation](https://htmx.org/docs/)
- [FastAPI documentation](https://fastapi.tiangolo.com)
- [Jinja2 templating](https://jinja.palletsprojects.com)
- [asyncpg PostgreSQL driver](https://github.com/MagicStack/asyncpg)

### Why Deploy on Railway?

Railway is a singular platform to deploy your infrastructure stack. Railway will host your infrastructure so you don't have to deal with configuration, while allowing you to vertically and horizontally scale it.

By deploying HTMX + FastAPI + PostgreSQL Starter on Railway, you are one step closer to supporting a complete full-stack application with minimal burden. Host your servers, databases, AI agents, and more on Railway.

<br>

## What's Inside

A complete, working Todo application that demonstrates the full HTMX + FastAPI stack. No JavaScript frameworks, no build steps for the frontend, no client-side state management. Just HTML over the wire.

| Layer | Technology | Role |
|-------|-----------|------|
| **Frontend** | HTMX 2.0.7 + Tailwind CSS | Hypermedia-driven interactions via CDN |
| **Templating** | Jinja2 3.1 | Server-side HTML rendering with template inheritance |
| **Routing** | FastAPI 0.115 | High-performance async Python framework |
| **Database** | PostgreSQL + asyncpg 0.30 | Async connection pooling, prepared statements |
| **Deploy** | Dockerfile (multi-stage) | Python 3.12-slim final image |

<br>

## Why This Stack

**HTMX** lets you build dynamic UIs by returning HTML fragments from the server instead of JSON. No React, no Vue, no bundle. Your FastAPI backend renders HTML, HTMX swaps it into the DOM. The browser does what browsers do best.

**Jinja2** is the standard Python templating engine with template inheritance, macros, and filters. It integrates natively with FastAPI through Starlette's templating support.

**FastAPI** is one of the fastest Python web frameworks with automatic OpenAPI docs, type validation via Pydantic, and native async/await support. It handles the HTTP layer so you focus on your application.

**PostgreSQL** needs no introduction. The asyncpg driver gives you connection pooling and direct access to PostgreSQL-specific features with full async support, no ORM in the way.

<br>

## Project Structure

```
.
├── main.py                    # FastAPI app, routes, middleware
├── database.py                # asyncpg connection pool + auto-migration
├── templates/
│   ├── layout.html            # Base HTML with HTMX + Tailwind CDN
│   ├── home.html              # Home page with todo list
│   └── todo_item.html         # HTMX-powered todo item component
├── requirements.txt           # Python dependencies
└── Dockerfile                 # Multi-stage build (python:3.12-slim)
```

<br>

## HTMX Patterns Demonstrated

The Todo app showcases core HTMX patterns you'll use in real projects:

- **`hx-post` + `hx-target` + `hx-swap="afterbegin"`** - Create items and prepend to list without page reload
- **`hx-patch` + `hx-target` (self)** - Toggle completion with in-place swap
- **`hx-delete` + `hx-swap="outerHTML"`** - Remove items with smooth DOM removal
- **`hx-on::after-request`** - Reset form after successful submission
- **Health check endpoint** - `/health` returns JSON status with DB ping

<br>

## Deploy to Railway

Click the button above or:

1. Fork this repo
2. Create a new project on [Railway](https://railway.com)
3. Add a **PostgreSQL** database
4. Add a service from your forked repo
5. Set the variable: `DATABASE_URL` = `${{Postgres.DATABASE_URL}}`
6. Railway auto-detects the Dockerfile and deploys

The app auto-migrates the database on startup. No manual SQL needed.

<br>

## Local Development

```bash
# Prerequisites: Python 3.12+, PostgreSQL running locally

# Clone and run
git clone https://github.com/atoolz/railway-htmx-python-fastapi-jinja2-pg.git
cd railway-htmx-python-fastapi-jinja2-pg

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set your database URL
export DATABASE_URL="postgres://user:pass@localhost:5432/mydb"

# Run the server
python main.py
```

Open [http://localhost:8080](http://localhost:8080).

<br>

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes | - | PostgreSQL connection string |
| `PORT` | No | `8080` | Server port (Railway sets this automatically) |

<br>

## Part of the HTMX Railway Collection

This is one of 15 HTMX starter templates covering different backend stacks, all following the same pattern and ready for Railway deployment:

| Stack | Status |
|-------|--------|
| Bun + Elysia | Coming soon |
| .NET + Razor | Coming soon |
| Elixir + Phoenix | Coming soon |
| Go + Chi | [Live](https://github.com/atoolz/railway-htmx-go-templ-chi-pg) |
| Go + Echo | [Live](https://github.com/atoolz/railway-htmx-go-templ-echo-pg) |
| Go + Fiber | [Live](https://github.com/atoolz/railway-htmx-go-templ-fiber-pg) |
| Java + Spring Boot (MySQL) | [Live](https://github.com/atoolz/railway-htmx-java-spring-thymeleaf-mysql) |
| Java + Spring Boot (PostgreSQL) | [Live](https://github.com/atoolz/railway-htmx-java-spring-thymeleaf-pg) |
| Node + Express | [Live](https://github.com/atoolz/railway-htmx-node-express-ejs-pg) |
| Node + Hono | [Live](https://github.com/atoolz/railway-htmx-node-hono-jsx-pg) |
| PHP + Laravel | [Live](https://github.com/atoolz/railway-htmx-php-laravel-mysql) |
| Python + Django | [Live](https://github.com/atoolz/railway-htmx-python-django-pg) |
| **Python + FastAPI** | **This repo** |
| Ruby + Rails 8 | [Live](https://github.com/atoolz/railway-htmx-ruby-rails8-pg) |
| Rust + Axum + Askama | [Live](https://github.com/atoolz/railway-htmx-rust-axum-askama-pg) |

<br>

## License

[MIT](LICENSE)

---

<p align="center">
  <sub>Built by <a href="https://github.com/atoolz">AToolZ</a> for the HTMX community</sub>
</p>
