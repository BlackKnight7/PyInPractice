import svgwrite
from new.DiagramFactory import DiagramFactory


class SvgDiagramFactory(DiagramFactory):
    class Diagram:
        def __init__(self, width, height):
            self.height = height
            self.width = width
            self.dwg = svgwrite.Drawing('test.svg', profile='tiny')

        def add(self, component):
            self.dwg.add(component.rows)

        def save(self):
            self.dwg.save()

    class Rectangle:
        def __init__(self, x, y, width, height, fill, stroke):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.rows = svgwrite.shapes.Rect(insert=(x, y), size=(width, height))

    class Text:
        def __init__(self, x, y, text, fontsize):
            self.x = x
            self.y = y
            self.rows = svgwrite.text.Text(text=text, insert=(x, y), fill='blue')

    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)

    @classmethod
    def make_rectangle(Class, x, y, width, height, fill="white", stroke="black"):
        return Class.Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(Class, x, y, text, fontsize=12):
        return Class.Text(x, y, text, fontsize)
