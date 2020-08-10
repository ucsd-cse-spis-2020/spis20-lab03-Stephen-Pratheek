#Stephen - a program to draw the first letter of your name

import turtle

def drawFirstInitial(theTurtle):
    '''
    Drawing the first initial of my first name: Stephen
    Parameters:
        theTurtle - a turtle object
    '''
    theTurtle.backward(25)
    theTurtle.right(90)
    theTurtle.forward(50)
    theTurtle.left(90)
    theTurtle.forward(25)
    theTurtle.right(90)
    theTurtle.forward(50)
    theTurtle.right(90)
    theTurtle.forward(25)

firstInitial = turtle.Turtle()
secondInitial = turtle.Turtle()
drawFirstInitial(firstInitial)

secondInitial.penup()
secondInitial.setpos(0,150)
secondInitial.pendown()
drawFirstInitial(secondInitial)