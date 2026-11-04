# 第 2 关：房子 = 正方形 120 + 三角形屋顶 120 / Level 2: house = square 120 + triangle roof 120
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# 先画正方形 / square first
for i in range(4):
    t.forward(120)
    t.left(90)

# 抬笔走到左上角，再画屋顶 / pen up, go to the top-left corner, then the roof
t.penup()
t.goto(0, 120)
t.pendown()
t.left(60)
