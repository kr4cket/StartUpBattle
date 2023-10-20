import json
from tgbot.core.models import *
from tgbot.core.RabbitmqTgbot import RabbitmqTgbot


class ConversationService:

    @classmethod
    def is_theme_set(cls, user_id: int) -> bool:
        chat = Chat.get(Chat.id == user_id)
        if chat.theme is None:
            return False
        else:
            return True

    @classmethod
    def is_level_set(cls, user_id: int) -> bool:
        chat = Chat.get(Chat.id == user_id)
        if chat.lvl is None:
            return False
        else:
            return True

    @classmethod
    def start(cls, user_id):
        chat = Chat.get_or_none(Chat.id == user_id)
        if chat is None:
            Chat.insert(id=user_id).execute()

    @classmethod
    def set_lang_data(cls, user_id: int, language: str):
        (Chat.update(
            lang=Language.select()
            .where(Language.name == language)
        ).where(Chat.id == user_id)
         .execute())

    @classmethod
    def set_level_data(cls, user_id: int, level: str):
        (Chat.update(
            lvl=LanguageLevel.select()
            .where(LanguageLevel.name == level)
        ).where(Chat.id == user_id)
         .execute())

    @classmethod
    def set_theme_data(cls, user_id: int, theme: str):
        (Chat.update(
            theme=Theme.select()
            .where(Theme.name == theme)
        ).where(Chat.id == user_id)
         .execute())

    @classmethod
    async def send_data_rabbitmq(cls, user_id: int, message_type: str, text_data: str = ""):
        chat = Chat.get(Chat.id == user_id)
        request = (json.dumps(
            {
                "type": message_type,
                "user_id": chat.id,
                "lang": chat.lang.name,
                "theme": chat.theme.name,
                "lvl": chat.lvl.name,
                "text": text_data
            }))

        RabbitmqTgbot().send(request)

    def send_message_to_user(self, data: list):
        print(data)
