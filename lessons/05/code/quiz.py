# test-input: hello | family | food | sea | sun
# 🇳🇿 毛利语单词小测验 / Te reo Māori word quiz
# 两个列表是「配对」的：maori[0] 的意思就是 english[0]
# The two lists are paired: maori[0] means english[0]
import random

maori = ["kia ora", "whānau", "kai", "moana", "rā"]
english = ["hello", "family", "food", "sea", "sun"]

score = 0
for round in range(5):
    i = random.randint(0, 4)                 # 随机选一个编号 / pick a random number
    answer = input(f"「{maori[i]}」是什么意思？What does it mean? ")
    if answer == english[___]:               # 填空：应该和第几个英文比？/ Fill in: compare with which English word?
        print("✅ Ka pai! 答对了")
        score = score + 1
    else:
        print(f"❌ 是 {english[i]}")

print(f"得分 Score: {score} / 5")
