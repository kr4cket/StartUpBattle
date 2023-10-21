import json

import g4f


class AIService:
    @classmethod
    def send_message(cls, prompt):
        """
            Генерация запроса к нейросетке
            #TODO Посмотреть другого провайдера
        """
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        result = ""
        for message in response:
            result += message

        return result
