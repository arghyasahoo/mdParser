# Standard library imports
import sys

# Custom library imports
from inline_parser import InlineParser


class BoldParser:
    def __init__(self, line):
        self.currline = line
        self.parse_bold()

    def parse_bold(self):
        formatted_line = InlineParser(self.currline, "bold").parse(r"\*\*", r"\_\_")
        sys.stdout.write(formatted_line)
