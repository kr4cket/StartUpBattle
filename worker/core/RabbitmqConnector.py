import json
from rabbitmq.Rabbitmq import Rabbitmq


class RabbitmqConnector(Rabbitmq):
    @classmethod
    def listen(cls):
        def input_callback(ch, method, properties, body):
            print(f" [x] Received2 {body}")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        cls.__channel.basic_consume(
            queue=cls.__config['input_queue'],
            on_message_callback=input_callback
        )

        print('The listener is working, don\'t close this window!')
        cls.__channel.start_consuming()

    @classmethod
    def send(cls, data: json):
        cls.__channel.basic_publish(
            exchange=cls.__config['out_exchange'],
            routing_key=cls.__config['output_queue'],
            body=data)
        print("Your message has been send")
