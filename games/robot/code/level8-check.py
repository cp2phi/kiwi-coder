# 💎 宝石机器人 第 8 关：过关检查 / Gem Robot level 8: win check
try:
    _has_fn = callable(sweep_row) and callable(next_row)
except NameError:
    _has_fn = False
if not _has_fn:
    print("__KC_HINT__ 🧩 这一关要用两个招式：def sweep_row(): 扫一行，def next_row(side): 掉头到上一行。|🧩 This level uses two tricks: def sweep_row(): sweeps one row, def next_row(side): U-turns onto the next row.")
elif _tired:
    print("__KC_HINT__ 🔋 机器人做了太多动作，没电了——是不是在两行之间来回跑？掉头方向要左、右轮流换；上面没路的时候 next_row() 要 return False。|🔋 The robot's battery ran out — is it running back and forth between two rows? The U-turn must switch left, right, left…; and next_row() must return False when there is no row above.")
elif crashed:
    print("__KC_HINT__ 💥 机器人撞到石头了（红点的地方）。掉头之前先问 front_is_clear()！|💥 The robot hit a rock (see the red dot). Ask front_is_clear() before the U-turn!")
elif missed > 0:
    print("__KC_HINT__ 🙅 有 " + str(missed) + " 次 pick() 的地方没有宝石。只在 gem_here() 的时候才 pick()。|🙅 " + str(missed) + " pick() calls happened where there was no gem. Only pick() when gem_here().")
elif len(gems) == 0:
    print("__KC_WIN__")
else:
    print("__KC_HINT__ 💎 还有 " + str(len(gems)) + " 颗宝石没捡。田地有 " + str(field_h) + " 行——每一行都扫了吗？掉头的方向要左、右、左、右轮流换。|💎 " + str(len(gems)) + " gems left. The field has " + str(field_h) + " rows — did you sweep every one? The U-turn must switch: left, right, left, right…")
