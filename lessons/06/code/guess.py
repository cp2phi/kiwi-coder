# test-input: 1 | 2 | 3 | 4 | 5 | 6
# 🎲 猜数字 2.0：只要「还没猜对」而且「还有机会」就继续 / Guess 2.0: keep going while "not right yet" AND "tries left"
import random

secret = random.randint(1, 50)
guess = 0
tries = 0

while guess != secret and tries < 6:          # 两个条件都要 True / both must be True
    guess = int(input(f"第 {tries + 1} 次，猜 1 到 50 / Try {tries + 1}, guess 1-50: "))
    tries += 1                                # 和 tries = tries + 1 一样 / same as tries = tries + 1
    if guess < secret:
        print("太小了 / Too small")
    elif guess > secret:
        print("太大了 / Too big")

# ✍️ 循环停下来只有两个原因：猜对了，或者机会用完了。
#    写 if / else：猜对 → 「🎉 用了 ? 次」；不然 → 「😢 答案是 ?」
# ✍️ The loop stops for only two reasons: you got it, or you ran out of tries.
#    Write if / else: right → "🎉 took ? tries"; otherwise → "😢 the answer was ?"
