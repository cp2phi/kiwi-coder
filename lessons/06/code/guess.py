# test-input: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
# 🎲 猜数字 2.0：用 while 一直猜到对为止，还会数你猜了几次
# Guess the number 2.0: keep guessing with while until you get it, and count the tries
import random

secret = random.randint(1, 10)
guess = 0
tries = 0

while guess != secret:                        # 没猜对就继续 / keep going until correct
    guess = int(input("猜一个 1 到 10 的数字 / Guess 1 to 10: "))
    tries += 1                                # 和 tries = tries + 1 一样 / same as tries = tries + 1
    if guess < secret:
        print("太小了 / Too small")
    elif guess > secret:
        print("太大了 / Too big")

print(f"🎉 答对了！一共猜了 {tries} 次 / Correct! It took {tries} tries")
