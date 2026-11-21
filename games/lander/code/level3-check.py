# 🛬 火箭着陆 第 3 关：过关检查 / Rocket Lander level 3: win check
if _ok_count == _FLIGHTS:
    print("__KC_WIN__")
elif not _done:
    print(f"__KC_HINT__ 🛬 第 {_flight} 枚助推器还在天上（高度 {_h}）。用 while not landed(): 一直飞到三枚都落地。|🛬 Booster #{_flight} is still in the air (height {_h}). Use while not landed(): to keep flying until all three are down.")
elif _f == 0:
    print(f"__KC_HINT__ ⛽ 第 {_flight} 枚只有 {_fs} 份燃料，用光了（落地速度 {_touch}）。慢慢往下飘太费油！高的时候让它快点掉，快到海面再使劲刹车。|⛽ Booster #{_flight} had only {_fs} fuel and it ran out (touchdown speed {_touch}). Drifting down slowly wastes fuel! Fall fast while you're high, brake hard near the sea.")
else:
    print(f"__KC_HINT__ 💥 第 {_flight} 枚落地速度 {_touch}，刹车晚了。越快越要早点刹车：可以让「允许的速度」跟着高度变，比如 height() // 10 + 2。|💥 Booster #{_flight} touched down at speed {_touch}: you braked too late. The faster you go, the earlier you must brake: let the \"allowed speed\" depend on height, e.g. height() // 10 + 2.")
