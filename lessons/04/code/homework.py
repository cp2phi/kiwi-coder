# 🎲 第 4 课作业：猜数字豪华版  Lesson 4 homework: Guess Deluxe
# 作者 By：（写你的昵称 your nickname）
# AI 帮忙的地方 How AI helped：（如果问了 AI，写下它给的提示 / any hint AI gave you）
# test-input: 10 | 15 | 12 | 18 | 7 | 3 | n
import random
import turtle

# ===== 🥉 第 1 部分：1 到 20，6 次机会，记录猜了几次  Part 1: 1-20, 6 tries, count the tries =====
secret = random.randint(1, 20)
count = 0                                   # 猜了几次 / how many guesses so far
print("🎲 我想了一个 1 到 20 的数字，你有 6 次机会！")
print("🎲 I'm thinking of a number from 1 to 20. You have 6 tries!")

for tries in range(6):
    guess = int(input("你猜 Your guess: "))
    count = count + 1                       # 每猜一次加 1 / add 1 every guess
    if guess == secret:
        print(f"🎉 猜对了！你用了 {count} 次 You got it in {count} tries!")
        break
    elif guess > secret:
        print("📉 太大了 Too big")
    else:
        # TODO 1：猜小了的时候该说什么？ / what to say when the guess is too small?
        print("…")

print(f"答案是 The answer was {secret}")

# ===== 🥈 第 2 部分：猜对了就放烟花 + 再玩一次？  Part 2: fireworks when you win + play again? =====
# TODO 2：在上面「猜对了」的地方，让海龟画一个随机颜色的庆祝图案（提示：先写一个列表 colors，用 random.randint 选下标）
# TODO 2: where it says "猜对了", make the turtle draw a celebration in random colours
# TODO 3：问「再玩一次吗？(y/n)」，如果回答是 "y" 就打印「下次见！」……想一想还能做什么
# TODO 3: ask "play again? (y/n)"; if the answer == "y" print something fun

# ===== 🥇 第 3 部分：冷热提示  Part 3: hot & cold hints =====
# TODO 4：用 abs(guess - secret) 算出「差多少」；差 ≤ 2 就说「🔥 很热」，差 ≤ 5 说「🌤 温的」，不然说「🧊 很冷」
# TODO 4: use abs(guess - secret); ≤ 2 → "🔥 hot", ≤ 5 → "🌤 warm", else "🧊 cold"
