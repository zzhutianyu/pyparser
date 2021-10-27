from parser.parser import Parser, ParserException
from parser.state import State, EofException


class Eof(Parser):

    def parse(self, s: State):
        try:
            s.next()
            raise ParserException(s.status(), "expect eof")
        except EofException:
            return