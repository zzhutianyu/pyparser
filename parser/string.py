from parser.attempt import Try
from parser.ch import Ch
from parser.digit import Digit
from parser.letter import Letter
from parser.many import Many
from parser.parser import Parser
from parser.state import State


class String(Parser):

    def parse(self, s: State):
        p = (Try(Digit()) | Try(Letter()))
        return Many(p).parse(s)
