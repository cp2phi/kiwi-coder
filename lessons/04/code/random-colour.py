# 🎨 例 2b：海龟掷硬币选颜色 Example 2b: the turtle flips a coin for colours
import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

for i in range(36):
    coin = random.randint(1, 2)       # 1 或 2，像掷硬币 / 1 or 2, like a coin flip
    if coin == 1:
        t.color("red")
    else:
        t.color("blue")
    t.forward(100)
    t.backward(100)                   # 回到中间 / back to the middle
    t.left(10)
