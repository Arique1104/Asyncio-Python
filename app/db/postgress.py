import psycopg2
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