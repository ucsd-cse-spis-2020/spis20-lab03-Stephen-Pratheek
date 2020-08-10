#Pratheek S. Math-CS from Warren
#SPIS 2020
#The purpose of the file is to explore the usage of the turtle Module

import turtle
#The function draws the letter P
#The parameter is a turtle type object

def drawP(theTurtle):
    ''' Draw a simple picture using a turtle '''
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.forward(100)
    

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle2.penup()

turtle2.setpos(50, 50)
'''
turtle1.forward(100)
turtle2.left(90)
turtle2.forward(100)
'''
drawP(turtle1)
turtle2.pendown()
drawP(turtle2)
