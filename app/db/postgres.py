import psycopg2
import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()

def get_pg_conn():
    return psycopg2.connect(
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASS"),
        host = os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT")
    )

def insert_user(conn, user):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (id, name, email) VALUES (%s, %s, %s)",
                   (user.id, user.name, user.email)
                   )
        conn.commit()

async def get_pg_pool():
    return await asyncpg.create_pool(
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASS"),
        database=os.getenv("PG_DB"),
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        min_size=1,
        max_size=10
    )
async def insert_user_pool(pool, user):
    async with pool.acquire() as conn: await conn.execute(
        "INSERT INTO users (id,name, email) VALUES ($1, $2, $3)",
        user.id, user.name, user.email
    )