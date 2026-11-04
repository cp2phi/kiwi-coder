# 🌈 例 3：彩虹螺旋 Example 3: rainbow spiral
# i 每次都会变大：0, 1, 2, 3 …… 所以每条线都比上一条长！
# i grows every time: 0, 1, 2, 3 … so each line is longer than the last!
import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# 这是一个「列表」，第 5 课会正式学。现在先当魔法用：colors[i % 6] 会轮流拿出 6 种颜色
# This is a "list" (lesson 5). For now it's magic: colors[i % 6] takes the 6 colours in turn
colors = ["red", "orange", "gold", "limegreen", "deepskyblue", "purple"]

for i in range(100):
    t.color(colors[i % 6])
    t.forward(i * 2)        # i = 0 时走 0 步，i = 1 时走 2 步，i = 50 时走 100 步 / i=0 → 0, i=1 → 2, i=50 → 100
    t.left(59)              # 试试 90、91、120、121 / try 90, 91, 120, 121

t.hideturtle()
