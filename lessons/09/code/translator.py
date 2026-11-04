# test-input: kai | sun | ra | 再见
# 🗣️ 翻译机 app  Translator app
# 会翻译学过的词；不认识的词，你来教它！
# Translates words it knows; teach it the ones it doesn't!

maori = {
    "kia ora": "hello",
    "kai": "food",
    "moana": "sea",
    "whānau": "family",
}

print("🌏 毛利语翻译机！输入一个词，输入 再见 就结束。")
print("🌏 Te reo translator! Type a word, or 再见 to stop.")

while True:
    word = input("词 / word: ").strip().lower()
    if word == "再见":
        break
    if word in maori:                       # 字典里有这个标签吗？ / is the label in the dict?
        print(f"👉 {word} = {maori[word]}")
    else:
        print("🤔 不知道这个词，你来教我？ / I don't know it. Teach me?")
        meaning = input("它的意思是 / it means: ")
        maori[word] = meaning               # 放进一个新抽屉 / put it in a new drawer
        print("✅ 学会了！/ Learned!")

print("\n📚 我现在会的词 / Words I know now:")
for k in maori:                             # 一个标签一个标签地看 / go through every label
    print(f"  {k} = {maori[k]}")
