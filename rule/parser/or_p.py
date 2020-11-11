from parser.parser import Parser
from parser.skip_white_space import SkipWhiteSpace
from parser.state import State
from parser.text import Text
from rule.or_expr import Or


class OrP(Parser):
    def __init__(self):
        from rule.parser.expression import ExpressionP
        self._e_p = ExpressionP()
        skip = SkipWhiteSpace()
        self._p = skip >> Text("or", False) >> skip

    def parse(self, s: State):
        left = self._e_p.parse(s)
        self._p.parse(s)
        right = self._e_p.parse(s)
        return Or(left, right)
