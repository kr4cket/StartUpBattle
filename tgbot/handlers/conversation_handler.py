from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery
from tgbot.keyboards.for_lang import LangKeyBoard
from tgbot.keyboards.for_level import LevelKeyBoard
from tgbot.keyboards.for_theme import ThemeKeyBoard
from tgbot.service.conversation_service import ConversationService

router = Router()
service = ConversationService()

@router.message(CommandStart())
async def bot_start(message: types.Message):
    service.start(message.from_user.id)
    await message.answer(text='Выберете язык',
                         reply_markup=LangKeyBoard().get_buttons())


@router.callback_query(F.data.contains('язык'))
async def level_list(callback: CallbackQuery):
    service.set_lang_data(callback.from_user.id, callback.data)
    await callback.message.answer(
        text=f'вы выбрали {callback.data}\nВыберите уровень',
        reply_markup=LevelKeyBoard(callback.data).get_buttons()
    )
    await callback.answer()


@router.callback_query()
async def theme_list(callback: CallbackQuery):
    if not service.is_theme_set(callback.from_user.id) and not service.is_level_set(callback.from_user.id):
        service.set_level_data(callback.from_user.id, callback.data)
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
    msg = await service.create_message(message.from_user.id, message.text)
    await message.answer(text=msg)


async def greeting_phrase(callback: CallbackQuery):
    service.set_theme_data(callback.from_user.id, callback.data)
    await callback.message.answer(
        text=f'Вы выбрали тему: "{callback.data}"\n',
    )
    msg = await service.create_greeting(callback.from_user.id)
    await callback.message.answer(text=msg)
