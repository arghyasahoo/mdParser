# Standard library imports
import re


class BoldParser:
    def __init__(self, line):
        self.currline = line

    def parse_bold(self):
        for match in re.finditer(r"**", self.currline):
            start = match.start()
            end = match.end()

            # split line at these positions
            # individually format each piece
