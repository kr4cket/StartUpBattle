import json


class PromptGenerator:

    @classmethod
    def generate_prompt(cls, data):

        prompt_data = json.loads(data)

        if prompt_data["type"] == "generate_message":
            return f"Проверь это сообщение на грамматические и лексические ошибки и исправь их (если сообщенеи правильное, то не упоминай это в ответе): {prompt_data['text']}. А также напиши ответ на сообщение пользователя: {prompt_data['text']} по теме {prompt_data['theme']} (все это в одном сообщении). Сообщение генерируй на языке: {prompt_data['lang']} уровня {prompt_data['lvl']}"
        elif prompt_data["type"] == "generate_greeting":
            return f"Напиши приветственное предложение на тему {prompt_data['theme']} на {prompt_data['lang']} уровня {prompt_data['lvl']}"
