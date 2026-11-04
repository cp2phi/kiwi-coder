# 🔁 热身：掷骰子 5 次 / Warm-up: roll the dice 5 times
# 上节课的 if / elif / else + random，加上第 3 课的 for
# Last lesson's if / elif / else + random, plus for from Lesson 3
import random

for i in range(5):
    dice = random.randint(1, 6)
    if dice == 6:
        print(f"🎲 {dice}  哇！六点！/ Wow, a six!")
    elif dice >= 4:
        print(f"🎲 {dice}  不错 / Not bad")
    else:
        print(f"🎲 {dice}  再来 / Try again")
