import asyncio
import configparser
import core.logger as logger
import threading

from aiogram import Dispatcher
from handlers import conversation_callback_handler
from core.TelegramBot import TelegramBot
from core.RabbitmqTgbot import RabbitmqTgbot


async def main(parser):

    logger.create()
    dp = Dispatcher()
    dp.include_router(conversation_callback_handler.router)

    loop = asyncio.get_event_loop()

    threading.Thread(target=RabbitmqTgbot().listen, args=(loop,)).start()

    await dp.start_polling(TelegramBot().get_bot_instance())

if __name__ == '__main__':
    parser = configparser.ConfigParser()
    parser.read("settings.ini")
    asyncio.run(main(parser))



