from core.RabbitmqWorker import RabbitmqWorker
import core.logger as logger

if __name__ == "__main__":
    logger.create()
    RabbitmqWorker().listen()
