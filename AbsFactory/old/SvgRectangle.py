import svgwrite


class SvgRectangle:
    def __init__(self, x, y, width, height, fill, stroke):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = svgwrite.shapes.Rect(insert=(x, y), size=(width, height))
