import json
from aiogram import Bot
from tgbot.service.ai_service import AIService
from tgbot.core.models import *


class ConversationService:

    def is_theme_set(self, user_id: int) -> bool:
        chat = Chat.get(Chat.id == user_id)
        if chat.theme is None:
            return False
        else:
            return True

    def is_level_set(self, user_id: int) -> bool:
        chat = Chat.get(Chat.id == user_id)
        if chat.lvl is None:
            return False
        else:
            return True

    def start(self, user_id):
        chat = Chat.get(Chat.id == user_id)
        if chat is None:
            Chat.insert(id=user_id).execute()

    def create_message(self, user_id: int = 0, msg: str = ""):
        return self.__send(user_id, "generate_message", msg)

    def create_greeting(self, user_id: int = 0):
        return self.__send(user_id, "generate_greeting")

    def set_lang_data(self, user_id: int, language: str):
        (Chat.update(
            lang=Language.select()
            .where(Language.name == language)
        ).where(Chat.id == user_id)
         .execute())

    def set_level_data(self, user_id: int, level: str):
        (Chat.update(
            lvl=LanguageLevel.select()
            .where(LanguageLevel.name == level)
        ).where(Chat.id == user_id)
         .execute())

    def set_theme_data(self, user_id: int, theme: str):
        (Chat.update(
            theme=Theme.select()
            .where(Theme.name == theme)
        ).where(Chat.id == user_id)
         .execute())

    async def __send(self, user_id: int, message_type: str, text_data: str = ""):
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

        # TODO Заменить на отправку RabbitMQ
        return await AIService().send_message(AIService().generate_prompt(request))


    # def __send(self, user_id: int, message_type: str):
    #     chat = Chat.get(Chat.id == user_id)
    #     request = json.dumps({
    #         "type": message_type,
    #         "user_id": chat.id,
    #         "lang": chat.lang,
    #         "theme": chat.theme,
    #         "level": chat.lvl}
    #     )
    #     #отправка в rabbit
    #
    # def __answer(self, data: dict):
    #     self.__bot.send_message()

