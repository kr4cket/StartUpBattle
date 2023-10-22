import logging


conversation_service = logging.getLogger("tg.bot.service.conversation")
conversation_handler = logging.getLogger("tg.bot.handler.conversation")

def create():
    logging.basicConfig(filename='logs/logs.log',
                        filemode='w',
                        format='[%(asctime)s:%(levelname)s] [%(name)s] %(message)s',
                        level=logging.DEBUG)

    logging.info('Application started!')
