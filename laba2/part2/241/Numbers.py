import turtle

class Three():
    def __init__(self):
        self = None

    def drow(self):
        turtle.home()
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

        turtle.up()  #1
        turtle.left(180)
        turtle.forward(30)
        turtle.right(90)
        turtle.down()
        turtle.forward(40)
        turtle.left(140)
        turtle.forward(20)
        turtle.up()

class Eleven:
    def __init__(self):
        self = None

    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(120)
        turtle.forward(180)
        turtle.left(240)
        turtle.down()

        turtle.right(90)
        turtle.forward(20)
        turtle.left(180)
        turtle.forward(40)
        turtle.left(140)
        turtle.forward(20)
        turtle.up()

        turtle.left(40)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.down()
        turtle.forward(40)
        turtle.left(140)
        turtle.forward(20)
        turtle.up()

class Ten:
    def __init__(self):
        self = None
    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(150)
        turtle.forward(180)
        turtle.left(120)

        turtle.down()  # 0
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)


        turtle.up()  # 1
        turtle.forward(25)
        turtle.right(90)
        turtle.down()
        turtle.forward(40)
        turtle.left(140)
        turtle.forward(20)
        turtle.up()

class Nine:
    def __init__(self):
        self = None
    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(180)
        turtle.forward(180)
        turtle.down()
        for i in range(3):
            turtle.forward(20)
            turtle.right(90)
        turtle.forward(40)
        turtle.up()

class Eight:
    def __init__(self):
        self = None
    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(210)
        turtle.forward(180)

        turtle.right(30)
        turtle.down()
        for i in range(3):
            turtle.forward(20)
            turtle.right(90)
        turtle.forward(40)
        for i in range(2):
            turtle.right(90)
            turtle.forward(20)
        turtle.up()

class Seven:
    def __init__(self):
        self = None
    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(240)
        turtle.forward(180)

        turtle.right(60)
        turtle.down()
        turtle.forward(20)
        turtle.right(180)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(40)
        turtle.up()

class Six:
    def __init__(self):
        self = None
    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(270)
        turtle.forward(180)

        turtle.down()
        turtle.left(90)
        turtle.forward(10)
        turtle.left(180)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(40)
        for i in range(3):
            turtle.left(90)
            turtle.forward(20)
        turtle.up()

class Five:
    def __init__(self):
        self = None
    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(300)
        turtle.forward(180)

        turtle.down()
        turtle.left(60)
        turtle.forward(20)
        for i in range(2):
            turtle.right(90)
            turtle.forward(20)
        turtle.right(90)
        turtle.up()
        turtle.forward(20)
        turtle.down()
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)

        turtle.up()

class Four:
    def __init__(self):
        self = None
    def drow(self):
        turtle.home()
        turtle.up()
        turtle.left(330)
        turtle.forward(180)

        turtle.down()
        turtle.left(120)
        turtle.forward(20)
        turtle.left(180)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(180)
        turtle.forward(40)
        turtle.up()
        turtle.home()
