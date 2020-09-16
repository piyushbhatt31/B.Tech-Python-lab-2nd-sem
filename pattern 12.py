import turtle
c=turtle.Turtle()
c.speed(100)
i=0
j=0
a=10
b=10
x=0
y=-10
while j<10:
    while i<12:
        c.forward(a)
        c.right(b)
        c.forward(a)
        c.backward(5*a)
        c.right(2*b)
        i=i+1
    c.penup()    
    c.goto(x,y)
    c.pendown()
    i=0
    j=j+1
    y=y-10

