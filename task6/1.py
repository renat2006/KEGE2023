from turtle import *
tracer(0)
lt(90)
k = 10
for i in range(8):
    lt(45)
    forward(12 * k)
penup()
rt(90)
back(8 * k)
pendown()
for i in range(4):
    forward(33 * k)
    rt(90)
penup()
goto(0, 0)
pendown()
for i in range(-50, 50):
    for j in range(-50, 50):
        penup()
        goto(i * k, j * k)
        pendown()
        dot(3)


update()
done()