# 🔁 热身：上次的 while + 列表还记得吗？ Warm-up: remember while + lists?
# 把 ___ 填好，让海龟按列表里的颜色画 5 个圆，画完停下
# Fill in ___ so the turtle draws 5 circles using the colours in the list, then stops

import turtle

t = turtle.Turtle()
t.speed(0)
colours = ["red", "orange", "gold", "green", "blue"]

count = 0
while count < ___:            # 画几次？ how many times?
    t.color(colours[count])   # 第 count 个颜色 / the count-th colour
    t.circle(30 + count * 15)
    count = count + ___       # 别忘了加 1，不然停不下来！ don't forget +1 or it never stops!

print("画了", count, "个圆 / circles drawn")
