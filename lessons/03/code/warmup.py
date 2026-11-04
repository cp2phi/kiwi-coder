# 🔁 热身：用变量控制正方形的大小 Warm-up: a square controlled by a variable
# 第 2 课学的：变量就是一个有名字的盒子 / From lesson 2: a variable is a box with a name
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(6)

size = 100          # 改这一个数字，4 条边一起变！ / change this one number and all 4 sides change!
colour = "blue"     # 颜色也放进盒子 / the colour lives in a box too

t.color(colour)
t.pensize(4)

t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
