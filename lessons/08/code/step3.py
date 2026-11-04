# ✊ 第 3 步：judge() 判断输赢 Step 3: judge() decides who wins
# 规则 Rules:  石头 赢 剪刀    剪刀 赢 布    布 赢 石头
#              rock beats scissors, scissors beat paper, paper beats rock
# test-input: 剪刀
import random

choices = ["石头", "剪刀", "布"]

def judge(me, computer):
    if me == computer:
        return "平"                                  # tie
    elif me == "石头" and computer == "剪刀":
        return "赢"                                  # win
    elif me == ___ and computer == ___:             # 剪刀赢布 / scissors beat paper
        return "赢"
    elif me == ___ and computer == ___:             # 布赢石头 / paper beats rock
        return "赢"
    else:
        return "输"                                  # lose

# 先用固定的拳测试 judge / first test judge with fixed plays
print(judge("石头", "剪刀"), "← 应该是 赢 / should be 赢")
print(judge("布", "布"), "← 应该是 平 / should be 平")
print(judge("剪刀", "石头"), "← 应该是 输 / should be 输")

# 再真的玩一次 / now play for real
computer = random.choice(choices)
me = input("你出什么？ ").strip()
if me not in choices:
    print("只能出 石头 / 剪刀 / 布 哦！")
else:
    print("你:", me, " 电脑:", computer, " 结果:", judge(me, computer))
