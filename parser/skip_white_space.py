from parser.parser import Parser
from parser.skip import Skip
from parser.state import State
from parser.white_space import WhiteSpace


class SkipWhiteSpace(Parser):

    def parse(self, s: State):
        return Skip(WhiteSpace()).parse(s)
