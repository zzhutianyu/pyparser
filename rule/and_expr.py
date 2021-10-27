from rule.expression import Expression


class And(Expression):

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def expression(self) -> str:
        return f"{self._left.expression()} and test {self._right.expression()}"