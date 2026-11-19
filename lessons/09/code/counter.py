# 🔢 例 4：用字典数数  Example 4: counting with a dictionary
# 还记得上节课「会学习的电脑」吗？counts = [0, 0, 0] 要记住第 0 个是石头……
# 用字典，标签就是拳的名字，清清楚楚！
# Remember last lesson's learning computer? counts = [0, 0, 0] meant remembering slot 0 = rock…
# With a dict, the label IS the move's name — crystal clear!

moves = ["石头", "布", "石头", "剪刀", "石头", "布"]

counts = {}                                   # 一个空字典 / an empty dict
for m in moves:
    counts[m] = counts.get(m, 0) + 1          # 🌟 数数的魔法公式 / the magic counting line
    print("看到 / saw", m, "→", counts)

print()
# 找出出得最多的拳 / find the most played move
best = ""
for move, n in counts.items():
    if best == "" or n > counts[best]:
        best = move
print("最爱出 / favourite:", best, "（", counts[best], "次 / times）")
