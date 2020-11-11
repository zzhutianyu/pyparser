from parser.attempt import Try
from parser.parser import Parser
from parser.state import State


class Skip(Parser):
    def __init__(self, parser: Parser):
        self._p = Try(parser)

    def parse(self, s: State):
        while True:
            try:
                self._p.parse(s)
            except Exception:
                return
