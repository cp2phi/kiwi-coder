# test-input: 石头 | 布 | 剪刀
# 🏆 记分板字典  Scoreboard dictionary
# 还记得第 8 课的石头剪刀布吗？这次用字典记分 / RPS from Lesson 8, now scored with a dict
import random

choices = ["石头", "剪刀", "布"]
beats = {"石头": "剪刀", "剪刀": "布", "布": "石头"}   # 谁赢谁 / what beats what
score = {"我": 0, "电脑": 0}                           # 两个抽屉记分 / two drawers for scores

for round_number in range(3):
    me = input("石头 / 剪刀 / 布？ ").strip()
    computer = random.choice(choices)
    print(f"电脑出了 {computer}")
    if me == computer:
        print("平局！")
    elif beats.get(me) == computer:        # 我出的能赢电脑出的吗？ / does mine beat theirs?
        print("我赢了！")
        score["我"] = score["我"] + 1
    else:
        print("电脑赢了！")
        score["电脑"] = score["电脑"] + 1

print("\n📊 最后比分 / Final score:")
for who in score:
    print(f"  {who}: {score[who]}")
