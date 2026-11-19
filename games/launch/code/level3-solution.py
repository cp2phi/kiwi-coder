# 第 3 关参考答案 / Level 3 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
tick = 0
speed = 0
altitude = 0

while fuel >= burn and altitude < 100:
    fuel = fuel - burn
    speed = speed + boost
    altitude = altitude + speed
    tick = tick + 1

if altitude >= 100:
    print(f"SPACE at T+{tick}, altitude {altitude}, fuel {fuel}")
else:
    print(f"OUT OF FUEL at T+{tick}, altitude {altitude}, fuel {fuel}")
