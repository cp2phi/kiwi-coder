# 🛰️ 第 4 关：熔岩管迷宫 / Level 4: lava-tube maze
# 迷宫每次运行都不一样，朝向也是随机的！写一条规则，让火星车自己走到基地 H。电池只有 120 格。
# The maze is different every run, and so is the starting direction! Write a rule so the rover finds base H by itself. Only 120 battery.
# 右手扶墙法 / the right-hand rule:
#   右边能走 → 右转，走一步 / right is open → turn right, move
#   不然前面能走 → 走一步 / else ahead is open → move
#   都不行 → 左转 / otherwise → turn left
# 现在的程序只会往前开，开到墙跟前就停 / for now the rover only drives straight until it meets a wall

while not rock_ahead():
    move()
