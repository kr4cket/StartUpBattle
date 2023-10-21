import json
import configparser

from asyncio import ProactorEventLoop
from pika import ConnectionParameters, PlainCredentials, BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel
from abc import ABC, abstractmethod


class Rabbitmq(ABC):
    _instance = None
    __connection: BlockingConnection = None
    __channel: BlockingChannel = None
    __config = None

    @classmethod
    def get_config(cls) -> list:
        return cls.__config

    @classmethod
    @abstractmethod
    def listen(cls, loop: ProactorEventLoop = None):
        pass

    @classmethod
    @abstractmethod
    def send(cls, data: json):
        pass
