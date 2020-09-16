import turtle
c=turtle.Turtle()
c.speed(200) 
for i in range(25):
    c.circle(2*i) 
    c.circle(-2*i) 
    c.left(i) 

