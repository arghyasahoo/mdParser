# Standard Library imports

# Custom library imports
from read_file import FileReader
from parser import Parser

reader = FileReader()
content = reader.read_file()

for line in content:
    Parser(line)
