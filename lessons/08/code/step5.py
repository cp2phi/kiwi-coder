# ✊ 第 5 步：海龟庆祝！ Step 5: the turtle celebrates!
# test-input: 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头
import random
import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

choices = ["石头", "剪刀", "布"]

def judge(me, computer):
    if me == computer:
        return "平"
    elif me == "石头" and computer == "剪刀":
        return "赢"
    elif me == "剪刀" and computer == "布":
        return "赢"
    elif me == "布" and computer == "石头":
        return "赢"
    else:
        return "输"

# 第 7 课的招式：赢了画星星 / Lesson 7 trick: draw a star when you win
def star(x, y, size, colour):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(colour)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()

# TODO：写一个 sad_face(x, y) 招式，输了的时候画（提示：circle + 两个 dot + 一条弧线）
# TODO: write a sad_face(x, y) trick for when you lose (hint: circle + two dots + an arc)


my_score = 0
computer_score = 0
rounds = 0
while my_score < 3 and computer_score < 3 and rounds < 15:
    computer = random.choice(choices)
    me = input("你出什么？石头 / 剪刀 / 布： ").strip()
    if me not in choices:
        print("只能出 石头 / 剪刀 / 布 哦！")
        continue
    rounds = rounds + 1
    result = judge(me, computer)
    print("你:", me, " 电脑:", computer, " →", result)
    if result == "赢":
        my_score = my_score + 1
        star(-200 + my_score * 100, 100, 40, "gold")      # 每赢一次多一颗星 / one star per win
    elif result == "输":
        computer_score = computer_score + 1
        # TODO：在这里喊 sad_face / call sad_face here
    print("比分  你", my_score, ":", computer_score, "电脑")

if my_score > computer_score:
    print("🏆 你赢了！")
    t.penup(); t.goto(0, -50); t.color("purple")
    t.write("WINNER!", align="center", font=("Arial", 36, "bold"))
else:
    print("🤖 电脑赢了！")
