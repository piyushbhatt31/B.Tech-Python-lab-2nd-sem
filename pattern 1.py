import turtle
c=turtle.Turtle()
c.speed(30)
i=0
y=0
a=0
x=0
while i<100:
 c.circle(a)
 c.penup()
 c.goto(x,-y)
 c.pendown()
 a=a+4
 y=y+4
 i+=1
