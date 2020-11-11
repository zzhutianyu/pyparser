from parser.parser import Parser, ParserException
from parser.state import State


class WhiteSpace(Parser):

    def parse(self, s: State):
        space = s.next()
        if space.isspace():
            return space
        raise ParserException(s.status(), f"expect a whitespace but get {space}")
