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


if __name__ == '__main__':
    turtle.speed(1)
    three = Three()
    three.drow()
    two = Two()
    two.drow()


turtle.mainloop()