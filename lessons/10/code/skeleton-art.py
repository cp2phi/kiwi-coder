# 🎨 项目骨架：点一下就画  Project skeleton: Click to draw
# 作者 By：（昵称 nickname）
# 玩法：在画布上点一下，那里就会长出一朵随机颜色的花 🌸
# How to play: click on the canvas and a random-coloured flower grows there 🌸
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

COLOURS = ["hotpink", "gold", "deepskyblue", "limegreen", "orange", "violet"]
PETALS = 6                  # 花瓣数量 / number of petals（改一改！/ change it!）

def flower(x, y, size):     # 在 (x, y) 画一朵花 / draw a flower at (x, y)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(COLOURS))
    for i in range(PETALS):
        t.circle(size)
        t.left(360 / PETALS)

def on_click(x, y):         # 鼠标点到哪里，就画到哪里 / draw where the mouse clicked
    flower(x, y, random.randint(10, 40))
    # TODO: 必做功能 2：每点一次换一种形状（星星？正方形？）/ a different shape each click
    # TODO: 必做功能 3：按空格键清空画布（screen.onkey + t.clear）/ space bar clears the canvas

def test():                 # 🧪 小测试 / tiny tests
    assert PETALS >= 3, "至少 3 片花瓣"
    assert len(COLOURS) > 0, "要有颜色"

test()
flower(0, 0, 30)            # 先画一朵给你看 / one flower to start
screen.onclick(on_click)
screen.listen()
