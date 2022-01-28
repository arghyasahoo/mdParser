# Standard Library imports

# Custom library imports
from read_file import FileReader
from parser import Parser

reader = FileReader()
content = reader.read_file()

# print(''.join(content))

for line in content:
    Parser(line)

print("\033[38;5;42mHello World\033[0m")