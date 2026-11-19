# 第 7 关：会看路的海龟 / Level 7: the turtle that looks where it's going
# ⚠️ 每次运行，迷宫都会变！不能数格子，要让海龟自己「看路」。
# ⚠️ The maze changes every run! Counting cells won't work — the turtle must look for itself.
# 新指令 / new commands: wall_ahead()  wall_left()  wall_right()  at_goal()
# 每一格是 60 步 / each cell is 60 steps

while not at_goal():
    if not wall_ahead():
        forward(60)
    else:
        left(90)    # 🤔 一碰到墙就左转……永远对吗？/ always turn left at a wall... is that always right?
