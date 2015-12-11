from old.DiagramFactory import DiagramFactory
from old.SvgDiagramFactory import SvgDiagramFactory


def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


def main():
    # create txt Diagram
    txtDiagram = create_diagram(DiagramFactory())
    txtDiagram.show()

    # create svg Diagram
    # svgDiagram = create_diagram(SvgDiagramFactory())
    # svgDiagram.show()
    pass

if __name__ == '__main__':
    main()
