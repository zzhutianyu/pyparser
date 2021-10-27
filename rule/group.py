from rule.expression import Expression


class Group(Expression):

    def __init__(self, expr: Expression):
        self._expr = expr

    def expression(self) -> str:
        return f"({self._expr.expression()})"