import turtle
c=turtle.Turtle()
c.speed(30)
i=0
a=0
y=0
x=0
b=90
while i<100:
 c.forward(a)
 c.left(b)
 c.forward(a)
 c.left(b)
 c.forward(a)
 c.left(b)
 c.forward(a)
 c.left(b)
 c.penup()
 c.goto(-x,-y)
 c.pendown()
 y=y+4
 x+=4
 a=a+8
 i+=1

