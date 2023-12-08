import turtle
t=turtle.Turtle()
col="blue"
l1 =[[]]


def drawseg(l):
    turtle.pu()
    turtle.goto(l[0][0], l[0][1])
    turtle.pd()
    for a, b in l[1:]:
        turtle.goto(a, b)
t.fillcolor(col)  
t.begin_fill()      
drawseg(l1)
t.end_fill()
turtle.mainloop()