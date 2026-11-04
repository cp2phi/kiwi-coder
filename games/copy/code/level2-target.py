# 🎨 图案复刻 第 2 关：目标图案 / Copy the Pattern level 2: target drawing
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.color("saddlebrown")
for i in range(4):
    t.forward(120)
    t.left(90)
t.penup()
t.goto(0, 120)
t.pendown()
t.color("firebrick")
t.left(60)
t.forward(120)
t.left(120)
t.forward(120)
t.hideturtle()
