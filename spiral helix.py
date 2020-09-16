import turtle
p = turtle.Turtle()
p.speed(10)
L = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
x = 0
while x <= 202:
    color = L[x % len(L)]
    p.pencolor(color)
    p.forward(x) 
    p.left(59) 
    x = x+1
