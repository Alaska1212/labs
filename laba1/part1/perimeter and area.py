from laba1.part1.FigureReader import FigureReader

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


file_path = 'input02.txt'

reader = FigureReader(file_path)
figures_list = reader.read()

max_area_figure = max_area(figures_list)
max_perimeter_figure = max_perimeter(figures_list)


print(f"Фігура з найбільшою площею {max_area_figure.__class__.__name__} : {max_area_figure.area()}")
print(f"Фігура з найбільшим периметром {max_perimeter_figure.__class__.__name__} : {max_perimeter_figure.perimeter()}")
