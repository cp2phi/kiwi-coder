# test-input: no | no | no | yes | yes | no | no | no
# 🏠 第 6 课作业：动物侦探  Lesson 6 homework: Animal Detective
# 作者 By：（写你的昵称 your nickname）
# 🥇 我在 Teachable Machine 训练了：（写下你教它认什么、用了几张图 / what you trained it to recognise and how many pictures）
# AI 帮忙的地方 How AI helped：
import turtle

# ===== 🥉 第 1 部分：动物侦探，至少 5 种动物 Part 1: animal detective, at least 5 animals =====
questions_asked = 0          # 🥈 第 2 部分用：数一数问了几个问题 / Part 2: count the questions
again = "yes"

while again == "yes":
    print("想好一个动物了吗？我来猜！/ Think of an animal. I'll guess!")
    fur = input("它有毛吗？Does it have fur? (yes/no) ")
    fly = input("它会飞吗？Can it fly? (yes/no) ")
    water = input("它住在水里吗？Does it live in water? (yes/no) ")
    questions_asked += 3     # 每轮问了 3 个问题 / 3 questions each round

    if water == "yes":
        print("🦈 是鲨鱼 shark？")
    elif fur == "yes" and fly == "no":
        print("🐱 是猫 cat？")
    elif fur == "no" and fly == "yes":
        print("🐦 是 tūī？")
    elif fur == "no" and fly == "no":
        print("🥝 是奇异鸟 kiwi？")
    else:
        print("🤷 我不知道 / I don't know")
    # 👉 在上面加更多 elif，让它认识至少 5 种动物（蝙蝠？企鹅？狗？）
    # 👉 Add more elif lines above so it knows at least 5 animals (bat? penguin? dog?)

    again = input("再玩一次？Play again? (yes/no) ")

print(f"🧮 我一共问了 {questions_asked} 个问题 / I asked {questions_asked} questions")

# ===== 🥇 第 3 部分：用 while 画一幅画 Part 3: draw something with while =====
# 下面是一个例子：越来越大的圆圈，画到半径 120 为止。改成你自己的！
# Example: bigger and bigger circles until the radius reaches 120. Make it yours!
t = turtle.Turtle()
t.speed(0)
t.color("purple")
r = 10
while r < 120:
    t.circle(r)
    r = r + 15
