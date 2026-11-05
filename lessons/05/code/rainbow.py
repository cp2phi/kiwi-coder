# 🌈 彩虹六边形：让海龟按列表换颜色 / Rainbow hexagon: the turtle takes colours from a list
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(6)

colours = ["red", "orange", "gold", "green", "blue", "purple"]

# 「for 颜色 in 列表」：把列表里的东西一个一个拿出来
# "for colour in list": take the items out one by one
for colour in colours:
    t.color(colour)
    t.forward(100)
    t.left(60)
