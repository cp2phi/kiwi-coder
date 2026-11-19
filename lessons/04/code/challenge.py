# 🏆 挑战：火箭发射控制中心 Challenge: rocket launch control
# test-input: 95 | 20
# 这些发射规则是我们为游戏编的 / these launch rules are made up for our game
fuel = int(input("燃料还剩百分之几？Fuel % (0-100): "))
wind = int(input("风速多少 km/h？Wind speed in km/h: "))

# ✍️ 第 1 步 Step 1：
#   燃料 < 90 → 打印「⛔ NO GO：燃料不够」 / fuel < 90 → print "⛔ NO GO: not enough fuel"
#   不然（else）里面，再用一个 if 检查风： / otherwise, put another if INSIDE the else to check the wind:
#     风 > 40 → 「⛔ NO GO：风太大」，不然 → 「✅ GO!」 / wind > 40 → "⛔ NO GO: too windy", else → "✅ GO!"
#
# ✍️ 第 2 步 Step 2：GO 的时候从 10 倒数到 1：双数秒打印「📡 系统正常」，单数秒只打印数字，最后「🚀 点火！」
#   On GO, count down from 10 to 1: on even seconds print "📡 systems OK", on odd seconds just the number, then "🚀 Ignition!"
#
# ✍️ 第 3 步 Step 3（超难 extra hard）：GO 的时候，用海龟画一枚火箭飞上天！ / On GO, draw a rocket flying up with the turtle!
