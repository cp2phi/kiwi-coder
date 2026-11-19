# test-input: no | no | no | yes | no
# 🏠 第 6 课作业：动物侦探  Lesson 6 homework: Animal Detective
# 作者 By：（写你的昵称 your nickname）
# 🥈 我的 Teachable Machine：教它认 ______ 和 ______，每类 ___ 张图，测试 10 次对了 ___ 次
# 🥈 My Teachable Machine: taught it ______ vs ______, ___ photos each, right ___ out of 10 tests
# AI 帮忙的地方 How AI helped：

# ===== 🥉 第 1 部分：动物侦探，至少 6 种动物 Part 1: animal detective, at least 6 animals =====
rounds = 0                   # 🥈 玩了几局 / games played
right = 0                    # 🥈 猜对几局 / games guessed right
again = "yes"

while again == "yes":
    print("想好一个动物了吗？我来猜！/ Think of an animal. I'll guess!")
    fur = input("它有毛吗？Does it have fur? (yes/no) ")
    fly = input("它会飞吗？Can it fly? (yes/no) ")
    water = input("它住在水里吗？Does it live in water? (yes/no) ")

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
    # 👉 TODO 1：让它认识至少 6 种动物，一定要有 🐶 狗、🦇 蝙蝠、🐧 企鹅。需要新问题就加 input。
    # 👉 TODO 1: make it know at least 6 animals, including 🐶 dog, 🦇 bat and 🐧 penguin. Add an input if you need a new question.

    # 👉 TODO 2（🥈）：问「我猜对了吗？(yes/no)」，用 rounds 和 right 记下来
    # 👉 TODO 2 (🥈): ask "Did I guess right? (yes/no)" and count with rounds and right

    again = input("再玩一次？Play again? (yes/no) ")

# 👉 TODO 3（🥈）：打印「规则 AI 猜对了 right / rounds 局」；全对就再说「🏆 完美侦探」
# 👉 TODO 3 (🥈): print "the rule AI got right / rounds"; if all right, also say "🏆 perfect detective"

# ===== 🥇 第 3 部分：聪明侦探——只问需要的问题 Part 3: smart detective — only ask what's needed =====
# 上面的侦探每局都问一样多的问题。聪明的侦探会根据回答决定「下一个问题问什么」（if 里面再 input）。
# 写一个新版本：用 asked 计数，每问一个问题就 asked += 1。最后打印「这次只问了 ? 个问题」。
# The detective above asks the same number of questions every time. A smart one picks the NEXT question
# based on the last answer (an input inside an if). Write a new version that counts asked += 1 per question.
