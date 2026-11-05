# 🏭 第 3 课作业：万花筒工厂  Lesson 3 homework: Kaleidoscope Factory
# 作者 By：（写你的昵称 your nickname）
# AI 帮忙的地方 How AI helped：（如果问了 AI，写下它解释了哪一行 / which line AI explained）
import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

# ===== 🥉 第 1 部分：倒计时 + 我的多边形  Part 1: countdown + my polygon =====
# TODO 1：用 for 循环打印 3, 2, 1，然后打印「开工！」 / print 3, 2, 1 then "Go!"


# TODO 2：用 for 循环画一个你选的多边形（边数你定，角度 = 360 / 边数）
# draw a polygon of your choice with a for loop (angle = 360 / sides)
sides = 5
t.color("gold")
for i in range(sides):
    t.forward(100)
    t.left(360 / sides)

# ===== 🥈 第 2 部分：彩色螺旋  Part 2: colourful spiral =====
# TODO 3：画一个螺旋，至少 2 种颜色，笔越来越粗（提示：t.pensize(i / 10)）
# a spiral with at least 2 colours and a pen that gets thicker (hint: t.pensize(i / 10))


# ===== 🥇 第 3 部分：我设计的万花筒（循环里面有循环）  Part 3: my own kaleidoscope (loop in a loop) =====
# TODO 4：问 AI「请解释第 __ 行」，把它的解释写成注释 / ask AI to explain one line, write its answer as a comment

