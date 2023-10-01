import json
import config
# для функционирования класса, необходим конфиг Rabbitmq. за примером конфига обращаться к Матвею
from pika import ConnectionParameters, PlainCredentials, BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel


class Rabbitmq:
    _instance = None
    __connection: BlockingConnection = None
    __channel: BlockingChannel = None
    __parameters: ConnectionParameters = ConnectionParameters(
        host=config.rabbit_host,
        virtual_host=config.rabbit_vhost,
        port=config.rabbit_port,
        credentials=PlainCredentials(config.rabbit_login, config.rabbit_password),
        heartbeat=600,
        blocked_connection_timeout=14400
    )

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Rabbitmq, cls).__new__(cls)

            cls.__connection = BlockingConnection(cls.__parameters)

            cls.__channel = cls.__connection.channel()

            cls.__channel.queue_bind(
                queue=config.output_queue,
                exchange=config.out_exchange,
                routing_key=config.output_queue
            )

        return cls._instance

    @classmethod
    def listen(cls):
        def callback(ch, method, properties, body):
            print(f" [x] Received {body}")

        cls.__channel.basic_consume(
            queue=config.output_queue,
            on_message_callback=callback
        )

        print(' [*] Waiting for messages. To exit press CTRL+C')
        cls.__channel.start_consuming()

    @classmethod
    def send(cls, data: json = None):
        cls.__channel.basic_publish(exchange=config.out_exchange, routing_key=config.output_queue, body=data)
        print(f" [x] Sent {data}")
