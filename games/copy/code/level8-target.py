# 🎨 图案复刻 第 8 关：目标图案 / Copy the Pattern level 8: target drawing
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
colors = ["red", "darkorange", "green", "blue", "purple"]
x = -255
for sides in range(3, 8):
    t.color(colors[sides % len(colors)])
    t.penup()
    t.goto(x, -40)
    t.setheading(0)
    t.pendown()
    for k in range(sides):
        t.forward(45)
        t.left(360 / sides)
    x = x + 115
t.hideturtle()
