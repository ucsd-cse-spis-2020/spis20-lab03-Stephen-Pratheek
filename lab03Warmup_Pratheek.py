import turtle

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
    

#myTurtle = turtle.Turtle()  # Create a new Turtle object
#drawP(myTurtle)   # make the new Turtle draw the shape

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
