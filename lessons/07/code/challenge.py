# 🏆 挑战：我的小镇 Challenge: my town
# 规则：至少 3 个自己写的招式（def），至少一个有参数，用 for 循环喊它们
# Rules: at least 3 functions (def) you wrote, at least one with parameters, called inside a for loop
# 点子：路灯、云、车、彩虹、围栏、花…… Ideas: lamp posts, clouds, cars, a rainbow, a fence, flowers...
import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("lightblue")

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

# 在这里写你的第 2 个招式 / write your 2nd trick here
def cloud(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for i in range(3):
        t.circle(20)
        t.penup()
        t.forward(25)
        t.pendown()
    t.end_fill()
    t.color("black")

# 在这里写你的第 3 个招式 / write your 3rd trick here


# 现在喊它们！ Now call them!
for i in range(4):
    house(-240 + i * 130, -120, 90, "khaki")

cloud(-200, 150)
cloud(100, 200)

t.hideturtle()
