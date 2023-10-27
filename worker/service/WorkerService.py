import json

from core.AIModule import AIService
from core.PromptGenerator import PromptGenerator


class WorkerService:
    @classmethod
    def run(cls, data):
        answer = AIService().send_message(PromptGenerator().generate_prompt(data))

        data = json.loads(data)
        data["answer"] = answer
        data = json.dumps(data)

        return data
