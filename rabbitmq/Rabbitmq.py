import json
import configparser
# для функционирования класса, необходим конфиг Rabbitmq. за примером конфига обращаться к Матвею
from pika import ConnectionParameters, PlainCredentials, BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel
from worker.actions.router import Router


class Rabbitmq:
    _instance = None
    __connection: BlockingConnection = None
    __channel: BlockingChannel = None
    __config = None

    def __new__(cls):
        if not cls._instance:
            parser = configparser.ConfigParser()
            parser.read("../settings.ini")
            cls.__config = parser['rabbitmq']

            parameters = ConnectionParameters(
                host=cls.__config['rabbit_host'],
                virtual_host=cls.__config['rabbit_vhost'],
                port=int(cls.__config['rabbit_port']),
                credentials=PlainCredentials(cls.__config['rabbit_login'], cls.__config['rabbit_password']),
                heartbeat=600,
                blocked_connection_timeout=14400
            )

            cls._instance = super(Rabbitmq, cls).__new__(cls)

            cls.__connection = BlockingConnection(parameters)

            cls.__channel = cls.__connection.channel()

            cls.__channel.queue_bind(
                queue=cls.__config['output_queue'],
                exchange=cls.__config['out_exchange'],
                routing_key=cls.__config['output_queue']
            )

        return cls._instance

    @classmethod
    def listen(cls):
        def output_callback(ch, method, properties, body):
            print(f" [x] Received {body}")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        def input_callback(ch, method, properties, body):
            Router().run(body)
            print(f" [x] Received2 {body}")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        cls.__channel.basic_consume(
            queue=cls.__config['output_queue'],
            on_message_callback=output_callback
        )

        cls.__channel.basic_consume(
            queue=cls.__config['input_queue'],
            on_message_callback=input_callback
        )

        print('The listener is working, don\'t close this window!')
        cls.__channel.start_consuming()

    @classmethod
    def send(cls, data: json, routing_key: str):
        """
        Аргумент data - JSON, который необходимо передать в rabbitmq

        Аргумент routing_key - очередь в rabbitmq, в которую необходимо поместить ваш JSON
        (input_queue - для информации от пользователя или output_queue - для ответа нейросети)
        """
        cls.__channel.basic_publish(exchange=cls.__config['out_exchange'], routing_key=routing_key, body=data)
        print("Your message has been send")

    @classmethod
    def get_config(cls) -> list:
        return cls.__config
