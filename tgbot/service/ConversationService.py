from core.models import *
import core.logger as logger


class ConversationService:

    @classmethod
    def is_theme_set(cls, user_id: int) -> bool:
        try:
            chat = Chat.get(Chat.id == user_id)
            logger.conversation_service.debug(f"Chat: {chat.theme}")
            if chat.theme is None:
                return False
            else:
                return True
        except:
            logger.conversation_service.exception(f"Error occured while checking theme")

    @classmethod
    def is_level_set(cls, user_id: int) -> bool:
        try:
            chat = Chat.get(Chat.id == user_id)
            logger.conversation_service.debug(f"Chat: {chat.lvl}")
            if chat.lvl is None:
                return False
            else:
                return True
        except:
            logger.conversation_service.exception(f"Error occured while checking level")

    @classmethod
    def start(cls, user_id):
        try:
            chat = Chat.get_or_none(Chat.id == user_id)
            if chat is None:
                Chat.insert(id=user_id).execute()
        except:
            logger.conversation_service.exception(f"Error occured while starting chatting with user: {user_id}")

    @classmethod
    def set_language_data(cls, user_id: int, language: str):
        try:
            (Chat.update(
                lang=Language.select()
                .where(Language.name == language)
            ).where(Chat.id == user_id)
             .execute())
        except:
            logger.conversation_service.exception(f"Error occured while setting language data")

    @classmethod
    def set_level_data(cls, user_id: int, level: str):
        try:
            (Chat.update(
                lvl=LanguageLevel.select()
                .where(LanguageLevel.name == level)
            ).where(Chat.id == user_id)
             .execute())
        except:
            logger.conversation_service.exception(f"Error occured while setting level data")

    @classmethod
    def set_theme_data(cls, user_id: int, theme: str):
        try:
            (Chat.update(
                theme=Theme.select()
                .where(Theme.name == theme)
            ).where(Chat.id == user_id)
             .execute())
        except:
            logger.conversation_service.exception(f"Error occured while setting theme data")

    @classmethod
    def get_chat_info(cls, user_id: int):
        return Chat.select().where(Chat.id == user_id).get()

    @classmethod
    def clear_user_data(cls, user_id: int):
        Chat.delete().where(Chat.id == user_id).execute()
        logger.conversation_service.info(f"Chat deleted with user {user_id}")
