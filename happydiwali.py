import turtle
import random
import time
#Create a turtle screen
t = turtle.Turtle()
s = turtle.Screen()
#Define height and width of screen
s.setup(width=.9912, height=1.0)
s.colormode(255)
#Define Background color of screen
turtle.Screen().bgcolor("Black")
#Initialize a variable for turtle
t=turtle.Turtle()
#Defining speed of turtle
t.speed(20.0)
#To hide the turtle pointer
t.pencolor('orange')
t.hideturtle()
size=random.randint(10,200)
def write(message,pos):
        x,y=pos
        # Define color of the text
        t.pencolor("orange")
        t.penup()
        t.goto(x,y)
        # Defining font style and size
        style=('ALGERIAN',100)
        t.write(message,font=style)
def write1(message,pos):
        x,y=pos
        # Define color of the text
        t.pencolor("red")
        t.penup()
        t.goto(x,y)
        # Defining font style and size
        style=('ALGERIAN',20)
        t.write(message,font=style)
t.pensize(2)
def draw(radius):
    for i in range(10):
        t.circle(radius)
        radius = radius-4
def design():
    for i in range(10):
        draw(120)
        t.right(36)
    t.penup()
design()

    ##########<<<------third part------>>>>>#######
    # draw last crackers to make it more good
def crackers():
    # it randomly selects radius between the given values
    Radius = random.randint(80, 180)
    x_coord = (400)
    y_coord = (350)
    t.penup()
    t.setpos(x_coord, y_coord)  # sets the position of the cracker's center
    t.pendown()
    t.pencolor('blue')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (360)
    y_coord = (250)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('red')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (560)
    y_coord = (130)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('pink')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (-360)
    y_coord = (180)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('orange')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (-480)
    y_coord = (120)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('purple')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(70, 120)
    x_coord = (-530)
    y_coord = (380)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('yellow')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(50, 100)
    x_coord = (540)
    y_coord = (350)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('orange')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)

    Radius = random.randint(80, 180)
    x_coord = (-530)
    y_coord = (150)
    t.penup()
    t.setpos(x_coord, y_coord)
    t.pendown()
    t.pencolor('green')
    for i in range(20):
        t.fd(Radius)
        t.backward(2*Radius)
        t.fd(Radius)
        t.right(10)
crackers()
write('Happy Diwali',(-430,250))
write1('designed by Ashish',(350,-300))
turtle.mainloop()