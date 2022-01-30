# Custom library imports
from parse_headers import HeaderParser
from parse_rules import RuleParser
from parse_bold import BoldParser
from parse_italics import ItalicsParser
from parse_strikethrough import StrikethroughParser


class Parser:
    def __init__(self, line):
        HeaderParser(line)
        RuleParser(line)
        BoldParser(line)
        ItalicsParser(line)
        StrikethroughParser(line)
