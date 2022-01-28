# Importing standard libraries
import sys


class FileReader:
    def __init__(self):
        self.len_of_args = len(sys.argv)
        self.filename = ""
    
    def check(self):
        if self.len_of_args == 2:
            self.filename = sys.argv[1]
        elif self.len_of_args < 2:
            sys.stderr.write("Provide a file to read")
        elif self.len_of_args > 2:
            sys.stderr.write("Too many files passed. Provide only one file at a time")
        else:
            sys.stderr.write("Unexpected error occurred")

    def read_file(self):
        self.check()
        fd = open(self.filename, 'r')
        data = fd.readlines()
        return data
