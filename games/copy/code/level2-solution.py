# 第 2 关参考答案 / Level 2 solution
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
for i in range(4):
    t.forward(120)
    t.left(90)
t.penup()
t.goto(0, 120)
t.pendown()
t.left(60)
t.forward(120)
t.left(120)
t.forward(120)
