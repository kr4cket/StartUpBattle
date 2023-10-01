from aiogram.enums import ParseMode
from aiogram import Bot
import configparser


config = configparser.ConfigParser()  # создаём объекта парсера
config.read("../settings.ini")  # читаем конфиг
api_key = config['Bot']["tokenapi"]  # обращаемся как к обычному словарю!

TOKEN_API = api_key
bot = Bot(TOKEN_API, parse_mode=ParseMode.HTML)

bot.send_message()