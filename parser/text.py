from parser.parser import Parser, ParserException
from parser.state import State


class Text(Parser):
    def __init__(self, text: str, case_sensitive = True):
        self._case_sensitive = case_sensitive
        self._content = text if case_sensitive else text.lower()

    def parse(self, s: State):
        text = ""
        for char in self._content:
            s_temp = s.next()
            compare_char = s_temp if self._case_sensitive else s_temp.lower()
            if compare_char != char:
                raise ParserException(s.status(), f"expect {char} but {compare_char}")
            text += compare_char
        return text
