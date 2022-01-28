# Standard library imports
import os
import sys


class RuleParser:
    def __init__(self, line):
        self.currline = line
        self.parse_horizontal_rule()

    def parse_horizontal_rule(self):
        if self.currline.strip() == '___' or self.currline.strip() == '**'+'*':
            sys.stdout.write('\n\n')
            # NOTE: This will not run in a simulated terminal like Pycharm's terminal
            sys.stdout.write(u'\u2501'*os.get_terminal_size()[0])
            sys.stdout.write('\n\n')
