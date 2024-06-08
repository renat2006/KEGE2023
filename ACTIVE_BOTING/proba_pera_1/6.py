from turtle import *

tracer(0)
left(90)
k = 10
pensize(2)
for i in range(2):
    forward(10 * k)
    rt(90)
    fd(18 * k)
    rt(90)
penup()
fd(5 * k)
rt(90)
fd(14 * k)
lt(90)
pendown()

for i in range(2):
    fd(17 * k)
    rt(90)
    fd(7 * k)
    rt(90)
penup()
for i in range(-50, 50):
    for j in range(-50, 50):
        goto(i * k, j * k)
        dot(4, "red")
update()
done()
