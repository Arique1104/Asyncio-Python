import asyncio
import sys
import pandas as pd
from app.models.user import User 
from app.db.postgres import get_pg_pool, insert_user_pool


async def ingest_csv(path):
    df = pd.read_csv(path)
    pool = await get_pg_pool()

    tasks = []
    for _, row in df.iterrows():
        user = User(**row.to_dict())
        tasks.append(insert_user_pool(pool,user))
    await asyncio.gather(*tasks)
    await pool.close()