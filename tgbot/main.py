import asyncio
import configparser
import threading

from aiogram import Bot, Dispatcher
from handlers import conversation_handler
from tgbot.core.RabbitmqTgbot import RabbitmqTgbot
from worker.core.RabbitmqWorker import RabbitmqWorker


async def main(parser):

    bot = Bot(token=parser['Bot']["tokenapi"])
    dp = Dispatcher()
    dp.include_router(conversation_handler.router)

    threading.Thread(target=RabbitmqTgbot().listen).start()

    await dp.start_polling(bot)

if __name__ == '__main__':
    parser = configparser.ConfigParser()
    parser.read("../settings.ini")
    asyncio.run(main(parser))
