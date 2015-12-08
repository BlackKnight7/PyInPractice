class SvgRectangle:
    def __init__(self, x, y, width, height, fill, stroke):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = [list("#")]