import json

from service.ConversationService import ConversationService
from core.RabbitmqTgbot import RabbitmqTgbot
from service.SenderService import SenderService


class RabbitmqService:
    @classmethod
    def send_data_rabbitmq(cls, user_id: int, message_type: str, text_data: str = ""):
        chat = ConversationService().get_chat_info(user_id)
        sender = RabbitmqTgbot()

        request = (json.dumps(
            {
                "type": message_type,
                "user_id": chat.id,
                "lang": chat.lang.name,
                "theme": chat.theme.name,
                "lvl": chat.lvl.name,
                "text": text_data,
                "answer": ""
            }))

        sender.send(request)
        sender.close_connection()


    @classmethod
    def send_message(cls, data: json, loop=None):
        data = json.loads(data)

        SenderService.send(data["user_id"], data["answer"], loop)
        # send_message_to_user(data["user_id"], data["answer"], loop)
