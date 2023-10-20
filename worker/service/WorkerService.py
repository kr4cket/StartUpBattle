from worker.service.ai_service import AIService
from worker.core.RabbitmqWorker import RabbitmqWorker



RabbitmqWorker.send("fdsfs")

class WorkerService:
    @classmethod
    def run(cls, data: list):
        answer = AIService().send_message(AIService().generate_prompt(data))

        print(answer)
