# 🐾 例 4：海龟随机散步 Example 4: the turtle's random walk
# 每一步掷硬币：1 就左转，2 就右转。每次跑出来都不一样！
# Every step flips a coin: 1 = turn left, 2 = turn right. Different every run!
import turtle
import random

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

for i in range(80):
    if random.randint(1, 2) == 1:
        t.left(90)
    else:
        t.right(90)

    if i % 2 == 0:                  # 偶数步 / even steps
        t.color("gold")
    else:                           # 奇数步 / odd steps
        t.color("cyan")

    t.forward(20)
