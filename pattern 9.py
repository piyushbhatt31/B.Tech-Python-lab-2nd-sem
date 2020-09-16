import turtle
p=turtle.Turtle()
p.speed(30)
j=0
r=50
x=0
y=0
a=90
b=50
p.penup()
p.goto(x+100,y-100)
p.write("Piyush")
while j<10:
    p.forward(b)
    p.begin_poly()
    p.circle(r)
    p.penup()
    p.goto(x,y)
    p.pendown()
    p.backward(b)
    p.right(a)
    p.circle(r)
    j+=1

