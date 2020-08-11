import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

        

def irma():
    """Animates the path of hurricane Irma
    """
    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()

    hurricaneFile = "data/irma.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)
        next(pointreader)
        t.penup()
        first_row = next(pointreader)
        t.setpos(float(first_row[2]), float(first_row[3]))
        t.pendown()
        for row in pointreader:
            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            # This code just prints out the date and time elements of each
            # row in the file.
            # Make sure you understand what is happening here.
            # Then, you'll need to change this code
            #Latitude is x and longitude is y
            print("Latitude:", row[3], "longitude:", row[2], "Wind:", row[4])
            lat = float(row[3])
            lon = float(row[2])
            mph = int(row[4])
            if mph < 74:
                t.pencolor("White")
                t.pensize(0)
                t.setpos(lat, lon)
                t.write('0')
            elif mph < 96:
                t.pencolor("Blue")
                t.pensize(1)
                t.setpos(lat, lon)
                t.write('1')
            elif mph < 111:
                t.pencolor("Green")
                t.pensize(2)
                t.setpos(lat, lon)
                t.write('2')
            elif mph < 131:
                t.pencolor("Yellow")
                t.pensize(3)
                t.setpos(lat, lon)
                t.write('3')
            elif mph < 156:
                t.pencolor("Orange")
                t.pensize(4)
                t.setpos(lat, lon)
                t.write('4')
            else:
                t.pencolor("Red")
                t.pensize(5)
                t.setpos(lat, lon)
                t.write('5')
    # Hack to make sure a reference to the background image stays around
    # Do not remove or change this line
    return map_bg_img


# Feel free to add "helper" functions here


if __name__ == "__main__":
    bg=irma()


