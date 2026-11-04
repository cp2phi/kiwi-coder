# 🎨 图案复刻 第 6 关：目标图案 / Copy the Pattern level 6: target drawing
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.color("deeppink")
for i in range(6):
    t.circle(60)
    t.left(60)
t.hideturtle()
