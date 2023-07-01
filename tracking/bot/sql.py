import asyncio
import asyncpg

from config import NAME, PG_USER, PASSWORD, HOST, PORT


async def create_pool():
    return await asyncpg.create_pool(
        name=NAME,
        user=PG_USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

