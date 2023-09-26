from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, BotCommand
import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг
api_key = config['Bot']["tokenapi"]  # обращаемся как к обычному словарю!

TOKEN_API = api_key

bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class PhraseForm(StatesGroup):
    phrase = State()


COMMANDS = {
    '/close': 'завершить работу',
}


async def setup_bot_commands(bott: bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in COMMANDS.items()
    ]
    await bott.set_my_commands(main_menu_commands)


# генерация кнопок
def generate_markup(data) -> types.InlineKeyboardMarkup:
    key = InlineKeyboardMarkup(row_width=1)
    i = 0
    for item in data:
        button = InlineKeyboardButton(text=item, callback_data=item)
        key.insert(button)
        i += 1
    return key


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await setup_bot_commands(bot)
    buttons = [
        'Русский язык',
        'Английский язык',
        'Китайский язык',
        'Турецкий язык',
        'Еврейский язык',
    ]
    await bot.send_photo(chat_id=message.chat.id,
                         caption='вы нажали на старт',
                         photo='https://www.meme-arsenal.com/memes/d641c0dfc3ac867ecacba59b13a4e7db.jpg',
                         reply_markup=generate_markup(buttons))


@dp.message_handler(commands=['close'])
async def bot_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Нажмите на /start')


@dp.callback_query_handler(text_contains='язык')
async def themes_list(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    buttons = [
        'тема 1',
        'тема 2',
        'тема 3',
        'тема 4',
        'тема 5',
        'тема 6',
        'тема 7',
    ]
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=f'вы выбрали {callback.data} \nВыберите тему',
        reply_markup=generate_markup(buttons)
    )
    await callback.answer()


@dp.callback_query_handler(text='close')
async def cancel_bot(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=f'нажмите /start',
    )


@dp.callback_query_handler(text='check_phrase')
async def check_phrase(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=f'Введите фразу',
    )


@dp.callback_query_handler()
async def greeting_phrase(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    ikb = InlineKeyboardMarkup()
    button_input = InlineKeyboardButton(text='Ввести фразу', callback_data='check_phrase')
    ikb.insert(button_input)

    await bot.send_message(
        chat_id=callback.from_user.id,
        text=f'Приветственная фраза бота \nВы выбрали тему "{callback.data}"',
        reply_markup=ikb
    )
    await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp)