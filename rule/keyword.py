from rule.expression import Expression


class Keyword(Expression):

    def __init__(self, value: str):
        self._value = value

    def expression(self):
        return self._value
