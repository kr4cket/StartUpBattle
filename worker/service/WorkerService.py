from worker.service.ai_service import AIService


class WorkerService:
    @classmethod
    def run(cls, data: list):
        answer = AIService().send_message(AIService().generate_prompt(data))

        print(answer)
