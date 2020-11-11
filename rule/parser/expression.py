from parser.parser import Parser
from parser.state import State
from rule.keyword import Keyword
from rule.parser.keyword import KeywordP


class ExpressionP(Parser):
    def __init__(self):
        pass

    def parse(self, s: State):
        return KeywordP().parse(s)
