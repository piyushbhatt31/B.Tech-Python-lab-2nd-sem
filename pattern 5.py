import turtle
c=turtle.Turtle()
c.speed(30)
i=0
j=0
a=1
b=45
while i<100:
     c.left(b)
     c.forward(a)
     c.right(b)
     c.forward(a)
     c.left(b)
     a=a+1 
     i=i+1

