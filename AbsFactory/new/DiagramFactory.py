class DiagramFactory:
    def __init__(self):
        pass

    class Diagram:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.diagram = [['*' for x in range(width)] for y in range(height)]

        def add(self, component):
            for y, row in enumerate(component.rows):
                for x, char in enumerate(row):
                    self.diagram[y + component.y][x + component.x] = char

        def save(self):
            print(self.diagram)

    class Rectangle:
        def __init__(self, x, y, width, height, fill, stroke):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.rows = [['%'] * width] * height

    class Text:
        def __init__(self, x, y, text, fontsize):
            self.x = x
            self.y = y
            self.rows = [list(text)]

    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)

    @classmethod
    def make_rectangle(Class, x, y, width, height, fill="white", stroke="black"):
        return Class.Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(Class, x, y, text, fontsize=12):
        return Class.Text(x, y, text, fontsize)
