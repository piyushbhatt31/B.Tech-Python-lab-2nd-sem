import turtle
p=turtle.Turtle()
p.shape("turtle")
s=100
r=250
f=10
l=55
p.speed(s)
for i in range(r):
    p.forward(f)
    p.left(l)
    f+=1
