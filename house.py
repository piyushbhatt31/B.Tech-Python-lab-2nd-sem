import turtle
c=turtle.Turtle()
c.speed(100)
a=100
b=90
r=35
x=0
y=-100
c.penup()
c.goto(x,y)
c.pendown()
c.forward(3*a)
c.left(b)
c.forward(2*a)
c.left(b)
c.forward(3*a)
c.left(b)
c.forward(2*a)
c.left(b)
c.penup()
c.goto(x,-y)
c.pendown()
c.right(b/2)
c.backward(a)
c.right(b)
c.forward(a)
c.left(b/2)
c.forward(2*a)
c.left(b)
c.forward(a+b/2)
c.write("Piyush Bhatt",align="left")
c.penup()
c.goto(x-70,y+3*b)
c.pendown()
c.forward(3*a)
c.right(b/2)
c.forward(a)
c.penup()
c.goto(-x-a-b/4,y)
c.pendown()
c.left(b+b/2)
c.forward(a+b/2)
c.right(b)
c.forward((a+b)/2)
c.right(b)
c.forward(a+b/2)
c.penup()
c.goto(x-2*a+b,y+2*a)
c.pendown()
c.circle(r)
c.penup()
c.goto(x+r*2,y+4*r)
c.pendown()
c.forward(b)
c.left(b)
c.forward(2*b)
c.left(b)
c.forward(b)
c.left(b)
c.forward(2*b)
