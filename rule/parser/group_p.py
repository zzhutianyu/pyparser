from parser.between import Between
from parser.ch import Ch
from parser.parser import Parser
from parser.skip_white_space import SkipWhiteSpace
from parser.state import State
from rule.group import Group


class GroupP(Parser):
    def __init__(self):
        from rule.parser.expression import ExpressionP
        skip = SkipWhiteSpace()
        self._p = Between(skip >> Ch("(") >> skip, ExpressionP(), skip >> Ch(")") >> skip)

    def parse(self, s: State):
        expr = self._p.parse(s)
        return Group(expr)