from random import randint
from Triangle import Triangle


trangles = []
for i in range(100):
    x1 = randint(-100, 100)
    y1 = randint(-100, 100)
    x2 = randint(-100, 100)
    y2 = randint(-100, 100)
    t = Triangle(x1, y1, x2, y2)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = r << 16 | g << 8 | b
