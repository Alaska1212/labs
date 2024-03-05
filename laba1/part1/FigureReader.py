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
        with open(self.file_name, "r") as f:
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

