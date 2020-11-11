from parser.parser import Parser, ParserException
from parser.state import State


class Ch(Parser):

    def __init__(self, ch: str, case_sensitive = True):
        self._case_sensitive = case_sensitive
        self._ch = ch if case_sensitive else ch.lower()

    def parse(self, s: State):
        string = s.next()
        if self._case_sensitive:
            if string == self._ch:
                return self._ch
        else:
            if string.lower() == self._ch:
                return self._ch
        raise ParserException(s.status(), f"expect {self._ch} but {string}")

