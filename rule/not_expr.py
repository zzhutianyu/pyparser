from rule.expression import Expression


class Not(Expression):
    def __init__(self, expr: Expression):
        self._expr = expr

    def expression(self) -> str:
        return f"not {self._expr.expression()}"