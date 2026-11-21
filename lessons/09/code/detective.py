# test-input: 惠灵顿 | 几维鸟 | 奥克兰 | 木星 | 1969 | 1840
# 🕵️ AI 侦探：这是「AI 写的」问答机，里面有错！ AI Detective: an "AI-written" quiz — it has mistakes!
# 任务：运行它，一条一条核实，找出错误的答案并改正。（不止一个哦！）
# Mission: run it, check every answer, find the wrong ones and fix them. (There's more than one!)

quiz = {
    "新西兰的首都是？": "奥克兰",
    "新西兰最有名的象征鸟是？": "几维鸟",
    "新西兰最大的城市是？": "奥克兰",
    "太阳系最大的行星是？": "土星",
    "人类第一次登上月球是哪一年？": "1969",
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
print("🕵️ 侦探任务：AI 的哪几条答案是错的？")
