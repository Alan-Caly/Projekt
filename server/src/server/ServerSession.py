from server import session


class Session:
    """Session class"""
    @classmethod
    def get_element(cls, _name: str) -> any:
        """
        Get element from session

        :param _name: Name of the element session
        :return: Returns the element session
        """
        return session[_name]

    @classmethod
    def set_element(cls, _name: str, _value: any) -> None:
        """
        Set element in session

        :param _name: Name of the element session
        :param _value: Value of the element session
        """
        session.setdefault(_name, _value)

    