import turtle

def gotoandprint(x, y):
    
    gotoresult = turtle.goto(x, y)
    #print(turtle.xcor(),turtle.ycor())
    return gotoresult


def clickToPaintUsingTurtle():
    '''as this onscrenfunction
    requires a two arg function which
    returns two coordinates to print
    '''
    turtle.title("Welcome to the turtle zoo!")
    turtle.onscreenclick(gotoandprint)
    

clickToPaintUsingTurtle()



    
