# 🌈 示例：彩虹螺旋 Example: rainbow spiral（老师放的，可以删掉 / from the teacher, you can delete me）
import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["red", "orange", "gold", "limegreen", "deepskyblue", "purple"]

# 第 3 课会学 for 循环——先猜猜它是干嘛的？
# You'll learn for loops in Lesson 3 — can you guess what it does?
for i in range(120):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.left(59)

t.hideturtle()
