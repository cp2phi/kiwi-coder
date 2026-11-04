# 第 5 关参考答案 / Level 5 solution
import turtle
t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "gold", "green", "blue", "purple"]
for i in range(60):
    t.color(colors[i % 6])
    t.forward(i * 4)
    t.left(91)
