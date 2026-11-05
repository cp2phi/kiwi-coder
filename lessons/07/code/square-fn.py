# ✨ 例 1：教海龟一个新招「画正方形」 Example 1: teach the turtle a new trick "square"
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# ===== 教招式（def = 定义）：这里只是「教」，还没画！ =====
# ===== Teach the trick (def = define): this only teaches, nothing is drawn yet! =====
def square():
    for i in range(4):
        t.forward(80)
        t.left(90)

# ===== 喊名字（调用）：喊一次，画一次 =====
# ===== Call it by name: each call draws one square =====
square()

t.penup()
t.goto(-200, 100)
t.pendown()
square()

t.penup()
t.goto(150, -150)
t.pendown()
square()
