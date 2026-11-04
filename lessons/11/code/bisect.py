# ✂️ 二分法：画出来不对，但不知道错在哪？把一半注释掉！ Binary search: wrong picture? Comment out half!
# 这个程序想画：一座房子 + 屋顶 + 太阳。可是画出来的样子不对。
# It should draw: a house + roof + sun. But the picture is wrong.
# 小技巧：选中几行，按 Ctrl + / 可以一起加 # 注释（有的编辑器支持）
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# ===== 第 1 部分：房子 / Part 1: house =====
t.color("brown")
for i in range(4):
    t.forward(120)
    t.left(90)

# ===== 第 2 部分：屋顶 / Part 2: roof =====
t.color("red")
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(120)
t.forward(120)
t.left(120)
t.forward(120)

# ===== 第 3 部分：太阳 / Part 3: sun =====
t.penup()
t.goto(180, 180)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(30)
t.end_fill()
t.hideturtle()
