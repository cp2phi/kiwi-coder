# ✊ 第 4 步：N 局几胜 + 统计 Step 4: best of N + stats
# test-input: 5 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头
import random

choices = ["石头", "剪刀", "布"]

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

best_of = int(input("几局几胜？输入 3、5 或 7 / Best of 3, 5 or 7? "))
target = int(best_of / 2) + 1          # 5 局 → 先到 3 分 / best of 5 → first to 3
print("先到", target, "分的赢！ First to", target, "wins!")

my_score = 0
computer_score = 0
ties = 0
rounds = 0

# rounds < 20 是安全带：万一一直平局也能停 / rounds < 20 is a seatbelt in case of endless ties
while my_score < target and computer_score < target and rounds < 20:
    computer = random.choice(choices)
    me = ask_player()
    rounds += 1
    result = judge(me, computer)
    print("你:", me, " 电脑:", computer, " →", result)
    # ✍️ TODO 1：根据 result，给 my_score、computer_score 或 ties 加 1
    #            add 1 to my_score, computer_score or ties, depending on result

    print("比分 Score  你 / you", my_score, ":", computer_score, "电脑 / computer")
    print()

# ✍️ TODO 2：打印谁赢了这一局 / print who won the game

# ✍️ TODO 3：打印统计：一共几轮、平了几次、你的胜率 %（你赢的轮数 ÷ 总轮数 × 100，用 int() 去掉小数）
#            print stats: rounds played, ties, your win rate % (rounds you won ÷ rounds × 100, int() drops the decimals)
