if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    print('Bot online')

    executor.start_polling(dp)
