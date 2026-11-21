# 🖱️ 点哪里，哪里就亮一颗星 / Click anywhere to light up a star
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)

colours = ["white", "gold", "lightblue", "pink"]

def star_here(x, y):               # 点击时电脑会把 x, y 交给你 / the computer hands you x, y
    t.goto(x, y)
    t.dot(random.randint(4, 12), random.choice(colours))
    print(f"星星在 star at ({int(x)}, {int(y)})")

screen.onclick(star_here)
print("点一下画布试试！ Click on the canvas!")
