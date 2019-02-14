import turtle

def draw_circle():
    window=turtle.Screen()
    window.bgcolor('red')

    
    degrees=5
    length=100
    man=turtle.Turtle()
    man.speed(300)
    man.color('yellow')
    man.setx(-200)
    man.sety(100)
    for z in range(4):
        for j in range(int(360/degrees)):
            for i in range(4):
                man.forward(length)
                man.right(90)
            man.right(degrees)
        man.forward(length*2)
        man.right(90)
         
    window.exitonclick()

turtle.begin_fill()
draw_circle()
turtle.end_fill()
