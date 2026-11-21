# 🚀 第 3 关：冲上太空 / Level 3: climb to space
# fuel、burn、boost 每次运行都会变 / fuel, burn and boost change every run
# 每一步 / every step:  fuel 减 burn → speed 加 boost → altitude 加 speed → tick 加 1
#                       fuel minus burn → speed plus boost → altitude plus speed → tick plus 1
# 两种情况要停下 / stop when:  燃料不够再烧一步 (fuel < burn)   或者 or   altitude 到了 100
# 最后打印其中一行 / finally print ONE of:
#   SPACE at T+5, altitude 105, fuel 12          OUT OF FUEL at T+7, altitude 84, fuel 3

tick = 0
speed = 0
altitude = 0

while fuel >= burn:
    fuel = fuel - burn
    tick = tick + 1
    # TODO: speed 和 altitude 也要变 / speed and altitude need to change too

# TODO: 到了 100 → SPACE ...；没到 → OUT OF FUEL ...
print(f"OUT OF FUEL at T+{tick}, altitude {altitude}, fuel {fuel}")
