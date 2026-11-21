# 🛰️ 火星车 第 1 关：过关检查 / Mars Rover level 1: win check
if _crashed:
    print("__KC_HINT__ 💥 火星车撞上岩石了（看红点）。每走一步之前先问 rock_ahead()：前面是岩石就 break 停下来。|💥 The rover hit a rock (see the red dot). Before every move, ask rock_ahead(): if there's a rock, break out of the loop.")
elif len(_drilled) == 3:
    print("__KC_WIN__")
elif len(_drilled) == 0 and _wasted_drills == 0:
    print("__KC_HINT__ 🪨 一块岩石都没钻。开到岩石跟前（岩石就在正前方），再 drill()。|🪨 No rock drilled yet. Drive right up to a rock (so it's straight ahead), then drill().")
elif _wasted_drills > 0:
    print(f"__KC_HINT__ 🪨 钻了 {len(_drilled)} / 3 块。有 {_wasted_drills} 次 drill() 的时候前面没有带金点的岩石（橙点的地方）——要正好停在岩石跟前。地图每次都变，别数格子，用 rock_ahead()！|🪨 {len(_drilled)} / 3 rocks drilled. {_wasted_drills} drill() calls had no gold-dot rock straight ahead (see the orange dots) — stop right in front of the rock. The map changes every run, so don't count cells: use rock_ahead()!")
else:
    print(f"__KC_HINT__ 🪨 钻了 {len(_drilled)} / 3 块。三段路是一样的套路：开到岩石跟前 → drill() → turn_left()。用一个循环重复 3 次！|🪨 {len(_drilled)} / 3 rocks drilled. All three legs are the same pattern: drive up to the rock → drill() → turn_left(). Repeat it 3 times with a loop!")
