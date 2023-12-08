# draw color filled circle in turtle 
import turtle 
t = turtle.Turtle() # creating turtle pen
r1 = int(200) # taking input for the radius of the circle 
r2=int(160)
r3=int(120)
r4=int(80)
col1 = "red" # taking the input for the color 
col2="white"
col3="blue" 
t.fillcolor(col1) # set the fillcolor
t.begin_fill() # start the filling color
t.circle(r1) # drawing the circle of radius r 
t.end_fill()# ending the filling of the color 
t.fillcolor(col2) 
t.begin_fill() 
t.circle(r2) 
t.end_fill()
t.fillcolor(col1) 
t.begin_fill() 
t.circle(r3) 
t.end_fill()
t.fillcolor(col3)
t.begin_fill() 
t.circle(r4)  
t.end_fill()
t.circle(-r1)
turtle.mainloop()