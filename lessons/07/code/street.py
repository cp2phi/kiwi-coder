# ✨ 例 3：把第 1 课的房子打包成 house()，一口气画一条街！
# Example 3: pack the Lesson 1 house into house() and draw a whole street!
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def house(x, y, size):
    # 走到左下角 / go to the bottom-left corner
    t.penup()
    t.goto(x, y)
    t.pendown()
    # 身体：正方形 / body: a square
    t.color("saddlebrown")
    for i in range(4):
        t.forward(size)
        t.left(90)
    # 屋顶：三角形，从左上角开始 / roof: a triangle starting at the top-left
    t.penup()
    t.goto(x, y + size)
    t.pendown()
    t.color("firebrick")
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)        # 转回来，脸朝右 / turn back to face right

# 一条街：5 座房子，每座往右挪 120
# A street: 5 houses, each 120 further right
for i in range(5):
    house(-250 + i * 120, -100, 80)
