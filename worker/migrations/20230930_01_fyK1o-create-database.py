"""
Create DataBase
"""

from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE IF NOT EXISTS users (id INT, PRIMARY KEY(id))", "DROP TABLE users"),
    step("CREATE TABLE IF NOT EXISTS chats (id INT, user_id INT, lang VARCHAR(255), "
         "theme VARCHAR(255), PRIMARY KEY(id), FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE)",
         "DROP TABLE chats"),
    step("CREATE TABLE IF NOT EXISTS messages (id INT, chat_id INT, message TEXT, PRIMARY KEY(id), "
         "FOREIGN KEY (chat_id) REFERENCES chats (id) ON DELETE CASCADE)", "DROP TABLE messages")
]
