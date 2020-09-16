import turtle
p=turtle.Turtle()
p.speed(30)
i=0
j=0
a=100
l=["red","blue","green","pink","yellow","brown","orange","gold","silver","lightblue","purple"]
for j in range (10):
    while i<10:
        p.circle(a)
        p.right(i)
        i+=1
        a=a+1
        p.color(l[i])
    p.right(180)    
    j+=1    
    i=0
