# 🎨 名字画家  Name Painter
# test-input: 小海龟 | hotpink
# 海龟会把你的名字写在画布上，还会画一个相框  The turtle writes your name and draws a frame

import turtle

name = input("你叫什么名字？ ")
colour = input("你喜欢什么颜色？（英文，比如 red / gold / blue） ")

t = turtle.Turtle()
t.speed(0)
t.color(colour)
t.pensize(5)

# 相框：改 size 试试！ The frame: try changing size!
size = 300
t.penup()
t.goto(-size / 2, -size / 2)
t.pendown()
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)

# 把名字写在中间  Write the name in the middle
t.penup()
t.goto(0, -20)
t.write(name, align="center", font=("Arial", 32, "bold"))
t.hideturtle()
