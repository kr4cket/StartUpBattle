from worker.core.db import DB


class ChatModel(DB):

    def __init__(self):
        super().__init__()

    def insert(self, data):
        try:

            sql = f"""
                    INSERT INTO chats (id, user_id) VALUES(%s, %s)
                """

            self._cursor.execute(sql, (data["chat_id"], data["user_id"]))
            super()._save()
            return True

        except Exception as e:
            print(f"Ошибка создания записи с в таблице chats:\n{e}")
            return False

    def delete(self, data):

        try:
            sql = f""" DELETE FROM chats
                        WHERE id = %s"""

            self._cursor.execute(sql, [data["id"]])
            super()._save()
            return True

        except Exception as e:
            print(f"Ошибка удаления записи в таблице Chats:\n{e}")
            return False

    def update(self, data):
        try:
            update_data = dict(data)
            chat_id = update_data.pop("chat_id")
            for key in update_data.keys():

                sql = f""" UPDATE chats
                            SET {key} = %s
                            WHERE id = %s"""

                self._cursor.execute(sql, (update_data[key], chat_id))
                super()._save()

            return True

        except Exception as e:
            print(f"Ошибка обновления записи в таблице chats:\n{e}")

            return False

    def get(self, data):
        try:
            sql = f""" SELECT * FROM chats
                        WHERE id = %s"""

            self._cursor.execute(sql, [data["chat_id"]])
            super()._save()
            return self._cursor.fetchone()

        except Exception as e:
            print(f"Ошибка удаления записи в таблице Chats:\n{e}")
            return False
