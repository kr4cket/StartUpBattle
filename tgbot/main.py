import asyncio
from aiogram import Bot, Dispatcher
from handlers import conversation_handler
from core.db_conn import DBConnection
from core.models import *



api = "6295948983:AAHxI8brOC3o0jvaKS2zGvmO4ju8rOvu3Pc"

async def main():

    bot = Bot(token=api)
    dp = Dispatcher()
    dp.include_router(conversation_handler.router)

#   await слушателя в рэбит
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
