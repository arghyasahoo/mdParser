# Standard library imports
import sys

# Custom library imports
from inline_parser import InlineParser


class StrikethroughParser:
    def __init__(self, line):
        self.currline = line
        self.parse_strikethrough()

    def parse_strikethrough(self):
        formatted_line = InlineParser(self.currline, "strikethrough").parse(r"~~")
        sys.stdout.write(formatted_line)
