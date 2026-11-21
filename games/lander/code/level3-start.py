# 🛬 第 3 关：燃料不够了 / Level 3: not enough fuel
# 这次更高，一开始就在往下掉，每枚燃料只有 16~20 份！第 2 关「慢慢飘下来」的办法会把油用光 ⛽
# Higher this time, already falling, and only 16-20 fuel per booster! Level 2's "drift down slowly" trick runs out of fuel ⛽
# 想一想：高的时候可以掉得快一点，越低越要慢——什么时候点火最省油？
# Think: high up you can fall fast; the lower you are, the slower you must be — when is the best time to burn?

while not landed():
    if speed() > 2:
        step(True)
    else:
        step(False)
