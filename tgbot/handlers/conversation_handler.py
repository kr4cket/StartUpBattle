from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery
from keyboards.for_lang import LangKeyBoard
from keyboards.for_level import LevelKeyBoard
from keyboards.for_theme import ThemeKeyBoard
from service.conversation_service import ConversationService

router = Router()
service = ConversationService()

@router.message(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text='Выберете язык',
                         reply_markup=LangKeyBoard().get_buttons())


@router.callback_query(F.data.contains('язык'))
async def level_list(callback: CallbackQuery):
    await callback.message.answer(
        text=f'вы выбрали {callback.data}\nВыберите уровень',
        reply_markup=LevelKeyBoard(callback.data).get_buttons()
    )
    await callback.answer()


@router.callback_query()
async def theme_list(callback: CallbackQuery):

    if service.is_theme_set(callback.from_user.id):
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
    msg = service.create_message()
    await message.answer(text=message.text)


async def greeting_phrase(callback: CallbackQuery):
    await callback.message.answer(
        text=f'Вы выбрали тему: "{callback.data}"\n',
    )
    await callback.answer()