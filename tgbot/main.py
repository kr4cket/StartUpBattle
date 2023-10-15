import asyncio
import configparser
from aiogram import Bot, Dispatcher
from handlers import conversation_handler

async def main(parser):

    bot = Bot(token=parser['Bot']["tokenapi"])
    dp = Dispatcher()
    dp.include_router(conversation_handler.router)
    # подключение к рэббит
    await dp.start_polling(bot)

if __name__ == '__main__':
    parser = configparser.ConfigParser()
    parser.read("../settings.ini")
    asyncio.run(main(parser))
