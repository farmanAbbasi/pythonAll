import turtle
import random

class Square:
    def __init__(self, x, y):
        print('in constructor')
        self.x = x
        self.y = y

    def drawself(self, turtle):
        # draw a black box at its coordinates, leaving a small gap between cubes
        print('in drawself')
        turtle.goto(self.x - 9, self.y - 9)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(18)
            turtle.left(90)
        turtle.end_fill()

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "ON"

    def changelocation(self):
        # I haven't programmed it to spawn outside the snake's body yet
        self.x = random.randint(0, 20)*20 - 200
        self.y = random.randint(0, 20)*20 - 200

    def drawself(self, turtle):
        # similar to the Square drawself, but blinks on and off
        if self.state == "ON":
            turtle.goto(self.x - 9, self.y - 9)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(18)
                turtle.left(90)
            turtle.end_fill()

    def changestate(self):
        # controls the blinking
        self.state = "OFF" if self.state == "ON" else "ON"        

sq=Square(-20,0)
sq.drawself(turtle)

sq1=Square(0,0)
sq1.drawself(turtle)

sq2=Square(20,0)
sq2.drawself(turtle)


sq3=Square(20,20)
sq3.drawself(turtle)

i=10
while(i<100):
    fd=Food(30,30+i)
    
    fd.drawself(turtle)
    fd.changestate()
    i+=10

        
