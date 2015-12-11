class Diagram:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.diagram = [['*' for x in range(width)] for y in range(height)]

    def add(self, component):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char

    def show(self):
        print(self.diagram)
