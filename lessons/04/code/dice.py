# 🎲 例 2：电子骰子 Example 2: electronic dice
# random.randint(1, 6) = 从 1 到 6 里随机挑一个（包括 1 和 6）
# random.randint(1, 6) = pick a random number from 1 to 6 (1 and 6 included)
import random

dice = random.randint(1, 6)
print(f"你掷出了 You rolled: {dice}")

if dice == 6:
    print("🏆 大吉！Jackpot!")
elif dice >= 4:                 # elif = 不然如果…… / otherwise, if…
    print("😊 不错 Not bad")
else:
    print("😅 再来一次 Try again")
