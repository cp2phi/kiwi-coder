# 🎨 图案复刻 第 5 关：目标图案 / Copy the Pattern level 5: target drawing
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
colors = ["red", "orange", "gold", "green", "blue", "purple"]
for i in range(60):
    t.color(colors[i % 6])
    t.forward(i * 4)
    t.left(91)
t.hideturtle()
