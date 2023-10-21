import asyncio

from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery

from tgbot.core.TelegramBot import TelegramBot
from tgbot.keyboards.for_lang import LangKeyBoard
from tgbot.keyboards.for_level import LevelKeyBoard
from tgbot.keyboards.for_theme import ThemeKeyBoard
from tgbot.service.RabbitmqService import *
from tgbot.core.ConversationModel import ConversationModel

router = Router()


@router.message(CommandStart())
async def bot_start(message: types.Message):
    ConversationModel().start(message.from_user.id)
    await message.answer(text='Выберете язык',
                         reply_markup=LangKeyBoard().get_buttons())


@router.callback_query(F.data.contains('язык'))
async def level_list(callback: CallbackQuery):
    ConversationModel().set_language_data(callback.from_user.id, callback.data)
    await callback.message.answer(
        text=f'вы выбрали {callback.data}\nВыберите уровень',
        reply_markup=LevelKeyBoard(callback.data).get_buttons()
    )
    await callback.answer()


@router.callback_query()
async def theme_list(callback: CallbackQuery):
    if not ConversationModel().is_theme_set(callback.from_user.id) and not ConversationModel().is_level_set(callback.from_user.id):
        ConversationModel().set_level_data(callback.from_user.id, callback.data)
        await callback.message.answer(
            text=f'Вы выбрали сложность: "{callback.data}"\nВыберите тему',
            reply_markup=ThemeKeyBoard().get_buttons()
        )
        await callback.answer()
    else:
        await greeting_phrase(callback)


@router.message(Command('close'))
async def close_dialog(message: types.Message):
    await message.answer(text='Нажмите на /start')


@router.message(F.text)
async def accept_new_massage(message: types.Message):
    msg = RabbitmqService().send_data_rabbitmq(message.from_user.id, "generate_message", message.text)
    await message.answer(text=msg)


async def greeting_phrase(callback: CallbackQuery):
    ConversationModel().set_theme_data(callback.from_user.id, callback.data)
    await callback.message.answer(
        text=f'Вы выбрали тему: "{callback.data}"\n',
    )
    RabbitmqService().send_data_rabbitmq(callback.from_user.id, "generate_greeting")


def send_message_to_user(user_id: int, text: str, loop: ProactorEventLoop):
    bot = TelegramBot().get_bot_instance()

    asyncio.set_event_loop(loop)

    asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=user_id, text=text), loop)
