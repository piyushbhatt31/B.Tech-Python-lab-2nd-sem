import turtle
p=turtle.Turtle()
p.speed(30)
p.shape("turtle")
i=0
j=0
a=100
x=0
q=0
y=-200
z=["gold","indigo","blue","green","yellow","orange","red","silver"]
while i<5:
 j=0   
 for e in range(1,8):
    p.pencolor(z[j])
    p.goto(x,y)
    if q==0:
            if j==1:
               p.clear()
    p.begin_poly()
    p.circle(a)
    p.pencolor("white")
    p.goto(0,0)
    j+=1
    y=y+10
    q=1
 i+=1
 
