import json
import configparser
from pika import ConnectionParameters, PlainCredentials, BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel
from abc import ABC, abstractmethod


class Rabbitmq(ABC):
    _instance = None
    __connection: BlockingConnection = None
    __channel: BlockingChannel = None
    __config = None

    @abstractmethod
    def __new__(cls):
        #TODO Переделать этот метод, так как в каждом потомке придется писать один и тот же код (обратиться к дк)

        pass

    @classmethod
    def get_config(cls) -> list:
        return cls.__config

    @classmethod
    @abstractmethod
    def listen(cls):
        pass

    @classmethod
    @abstractmethod
    def send(cls, data: json):
        pass
