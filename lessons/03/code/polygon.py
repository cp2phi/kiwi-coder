# 🧪 例 2：万能多边形机 Example 2: the any-polygon machine
# 把 ___ 换成边数，电脑自己算角度！ / Replace ___ with the number of sides. The computer works out the angle!
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.color("deepskyblue")
t.pensize(3)

sides = ___                 # 边数 / how many sides? 试试 3、5、8、12、36

for i in range(sides):
    t.forward(80)
    t.left(360 / sides)     # 一圈是 360 度，平均分给每条边 / 360 degrees shared between the sides
