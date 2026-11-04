# test-input: 惠灵顿 | 几维鸟 | 3 | 奥克兰
# 🧠 知识问答机  Quiz machine
# 问题是标签（键），答案是里面的东西（值） / question = key, answer = value

quiz = {
    "新西兰的首都是？": "惠灵顿",
    "新西兰的国鸟是？": "几维鸟",
    "一个三角形有几条边？": "3",
    "新西兰最大的城市是？": "奥克兰",
}

score = 0
for question in quiz:                 # 轮流问每一个问题 / ask every question in turn
    answer = input(question + " ")
    if answer.strip() == quiz[question]:
        print("✅ 对了！")
        score = score + 1
    else:
        print(f"❌ 不对，是 {quiz[question]}")

print(f"\n🏆 你答对了 {score} / {len(quiz)} 题！")
