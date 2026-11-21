# test-input: hello | family | food | sea | sun
# 🏠 第 5 课作业：故事机 3000  Lesson 5 homework: Story Machine 3000
# 作者 By：（写你的昵称 your nickname）
# AI 帮忙的地方 How AI helped：（如果问了 AI，写下它给的提示 / write any hint AI gave you）
import random

# ===== 🥉 第 1 部分：故事生成器 Part 1: story maker =====
who = ["一只奇异鸟", "我的老师", "一个机器人", "超级海龟"]
where = ["在学校食堂", "在海滩上", "在 Minecraft 里", "在天空塔顶上"]
did = ["吃掉了 100 个饺子", "跳了一支机器人舞", "打败了一条龙", "发明了会飞的鞋"]
# TODO 1：每个列表再加 2 样你自己的；再做第 4 个列表 when（至少 4 样，比如「在半夜」「在火星上」）
# TODO 1: add 2 of your own to each list; then make a 4th list called when (4+ items, like "at midnight", "on Mars")

# TODO 2：自己写一个 for 循环，打印 3 个带编号的故事，每个都用到 4 个列表：
#         「1. 在半夜，一只奇异鸟在海滩上发明了会飞的鞋！」
# TODO 2: write a for loop yourself that prints 3 numbered stories using all 4 lists


# ===== 🥈 第 2 部分：会记错题的测验 Part 2: a quiz that remembers mistakes =====
maori = ["kia ora", "whānau", "kai", "moana", "rā"]
english = ["hello", "family", "food", "sea", "sun"]
score = 0
wrong = []                    # 答错的毛利语词 / wrong Māori words
wrong_en = []                 # 它们的英文（和 wrong 配对）/ their English (paired with wrong)

for i in range(len(maori)):
    answer = input(f"「{maori[i]}」是什么意思？（用英文小写回答）What does it mean? (lowercase English) ")
    # TODO 3：答对 → score 加 1；答错 → 告诉正确答案，并把 maori[i] 和 english[i] 分别加进 wrong 和 wrong_en
    # TODO 3: right → add 1 to score; wrong → show the right answer and append maori[i] / english[i] to wrong / wrong_en

print(f"得分 Score: {score} / {len(maori)}")
# TODO 4：如果 wrong 不是空的，用 for 把错题一行一行打印成「📌 kai = food」；是空的就打印「💯 满分！」
# TODO 4: if wrong isn't empty, print each mistake on its own line like "📌 kai = food"; if it's empty print "💯 Full marks!"

# ===== 🥇 第 3 部分：测验 2.0 Part 3: Quiz 2.0 =====
# ① 再出一轮题：顺序随机，而且同一个词不会问两次（提示：pop）
# ② 这一轮结束后，只把这一轮答错的词再考一次（第二次机会）
# 先在纸上写步骤！需要哪些列表？每一步列表会怎么变？
# ① Run another round in random order where no word is asked twice (hint: pop)
# ② Afterwards, ask only the words missed in that round once more (a second chance)
# Plan on paper first! Which lists do you need? How does each list change at each step?
