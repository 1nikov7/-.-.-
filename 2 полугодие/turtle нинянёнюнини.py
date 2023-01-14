from turtle import *
left(90)
goto(x*-100,y*-100)
for i in range(3):
    forward(350)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*35,y*35)
        dot(5)
done()
