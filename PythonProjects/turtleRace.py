from turtle import *
from random import randint

def turtleRace():
    window=Screen()
    window.setup(800,800)
    window.bgcolor('gray')
    
    speed(500)
    penup()
    setx(-300)
    trackLength=0
    track=30 #change it to increase length of track on board
    for i in range(1,track):
        write(i,align='center')
        right(90)
        forward(10)
        pendown()
        forward(200)
        penup()
        backward(210)
        left(90)
        forward(40)
        trackLength+=40

    print(trackLength)
    winnerLength=0
    lrun=0
    l2run=0
    l3run=0
    l4run=0
    bob=Turtle()
    bob.color('blue')
    bob.shape('turtle')
    bob.penup()
    bob.goto(-320,-30)
    bob.pendown()

    bob2=Turtle()
    bob2.color('yellow')
    bob2.shape('turtle')
    bob2.penup()
    bob2.goto(-320,-80)
    bob2.pendown()

    bob3=Turtle()
    bob3.color('red')
    bob3.shape('turtle')
    bob3.penup()
    bob3.goto(-320,-130)
    bob3.pendown()
    
    bob4=Turtle()
    bob4.color('green')
    bob4.shape('turtle')
    bob4.penup()
    bob4.goto(-320,-180)
    bob4.pendown()

    while(trackLength>winnerLength):
        
        l=randint(1,5)
        lrun+=l
        bob.forward(l)
        l2=randint(1,5)
        l2run+=l2
        bob2.forward(l2)
        l3=randint(1,5)
        l3run+=l3
        bob3.forward(l3)
        l4=randint(1,5)
        l4run+=l4
        bob4.forward(l4)
        winnerLength=max(lrun,l2run,l3run,l4run)
        print(lrun,l2run,l3run,l4run)
        print(winnerLength)
                          
    if(winnerLength==lrun):
        bob.write("      winner!!")
    elif(winnerLength==l2run):
        bob2.write("      winner!!")
    elif(winnerLength==l3run):
        bob3.write("      winner!!")
    else:
        bob4.write("      winner!!")


turtleRace()    






