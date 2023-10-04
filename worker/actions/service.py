from worker.models.users import UserModel
from worker.models.chats import ChatModel
import g4f
import asyncio
from aiogram.enums import ParseMode
from aiogram import Bot
import configparser


class Service:

    def __init__(self):
        self.users = UserModel()
        self.chats = ChatModel()
        self.__connect_to_bot()

    def __connect_to_bot(self):
        tg_config = configparser.ConfigParser()
        tg_config.read("../settings.ini")
        api_key = tg_config['Bot']["tokenapi"]
        TOKEN_API = api_key
        self.bot = Bot(TOKEN_API, parse_mode=ParseMode.HTML)

    def start_dialog(self, data):
        print(data)
        self.users.insert(data)
        self.chats.insert(data)

    def set_lang(self, data):
        self.chats.update(data)

    def set_theme(self, data):
        self.chats.update(data)
        self.greeting_message(data)

    def finish_dialog(self, data):
        self.chats.delete(data)

    def greeting_message(self, data):
        request_data = self.chats.get(data)
        prompt = f"Напиши привественное предложение на тему {request_data[3]} на {request_data[2]}"
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.send_message(prompt, request_data[0]))

    def answer_message(self, data):
        request_data = self.chats.get(data)
        prompt = f"Напиши ответное сообщение на {data['prompt_data']} в тематике {request_data[3]} на {request_data[2]}"
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.send_message(prompt, request_data[0]))

    async def send_message(self, prompt, id):

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )

        result = ""
        for message in response:
            result += message

        await self.bot.send_message(chat_id=id, text=result)
