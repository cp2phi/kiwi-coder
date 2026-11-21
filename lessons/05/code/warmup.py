# 🔁 热身：掷骰子 10 次，数一数有几个 6 / Warm-up: roll 10 times and count the sixes
# 上节课的 if / elif / else + random，加上第 3 课的 for 和一个计数器
# Last lesson's if / elif / else + random, plus a for loop and a counter
import random

sixes = 0                                   # 计数器：一开始是 0 / counter: starts at 0

for i in range(10):
    dice = random.randint(1, 6)
    if dice == 6:
        print(f"🎲 {dice}  哇！六点！/ Wow, a six!")
        # ✍️ 在这里让 sixes 加 1 / add 1 to sixes here
    elif dice >= 4:
        print(f"🎲 {dice}  不错 / Not bad")
    else:
        print(f"🎲 {dice}  再来 / Try again")

print(f"一共掷出 {sixes} 个 6 / {sixes} sixes in total")
