# Standard library imports
import sys

# Custom library imports
from inline_parser import InlineParser


class ItalicsParser:
    def __init__(self, line):
        self.currline = line
        self.parse_italics()

    def parse_italics(self):
        formatted_line = InlineParser(self.currline, "italics").parse(
            "^\*[^*]+$", "^\_[^_]+$"
        )
        sys.stdout.write(formatted_line)
