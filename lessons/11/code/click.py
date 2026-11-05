# 🖱️ 点哪里，就在哪里盖章 / Click anywhere to stamp there
import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.speed(0)

colors = ["red", "orange", "gold", "limegreen", "deepskyblue", "violet"]

def stamp_here(x, y):              # 点击时电脑会把 x, y 交给你 / the computer hands you x, y
    t.goto(x, y)
    t.color(random.choice(colors))
    t.stamp()
    print(f"盖章在 ({int(x)}, {int(y)})")

screen.onclick(stamp_here)
print("点一下画布试试！ Click on the canvas!")
