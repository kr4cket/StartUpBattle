from db_connect import DBConnection


class DB:

    def __init__(self):
        self.__connection = DBConnection().get_connection()
        self._cursor = self.__connection.cursor()

    def insert(self, data: dict):
        pass

    def delete(self, data: dict):
        pass

    def update(self, data: dict):
        pass

    def get(self, data: dict):
        pass

    def _save(self):
        self.__connection.commit()