import asyncio
import json
import logging
import sys
import configparser
from aiogram.enums import ParseMode, ContentType
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import CallbackQuery
from rabbitmq.Rabbitmq import Rabbitmq

parser = configparser.ConfigParser()  # создаём объекта парсера
parser.read("../settings.ini")  # читаем конфиг
api_key = parser['Bot']["tokenapi"]  # обращаемся как к обычному словарю!

TOKEN_API = api_key
bot = Bot(TOKEN_API, parse_mode=ParseMode.HTML)
dp = Dispatcher()

COMMANDS = {
    '/close': 'завершить работу',
}

rabbitmq_config = Rabbitmq().get_config()


# генерация кнопок
def generate_markup(data) -> types.InlineKeyboardMarkup:
    key = InlineKeyboardBuilder()
    i = 0
    for item in data:
        key.button(text=item, callback_data=f'{item}')
        i += 1
    key.adjust(1)
    return key.as_markup()


@dp.message(CommandStart())
async def bot_start(message: types.Message):
    buttons = [
        'Английский язык'
    ]
    request = json.dumps({"type": "start_dialog", "chat_id": message.chat.id, "user_id": message.from_user.id})
    Rabbitmq().send(request, rabbitmq_config['input_queue'])
    await message.answer(text='вы нажали на старт',
                         reply_markup=generate_markup(buttons))


@dp.callback_query(F.data.contains('язык'))
async def themes_list(callback: CallbackQuery):
    # await bot.delete_message(callback.from_user.id, callback.message.message_id)
    buttons = [
        'Еда'
    ]
    request = json.dumps({"type": "set_lang", "lang": callback.data, "chat_id": callback.from_user.id})
    Rabbitmq().send(request, rabbitmq_config['input_queue'])
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=f'вы выбрали {callback.data} \nВыберите тему',
        reply_markup=generate_markup(buttons)
    )
    await callback.answer()


@dp.callback_query()
async def greeting_phrase(callback: CallbackQuery):
    # await bot.delete_message(callback.from_user.id, callback.message.message_id)
    request = json.dumps({"type": "set_theme", "theme": callback.data, "chat_id": callback.from_user.id})
    Rabbitmq().send(request, rabbitmq_config['input_queue'])
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=f'Вы выбрали тему "{callback.data}"',
    )
    await callback.answer()


@dp.message(Command('close'))
async def close_dialog(message: types.Message):
    # request = json.dumps({"type": "finish_dialog", "chat_id": message.from_user.id})
    # Rabbitmq().send(request, rabbitmq_config['input_queue'])
    await message.answer(text='Нажмите на /start')


@dp.message(F.text)
async def accept_new_massage(message: types.Message):
    request = json.dumps({"type": "answer_message", "prompt_data": message.text, "chat_id": message.from_user.id})
    Rabbitmq().send(request, rabbitmq_config['input_queue'])


async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
