import asyncio
import pandas as pd
from app.models.user import User
from app.db.postgres import get_pg_pool, insert_user_pool

async def ingest_csv(path):
    df = pd.read_csv(path)
    pool = await get_pg_pool()

    tasks = []
    for _, row in df.iterrows():
        try:
            user = User(**row.to_dict())
            # print(f"Prepared user: {user}")
            tasks.append(insert_user_pool(pool, user))  # ✅ no await here
        except Exception as e:
            print(f"Row skipped due to validation error: {e}")

    await asyncio.gather(*tasks)
    await pool.close()

if __name__ == "__main__":
    import sys
    asyncio.run(ingest_csv(sys.argv[1]))