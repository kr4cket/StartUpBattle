from worker.core.db import DB


class UserModel(DB):

    def __init__(self):
        super().__init__()

    def insert(self, data):
        try:

            sql = f"""
                    INSERT INTO users (id) VALUES(%s)
                """

            self._cursor.execute(sql, [data["id"]])
            super()._save()
            return True

        except Exception as e:
            print(f"Ошибка создания записи с в таблице Users:\n{e}")
            return False


    def delete(self, data):

        try:
            sql = f""" DELETE FROM users
                        WHERE id = %s"""

            self._cursor.execute(sql, [data["id"]])
            super()._save()
            return True

        except Exception as e:
            print(f"Ошибка удаления записи в таблице Users:\n{e}")
            return False

    def get(self, data):
        try:
            sql = f""" SELECT * FROM users
                        WHERE id = %s"""

            self._cursor.execute(sql, [data["id"]])
            super()._save()
            return self._cursor.fetchone()

        except Exception as e:
            print(f"Ошибка удаления записи в таблице Chats:\n{e}")
            return False