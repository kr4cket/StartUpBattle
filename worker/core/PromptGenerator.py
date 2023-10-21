import json


class PromptGenerator:

    @classmethod
    def generate_prompt(cls, data):

        prompt_data = json.loads(data)

        if prompt_data["type"] == "generate_message":
            return f"Напиши ответ на сообщение {prompt_data['text']} по теме {prompt_data['theme']} на {prompt_data['lang']} уровня {prompt_data['lvl']}"
        elif prompt_data["type"] == "generate_greeting":
            return f"Напиши приветственное предложение на тему {prompt_data['theme']} на {prompt_data['lang']} уровня {prompt_data['lvl']}"
