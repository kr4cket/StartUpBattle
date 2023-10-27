from peewee import *
import configparser

class DBConnection:

    def __init__(self):
        self.__handle = self.__create()
        self.__connect()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnection, cls).__new__(cls)
        return cls.instance

    def __create(self) -> PostgresqlDatabase:
        data = self.__get_config_data()
        return PostgresqlDatabase(
            data['DB_NAME'], user=data['DB_USER'],
            password=data['DB_PASS'],
            host=data['DB_HOST'],
            port=data['DB_PORT']
        )

    def __connect(self) -> None:
        self.__handle.connect()

    def get_handle(self):
        return self.__handle

    def __get_config_data(self):
        parser = configparser.ConfigParser()
        parser.read("../settings.ini")
        return parser['db']
