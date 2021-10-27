import unittest

from parser.state import BaseState
from rule.parser.and_p import AndP
from rule.parser.expression import ExpressionP
from rule.parser.keyword import KeywordP



class TestRule(unittest.TestCase):

    def test_keyword(self):
        value = "asdfasdf"
        string = BaseState(f"\"{value}\"\"\"")
        p = ExpressionP()
        keyword = p.parse(string)
        self.assertEqual(keyword.expression(), value)


    def test_and(self):
        value = "asdfasdf"
        s = f"\"{value}\""
        expr = f"{s} and {s}"
        string = BaseState(expr)
        p = ExpressionP()
        and_expr = p.parse(string)
        print(and_expr.expression())

    def test_not(self):
        value = "asdfasdf"
        s = f"\"{value}\""
        expr = f"not {s}"
        string = BaseState(expr)
        p = ExpressionP()
        and_expr = p.parse(string)
        print(and_expr.expression())

    def test_or(self):
        value = "asdfasdf"
        s = f"\"{value}\""
        expr = f"{s}or {s}"
        string = BaseState(expr)
        p = ExpressionP()
        and_expr = p.parse(string)
        print(and_expr.expression())

    def test_group(self):
        value = "asdfasdf"
        s = f"\"{value}\""
        expr = f"({s}) or {s}"
        string = BaseState(expr)
        p = ExpressionP()
        and_expr = p.parse(string)
        print(and_expr.expression())

    def test_parser(self):
        value = "asdfasdf"
        s = f"\"{value}\""
        expr = f"({s}) or {s} and {s} or ({s} and (({s} and {s})))"
        string = BaseState(expr)
        p = ExpressionP()
        and_expr = p.parse(string)
        print(and_expr.expression())
