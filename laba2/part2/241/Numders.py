import turtle

class Three():
    def __init__(self):
        self = None

    def drow(self):
        turtle.up()   #Підняти пензель
        turtle.forward(180) #Зміститися вперед на
        turtle.down()#Опустити пензель
        for i in range(3):
            turtle.forward(20)
            turtle.left(90)  #Поворот вліво на кут
        turtle.up()
        turtle.forward(40)
        turtle.down()
        for i in range(2):
            turtle.left(90)
            turtle.forward(20)
        turtle.up()



class Two():
    def __init__(self):
        self = None
    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(30)
        turtle.forward(180)
        turtle.right(30)
        turtle.down()
        for i in range(2):
            turtle.forward(20)
            turtle.left(90)

        turtle.forward(20)
        turtle.up()

        turtle.left(90)
        turtle.forward(20)
        turtle.down()
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.up()


class One:
    def __init__(self):
        self = None

    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(60)
        turtle.forward(180)
        turtle.right(60)
        turtle.down()

        turtle.right(90)
        turtle.forward(20)
        turtle.left(180)
        turtle.forward(40)
        turtle.left(140)
        turtle.forward(20)
        turtle.up()


class Twelve:
    def __init__(self):
        self = None

    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(90)
        turtle.forward(195)
        turtle.right(90)

        turtle.down()  # 2
        for i in range(2):
            turtle.forward(20)
            turtle.right(90)
        for i in range(2):
            turtle.forward(20)
            turtle.left(90)
        turtle.forward(20)

        turtle.up()
        turtle.left(180)
        turtle.forward(30)
        turtle.right(90)
        turtle.down()
        turtle.forward(40)
        turtle.left(140)
        turtle.forward(20)


if __name__ == '__main__':
    turtle.speed(0)

    three = Three()
    three.drow()

    two = Two()
    two.drow()

    one = One()
    one.drow()

    twelve = Twelve()
    twelve.drow()

turtle.mainloop()