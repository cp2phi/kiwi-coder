# 🛰️ 火星车 第 5 关：过关检查 / Mars Rover level 5: win check
try:
    _has = callable(sweep_row) and callable(u_turn)
except NameError:
    _has = False
if not _has:
    print("__KC_HINT__ 🧩 这一关要两个函数：def sweep_row(): 和 def u_turn(side):（名字要一模一样），再用它们来扫。|🧩 This level needs two functions: def sweep_row(): and def u_turn(side): (exact names), then sweep with them.")
elif _crashed:
    print("__KC_HINT__ 💥 撞上悬崖了（看红点）。掉头之前先问 rock_ahead()：上面没有路了，就说明扫完了，u_turn 要 return False。|💥 Drove into a cliff (see the red dot). Before stepping up a row, ask rock_ahead(): if it's blocked, the survey is finished and u_turn should return False.")
elif _flat:
    print("__KC_HINT__ 🪫 电池用完了。每一格只要走一次就够了。|🪫 The battery ran out. Every cell only needs to be visited once.")
elif len(_samples) > 0:
    print(f"__KC_HINT__ 🧪 还有 {len(_samples)} 个样本没收。每一排都要扫到——一排扫完，换下一排，左右方向轮流换。|🧪 {len(_samples)} samples left. Sweep every row — finish a row, move up, and swap left/right each time.")
elif _wasted > 0:
    print(f"__KC_HINT__ 🧪 有 {_wasted} 次 collect() 的地方没有样本（橙点）。先问 sample_here()！|🧪 {_wasted} collect() calls were on empty cells (orange dots). Ask sample_here() first!")
else:
    print("__KC_WIN__")
