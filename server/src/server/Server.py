import pytest

from server import app
from server.src.server.ServerConfig import ServerConfig
from server.src.sqlite.Database import Database


class Server:
    """
    Server class
    Class representing the server application
    """
    __HOST: str
    __PORT: int
    __STATUS_SERVER: str

    __configServer: ServerConfig

    @classmethod
    def __init__(cls):
        cls.__STATUS_SERVER = 'down'
        cls.__HOST = 'localhost'
        cls.__PORT = 5000

        cls.__configServer = ServerConfig()
        cls._load_config()

    @classmethod
    def _load_config(cls):
        cls.__configServer.new_setting_add('DATABASE_NAME', 'database.db')
        cls.__configServer.new_setting_add('DATABASE_PATH', '')

    @classmethod
    def get_status(cls) -> str:
        """
        Get server status
        :return: Server status
        """
        return cls.STATUS_SERVER

    @classmethod
    def help(cls):
        """ Show help """
        with open('serverCommandHelp.txt', 'r') as f:
            print(f.read())

    @classmethod
    def run_test(cls):
        """ Run tests """
        pytest.main([])

    @classmethod
    def init_db(cls):
        """ Initialize database """
        Database(True)

    @classmethod
    def run(cls) -> bool | None:
        """ Run server

            :return: Return False if server is already running
        """
        if cls.__STATUS_SERVER == 'running':
            print('Server is already running')
            return False

        app.run(
            host=cls.__HOST,
            port=cls.__PORT
        )

        cls.__STATUS_SERVER = 'down'
