import os

import asyncpg


pool: asyncpg.Pool | None = None


async def connect() -> asyncpg.Pool:
    global pool
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        database_url = (
            f"postgres://{os.getenv('PGUSER', 'postgres')}:{os.getenv('PGPASSWORD', '')}"
            f"@{os.getenv('PGHOST', 'localhost')}:{os.getenv('PGPORT', '5432')}"
            f"/{os.getenv('PGDATABASE', 'postgres')}"
        )
    pool = await asyncpg.create_pool(database_url)
    return pool


async def migrate(db_pool: asyncpg.Pool) -> None:
    await db_pool.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT FALSE,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)


async def close() -> None:
    global pool
    if pool:
        await pool.close()
        pool = None
