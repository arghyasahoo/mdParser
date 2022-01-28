# Standard Library imports
import os
import sys

# Custom library imports
from color import Color


class HeaderParser:
    def __init__(self, line):
        self.currline = line
        self.parse_h1()
        self.parse_h2()
        self.parse_h3()
        self.parse_h4()
        self.parse_h5()
        self.parse_h6()

    def parse_h1(self):
        if self.currline.startswith('# '):
            sys.stdout.write(Color().format(self.currline, 'h1'))
            # NOTE: This will not run in a simulated terminal like Pycharm's terminal
            sys.stdout.write(u'\u2500'*os.get_terminal_size()[0])

    def parse_h2(self):
        if self.currline.startswith('## '):
            sys.stdout.write(Color().format(self.currline, 'h2'))
            # NOTE: This will not run in a simulated terminal like Pycharm's terminal
            sys.stdout.write(u'\u2504'*os.get_terminal_size()[0])

    def parse_h3(self):
        if self.currline.startswith('### '):
            sys.stdout.write(Color().format(self.currline, 'h3'))

    def parse_h4(self):
        if self.currline.startswith('#### '):
            sys.stdout.write(Color().format(self.currline, 'h4'))

    def parse_h5(self):
        if self.currline.startswith('##### '):
            sys.stdout.write(Color().format(self.currline, 'h5'))

    def parse_h6(self):
        if self.currline.startswith('###### '):
            sys.stdout.write(Color().format(self.currline, 'h6'))
