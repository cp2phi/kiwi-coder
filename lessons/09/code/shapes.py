# 🔷 按名字画图形  Draw shapes by name
# 字典告诉我们每种图形有几条边 / the dict says how many sides each shape has
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

shapes = {
    "三角形": 3,
    "正方形": 4,
    "六边形": 6,
    "八边形": ___,      # 👈 填：八边形有几条边？ / fill in: how many sides?
}

def draw(name, size, colour):
    sides = shapes[name]            # 查字典：几条边？ / look it up: how many sides?
    t.color(colour)
    for i in range(sides):
        t.forward(size)
        t.left(360 / sides)         # 还记得第 3 课的 360 ÷ 边数吗？ / remember 360 ÷ sides?

t.penup(); t.goto(-200, 0); t.pendown()
draw("三角形", 80, "red")
t.penup(); t.goto(-60, 0); t.pendown()
draw("正方形", 70, "green")
t.penup(); t.goto(80, 0); t.pendown()
draw("六边形", 50, "blue")
t.penup(); t.goto(200, 0); t.pendown()
draw("八边形", 40, "purple")
