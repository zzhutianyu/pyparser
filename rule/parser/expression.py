from parser.attempt import Try
from parser.between import Between
from parser.eof import Eof
from parser.parser import Parser
from parser.skip_white_space import SkipWhiteSpace
from parser.state import State
from rule.keyword import Keyword
from rule.parser.and_p import AndP
from rule.parser.group_p import GroupP
from rule.parser.keyword import KeywordP
from rule.parser.not_p import NotP
from rule.parser.or_p import OrP


class ExpressionP(Parser):
    def __init__(self):
        pass

    def parse(self, s: State):
        keyword = Try(KeywordP())
        group_p = GroupP()
        not_p = Try(NotP())
        np = Try(not_p | keyword | group_p)
        expr = np.parse(s)
        skip = SkipWhiteSpace()
        try:
            Try(skip.parse(s))
            Try(Eof()).parse(s)
        except Exception as e:
            and_p = Try(AndP(expr))
            or_p = Try(OrP(expr))
            p = Try(Between(skip, Try(and_p | or_p) , skip))
            try:
                return p.parse(s)
            except Exception:
                return expr
        return expr
