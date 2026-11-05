# 🐞 病号 2：这个程序会报错。读报错，找到那一行，治好它！
# Patient 2: this program crashes. Read the error, find the line, cure it!
# test-expect-error: SyntaxError
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
result = judge("石头", "剪刀")
if result = "赢":
    my_score = my_score + 1
print("比分", my_score)
