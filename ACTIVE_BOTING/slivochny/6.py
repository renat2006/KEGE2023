from turtle import *

tracer(0)
lt(90)
k = 15
for i in range(9):
    fd(29 * k)
    rt(90)
    fd(17 * k)
    rt(90)
penup()

fd(5 * k)
rt(90)
fd(1 * k)
lt(90)
pendown()
for i in range(9):
    fd(64 * k)
    rt(90)
    fd(48 * k)
    rt(90)
penup()
for i in range(-50, 50):
    for j in range(-50, 50):
        goto(i * k, j * k)
        dot(3, "red")

update()
done()
