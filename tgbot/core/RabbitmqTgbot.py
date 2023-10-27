import json
import configparser

from pika import ConnectionParameters, PlainCredentials, BlockingConnection
from rabbitmq.Rabbitmq import Rabbitmq


class RabbitmqTgbot(Rabbitmq):
    def __new__(cls):

        parser = configparser.ConfigParser()
        parser.read("settings.ini")
        cls.__config = parser['rabbitmq']

        parameters = ConnectionParameters(
            host=cls.__config['rabbit_host'],
            virtual_host=cls.__config['rabbit_vhost'],
            port=int(cls.__config['rabbit_port']),
            credentials=PlainCredentials(cls.__config['rabbit_login'], cls.__config['rabbit_password']),
            heartbeat=600,
            blocked_connection_timeout=14400
        )

        cls.__connection = BlockingConnection(parameters)

        cls.__channel = cls.__connection.channel()

        cls.__channel.queue_bind(
            queue=cls.__config['output_queue'],
            exchange=cls.__config['out_exchange'],
            routing_key=cls.__config['output_queue']
        )

        return cls

    @classmethod
    def close_connection(cls):
        cls.__connection.close()

    @classmethod
    def listen(cls, loop=None):
        def output_callback(ch, method, properties, body):
            print(f" [x] Tgbot received from worker: {body}")

            from service.RabbitmqService import RabbitmqService

            RabbitmqService().send_message(body, loop)

            ch.basic_ack(delivery_tag=method.delivery_tag)

        cls.__channel.basic_consume(
            queue=cls.__config['output_queue'],
            on_message_callback=output_callback
        )

        print('Tgbot listener is working, don\'t close this window!')
        cls.__channel.start_consuming()

    @classmethod
    def send(cls, data: json):
        cls.__channel.basic_publish(
            exchange=cls.__config['out_exchange'],
            routing_key=cls.__config['input_queue'],
            body=data)
        print("Your message has been send")
