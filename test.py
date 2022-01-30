from read_file import FileReader
from parse_bold import BoldParser

reader = FileReader()
content = reader.read_file()

for line in content:
    BoldParser(line).parse_bold()
