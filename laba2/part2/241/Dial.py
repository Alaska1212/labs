import turtle
from Numbers import One
from Numbers import Two
from Numbers import Three
from Numbers import Four
from Numbers import Five
from Numbers import Six
from Numbers import Seven
from Numbers import Eight
from Numbers import Nine
from Numbers import Ten
from Numbers import Eleven
from Numbers import Twelve
from Arrow import Arrow



class Dial:
    def __init__(self):
        self = None

    def circle(self):
        turtle.right(90)
        turtle.up()
        turtle.forward(230)
        turtle.left(90)
        turtle.down()
        turtle.circle(230)
        turtle.up()



if __name__ == '__main__':
    turtle.speed(50)

    dial = Dial()
    dial.circle()

    three = Three()
    three.drow()

    two = Two()
    two.drow()

    one = One()
    one.drow()

    twelve = Twelve()
    twelve.drow()

    eleven = Eleven()
    eleven.drow()

    ten = Ten()
    ten.drow()

    nine = Nine()
    nine.drow()

    eight = Eight()
    eight.drow()

    seven = Seven()
    seven.drow()

    six = Six()
    six.drow()

    five = Five()
    five.drow()

    four = Four()
    four.drow()

    arrow = Arrow()
    arrow.drow()

turtle.mainloop()