# ✊ 第 4 步：记分 + 一直玩到 3 分 Step 4: scores + play until 3 points
# test-input: 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头
import random

choices = ["石头", "剪刀", "布"]

def judge(me, computer):
    if me == computer:
        return "平"
    elif me == "石头" and computer == "剪刀":
        return "赢"
    elif me == "剪刀" and computer == "布":
        return "赢"
    elif me == "布" and computer == "石头":
        return "赢"
    else:
        return "输"

my_score = 0
computer_score = 0
rounds = 0

# 谁先到 3 分谁赢；rounds < 15 是安全带，万一一直平局也能停
# First to 3 wins; rounds < 15 is a seatbelt so endless ties still stop
while my_score < 3 and computer_score < 3 and rounds < 15:
    computer = random.choice(choices)
    me = input("你出什么？石头 / 剪刀 / 布： ").strip()
    if me not in choices:
        print("只能出 石头 / 剪刀 / 布 哦！")
        continue                         # 跳过这一轮，重新问 / skip this round and ask again
    rounds = rounds + 1
    result = judge(me, computer)
    print("你:", me, " 电脑:", computer, " →", result)
    if result == "赢":
        my_score = my_score + ___        # 加分 / add a point
    elif result == "输":
        computer_score = ___ + 1
    print("比分 Score  你 / you", my_score, ":", computer_score, "电脑 / computer")
    print()

if my_score > computer_score:
    print("🏆 你赢了！ You win!")
elif my_score < computer_score:
    print("🤖 电脑赢了！ Computer wins!")
else:
    print("🤝 平手！ It's a tie!")
