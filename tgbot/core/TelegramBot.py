import configparser

from aiogram import Bot


class TelegramBot:
    __bot: Bot | None = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            parser = configparser.ConfigParser()
            parser.read("../settings.ini")

            cls.instance = super(TelegramBot, cls).__new__(cls)

            cls.__bot = Bot(token=parser['Bot']["tokenapi"])

        return cls.instance

    @classmethod
    def get_bot_instance(cls):
        return cls.__bot
