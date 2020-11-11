import unittest

from parser.state import BaseState
from rule.parser.and_p import AndP
from rule.parser.keyword import KeywordP



class TestRule(unittest.TestCase):

    def test_parser(self):
        value = "asdfasdf"
        string = BaseState(f"\"{value}\"")
        p = KeywordP()
        keyword = p.parse(string)
        self.assertEqual(keyword.expression(), value)

        s = f"\"{value}\""
        expr = f"{s} and {s}"
        string = BaseState(expr)
        p = AndP()
        and_expr = p.parse(string)
        print(and_expr.expression())
