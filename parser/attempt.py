from parser.parser import Parser
from parser.state import State


class Try(Parser):

    def __init__(self, parser: Parser):
        self._parser = parser

    def parse(self, s: State):
        tran = s.begin()
        try:
            ret = self._parser.parse(s)
        except Exception:
            s.rollback(tran)
            raise
        s.commit(tran)
        return ret
