# 第 7 关：方块隧道——8 个正方形，中心都在画布正中间 / Level 7: square tunnel: 8 squares, all centred on the middle
# 最小的边长 30，后面每个比前一个大 30 / the smallest has sides of 30, each next one is 30 bigger
# 起始代码只画了最小的那个。先想一想：为什么是 goto(-15, -15)？/ The starter only draws the smallest. Think first: why goto(-15, -15)?
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

size = 30
t.penup()
t.goto(-15, -15)
t.pendown()
for k in range(4):
    t.forward(size)
    t.left(90)
