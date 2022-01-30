# Standard library imports
import re

# Custom library imports
from color import Color


class InlineParser:
    def __init__(self, line, ftype):
        self.currline = line
        self.format_type = ftype
        self.word_positions = []

    def parse(self, pattern1, pattern2=None):
        self.find_positions(pattern1)
        if pattern2 is not None:
            self.find_positions(pattern2)

        formatted_line = ""
        for i in range(len(self.word_positions)):
            if len(self.word_positions) == 1:
                formatted_line += (
                    self.currline[: self.word_positions[i][0] - 2]
                    + Color().format(
                        self.currline[
                            self.word_positions[i][0] : self.word_positions[i][1]
                        ],
                        self.format_type,
                    )
                    + self.currline[self.word_positions[i][1] + 2 :]
                )

            else:
                if i - 1 < 0:
                    formatted_line += self.currline[
                        : self.word_positions[i][0] - 2
                    ] + Color().format(
                        self.currline[
                            self.word_positions[i][0] : self.word_positions[i][1]
                        ],
                        self.format_type,
                    )

                elif i + 1 >= len(self.word_positions):
                    formatted_line += self.currline[
                        self.word_positions[i - 1][1]
                        + 2 : self.word_positions[i][0]
                        - 2
                    ] + (
                        Color().format(
                            self.currline[
                                self.word_positions[i][0] : self.word_positions[i][1]
                            ],
                            self.format_type,
                        )
                        + self.currline[self.word_positions[i][1] + 2 :]
                    )

                else:
                    formatted_line += self.currline[
                        self.word_positions[i - 1][1]
                        + 2 : self.word_positions[i][0]
                        - 2
                    ] + Color().format(
                        self.currline[
                            self.word_positions[i][0] : self.word_positions[i][1]
                        ],
                        self.format_type,
                    )
        return formatted_line

    def find_positions(self, pattern):
        flag = True
        x, y = -1, -1
        for match in re.finditer(pattern, self.currline):
            if flag:
                x = match.end()
                flag = False
            else:
                y = match.start()
                self.word_positions.append([x, y])
                flag = True

        # if self.word_positions:
        #     print(self.word_positions)
