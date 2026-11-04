# 🔁 热身：上节课的列表 + random.choice / Warm-up: lists + random.choice from last lesson
import random

moods = ["😀 开心", "😴 想睡觉", "🤩 超级兴奋", "🤔 在思考"]
names = ["小海龟", "Kiwi", "机器人 9 号"]

for i in range(3):
    print(f"{random.choice(names)} 今天 {random.choice(moods)}")

# 任务：加一个新列表 foods，让句子多一句「想吃……」
# Task: add a new list foods and make the sentence say what they want to eat
