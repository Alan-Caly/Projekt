import sqlite3
from server import app


class Database:
    """ A class to connect to the database """
    __conn: sqlite3.Connection
    __cursor: sqlite3.Cursor

    @classmethod
    def __init__(cls, _init: bool = False):
        cls.open()

        if _init:
            cls._init_database()

    @classmethod
    def _init_database(cls):
        cls.load_schema('init.schema.sql')
        cls.load_schema('insert_data.sql')

        cls.commit()
        print('Successfully initialized database!\n')

    @classmethod
    def load_schema(cls, _name_schema: str):
        """
            Load the schema of the database

            :param _name_schema: The name of the schema to load
        """
        with open(f"server/migration/schema/{_name_schema}") as file:
            cls.__conn.executescript(file.read())

    @classmethod
    def commit(cls):
        """ Commit the changes to the database """
        cls.__conn.commit()

    @classmethod
    def execute(cls, _sql: str, _params: tuple = ()):
        """
            Execute a query on the database

            :param _sql: Query to execute
            :param _params: Parameters to pass

            :return: Return True if the query was successful, False otherwise
        """
        try:
            cls.__cursor.execute(_sql, _params)
            cls.commit()
            return True

        except sqlite3.Error as error:
            print(error)
            return False

    @classmethod
    def fetchall(cls):
        """ Fetch all the rows from the database """
        return cls.__cursor.fetchall()

    @classmethod
    def fetchone(cls):
        """ Fetch one row from the database """
        return cls.__cursor.fetchone()

    @classmethod
    def fetchmany(cls, _how_many: int = 1):
        """ Fetch many rows from the database """
        return cls.__cursor.fetchmany(_how_many)

    @classmethod
    def open(cls):
        """ Open the database """
        cls.__conn = sqlite3.connect(app.config['DATABASE_PATH'] + app.config['DATABASE_NAME'])
        cls.__cursor = cls.__conn.cursor()

        cls.__conn.row_factory = sqlite3.Row

    @classmethod
    def close(cls):
        """ Close the database """
        cls.__cursor.close()
        cls.__conn.close()
