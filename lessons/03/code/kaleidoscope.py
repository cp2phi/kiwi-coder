# 🔮 例 4：万花筒（循环里面还有循环！） Example 4: kaleidoscope (a loop inside a loop!)
# 里面的循环画一个正方形，外面的循环把正方形转 12 次
# The inner loop draws one square; the outer loop turns and repeats it 12 times
import turtle

turtle.bgcolor("navy")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("gold")

for i in range(12):           # 外面：12 次 / outer: 12 times
    for j in range(4):        # 里面：4 条边 = 1 个正方形 / inner: 4 sides = 1 square
        t.forward(100)
        t.left(90)
    t.left(30)                # 画完一个正方形，转一点点 / after each square, turn a little (12 × 30 = 360!)

t.hideturtle()
