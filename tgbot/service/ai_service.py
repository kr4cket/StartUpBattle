import json

import g4f


class AIService:
    async def send_message(self, prompt):
        """
            Генерация запроса к нейросетке
            #TODO Посмотреть другого провайдера
        """
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.PerplexityAi,
            messages=[{"role": "user", "content": prompt}]
        )

        result = ""
        for message in response:
            result += message

        return result

    def generate_prompt(self, data):

        # TODO Перенести в другой класс / или убрать вообще

        prompt_data = json.loads(data)

        if prompt_data["type"] == "generate_message":
            prompt = f"Напиши ответ на сообщение {prompt_data['text']} по теме {prompt_data['theme']} на {prompt_data['lang']} уровня {prompt_data['lvl']}"
        elif prompt_data["type"] == "generate_greeting":
            prompt = f"Напиши приветственное предложение на тему {prompt_data['theme']} на {prompt_data['lang']} уровня {prompt_data['lvl']}"

        return prompt
