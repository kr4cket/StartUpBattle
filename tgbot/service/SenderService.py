import asyncio

from tgbot.core.TelegramBot import TelegramBot
from tgbot.service.RabbitmqService import *


class SenderService:
    @staticmethod
    def send(user_id: int, text: str, loop: ProactorEventLoop):

        bot = TelegramBot().get_bot_instance()

        asyncio.set_event_loop(loop)

        asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=user_id, text=text), loop)