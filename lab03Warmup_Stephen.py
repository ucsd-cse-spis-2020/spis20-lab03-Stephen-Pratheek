import turtle

'''
def drawPicture(theTurtle):
    ''' Draw a simple picture using a turtle '''
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)    

myTurtle = turtle.Turtle()  # Create a new Turtle object
drawPicture(myTurtle)   # make the new Turtle draw the shape

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.setpos(-50, -50)
turtle2.setpos(200, 100)
turtle1.forward(100)
turtle2.left(90)
turtle2.forward(100)
'''
def drawFirstInitial(theTurtle):
'''
Drawing the first initial of my first name: Stephen
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