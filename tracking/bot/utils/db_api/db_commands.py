from aiogram import types
from loader import dp, bot, db, chat_id
from asyncpg import Connection, Record


class DBCommands:
    pool: Connection = db
    # ADD_NEW_USER = "INSERT INTO dataoutput_user(name, last_name) VALUES ($1, $2) RETURNING id"
    COUNT_USERS = "SELECT COUNT(*) FROM dataoutput_user"

    async def count_user(self):
        record: Record = await self.pool.fetchval(self.COUNT_USERS)
        return record


database = DBCommands()
