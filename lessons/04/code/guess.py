# 🎯 例 3：猜数字游戏——这次判断的部分你来写！ Example 3: the guessing game — you write the deciding part!
# test-input: 10 | 15 | 12 | 18 | 7
import random

secret = random.randint(1, 20)                  # 电脑出题 / the computer picks
print("我想了一个 1 到 20 的数字，你有 5 次机会！")
print("I'm thinking of a number from 1 to 20. You have 5 tries!")

for tries in range(5):
    guess = int(input(f"第 {tries + 1} 次 Try {tries + 1}: "))
    # ✍️ 你来写（大约 7 行，和上面的 guess 对齐）/ you write it (about 7 lines, lined up with guess above):
    #   猜对了 → 打印 🎉，然后 break      / correct  → print 🎉, then break
    #   太大了 → 打印 📉 太大了           / too big  → print 📉 too big
    #   不然   → 打印 📈 太小了           / otherwise → print 📈 too small


print(f"游戏结束！答案是 The answer was {secret}")
