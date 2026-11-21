# 🏆 挑战：我的太空小镇 Challenge: my space town
# 规则 Rules（全部做到才算过关 / all of them!）:
#   ① 至少 4 个自己写的招式（def）                at least 4 tricks (def) you wrote
#   ② 至少 1 个参数有默认值，比如 size=50          at least 1 parameter with a default, like size=50
#   ③ 至少 1 个招式会 return，结果用在 if 里或递给别的招式
#                                                 at least 1 trick that returns something used in an if or handed to another trick
#   ④ 至少 1 个招式里面喊了别的招式               at least 1 trick that calls another trick
#   ⑤ 用 for 循环喊招式                           call tricks from a for loop
# 点子：发射台、星星、月亮、云、卫星、路灯、围栏、彩虹……
# Ideas: launch pad, stars, moon, clouds, satellites, lamp posts, a fence, a rainbow...
import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("midnightblue")

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

# 一个会「交回」东西的招式（规则 ③）/ a trick that hands something back (rule ③)
def random_colour():
    return random.choice(["khaki", "plum", "lightgreen", "lightsalmon"])

# 在这里写你的招式 / write your tricks here


# 现在喊它们！ Now call them!
for i in range(4):
    house(-260 + i * 120, -150, 80, random_colour())

t.hideturtle()
