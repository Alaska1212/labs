import turtle
turtle.shape("turtle")
from random import randint

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)

        self.position = (0,0)

    def calc_abs_pos(self):
        v1 = (self.position[0] + self.vertex1[0],
              self.position[1] + self.vertex1[1])
        v2 = (self.position[0] + self.vertex2[0],
              self.position[1] + self.vertex2[1])
        return v1, v2

    def draw(self):
        v1, v2 = self.calc_abs_pos()
        turtle.up()
        turtle.setpos(*self.position)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.position)
        turtle.up()

if __name__ == '__main__':
    turtle.speed(1)
    triangle = Triangle((randint(-100, 200)), (randint(-100, 200)), (randint(-100, 200)), (randint(-100, 200)))

for _ in range(120):
    triangle.draw()
    turtle.clear()
    triangle.draw()
turtle.mainloop()