# 🧠 第 5 步（进阶）：会学习的电脑 Step 5 (stretch): a computer that learns
# 电脑偷偷数你每种拳出了几次，然后专门出能赢你「最爱」的拳！
# The computer secretly counts how often you play each move, then plays what beats your favourite!
# test-input: 石头 | 石头 | 石头 | 剪刀 | 石头 | 石头 | 布 | 石头 | 石头 | 石头
import random

choices = ["石头", "剪刀", "布"]
counts = [0, 0, 0]            # 你出了几次 石头 / 剪刀 / 布 — 和 choices 一一对应 / matches choices one to one

def beats_what(play):
    if play == "石头":
        return "剪刀"
    elif play == "剪刀":
        return "布"
    else:
        return "石头"

def judge(me, computer):
    if me == computer:
        return "平"
    if beats_what(me) == computer:
        return "赢"
    return "输"

def ask_player():
    while True:
        me = input("你出什么？石头 / 剪刀 / 布： ").strip()
        if me in choices:
            return me
        print("只能出 石头 / 剪刀 / 布 哦！")

# 谁能赢 play？/ what beats play?
def winner_against(play):
    if play == "石头":
        return "布"
    elif play == "剪刀":
        return "石头"
    else:
        return "剪刀"

# 交回你出得最多的拳 / return the move you played most
def favourite():
    best = 0
    for i in range(len(choices)):
        if counts[i] > counts[best]:
            best = i
    return choices[best]

def smart_computer(rounds):
    if rounds < 3:
        return random.choice(choices)       # 前 3 轮还不了解你 / doesn't know you yet
    return winner_against(favourite())      # 出能赢你最爱的拳 / play what beats your favourite

my_wins = 0
computer_wins = 0
for rounds in range(10):
    computer = smart_computer(rounds)       # 电脑先决定（不偷看你这一轮！）/ computer decides first (no peeking!)
    me = ask_player()
    for i in range(len(choices)):           # 记下你出了什么 / remember what you played
        if choices[i] == me:
            counts[i] += 1
    result = judge(me, computer)
    print("你:", me, " 电脑:", computer, " →", result)
    if result == "赢":
        my_wins += 1
    elif result == "输":
        computer_wins += 1

print("比分 Score", my_wins, ":", computer_wins)
print("电脑的小本本 / The computer's notes:", counts)
print("它觉得你最爱出 / It thinks your favourite is:", favourite())
