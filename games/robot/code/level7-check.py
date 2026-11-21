# 💎 宝石机器人 第 7 关：过关检查 / Gem Robot level 7: win check
if _tired:
    print("__KC_HINT__ 🔋 机器人做了太多动作，没电了——是不是有个循环停不下来？|🔋 The robot did so many actions its battery ran out — is a loop never stopping?")
elif crashed:
    print("__KC_HINT__ 💥 机器人撞到石头了（红点的地方）。走之前先问 front_is_clear()！|💥 The robot hit a rock (see the red dot). Ask front_is_clear() before you move!")
elif missed > 0:
    print("__KC_HINT__ 🙅 有 " + str(missed) + " 次 pick() 的地方没有宝石。只在 gem_here() 是 True 的时候才 pick()——用 if！|🙅 " + str(missed) + " pick() calls happened where there was no gem. Only pick() when gem_here() is True — use if!")
elif len(gems) == 0:
    print("__KC_WIN__")
else:
    print("__KC_HINT__ 💎 还有 " + str(len(gems)) + " 颗宝石没捡。房间有 4 面墙——机器人每面墙都走了吗？（墙角那一格也别忘了）|💎 " + str(len(gems)) + " gems left. The room has 4 walls — did the robot walk along every one? (Don't forget the corner cells.)")
