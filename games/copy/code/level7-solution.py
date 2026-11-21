# 第 7 关参考答案 / Level 7 solution
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
for i in range(1, 9):
    size = i * 30                    # 30, 60, 90 … 240
    t.penup()
    t.goto(-size / 2, -size / 2)     # 左下角 = 往左、往下各走一半 / bottom-left corner = half the size left and down
    t.pendown()
    for k in range(4):
        t.forward(size)
        t.left(90)
