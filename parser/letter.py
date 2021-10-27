from parser.parser import Parser, ParserException
from parser.state import State


class Letter(Parser):
    def parse(self, s: State):
        next: str = s.next()
        if next.isalpha():
            return next
        raise ParserException(s.status(), "")
