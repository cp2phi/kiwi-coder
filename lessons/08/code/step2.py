# ✊ 第 2 步：你出拳——不合格就一直问 Step 2: you play — keep asking until it's valid
# test-input: 香蕉 | 布
import random

choices = ["石头", "剪刀", "布"]

# 一直问，直到输入合格，才把它「交回」/ keep asking until the input is OK, then return it
def ask_player():
    while True:
        me = input("你出什么？石头 / 剪刀 / 布： What do you play? ").strip()
        if me in choices:          # 在列表里吗？ is it in the list?
            return me              # return 直接跳出循环，也跳出招式！ return jumps out of the loop AND the trick!
        print("只能出 石头 / 剪刀 / 布 哦！ Only 石头 / 剪刀 / 布 please!")

me = ask_player()
computer = random.choice(choices)
print("你出了 / You played:", me)
print("电脑出了 / Computer played:", computer)
