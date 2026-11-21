# 🛬 第 5 关：自动驾驶 / Level 5: autopilot
# 刹车的时候，每一拍速度少 2，然后掉「新的速度」那么多。速度到 2 或更小就算停住了。
# While braking, speed drops by 2 every tick, then the booster falls by the NEW speed. At speed 2 or less it counts as stopped.
# 例 / e.g.  brake_distance(10) = 8 + 6 + 4 + 2 = 20      brake_distance(7) = 5 + 3 + 1 = 9

def brake_distance(v):
    # TODO: 用 while 循环把每一拍掉的距离加起来 / add up the distance of every tick with a while loop
    return 0

def autopilot(h, v, fuel):
    # 交回 True = 这一拍点火，False = 不点 / return True = burn this tick, False = don't
    # 想一想：如果这一拍「不」点火，速度会变成 v + 1，还会掉 v + 1……那时候还刹得住吗？
    # Think: if you DON'T burn this tick, speed becomes v + 1 and you drop v + 1... could you still stop in time?
    return v > 2

print(brake_distance(10), "← 应该是 should be 20")
print(brake_distance(7), "← 应该是 should be 9")
fly(autopilot)
