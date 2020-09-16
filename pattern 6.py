import turtle
c=turtle.Turtle()
c.speed(30)
i=0
j=0
r=50
b=180
x=0
y=0
while i<100:
    c.circle(r)
    r+=1
    i=i+1
c.right(b)
r=50
while j<100:
    c.circle(r)
    r+=1
    j+=1
