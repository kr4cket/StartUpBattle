from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from tgbot.core.models import LanguageLevel
from tgbot.core.models import Language


class LevelKeyBoard:

    def __init__(self, lang):
        self.__data = []
        self.btn = 0
        for row in (LanguageLevel
                .select()
                .join(Language)
                .where(Language.name == lang)):
            self.__data.append(row.name)

    def get_buttons(self) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()
        self.btn = 0
        for item in self.__data:
            key.button(text=item, callback_data=f'{item}')
            self.btn += 1

        if self.btn >= 6 and self.btn % 2 == 0:
            key.adjust(2)
        elif self.btn >= 9:
            key.adjust(3)
        else:
            key.adjust(1)

        return key.as_markup()
