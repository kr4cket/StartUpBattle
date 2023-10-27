from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery

from keyboards.for_lang import LangKeyBoard
from keyboards.for_level import LevelKeyBoard
from keyboards.for_theme import ThemeKeyBoard
from service.RabbitmqService import *
from service.ConversationService import ConversationService

router = Router()


@router.message(CommandStart())
async def bot_start(message: types.Message):
    ConversationService().start(message.from_user.id)
    await message.answer(text='Выберете язык',
                         reply_markup=LangKeyBoard().get_buttons())


@router.callback_query(F.data.contains('язык'))
async def level_list(callback: CallbackQuery):
    ConversationService().set_language_data(callback.from_user.id, callback.data)
    await callback.message.answer(
        text=f'вы выбрали {callback.data}\nВыберите уровень',
        reply_markup=LevelKeyBoard(callback.data).get_buttons()
    )
    await callback.answer()


@router.callback_query()
async def theme_list(callback: CallbackQuery):
    if not ConversationService().is_theme_set(callback.from_user.id) and not ConversationService().is_level_set(callback.from_user.id):
        ConversationService().set_level_data(callback.from_user.id, callback.data)
        await callback.message.answer(
            text=f'Вы выбрали сложность: "{callback.data}"\nВыберите тему',
            reply_markup=ThemeKeyBoard().get_buttons()
        )
    else:
        await greeting_phrase(callback)


@router.message(Command('close'))
async def close_dialog(message: types.Message):
    ConversationService().clear_user_data(message.from_user.id)
    await message.answer(text='Нажмите на /start')


@router.message(F.text)
async def accept_new_massage(message: types.Message):
    await RabbitmqService().send_data_rabbitmq(message.from_user.id, "generate_message", message.text)


async def greeting_phrase(callback: CallbackQuery):
    ConversationService().set_theme_data(callback.from_user.id, callback.data)
    await callback.message.answer(
        text=f'Вы выбрали тему: "{callback.data}"\n',
    )
    RabbitmqService().send_data_rabbitmq(callback.from_user.id, "generate_greeting")
