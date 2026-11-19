# 🛰️ 火星车 第 3 关：过关检查 / Mars Rover level 3: win check
if _crashed:
    print("__KC_HINT__ 💥 撞上了（看红点）。大石头有的 1 格长、有的 2 格、3 格——绕的时候别数格子：在上面一排「只要右边还是石头就继续往前走」（while rock_right(): move()）。|💥 Crash (see the red dot). Boulders can be 1, 2 or 3 cells long — don't count while going around: on the upper row, \"keep moving while there's still rock on your right\" (while rock_right(): move()).")
elif _flat:
    print("__KC_HINT__ 🪫 电池用完了。是不是绕来绕去回不到路上？|🪫 The battery ran out. Is the rover going round in circles?")
elif (_pos[0], _pos[1]) == _base:
    print("__KC_WIN__")
else:
    print("__KC_HINT__ 🏠 还没到基地 H。用 while not at_base(): 一直开，前面有石头就绕过去。|🏠 Not at base H yet. Use while not at_base(): to keep driving, and go around any boulder in front.")
