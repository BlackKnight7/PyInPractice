import svgwrite


class SvgText:
    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = svgwrite.text.Text(text=text, insert=(x, y), fill='blue')
