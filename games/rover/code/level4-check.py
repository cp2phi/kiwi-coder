# 🛰️ 火星车 第 4 关：过关检查 / Mars Rover level 4: win check
if _crashed:
    print("__KC_HINT__ 💥 撞墙了（看红点）。每次 move() 之前都要确定那个方向是空的。|💥 Hit a wall (see the red dot). Before every move(), make sure that direction is clear.")
elif _flat:
    print("__KC_HINT__ 🪫 电池用完了，还没找到基地。乱走是走不出迷宫的——试试「右手扶墙」：右边能走就右转再走，不能就往前，前面也不行就左转。|🪫 Battery empty before reaching base. Wandering won't solve a maze — try the right-hand rule: if you can go right, turn right and move; else go straight; if that's blocked too, turn left.")
elif (_pos[0], _pos[1]) == _base:
    print("__KC_WIN__")
else:
    print("__KC_HINT__ 🏠 还没到基地 H。迷宫每次都变，要用 while not at_base(): 加上一条「怎么走」的规则。|🏠 Not at base H yet. The maze changes every run, so use while not at_base(): with a rule for which way to go.")
