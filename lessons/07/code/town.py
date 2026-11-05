# ✨ 例 5：小镇！把 ___ 填好，三个招式合在一起 Example 5: a town! Fill in ___ to combine three tricks
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def house(x, y, size, colour):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    # 屋顶 / roof
    t.penup()
    t.goto(x, y + size)
    t.pendown()
    t.fillcolor("firebrick")
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def tree(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("saddlebrown")
    t.left(90)
    t.forward(40)          # 树干 / trunk
    t.right(90)
    t.color("green")
    t.begin_fill()
    t.circle(25)           # 树叶 / leaves
    t.end_fill()
    t.color("black")

def sun(x, y, r):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.color("black")

# 一条街：喊 house 4 次 / a street: call house 4 times
def street(n):
    for i in range(n):
        house(-260 + i * 130, -150, 80, "tan")

street(___)            # 画几座房子？ how many houses?
tree(-280, -150)
tree(___, -150)        # 第二棵树放哪？ where does the 2nd tree go?
sun(200, 180, ___)     # 太阳多大？ how big is the sun?
t.hideturtle()
