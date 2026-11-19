# 第 8 关参考答案 / Level 8 solution
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

def polygon(sides, length):
    for k in range(sides):
        t.forward(length)
        t.left(360 / sides)          # 每个角转 360 ÷ 边数 / each corner turns 360 ÷ sides

x = -255
for sides in range(3, 8):            # 3, 4, 5, 6, 7
    t.penup()
    t.goto(x, -40)
    t.pendown()
    polygon(sides, 45)
    x = x + 115                      # 下一个往右挪 115 / the next one is 115 further right
