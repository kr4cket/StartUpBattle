import asyncio
import configparser
import threading

from aiogram import Dispatcher
from handlers import conversation_handler
from tgbot.core.TelegramBot import TelegramBot
from tgbot.core.RabbitmqTgbot import RabbitmqTgbot


async def main(parser):
    dp = Dispatcher()
    dp.include_router(conversation_handler.router)

    loop = asyncio.get_event_loop()

    threading.Thread(target=RabbitmqTgbot().listen, args=(loop,)).start()

    await dp.start_polling(TelegramBot().get_bot_instance())

if __name__ == '__main__':
    parser = configparser.ConfigParser()
    parser.read("../settings.ini")
    asyncio.run(main(parser))



