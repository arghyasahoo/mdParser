# Standard library imports
import json

# Custom Library imports
from color_map import color_map


class Color:
    def __init__(self):
        # TODO: Select a color scheme for color_map
        # TODO:Find a way to load this dict from a json file
        self.color_map = color_map
        self.clear = '\033[0m'

    def format(self, line, component_type):
        return self.color_map[component_type] + line + self.clear
