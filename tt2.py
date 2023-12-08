import turtle
l2 = [[0.0,45],[89,98]]


def drawseg(l):
    turtle.pu()
    turtle.goto(l[0][0], l[0][1])
    turtle.pd()
    for a, b in l[1:]:
        turtle.goto(a, b)

drawseg(l2)
turtle.mainloop()
