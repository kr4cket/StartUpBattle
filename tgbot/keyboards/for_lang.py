from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from tgbot.core.models import Language


class LangKeyBoard:

    def __init__(self):
        self.__data = []
        for row in Language.select():
            self.__data.append(row.name)

    def get_buttons(self) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()
        i = 0
        for item in self.__data:
            key.button(text=item, callback_data=f'{item}')
            i += 1
        key.adjust(1)
        return key.as_markup()

