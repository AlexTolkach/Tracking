import asyncpg

from config import PG_USER, PASSWORD, HOST, PORT


async def create_pool():
    return await asyncpg.create_pool(
        user=PG_USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
