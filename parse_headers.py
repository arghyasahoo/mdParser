# Standard Library imports
import sys

# Custom library imports
from color import Color


class ParseHeaders:
    def __init__(self):
        self.currLine = ""

    def parse_h1(self):
        if self.currLine.startswith('# '):
            sys.stdout.write(Color(self.currLine, 'h1'))

    def parse_h2(self):
        if self.currLine.startswith('## '):
            sys.stdout.write(Color(self.currLine, 'h2'))

    def parse_h3(self):
        if self.currLine.startswith('### '):
            sys.stdout.write(Color(self.currLine, 'h3'))

    def parse_h4(self):
        if self.currLine.startswith('#### '):
            sys.stdout.write(Color(self.currLine, 'h4'))

    def parse_h5(self):
        if self.currLine.startswith('##### '):
            sys.stdout.write(Color(self.currLine, 'h5'))

    def parse_h6(self):
        if self.currLine.startswith('###### '):
            sys.stdout.write(Color(self.currLine, 'h6'))

