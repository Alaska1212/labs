from laba1.part1.Triangle import Triangle
from laba1.part1.Rectangle import Rectangle
from laba1.part1.Trapeze import Trapeze
from laba1.part1.Parallelogram import Parallelogram
from laba1.part1.Circle import Circle

class FigureReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        figures = []
        with open(self.file_name) as f:
            for line in f:
                data = line.split()
                type = data[0]
                try:
                    if type == "Triangle":
                        a, b, c = [float(el) for el in data[1:]]
                        triangle = Triangle(a, b, c)
                        figures.append(triangle)
                    elif type == "Rectangle":
                        a, b = [float(el) for el in data[1:]]
                        rectangle = Rectangle(a, b)
                        figures.append(rectangle)
                    elif type == "Trapeze":
                        a, b, c, d = [float(el) for el in data[1:]]
                        trapeze = Trapeze(a, b, c, d)
                        figures.append(trapeze)
                    elif type == "Parallelogram":
                        a, b, h = [float(el) for el in data[1:]]
                        parallelogram = Parallelogram(a, b, h)
                        figures.append(parallelogram)
                    elif type == "Circle":
                        a = float(data[1])
                        circle = Circle(a)
                        figures.append(circle)
                except AssertionError:
                    pass
        return figures

def max_area(figures):
    max_area = 0
    max_area_figure = None

    for figure in figures:
        area = figure.area()
        if area is not None and area > max_area:
            max_area = area
            max_area_figure = figure
    return max_area_figure


def max_perimeter(figures):
    max_perimeter = 0
    max_perimeter_figure = None

    for figure in figures:
        perimeter = figure.perimeter()
        if perimeter > max_perimeter:
            max_perimeter = perimeter
            max_perimeter_figure = figure
    return max_perimeter_figure

reader = FigureReader("input02.txt")
figures_list = reader.read()
max_area_figure = max_area(figures_list)
max_perimeter_figure = max_perimeter(figures_list)
