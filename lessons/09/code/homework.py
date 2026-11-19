# 🏠 第 9 课作业：我的翻译 app  Lesson 9 homework: my translator app
# 作者 By：（写你的昵称 your nickname）
# test-input: kai | 全部 | 再见
import random

# ===== 🥉 必做 Part 1 / Must do =====
# 1) 字典里至少 8 个词（毛利语、英语、火星语……都行）  at least 8 words (te reo, English, Martian…)
# 2) 查不到的词：问意思，然后「记住」它（words[word] = …）  unknown word: ask its meaning, then remember it
# 3) 输入「全部」：用 .items() 打印所有的词                 type "全部": print every word with .items()
# 4) 结束时打印：这次一共教会了它几个新词                   at the end: print how many new words you taught it this time
words = {
    "kia ora": "你好",
    "kai": "食物",
    "moana": "大海",
    # 👇 在这里加更多 / add more here
}

print("📖 翻译 app！输入一个词；输入 全部 看所有的词；输入 再见 结束。")
print("📖 Translator! Type a word; 全部 to list all; 再见 to stop.")
while True:
    word = input("词 / word: ").strip().lower()
    if word == "再见":
        break
    # ✍️ TODO：「全部」、查到了、查不到（教它）三种情况 / three cases: 全部, found, not found (teach it)
    print("👉", words.get(word, "不知道这个词 / unknown word"))

print("👋 再见！")


# ===== 🥈 加分 Part 2：测验模式 + 错题本 / Bonus: quiz mode + a mistakes book =====
# 1) 开头先问「翻译 还是 测验？」/ first ask "translate or quiz?"
# 2) 测验：随机考 5 个词（random.choice(list(words))），答对记分
#    quiz: test 5 random words (random.choice(list(words))) and keep score
# 3) 错题本：mistakes = {}，答错就 mistakes[w] = mistakes.get(w, 0) + 1；最后打印「你最容易错的词是 ___」
#    mistakes book: mistakes = {}; on a wrong answer mistakes[w] = mistakes.get(w, 0) + 1; at the end print your hardest word


# ===== 🥇 挑战 Part 3：AI 侦探报告（用程序写！）/ Challenge: an AI detective report (as a program!) =====
# 1) 请 AI 给你 10 个毛利语（或别的语言）单词和意思，放进字典 ai_words
#    ask an AI for 10 te reo Māori (or other) words with meanings; put them in a dict ai_words
# 2) 至少挑 3 个，用词典 / 老师核实，结果放进第二个字典 checked = {"kai": True, ...}（对 True，错 False）
#    check at least 3 with a dictionary or your teacher; record the results in checked = {"kai": True, ...}
# 3) 程序打印一份报告：每个查过的词 ✅ / ❌，没查过的标 ❓，最后算出「AI 在查过的词里对了 ___%」
#    print a report: ✅ / ❌ for each checked word, ❓ for unchecked ones, and "AI was right ___% of the checked words"
