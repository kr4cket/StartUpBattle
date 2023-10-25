from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command

from tgbot.keyboards.for_lang import LangKeyBoard
from tgbot.keyboards.for_level import LevelKeyBoard
from tgbot.keyboards.for_theme import ThemeKeyBoard
from tgbot.service.ConversationService import ConversationService


router = Router()

@router.message(CommandStart())
async def bot_start(message: types.Message):
    ConversationService().start(message.from_user.id)
    await message.answer(text='Выберете язык',
                         reply_markup=LangKeyBoard().get_buttons())


@router.message(Command('close'))
async def close_dialog(message: types.Message):
    ConversationService().clear_user_data(message.from_user.id)
    await message.answer(text='Нажмите на /start')
