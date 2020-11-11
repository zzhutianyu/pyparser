import abc

from parser.state import State




class Parser(abc.ABC):

    @abc.abstractmethod
    def parse(self, s: State):
        pass

    def bind(self, other: "Parser") -> "Parser":
        @ParserFunc
        def _parser(s: State):
            self.parse(s)
            return other.parse(s)
        return _parser

    def __rshift__(self, other):
        return self.bind(other)

    def __or__(self, other):
        from parser.choice import Choice
        return Choice([self, other])


class ParserFunc(Parser):
    def __init__(self, func):
        self._func = func

    def parse(self, s: State):
        return self._func(s)


class ParserException(Exception):

    def __init__(self, status, message):
        pass
