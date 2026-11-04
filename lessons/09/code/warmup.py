# 🔁 热身：函数 + 列表  Warm-up: a function + a list
# 还记得第 7 课的函数和第 5 课的列表吗？ Remember functions (L7) and lists (L5)?
import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 一个画星星的函数 / a function that draws a star
def star(x, y, size, colour):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(colour)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# 一个颜色列表 / a list of colours
colours = ["gold", "orange", "hotpink", "deepskyblue"]

# 用列表里的每个颜色画一颗星 / one star for each colour in the list
x = -150
for c in colours:
    star(x, 0, 60, c)
    x = x + 100
