import turtle
p=turtle.Turtle()
p.speed(30)

i=0
j=0
a=50
b=45
z=["gold","indigo","blue","green","yellow","orange","red","silver"]
while i<100:
 j=0   
 for e in range(1,8):
    p.pencolor(z[j])
    p.forward(a)
    p.right(b)
    a+=1
    j+=1
 i+=1   
