# ✨ 例 2：带「参数」的招式：你说多大、什么颜色 Example 2: a trick with parameters: you choose size and colour
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# size 和 colour 叫「参数」：喊招式的时候把东西递给它
# size and colour are "parameters": you hand them in when you call the trick
def square(size, colour):
    t.color(colour)
    for i in range(4):
        t.forward(size)
        t.left(90)

t.penup()
t.goto(-250, 0)
t.pendown()

colours = ["red", "orange", "gold", "green", "blue", "purple"]

# 一排正方形：列表里有几个颜色就画几个
# A row of squares: one for every colour in the list
for c in colours:
    square(60, c)          # 试试把 60 改成别的 / try changing 60
    t.penup()
    t.forward(80)          # 往右挪一点 / shift right
    t.pendown()
