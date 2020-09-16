import turtle
c=turtle.Turtle()
c.speed(30)
c.color("blue")
i=0
r=10
while i<100000000:
    c.circle(r)
    c.right(r)
    r=r+1
    i=i+r
    
