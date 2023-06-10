from flask_server import app


class FlaskConfig:
    __default_settings_list: list
    __last_operation: str

    @classmethod
    def __init__(cls):
        cls.__default_settings_list = [
            'APPLICATION_ROOT',
            'DEBUG',
            'EXPLAIN_TEMPLATE_LOADING',
            'JSONIFY_MIMETYPE',
            'JSONIFY_PRETTYPRINT_REGULAR',
            'JSON_AS_ASCII',
            'JSON_SORT_KEYS',
            'LOGGER_HANDLER_POLICY',
            'LOGGER_NAME',
            'MAX_CONTENT_LENGTH',
            'PERMANENT_SESSION_LIFETIME',
            'PREFERRED_URL_SCHEME',
            'PRESERVE_CONTEXT_ON_EXCEPTION',
            'PROPAGATE_EXCEPTIONS',
            'SECRET_KEY',
            'SEND_FILE_MAX_AGE_DEFAULT',
            'SERVER_NAME',
            'SESSION_COOKIE_DOMAIN',
            'SESSION_COOKIE_HTTPONLY',
            'SESSION_COOKIE_NAME',
            'SESSION_COOKIE_PATH',
            'SESSION_COOKIE_SECURE',
            'SESSION_REFRESH_EACH_REQUEST',
            'TEMPLATES_AUTO_RELOAD',
            'TESTING',
            'TRAP_BAD_REQUEST_ERRORS',
            'TRAP_HTTP_EXCEPTIONS',
            'USE_X_SENDFILE'
        ]
        cls.__last_operation = str()

    @classmethod
    def get_config(cls, _name_element):
        return app.config[_name_element]

    @classmethod
    def set_config(cls, _name_element, _value):
        app.config[_name_element] = _value

    @classmethod
    def del_element_config(cls, _name_element):
        if _name_element not in cls.__default_settings_list:
            app.config.pop(_name_element)

    @classmethod
    def add_new_element_config(cls, _name_element, _value):
        app.config.setdefault(_name_element, _value)
