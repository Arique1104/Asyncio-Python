import pandas as pd
from app.models.user import User
from app.db.postgres import get_pg_conn, insert_user

def ingest_csv_to_pg(path):
    df = pd.read_csv(path)
    conn = get_pg_conn()

    for _, row in df.iterrows():
        try:
            user = User(**row.to_dict())
            # print(f"Prepared user: {user}")
            insert_user(conn, user)
        except Exception as e:
            print(f"Row skipped due to validation error: {e}")

    conn.close()