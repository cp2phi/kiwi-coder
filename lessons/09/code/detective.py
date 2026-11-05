# test-input: 惠灵顿 | 几维鸟 | 奥克兰 | 3 | 1840
# 🕵️ AI 侦探：这是 AI 写的问答机，里面有错！ AI Detective: an AI wrote this quiz — it has mistakes!
# 任务：运行它，和老师一起找出哪条答案是错的，改正它。
# Mission: run it, find the wrong answer(s) with your teacher, and fix them.

quiz = {
    "新西兰的首都是？": "奥克兰",
    "新西兰最有名的象征鸟是？": "几维鸟",
    "新西兰最大的城市是？": "奥克兰",
    "一个三角形有几条边？": "3",
    "《怀唐伊条约》是哪一年签的？": "1840",
}

score = 0
for question in quiz:
    answer = input(question + " ")
    if answer.strip() == quiz[question]:
        print("✅ 对了！")
        score = score + 1
    else:
        print(f"❌ AI 说答案是 {quiz[question]}……真的吗？🤔")

print(f"\n你答对了 {score} / {len(quiz)}（按 AI 的标准）")
print("🕵️ 侦探任务：AI 的哪一条答案是错的？")
