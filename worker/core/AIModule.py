import configparser
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
            parser = configparser.ConfigParser()
            parser.read("../settings.ini")

            # полностью рабочий чат бот - g4f.Provider.FakeGpt
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                provider=g4f.Provider.Bard,
                messages=[{"role": "user", "content": prompt}],
                auth="cookies",
                cookies={
                    "__Secure-1PSID": parser["Bard"]["__Secure-1PSID"],
                    "__Secure-1PSIDTS": parser["Bard"]["__Secure-1PSIDTS"]
                },
                proxy="https://144.48.38.39:8443"
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

