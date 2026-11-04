# 📖 我的第一个字典  My first dictionary
# 字典 = 带标签的抽屉：标签（键）→ 里面的东西（值）
# A dictionary = labelled drawers: label (key) → what's inside (value)

maori = {
    "kia ora": "hello",
    "kai": "food",
    "moana": "sea",
    "whānau": "family",
}

# 用标签拿东西 / use the label to get the thing
print(maori["kai"])
print(maori["moana"])

# 字典里有几个词？ / how many words?
print(len(maori))

# 🤔 试一试：把下面这行前面的 # 去掉，运行，看电脑怎么说
# Try: remove the # in front of the next line, run it, see what the computer says
# print(maori["sun"])

# 💡 安全的拿法：没有这个标签就给「默认值」 / safe way: a default if the label is missing
print(maori.get("sun", "不知道 / don't know"))

# 🏷️ 所有的标签 / all the labels: .keys()
for k in maori.keys():
    print("🏷️", k)
