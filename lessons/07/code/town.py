# 🏙️ 例 6：火箭小镇 Example 6: rocket town
# house、tree、rocket 三个招式已经写好。street(n, y) 要你自己写！
# house, tree and rocket are ready. You write street(n, y) yourself!
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.bgcolor("skyblue")

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

# size 有默认值：rocket(200, -150) 就是 size = 120 / size has a default: rocket(200, -150) means size = 120
def rocket(x, y, size=120):
    w = size / 3                       # 机身宽 / body width
    t.color("black")
    # 机身 / body
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y + size)
    t.goto(x, y + size)
    t.goto(x, y)
    t.end_fill()
    # 机头 / nose cone
    t.penup()
    t.goto(x, y + size)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.goto(x + w, y + size)
    t.goto(x + w / 2, y + size + w)
    t.goto(x, y + size)
    t.end_fill()
    # 尾翼 / fins
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("gray")
    t.begin_fill()
    t.goto(x - w / 2, y)
    t.goto(x, y + w)
    t.goto(x, y)
    t.end_fill()
    t.penup()
    t.goto(x + w, y)
    t.pendown()
    t.begin_fill()
    t.goto(x + w + w / 2, y)
    t.goto(x + w, y + w)
    t.goto(x + w, y)
    t.end_fill()

colours = ["tan", "khaki", "lightpink", "lightblue"]

# ===== 🛠️ 你的任务 Your job =====
# 自己写 street(n, y)：在高度 y 从 x = -280 开始画 n 座房子（size 70），每座往右挪 100。
#   颜色从 colours 列表里轮流拿：第 i 座用 colours[i % len(colours)]
# Write street(n, y) yourself: draw n houses (size 70) at height y, starting at x = -280, each 100 further right.
#   Take colours in turn from the list: house i uses colours[i % len(colours)]


# 写好以后，去掉下面两行前面的 #  / when it works, remove the # in front of these two lines
# street(4, -150)
# street(3, 0)

tree(40, 0)
tree(110, 0)
rocket(200, -150)            # 用默认大小 / default size
rocket(130, -150, 60)        # 小一号的火箭 / a smaller rocket
t.hideturtle()
