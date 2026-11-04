# ✊ 第 6 步：加料！石头剪刀布蜥蜴史波克 Step 6: extras! Rock Paper Scissors Lizard Spock
# 规则 Rules（每个拳赢两个 / each beats two）:
#   剪刀 赢 布、蜥蜴   布 赢 石头、史波克   石头 赢 剪刀、蜥蜴
#   蜥蜴 赢 史波克、布   史波克 赢 剪刀、石头
# test-input: 蜥蜴 | 史波克 | 石头 | 布 | 剪刀 | 蜥蜴 | 史波克 | 石头 | 布 | 剪刀 | 蜥蜴 | 史波克
import random

choices = ["石头", "剪刀", "布", "蜥蜴", "史波克"]

# 用「谁赢谁」的列表代替一大堆 elif：每一对 [赢家, 输家]
# A list of [winner, loser] pairs instead of a pile of elifs
beats = [
    ["剪刀", "布"], ["剪刀", "蜥蜴"],
    ["布", "石头"], ["布", "史波克"],
    ["石头", "剪刀"], ["石头", "蜥蜴"],
    ["蜥蜴", "史波克"], ["蜥蜴", "布"],
    ["史波克", "剪刀"], ["史波克", "石头"],
]

def judge(me, computer):
    if me == computer:
        return "平"
    if [me, computer] in beats:       # 先猜：这一行在问什么？ Guess: what is this line asking?
        return "赢"
    return "输"

my_score = 0
computer_score = 0
rounds = 0
while my_score < 3 and computer_score < 3 and rounds < 12:
    computer = random.choice(choices)
    me = input("你出什么？" + " / ".join(choices) + "： ").strip()
    if me not in choices:
        print("只能出", " / ".join(choices))
        continue
    rounds = rounds + 1
    result = judge(me, computer)
    print("你:", me, " 电脑:", computer, " →", result)
    if result == "赢":
        my_score = my_score + 1
    elif result == "输":
        computer_score = computer_score + 1
    print("比分  你", my_score, ":", computer_score, "电脑")

print("最终 Final:", my_score, ":", computer_score)
