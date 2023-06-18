from abc import ABC, abstractmethod


class TestBase(ABC):
    """Base class for all tests."""

    @abstractmethod
    def setup_class(self):
        pass

    @abstractmethod
    def teardown_class(self):
        pass
