import g4f
from worker.core.logger import ai_module


class AIService:
    @classmethod
    def send_message(cls, prompt):
        """
            Генерация запроса к нейросетке
            #TODO Посмотреть другого провайдера
        """

        try:
            # g4f.Provider.FakeGpt
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                provider=g4f.Provider.FakeGpt,
                messages=[{"role": "user", "content": prompt}]
            )

            result = ""
            for message in response:
                result += message

            print(response)

            return result

        except:
            ai_module.exception("Error occurred while sending message to AI")
            result = "Sorry, something went wrong, please try again!"

            return result

