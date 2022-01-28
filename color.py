class Color:
    def __init__(self, line, component_type):
        # TODO: Select a color scheme for color_map
        self.color_map = dict()
        self.clear = '\033[0m'

        self.format(line, component_type)

    def format(self, line, component_type):
        return self.color_map[component_type] + line + self.clear
