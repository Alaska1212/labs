import turtle
from datetime import datetime
class Arrow:
    def __init__(self):
        self = None

    def drow(self):
        turtle.left(90)
        turtle.down()
        for i in range(800):
            now = datetime.now()
            dt_string = now.strftime("%S")
            sec = int(dt_string) * 6
            #turtle.left(90)
            #turtle.speed(0)
            turtle.right(sec)
            #turtle.speed(2)
            turtle.forward(150)
            turtle.undo()
            #turtle.speed(0)
            turtle.left(sec)







