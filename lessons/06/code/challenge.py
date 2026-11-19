# 🏆 挑战：太空知识闯关（3 条命）/ Challenge: space quiz with 3 lives
# test-input: mercury | jupiter | 8 | mars | saturn
# 用英文小写回答 / answer in lowercase English
import random

questions = ["离太阳最近的行星是？Which planet is closest to the Sun?",
             "太阳系里最大的行星是？Which is the biggest planet in our Solar System?",
             "太阳系有几颗行星？How many planets are in our Solar System?",
             "哪颗行星被叫做「红色星球」？Which planet is called the Red Planet?",
             "哪颗行星的光环最大最亮？Which planet has the biggest, brightest rings?"]
answers = ["mercury", "jupiter", "8", "mars", "saturn"]

lives = 3
score = 0

# ✍️ 设计你的闯关游戏 Design your game:
# 1. 只要「还有命」而且「分数还不到 5」，就继续出题（while + and）
#    keep asking while you still have lives AND score is below 5 (while + and)
# 2. 每次随机选一个编号 i，问 questions[i]，和 answers[i] 比 / pick a random i, ask questions[i], compare with answers[i]
# 3. 答对 score += 1；答错 lives -= 1，告诉他答案和还剩几条命 / right: score += 1; wrong: lives -= 1, show the answer and lives left
# 4. 循环结束后：通关了，还是没命了？/ after the loop: did you win, or run out of lives?
# 🌟 超难：同一题不要问两次（第 5 课的 pop）——想一想，while 的条件要不要改？
# 🌟 Extra hard: never ask the same question twice (lesson 5's pop) — does the while condition need to change?
