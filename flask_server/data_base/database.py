import sqlite3
from flask_server.ServerConfig import FlaskConfig


class DataBase:
    __conn: sqlite3.Connection
    __cursor: sqlite3.Cursor

    @classmethod
    def __int__(cls):
        flaskconfig = FlaskConfig()

        cls.__conn = sqlite3.connect(
            flaskconfig.get_config('DATABASE_PATH') +
            flaskconfig.get_config('DATABASE_NAME')
        )
        cls.__cursor = cls.__conn.cursor()
        cls.__conn.row_factory = sqlite3.Row

        cls.load_schema('init.schema.sql')
        cls.load_schema('insert_data.sql')
        cls.commmit()

    @classmethod
    def close(cls):
        cls.__conn.close()

    @classmethod
    def execute(cls, _query, _params=()):
        cls.__cursor.execute(_query, _params)
        return cls.__cursor.fetchall()

    @classmethod
    def load_schema(cls, _nameschema):
        with open(f"schema/{_nameschema}") as file:
            cls.__conn.executescript(file.read())

    @classmethod
    def commmit(cls):
        cls.__conn.commit()