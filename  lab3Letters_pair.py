'''
Stephen + Pratheek - drawing pratheek's first initial in a specific size and answering questions

Answers to Step 2.0 questions

1) The anonymous turtle is the turtle that is no longer represented by a variable and is therefore lost. Although lost, the turtle is still present in the canvas and its memory location.

2)
myTurtle = turtle.Turtle()
drawPicture(myTurtle) 

turtle represents the library that the name is referring and Turtle represents the method in that library.

3) myTurtle.setpos(0, 100)
'''

import turtle

def drawP(theTurtle, size):
    ''' Draw a letter P given a turtle object and its desired size
    Parameters:
        theTurtle - turtle object
        size - desired size of pen
    '''
    theTurtle.pensize(size)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.forward(100)

firstInitial = turtle.Turtle()
drawP(firstInitial, 20)