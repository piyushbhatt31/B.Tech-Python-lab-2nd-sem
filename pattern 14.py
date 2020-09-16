import turtle
c=turtle.Turtle()
c.speed(100)
i=1
x=-50
y=-150
c.penup()
c.goto(x,y)
c.pendown()
while i<75:
    c.forward(i*200/i+1) 
    c.left(55) 
    i=i+1
