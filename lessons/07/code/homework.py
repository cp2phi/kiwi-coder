# 🏙️ 第 7 课作业：海龟城市规划师 Lesson 7 homework: Turtle City Planner
# 作者 By：（写你的昵称 your nickname）
# AI 帮忙的地方 How AI helped：（如果问了 AI，写下它教你的一招 / write the trick AI taught you）
import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# ===== 🥉 必做 Part 1：house(x, y, size, colour) + 一条 4 座房子的街 =====
# ===== 🥉 Must do: house(x, y, size, colour) + a street of 4 houses =====
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
    # TODO：加上屋顶（看第 3 个例子）/ add the roof (see Example 3)


for i in range(4):
    house(-250 + i * 130, -120, 90, "lightyellow")

# ===== 🥈 加分 Part 2：tree(x, y)、sun(x, y, r)，还有 一个 is_night 变量 =====
# ===== 🥈 Bonus: tree(x, y), sun(x, y, r), and an is_night variable =====
is_night = False          # 改成 True 试试！ try changing to True!
if is_night:
    turtle.bgcolor("midnightblue")
else:
    turtle.bgcolor("skyblue")

# def tree(x, y):
#     ...

# def sun(x, y, r):
#     ...


# ===== 🥇 挑战 Part 3：一个会「交回」随机颜色的招式 =====
# ===== 🥇 Challenge: a trick that returns a random colour =====
# def random_colour():
#     colours = ["tomato", "gold", "lightgreen", "skyblue", "plum"]
#     return random.choice(colours)
# 然后把上面的 "lightyellow" 换成 random_colour() / then replace "lightyellow" above with random_colour()

t.hideturtle()
