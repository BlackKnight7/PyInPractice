import svgwrite
from new.DiagramFactory import DiagramFactory

class SvgDiagram:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.dwg = svgwrite.Drawing('test.svg', profile='tiny')

    def add(self, component):
        self.dwg.add(component.rows)

    def save(self):
        self.dwg.save()

class SvgRectangle:
    def __init__(self, x, y, width, height, fill, stroke):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = svgwrite.shapes.Rect(insert=(x, y), size=(width, height))

class SvgText:
    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = svgwrite.text.Text(text=text, insert=(x, y), fill='blue')


class SvgDiagramFactory(DiagramFactory):
    def make_diagram(self, width, height):
        return SvgDiagram(width, height)

    def make_rectangle(self, x, y, width, height, fill="white", stroke="black"):
        return SvgRectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return SvgText(x, y, text, fontsize)
