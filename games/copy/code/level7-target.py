# 🎨 图案复刻 第 7 关：目标图案 / Copy the Pattern level 7: target drawing
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
colors = ["red", "orange", "gold", "green", "teal", "blue", "purple", "magenta"]
for i in range(1, 9):
    size = i * 30
    t.color(colors[i % len(colors)])
    t.penup()
    t.goto(-size / 2, -size / 2)
    t.pendown()
    for k in range(4):
        t.forward(size)
        t.left(90)
t.hideturtle()
