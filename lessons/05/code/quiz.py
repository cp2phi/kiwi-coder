# test-input: hello | family | food | sea | sun
# 🇳🇿 毛利语单词小测验 / Te reo Māori word quiz
# 两个列表是「配对」的：maori[0] 的意思就是 english[0]
# The two lists are paired: maori[0] means english[0]
import random

maori = ["kia ora", "whānau", "kai", "moana", "rā"]
english = ["hello", "family", "food", "sea", "sun"]

score = 0
wrong = []                                   # 答错的词放这里 / wrong words go here

for q in range(5):
    i = random.randint(0, len(maori) - 1)    # 随机编号，列表多长都行 / a random number that works for any length
    answer = input(f"「{maori[i]}」是什么意思？（用英文小写回答）What does it mean? (lowercase English) ")
    if answer == english[___]:               # 填空：应该和第几个英文比？/ Fill in: compare with which English word?
        print("✅ Ka pai! 答对了")
        score = score + 1
    else:
        print(f"❌ 是 {english[i]}")
        # ✍️ 把答错的毛利语词放进 wrong 列表 / put the Māori word into the wrong list

print(f"得分 Score: {score} / 5")
# ✍️ 如果 wrong 是空的（len(wrong) == 0），打印「💯 满分！」；不然打印「要复习 Review:」和 wrong
# ✍️ If wrong is empty (len(wrong) == 0) print "💯 Full marks!"; otherwise print "Review:" and wrong
