from flask_server import app
from flask_server.ServerConfig import FlaskConfig


class FlaskServer:
    __host: str
    __port: int
    __debug: bool
    __status: str
    __configINST: FlaskConfig

    @classmethod
    def __init__(cls):
        cls.__host = 'localhost'
        cls.__port = 2137
        cls.__debug = False
        cls.__status = 'stop'
        cls.__configINST = FlaskConfig()

        cls.set_config()

    @classmethod
    def start(cls):
        cls.status = 'run'
        app.run(
            host=cls.__host,
            port=cls.__port,
            debug=cls.__debug
        )

    @classmethod
    def set_config(cls):
        cls.__configINST.add_new_element_config("DATABASE_NAME", 'cardatabase.db')
        cls.__configINST.add_new_element_config("DATABASE_PATH", '')
