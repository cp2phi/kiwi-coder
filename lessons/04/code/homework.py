# 🎲 第 4 课作业：猜数字豪华版  Lesson 4 homework: Guess Deluxe
# 作者 By：（写你的昵称 your nickname）
# AI 帮忙的地方 How AI helped：（如果问了 AI，写下它给的提示 / any hint AI gave you）
# test-input: 25 | 40 | 30 | 35 | 33 | 34 | 32
import random

# ===== 🥉 第 1 部分：1 到 50，7 次机会  Part 1: 1-50, 7 tries =====
secret = random.randint(1, 50)
count = 0                                   # 猜了几次 / how many guesses so far
print("🎲 我想了一个 1 到 50 的数字，你有 7 次机会！")
print("🎲 I'm thinking of a number from 1 to 50. You have 7 tries!")

for tries in range(7):
    guess = int(input("你猜 Your guess: "))
    count = count + 1                       # 每猜一次加 1 / add 1 every guess
    # TODO 1：写 if / elif / else（和 count 那行对齐）：
    #   猜对 → 打印「🎉 你用了 ? 次」然后 break；太大 → 📉；太小 → 📈
    # TODO 1: write if / elif / else (lined up with the count line):
    #   correct → print "🎉 you took ? tries" then break; too big → 📉; too small → 📈

    # TODO 2：在这里打印「还剩 ? 次机会」（提示：7 - count）。猜对的时候它会不会出现？为什么？
    # TODO 2: print "? tries left" here (hint: 7 - count). Does it show when you win? Why?

print(f"答案是 The answer was {secret}")

# ===== 🥈 第 2 部分：更聪明的提示  Part 2: smarter hints =====
# TODO 3：太大或太小的时候，如果只差 3 以内，再说「🔥 很接近了！」（if 里面再放一个 if）
# TODO 3: when too big or too small, if it's within 3, also say "🔥 very close!" (an if inside an if)
# TODO 4：每猜到第 3、第 6 次（count % 3 == 0），送一条线索：答案是双数还是单数？
# TODO 4: on guesses 3 and 6 (count % 3 == 0), give a free clue: is the answer even or odd?
# TODO 5：循环结束后，用 if 判断 guess == secret，打印「🏆 你赢了」或者「😢 机会用完了」
# TODO 5: after the loop, use if guess == secret to print "🏆 you win" or "😢 out of tries"

# ===== 🥇 第 3 部分：反过来！电脑猜你的数字  Part 3: reverse! the computer guesses YOUR number =====
# 你心里想一个 1 到 100 的数，电脑来猜，你只回答 big（猜大了）/ small（猜小了）/ yes（对了）。
# 电脑最多猜 7 次，而且一定要猜中！先在纸上写下步骤，再写代码。
# Think of a number from 1 to 100. The computer guesses; you only answer big / small / yes.
# It gets at most 7 guesses and must always win! Plan the steps on paper first, then code it.
