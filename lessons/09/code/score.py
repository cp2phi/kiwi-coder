# 🏆 例 5（选做）：字典版石头剪刀布 + 会学习的电脑  Example 5 (optional): RPS with dicts + a learning computer
# 上节课的 beats_what()、counts = [0, 0, 0]，现在全部变成字典！
# Last lesson's beats_what() and counts = [0, 0, 0] — now all dictionaries!
# test-input: 石头 | 石头 | 布 | 石头 | 石头 | 剪刀
import random

choices = ["石头", "剪刀", "布"]
beats = {"石头": "剪刀", "剪刀": "布", "布": "石头"}              # X 能赢 beats[X] / X beats beats[X]
winner_against = {"剪刀": "石头", "布": "剪刀", "石头": "布"}     # 能赢 X 的是 winner_against[X] / what beats X
score = {"我": 0, "电脑": 0, "平局": 0}
counts = {}                                                       # 你每种拳出了几次 / how often you played each

for round_number in range(6):
    if len(counts) == 0:
        computer = random.choice(choices)            # 还不了解你 / doesn't know you yet
    else:
        favourite = ""
        for move, n in counts.items():               # 找你最爱的拳 / find your favourite
            if favourite == "" or n > counts[favourite]:
                favourite = move
        computer = winner_against[favourite]
    me = input("石头 / 剪刀 / 布？ ").strip()
    if me not in choices:
        print("看不懂，就算你出石头吧 / counting it as 石头")
        me = "石头"
    counts[me] = counts.get(me, 0) + 1
    print(f"电脑出了 {computer}")
    if me == computer:
        score["平局"] += 1
    elif beats[me] == computer:                      # 我出的能赢电脑出的吗？ does mine beat theirs?
        score["我"] += 1
    else:
        score["电脑"] += 1

print("\n📊 最后比分 / Final score:")
for who, n in score.items():
    print(f"  {who}: {n}")
print("电脑的小本本 / The computer's notes:", counts)
