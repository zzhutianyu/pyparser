from parser.parser import Parser, ParserException
from parser.state import State


class Digit(Parser):

    def parse(self, s: State):
        next: str = s.next()
        if next.isdigit():
            return next
        raise ParserException(s.status(), "")
