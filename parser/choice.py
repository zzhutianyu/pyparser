import typing

from parser.parser import Parser
from parser.state import State


class Choice(Parser):

    def __init__(self, parsers: typing.Sequence[Parser]):
        self._parsers = parsers

    def parse(self, s: State):
        status = s.status()
        err = None
        for parser in self._parsers:
            try:
                return parser.parse(s)
            except Exception as e:
                err = e
                if status != s.status():
                    raise e
