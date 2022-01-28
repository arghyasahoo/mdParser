# Custom library imports
from parse_headers import HeaderParser
from parse_rules import RuleParser


class Parser:
    def __init__(self, line):
        HeaderParser(line)
        RuleParser(line)
