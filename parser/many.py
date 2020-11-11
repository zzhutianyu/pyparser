from parser.parser import Parser
from parser.state import State


class Many(Parser):
    def __init__(self, parser: Parser):
        self._parser = parser

    def parse(self, s: State):
        ret = ""
        while True:
            try:
                ret = ret + self._parser.parse(s)
            except Exception:
                return ret
