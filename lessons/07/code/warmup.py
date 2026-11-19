# 🔁 热身：上次的 while + 列表还记得吗？ Warm-up: remember while + lists?
# 任务 1：把 ___ 填好，让海龟把列表里的每个颜色都画一个圆，画完停下。
#         要求：以后往列表里加颜色，while 那行不用改！（提示：len）
# Task 1: fill in ___ so the turtle draws one circle per colour in the list, then stops.
#         Rule: adding colours later must NOT need a change to the while line! (hint: len)
# 任务 2：这段代码少了一行，会永远停不下来——找到并补上。
# Task 2: one line is missing, so it would never stop — find it and add it.

import turtle

t = turtle.Turtle()
t.speed(0)
colours = ["red", "orange", "gold", "green", "blue"]

count = 0
while count < ___:            # 画几次？ how many times?
    t.color(colours[count])   # 第 count 个颜色 / the count-th colour
    t.circle(30 + count * 15)
    # 👈 TODO：少了一行！ a line is missing!

print("画了", count, "个圆 / circles drawn")
