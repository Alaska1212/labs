import turtle
from random import randint

class Triangle:
    default_color = None
    def __init__(self, x1, y1, x2, y2):
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)
        self.color = None

        self.position = (randint(-200, 200), randint(-200, 200))

    def set_position(self, x, y):
        x = randint(-100, 100)
        y = randint(-100, 100)
        self.position = (x, y)


    def calc_abs_pos(self):
        v1 = (self.position[0] + self.vertex1[0],
              self.position[1] + self.vertex1[1])
        v2 = (self.position[0] + self.vertex2[0],
              self.position[1] + self.vertex2[1])
        return v1, v2
    def draw(self):
        v1, v2 = self.calc_abs_pos()
        random_color = "#{:06x}".format(randint(0, 0xFFFFFF))
        turtle.color(random_color)
        turtle.up()
        turtle.setpos(*self.position)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.position)
        turtle.up()



if __name__ == '__main__':
    turtle.speed(0)

    for i in range(100):
        triangle = Triangle((randint(-100, 100)), (randint(-100, 100)), (randint(-100, 100)), (randint(-100, 100)))
        triangle.draw()
        triangle.set_position(-2 * i, -i)
        triangle.draw()

turtle.mainloop()