from server.src.sqlite.Database import Database
from test.base.TestBase import TestBase


class TEST_Database(TestBase):
    __database: Database

    @classmethod
    def setup_class(cls):
        cls.__database = Database()

    @classmethod
    def teardown_class(cls):
        cls.__database.close()

    @classmethod
    def CASE_execute_insert_error_syntax(cls):
        query = "INSERT INTO brand (brand_name) VALU_ERROR_ES ('TEST_VALUE')"
        assert cls.__database.execute(query) is False

    @classmethod
    def CASE_execute_insert_error_names_table(cls):
        query = "INSERT INTO br_Error_and (brand_name) VALUES ('TEST_VALUE')"
        assert cls.__database.execute(query) is False

    @classmethod
    def CASE_execute_insert(cls):
        query = "INSERT INTO brand (brand_name) VALUES ('TEST_VALUE')"
        assert cls.__database.execute(query) is True

    @classmethod
    def CASE_execute_update(cls):
        query = "UPDATE brand SET brand_name = 'TEST_NEW_VALUE' WHERE brand_name = 'TEST_VALUE'"
        assert cls.__database.execute(query) is True

    @classmethod
    def CASE_execute_select(cls):
        query = "SELECT brand_name FROM brand WHERE brand_name = 'TEST_NEW_VALUE'"
        assert cls.__database.execute(query) is True

    @classmethod
    def CASE_execute_fetchall(cls):
        query = "SELECT brand_name FROM brand WHERE brand_name = 'TEST_NEW_VALUE'"
        assert cls.__database.execute(query) is True
        assert cls.__database.fetchall() == [('TEST_NEW_VALUE',)]

    @classmethod
    def CASE_execute_fetchone(cls):
        query = "SELECT brand_name FROM brand WHERE brand_name = 'TEST_NEW_VALUE'"
        assert cls.__database.execute(query) is True
        assert cls.__database.fetchone() == ('TEST_NEW_VALUE',)

    @classmethod
    def CASE_execute_delete(cls):
        query = "DELETE FROM brand WHERE brand_name = 'TEST_NEW_VALUE'"
        assert cls.__database.execute(query) is True
