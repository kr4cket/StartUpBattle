from worker.core.RabbitmqWorker import RabbitmqWorker
import worker.core.logger as logger

if __name__ == "__main__":
    logger.create()
    RabbitmqWorker().listen()
