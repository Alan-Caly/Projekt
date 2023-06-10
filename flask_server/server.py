from flask_server import app


class FlaskServer:
    __host: str
    __port: int
    __debug: bool
    __status: str

    @classmethod
    def __init__(cls):
        cls.__host = 'localhost'
        cls.__port = 2137
        cls.__debug = False
        cls.__status = 'stop'

    @classmethod
    def start(cls):
        cls.status = 'run'
        app.run(
            host=cls.__host,
            port=cls.__port,
            debug=cls.__debug
        )