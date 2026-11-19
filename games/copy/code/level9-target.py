# 🎨 图案复刻 第 9 关：目标图案 / Copy the Pattern level 9: target drawing
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("black", "crimson")

def square(x, y, size, filled):
    t.penup()
    t.goto(x, y)
    t.pendown()
    if filled:
        t.begin_fill()
    for k in range(4):
        t.forward(size)
        t.left(90)
    if filled:
        t.end_fill()

for row in range(6):
    for col in range(6):
        square(-120 + col * 40, -120 + row * 40, 40, (row + col) % 2 == 0)
t.hideturtle()
