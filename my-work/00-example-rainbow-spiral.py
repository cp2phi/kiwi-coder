# 🌈 示例：彩虹螺旋（老师放的，等你有了自己的作品，就可以删掉我）
import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["red", "orange", "gold", "limegreen", "deepskyblue", "purple"]

# 你会在第 3 课学到 for 循环——先猜猜它是干嘛的？
for i in range(120):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.left(59)

t.hideturtle()
