# 🏆 挑战：晚饭决定器 / Challenge: dinner decider
# 改成你自己的：队名生成器？超能力抽奖？周末活动抽签？
# Make it yours: team name maker? superpower lottery? weekend activity picker?
import random

dinners = ["披萨 pizza", "寿司 sushi", "饺子 dumplings", "炸鱼薯条 fish and chips"]

print("今晚吃什么？让电脑决定！/ What's for dinner? Let the computer decide!")
print("👉 " + random.choice(dinners))

# 想一想 / Think:
# 1. 再加一个 drinks 列表，也随机选一个 / add a drinks list and pick one too
# 2. 用 for 循环一次抽 3 天的晚饭 / use a for loop to pick dinner for 3 days
