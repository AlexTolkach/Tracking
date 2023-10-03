from config import chat_id


def auth(func):
    async def wrapper(message):
        if message['from']['id'] != int(chat_id):
            return await message.reply('access denied', reply=False)
        return await func(message)

    return wrapper
