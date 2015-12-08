from old.DiagramFactory import DiagramFactory
from old.SvgDiagram import SvgDiagram
from old.SvgRectangle import SvgRectangle
from old.SvgText import SvgText


class SvgDiagramFactory(DiagramFactory):
    def make_diagram(self, width, height):
        return SvgDiagram(width, height)

    def make_rectangle(self, x, y, width, height, fill="white", stroke="black"):
        return SvgRectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return SvgText(x, y, text, fontsize)
