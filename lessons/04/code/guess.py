# 🎯 例 3：完整的猜数字游戏（填空） Example 3: the whole guessing game (fill in)
# 把 ___ 填好。提示：秘密数字是 1 到 10；猜大了要提示「太大了」
# Fill in ___. Hint: the secret is 1 to 10; a high guess gets "too big"
# test-input: 5 | 8 | 3
import random

secret = random.randint(1, ___)                 # 电脑出题 / the computer picks
print("我想了一个 1 到 10 的数字，你有 5 次机会！")
print("I'm thinking of a number from 1 to 10. You have 5 tries!")

for tries in range(5):
    guess = int(input("你猜 Your guess: "))
    if guess == ___:                            # 猜对了 / correct
        print("🎉 猜对了！你真厉害 You got it!")
        break                                   # break = 跳出循环，不用再猜 / break = leave the loop
    elif guess > secret:
        print("📉 太大了 Too big")
    else:
        print("📈 太___了 Too small")           # 把 ___ 换成一个字 / replace ___ with a word

print(f"游戏结束！答案是 The answer was {secret}")
