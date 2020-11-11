from rule.expression import Expression


class Not(Expression):
    def __init__(self, expr: Expression):
        self._expr = expr

    def expression(self) -> str:
        pass