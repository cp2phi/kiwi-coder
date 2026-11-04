# test-input: hello | family | food | sea | sun
# 🏠 第 5 课作业：故事机 3000  Lesson 5 homework: Story Machine 3000
# 作者 By：（写你的昵称 your nickname）
# AI 帮忙的地方 How AI helped：（如果问了 AI，写下它给的提示 / write any hint AI gave you）
import random
import turtle

# ===== 🥉 第 1 部分：故事生成器 Part 1: story maker =====
# 每个列表至少 4 样东西，打印 3 个故事 / at least 4 items in each list, print 3 stories
who = ["一只奇异鸟", "我的老师", "一个机器人", "超级海龟"]
where = ["在学校食堂", "在海滩上", "在 Minecraft 里", "在天空塔顶上"]
did = ["吃掉了 100 个饺子", "跳了一支机器人舞", "打败了一条龙", "发明了会飞的鞋"]

for i in range(3):
    print(f"{random.choice(who)}{random.choice(where)}{random.choice(did)}！")

# ===== 🥈 第 2 部分：带记分的小测验 Part 2: quiz with score =====
# 答错的题记到 wrong 列表里，最后打印出来 / put wrong ones into the wrong list and print them at the end
maori = ["kia ora", "whānau", "kai", "moana", "rā"]
english = ["hello", "family", "food", "sea", "sun"]
score = 0
wrong = []

for i in range(5):
    answer = input(f"「{maori[i]}」是什么意思？What does it mean? ")
    if answer == english[i]:
        score = score + 1
    else:
        wrong.append(maori[i])        # 记下答错的词 / remember the wrong word

print(f"得分 Score: {score} / 5")
print(f"要复习的词 Words to review: {wrong}")

# ===== 🥇 第 3 部分：随机图形 Part 3: a random shape =====
# 从列表里随机选一个图形、一个颜色、一个大小，用 if 决定画什么
# pick a random shape, colour and size from lists; use if to decide what to draw
t = turtle.Turtle()
t.speed(0)
t.pensize(4)
shapes = ["square", "triangle", "circle"]
colours = ["red", "gold", "deepskyblue", "hotpink", "limegreen"]

shape = random.choice(shapes)
t.color(random.choice(colours))
size = random.randint(50, 150)

if shape == "square":
    for i in range(4):
        t.forward(size)
        t.left(90)
elif shape == "triangle":
    for i in range(3):
        t.forward(size)
        t.left(120)
else:
    t.circle(size / 2)

print(f"画了一个 {shape}，大小 {size} / Drew a {shape}, size {size}")
