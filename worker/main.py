from models.users import UserModel
from models.chats import ChatModel
from rabbitmq.Rabbitmq import Rabbitmq

user = UserModel()
chat = ChatModel()
broker = Rabbitmq()

user_mock = {"id": 1}
chat_mock = {"id": 2, "user_id": 1}
chat_update_mock = {"id": 2, "lang": "en", "theme": "food"}


print(user.get(user_mock))

print(chat.get(chat_mock))

if chat.update(chat_update_mock):
    print("успешно")
else:
    print("провал")

print(chat.get(chat_mock))
broker.send()