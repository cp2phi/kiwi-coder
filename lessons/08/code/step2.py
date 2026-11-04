# ✊ 第 2 步：你出拳 + 整理输入 Step 2: you play + tidy the input
# test-input:  石头
import random

choices = ["石头", "剪刀", "布"]
computer = random.choice(choices)

me = input("你出什么？石头 / 剪刀 / 布： What do you play? ")
me = me.strip()        # 去掉前后的空格 / remove spaces at both ends
# 先猜：输入 "  石头 " 会变成什么？ Guess: what does "  石头 " become?

if me not in choices:                      # 不在列表里 = 乱打 / not in the list = nonsense
    print("只能出 石头 / 剪刀 / 布 哦！ Only 石头 / 剪刀 / 布 please!")
else:
    print("你出了 / You played:", me)
    print("电脑出了 / Computer played:", computer)
