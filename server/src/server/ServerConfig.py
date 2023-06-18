from server import app


class ServerConfig:
    """Server configuration"""
    __settings_list: list

    @classmethod
    def __init__(cls):
        cls.__settings_list = list()

    @classmethod
    def new_setting_add(cls, _nameSetting: str, _valueSetting: str) -> None:
        """
        Add new setting to flask config

        :param _nameSetting: Name of setting
        :param _valueSetting: Value of setting
        """
        if _nameSetting not in cls.__settings_list:
            cls.__settings_list.append(_nameSetting)
            app.config[_nameSetting] = _valueSetting

        else:
            raise Exception('Setting already exists')

    @classmethod
    def get_setting(cls, _nameSetting: str) -> any:
        """
        Get setting

        :param _nameSetting: Name of setting
        :return: Return value of setting if exists, None otherwise
        """
        try:
            return app.config[_nameSetting]
        except KeyError:
            return None

    @classmethod
    def get_dev_settings(cls) -> list:
        """
        Get all settings for development

        :return: Return all settings for development in a list
        """
        return cls.__settings_list

    @classmethod
    def update_setting(cls, _nameSetting: str, _valueSetting: str) -> None:
        """
        Update setting

        :param _nameSetting:  Name of setting
        :param _valueSetting: Value of setting
        """
        if _nameSetting in cls.__settings_list:
            app.config[_nameSetting] = _valueSetting

        else:
            raise Exception('Setting not found')

    @classmethod
    def delete_setting(cls, _nameSetting: str) -> None:
        """
        Delete setting

        :param _nameSetting: Name of setting
        """
        if _nameSetting in cls.__settings_list:
            cls.__settings_list.remove(_nameSetting)
            app.config.pop(_nameSetting)

        else:
            raise Exception('Setting not found')
