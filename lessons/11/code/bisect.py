# ✂️ 二分法：画出来不对，但不知道错在哪？把一半注释掉！ Halving: wrong picture? Comment out half!
# 这个程序想画一枚火箭：箭身 + 尖头 + 两片尾翼 + 火焰。可是画出来不对。
# It should draw a rocket: body + nose cone + two fins + a flame. But the picture is wrong.
# 小技巧：选中几行，按 Ctrl + /（Mac：⌘ + /）可以一起加 # 注释
# Tip: select some lines and press Ctrl + / (Mac: ⌘ + /) to comment them all at once
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# ===== 第 1 部分：箭身 / Part 1: body =====
t.penup()
t.goto(-30, -100)
t.pendown()
t.color("gray", "lightgray")
t.begin_fill()
for i in range(2):
    t.forward(60)
    t.left(90)
    t.forward(160)
    t.left(90)
t.end_fill()

# ===== 第 2 部分：尖头 / Part 2: nose cone =====
t.penup()
t.goto(-30, 60)
t.pendown()
t.color("red")
t.forward(60)
t.right(120)
t.forward(60)
t.right(120)
t.forward(60)

# ===== 第 3 部分：尾翼 / Part 3: fins =====
t.color("deepskyblue")
t.penup()
t.goto(-30, -60)
t.pendown()
t.goto(-60, -110)
t.goto(-30, -100)
t.penup()
t.goto(30, -60)
t.pendown()
t.goto(60, -110)
t.goto(30, -100)

# ===== 第 4 部分：火焰 / Part 4: flame =====
t.penup()
t.goto(0, -125)
t.dot(40, "orange")
t.dot(20, "yellow")
t.hideturtle()
