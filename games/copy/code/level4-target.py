# 🎨 图案复刻 第 4 关：目标图案 / Copy the Pattern level 4: target drawing
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("darkorange")
for i in range(36):
    t.forward(150)
    t.backward(150)
    t.left(10)
t.hideturtle()
