# 🍎 接水果 第 1 关：过关检查 / Fruit Catcher level 1: win check
# 这一关只要把游戏跑起来（接 5 个是诚实规则）；检查一下关键的部分还在 / This level just needs the game to run (5 catches is an honour rule); check the key parts are still there
try:
    _ok = callable(tick) and callable(move_left) and callable(move_right) and hasattr(fruit, "ycor") and hasattr(basket, "xcor")
except NameError:
    _ok = False
if _ok:
    print("__KC_WIN__")
else:
    print("__KC_HINT__ 游戏的关键部分（tick、move_left、move_right、fruit、basket）被改坏了。点「↺ 还原」再试试|A key part of the game (tick, move_left, move_right, fruit, basket) got broken. Click ↺ Reset and try again")
