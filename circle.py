
# Import TURTLE LIBRARY and RANDOM  & TIME MODULE using the command:
import turtle
import random
import time

# You have to create your own window to run each drawing command. You can do this by initializing variables.

t = turtle.Turtle()
s = turtle.Screen()

# Setting up the screen’s height and width (Here we have both height and width equals to 1 so, we will get a full screen.)

s.setup(width=1.0, height=1.0)
s.colormode(255)

# Giving screen a background colour

turtle.Screen().bgcolor("Black")

# setting colour of pen

t.pencolor('orange')

# speed refers to the speed of the pen here, 0 is the max speed and 1 is minimum speed.
t.speed(20.0)

# This will help us to hide the cursor of the turtle.
t.hideturtle()

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