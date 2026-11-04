# test-input: kai | 再见
# 🏠 第 9 课作业：我的翻译 app  Lesson 9 homework: my translator app
# 作者 By：（写你的昵称 your nickname）
# 🕵️ AI 侦探报告 AI detective report：（🥇 挑战：AI 给的 10 个词，我查了哪 3 个？哪个对哪个错？）

# ===== 第 1 部分：我的词典（至少 8 个词） Part 1: my dictionary (at least 8 words) =====
# 可以是毛利语、英语、或任何你喜欢的语言 / te reo Māori, English, or any language you like
words = {
    "kia ora": "你好",
    "kai": "食物",
    "moana": "大海",
    # 👇 在这里加更多 / add more here
}

# ===== 第 2 部分：翻译循环 Part 2: the translate loop =====
print("📖 翻译 app！输入一个词，输入 再见 就结束。")
while True:
    word = input("词 / word: ").strip().lower()
    if word == "再见":
        break
    # 用 .get 查词，查不到给一句默认的话 / look it up with .get, with a default message
    print("👉", words.get(word, "不知道这个词 / unknown word"))

# ===== 第 3 部分（🥈）：教我新词 + 小测验模式 Part 3 (🥈): teach me a word + quiz mode =====
# 提示：第 2 部分的 else 里可以 words[word] = input("它的意思是：")
# 提示：测验模式就是第 9 课的「知识问答机」，把 quiz 换成 words

print("👋 再见！")
