a= 100
b=90
import turtle
c=turtle.Turtle()
c.speed(30)
c.pencolor("blue")
if c.pencolor()=="red":
   c.forward(a)
   c.left(b)
   c.forward(a)
   c.left(b)
   c.forward(a)
   c.left(b)
   c.forward(a)   
elif c.pencolor()=="green":
    c.circle(a)
elif c.pencolor()=="blue":
    c.forward(a)
    c.left(b)
    c.forward(2*a)
    c.left(b)
    c.forward(a)
    c.left(b)
    c.forward(2*a)
else:
    c.forward(a)
    
    

    
            
    
    
