# 🎲 例 1：程序第一次做决定 Example 1: the program's first decision
# test-input: 7
secret = 7                                  # 秘密数字 / the secret number
guess = int(input("猜一个 1 到 10 的数字 Guess 1-10: "))   # int() 把文字变成数字 / int() turns text into a number

if guess == secret:                         # 如果猜对了…… / if the guess is right…
    print("🎉 猜对了！You got it!")
else:                                       # 不然…… / otherwise…
    print("❌ 不对哦 Nope!")

print("游戏结束 Game over")                 # 这一行没缩进，所以总是会跑 / not indented, so it always runs
