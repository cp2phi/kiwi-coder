# 第 5 关：教机器人一招「扫一行」/ Level 5: teach the robot a trick: "grab a row"
# 每行 5 颗宝石：走一格、捡一颗，重复 5 次 / each row has 5 gems: move, pick, 5 times
def grab_row():
    for i in range(___):
        move()
        ___()

grab_row()
# 换到上面一行（像蛇一样掉头）/ go up to the next row (turn around like a snake)
turn_left()
move()
move()
turn_left()
grab_row()
