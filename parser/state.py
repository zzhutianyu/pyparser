import abc
import typing

E = typing.TypeVar("E")
Tran = typing.TypeVar("Tran")
Status = typing.TypeVar("Status")


class State(abc.ABC):

    @abc.abstractmethod
    def begin(self) -> Tran:
        pass

    @abc.abstractmethod
    def begin_and_tran(self, tran: Tran) -> Tran:
        pass

    @abc.abstractmethod
    def status(self) -> Status:
        pass

    @abc.abstractmethod
    def next(self) -> E:
        pass

    @abc.abstractmethod
    def commit(self, tranction: Tran):
        pass

    @abc.abstractmethod
    def rollback(self, tranction: Tran):
        pass


class BaseState(State):

    def begin_and_tran(self, tran: Tran) -> Tran:
        if self._tran > tran:
            self._tran = tran
        return self._tran

    def begin(self) -> Tran:
        if self._tran == -1:
            self._tran = self._index
        return self._index

    def status(self) -> Status:
        return self._index

    def next(self) -> E:
        if self._index >= len(self._buffer):
            raise EofException
        re: E = self._buffer[self._index]
        self._index +=1
        return re

    def commit(self, tranction: Tran):
        if self._tran == tranction:
            self._tran = -1

    def rollback(self, tranction: Tran):
        if self._tran == tranction:
            self._tran = -1
        self._index = tranction

    def __init__(self, items: typing.Sequence[E]):
        super().__init__()
        self._buffer = items
        self._index = 0
        self._tran = -1


class EofException(Exception):
    pass