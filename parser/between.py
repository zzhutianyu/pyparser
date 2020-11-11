from parser.parser import Parser
from parser.state import State


class Between(Parser):
    def __init__(self, left: Parser, mid: Parser, right: Parser):
        self._left = left
        self._mid = mid
        self._right = right

    def parse(self, s: State):
        self._left.parse(s)
        ret = self._mid.parse(s)
        self._right.parse(s)
        return ret

