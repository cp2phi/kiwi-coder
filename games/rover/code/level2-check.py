# 🛰️ 火星车 第 2 关：过关检查 / Mars Rover level 2: win check
if _crashed:
    print("__KC_HINT__ 💥 火星车撞上悬崖了（看红点）。场地大小每次都变：先问 rock_ahead()，前面挡住了就 break，再转弯。|💥 The rover drove into a cliff (see the red dot). The field size changes every run: ask rock_ahead() first; if it's blocked, break and then turn.")
elif _flat:
    print("__KC_HINT__ 🪫 电池用完了。沿着边走一圈就够了，不用走别的地方。|🪫 The battery ran out. One lap around the edge is all you need.")
elif len(_samples) > 0:
    print(f"__KC_HINT__ 🧪 还有 {len(_samples)} 个样本没收（紫色的点）。每到一格都问 sample_here()，是的话就 collect()。|🧪 {len(_samples)} samples still out there (purple dots). On every cell ask sample_here(); if yes, collect().")
elif _wasted > 0:
    print(f"__KC_HINT__ 🧪 样本都收到了，可是有 {_wasted} 次 collect() 的地方没有样本（橙点）——浪费了机械臂的力气。用 if sample_here(): 再 collect()。|🧪 All samples collected, but {_wasted} collect() calls were on empty cells (orange dots) — wasted arm power. Use if sample_here(): before collect().")
elif (_pos[0], _pos[1]) != _base:
    print("__KC_HINT__ 🏠 样本都收好了！最后还要回到基地 H（就是起点）。一共 4 条边哦。|🏠 All samples collected! Now finish back at base H (where you started). There are 4 sides in total.")
else:
    print("__KC_WIN__")
