import svgwrite

dwg = svgwrite.Drawing('test.svg', profile='tiny')
svgLine = dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%'))
svgText = dwg.text('Test', insert=(0, 0.2), fill='red')
dwg.save()
