import svgwrite


class SvgDiagram:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.dwg = svgwrite.Drawing('test.svg', profile='tiny')

    def add(self, component):
        self.dwg.add(component.rows)

    def save(self):
        self.dwg.save()
