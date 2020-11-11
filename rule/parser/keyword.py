from parser.attempt import Try
from parser.between import Between
from parser.ch import Ch
from parser.parser import Parser
from parser.state import State
from parser.string import String
from rule.keyword import Keyword


class KeywordP(Parser):
    def __init__(self):
        string = String()
        single = Between(Ch("\'"), string, Ch("\'"))
        double = Between(Ch("\""), string, Ch("\""))
        self._p = Try(single) | double

    def parse(self, s: State):
        return Keyword(self._p.parse(s))
