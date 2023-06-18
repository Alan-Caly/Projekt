import pytest

from server.src.server.ServerConfig import ServerConfig
from test.base.TestBase import TestBase


class TEST_ServerConfig(TestBase):
    __configServer: ServerConfig

    @classmethod
    def setup_class(cls):
        cls.__configServer = ServerConfig()

    @classmethod
    def teardown_class(cls):
        pass

    @classmethod
    def CASE_new_setting_add(cls):
        nameSetting = 'TEST_NAME'
        valueSetting = 'TEST_VALUE'

        cls.__configServer.new_setting_add(nameSetting, valueSetting)
        assert cls.__configServer.get_setting(nameSetting) == valueSetting

    @classmethod
    def CASE_new_setting_add_duplicate(cls):
        nameSetting = 'TEST_NAME'
        valueSetting = 'TEST_VALUE'

        with pytest.raises(Exception):
            cls.__configServer.new_setting_add(nameSetting, valueSetting)

    @classmethod
    def CASE_get_setting(cls):
        nameSetting = 'TEST_NAME'
        valueSetting = 'TEST_VALUE'

        assert cls.__configServer.get_setting(nameSetting) == valueSetting

    @classmethod
    def CASE_get_dev_settings(cls):
        assert cls.__configServer.get_dev_settings() == ['TEST_NAME']

    @classmethod
    def CASE_update_setting(cls):
        nameSetting = 'TEST_NAME'
        valueSetting = 'TEST_NEW_VALUE'

        cls.__configServer.update_setting(nameSetting, valueSetting)
        assert cls.__configServer.get_setting(nameSetting) == valueSetting

    @classmethod
    def CASE_update_setting_error(cls):
        nameSetting = 'TEST_NAME_ERROR'
        valueSetting = 'TEST_NEW_VALUE'

        with pytest.raises(Exception):
            cls.__configServer.update_setting(nameSetting, valueSetting)

    @classmethod
    def CASE_delete_setting(cls):
        nameSetting = 'TEST_NAME'

        cls.__configServer.delete_setting(nameSetting)
        assert cls.__configServer.get_setting(nameSetting) is None