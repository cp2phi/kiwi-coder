# 🌀 例 1：用 for 循环画正方形 Example 1: a square with a for loop
# 4 行 forward + 4 行 left，变成了 2 行！ / 8 lines become 2!
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(6)
t.color("purple")
t.pensize(4)

for i in range(4):          # 下面缩进的两行，重复 4 次 / repeat the 2 indented lines 4 times
    t.forward(100)
    t.left(90)
