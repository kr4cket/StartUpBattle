import psycopg2
import configparser


class DBConnection:

    def __init__(self):
        self.__conn = self.__create()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnection, cls).__new__(cls)
        return cls.instance

    def __create(self):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        connection_data = config['db']
        conn = psycopg2.connect(f"postgresql://{connection_data.get('DB_USER')}:{connection_data.get('DB_PASS')}"
                                f"@{connection_data.get('DB_HOST')}:{connection_data.get('DB_PORT')}/"
                                f"{connection_data.get('DB_NAME')}")
        return conn

    def get_connection(self):
        return self.__conn
