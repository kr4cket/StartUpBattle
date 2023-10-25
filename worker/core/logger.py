import logging

ai_module = logging.getLogger("worker.core.ai-module")

def create():
    logging.basicConfig(filename='logs/logs.log',
                        filemode='w',
                        format='[%(asctime)s:%(levelname)s] [%(name)s] %(message)s',
                        level=logging.INFO)

    logging.info('Worker started!')
