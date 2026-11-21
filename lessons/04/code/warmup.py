# 🔁 热身：上周的 for 循环 + f-string Warm-up: last week's for loop + f-strings
# 先猜：range(10, 0, -3) 会数出哪几个数？再运行！ / Guess first: which numbers does range(10, 0, -3) count? Then run!
import turtle

for i in range(10, 0, -3):
    print(f"T-{i}")
print("🚀 发射！Lift-off!")

t = turtle.Turtle()
t.speed(0)
t.color("deepskyblue")
for i in range(60):
    t.forward(i * 3)
    t.left(91)
