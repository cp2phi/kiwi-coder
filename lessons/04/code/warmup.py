# 🔁 热身：上周的 for 循环 Warm-up: last week's for loop
# 任务：① 把倒计时改成从 5 开始 ② 把螺旋的 91 改成 120 看看
# Tasks: ① make the countdown start at 5 ② change the spiral's 91 to 120
import turtle

for i in range(3, 0, -1):
    print(i)
print("出发！Go!")

t = turtle.Turtle()
t.speed(0)
t.color("deepskyblue")
for i in range(60):
    t.forward(i * 3)
    t.left(91)
