# 🛰️ 第 3 关：绕开大石头 / Level 3: dodge the boulders
# 一直往右开到基地 H。路上的大石头可能是 1、2 或 3 格长，下面是陨石坑（不能走），只能从上面绕！
# Drive right until you reach base H. Boulders on the road may be 1, 2 or 3 cells long; below is a crater, so go around ABOVE them!

while not at_base():
    if rock_ahead():
        # 绕过去：左转、上去一格、右转…… / go around: turn left, up one cell, turn right...
        turn_left()
        move()
        turn_right()
        move()
        # TODO: 石头有多长？右边还是石头就继续走 / how long is the boulder? keep going while there's rock on your right
        turn_right()
        move()
        turn_left()
    else:
        move()
