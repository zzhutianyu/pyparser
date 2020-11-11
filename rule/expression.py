import abc


class Expression(abc.ABC):
    @abc.abstractmethod
    def expression(self) -> str:
        pass
