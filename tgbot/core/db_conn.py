from peewee import *

user = 'stbuser'
password = 'stbuser'
db_name = 'data'


class DBConnection:

    def __init__(self):
        self.__handle = self.__create()
        self.__connect()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnection, cls).__new__(cls)
        return cls.instance

    def __create(self) -> PostgresqlDatabase:
        #Добавить парсер конфига
        return PostgresqlDatabase(
            db_name, user=user,
            password=password,
            host='localhost',
            port=5436
        )

    def __connect(self) -> None:
        self.__handle.connect()

    def get_handle(self):
        return self.__handle

