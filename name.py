import turtle
name=input("enter your name")
l1=[[0.0,-234],[-234,-234],]
def drawseg(l):
    turtle.pu()
    turtle.goto(l[0][0], l[0][1])
    turtle.pd()
    for a, b in l[1:]:
        turtle.goto(a, b)
drawseg(l1)
turtle.mainloop()