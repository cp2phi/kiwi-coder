# 🏙️ 第 7 课作业：海龟城市规划师 Lesson 7 homework: Turtle City Planner
# 作者 By：（写你的昵称 your nickname）
# AI 帮忙的地方 How AI helped：（如果问了 AI，写下它教你的一招 / write the trick AI taught you）
import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# ===== 🥉 必做 Part 1（4 个小任务）/ Must do (4 small jobs) =====
# 1) 给 house 加上三角形屋顶——先别看例子，自己试！    give house a triangle roof — try it without looking first!
# 2) 写 random_colour()：从 colours 里随机「交回」一个颜色   write random_colour(): return a random colour from colours
# 3) 写 street(n, y)：在高度 y 画 n 座房子，每座往右挪 130，颜色用 random_colour()
#    write street(n, y): n houses at height y, each 130 further right, coloured with random_colour()
# 4) 喊 street 两次，画两排街                          call street twice for two rows
colours = ["tomato", "gold", "lightgreen", "skyblue", "plum"]

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
    # TODO 1：屋顶 / the roof


# TODO 2：def random_colour():


# TODO 3：def street(n, y):


# TODO 4：喊 street 两次 / call street twice
house(-250, -150, 90, "lightyellow")      # street 写好后删掉这行 / delete this line once street works


# ===== 🥈 加分 Part 2 / Bonus =====
# 5) rocket(x, y, size=80)：带默认值的火箭（机身 + 机头，可以加尾翼）
#    rocket(x, y, size=80): a rocket with a default size (body + nose cone, fins if you like)
# 6) sky(is_night)：True 画深蓝天 + 月亮 + 20 颗随机位置的星星（for + random.randint），False 画蓝天 + 太阳
#    sky(is_night): True → dark sky + moon + 20 stars at random spots (for + random.randint); False → blue sky + sun
is_night = False          # 改成 True 试试！ try changing to True!


# ===== 🥇 挑战 Part 3：城市规划电脑 / Challenge: the city-planning computer =====
# 7) plan_city(n)：「交回」一个列表，装 n 个随机的建筑名字，比如 ["house", "tree", "house", "rocket"]
#    规则：整座城最多 1 个 "rocket"（发射台只有一个！）
#    plan_city(n): return a list of n random building names, e.g. ["house", "tree", "house", "rocket"]
#    Rule: at most ONE "rocket" in the whole city (there's only one launch pad!)
# 8) draw_city(plan)：用 for 看列表里的每个名字，用 if / elif 喊对应的招式，从左往右排
#    draw_city(plan): for each name in the list, use if / elif to call the matching trick, left to right
# 9) 运行 5 次：每次都是新城市，而且永远不会出现 2 个火箭
#    Run it 5 times: a new city every time, and never 2 rockets

t.hideturtle()
