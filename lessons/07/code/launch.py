# 🚀 例 5：发射控制中心 Example 5: launch control
# 今天的进阶本领 Stretch skills:
#   ① 交回 True / False 的招式，直接放进 if      a trick that returns True / False, used right inside an if
#   ② 招式里喊招式                               tricks that call other tricks
#   ③ 默认值：不递东西就用它                     default values: used when nothing is handed in
#   ④ 交回一整个列表                             handing back a whole list
# ⚠️ 下面的发射规则是我们给玩具火箭编的，不是真火箭的规则
# ⚠️ These launch rules are made up for our toy rocket, not real rocket rules

def fuel_ok(fuel):
    return fuel >= 90                          # 油箱至少 90% / tank at least 90% full

def wind_ok(wind):
    return wind < 30                           # 风速小于 30 / wind below 30

def go_for_launch(fuel, wind):
    return fuel_ok(fuel) and wind_ok(wind)     # 招式里喊招式 / tricks calling tricks

def countdown(start=10):                       # start 的默认值是 10 / start defaults to 10
    numbers = []
    n = start
    while n > 0:
        numbers.append(n)
        n -= 1
    return numbers                             # 交回整个列表 / hand back the whole list

print(go_for_launch(95, 12))
print(go_for_launch(95, 45))
print(countdown(3))
print(len(countdown()))                        # 没递东西 → 用默认的 10 / nothing handed in → uses 10

fuel = 100
wind = 8
if go_for_launch(fuel, wind):
    for n in countdown(5):
        print(n, "...")
    print("🚀 点火！ Liftoff!")
else:
    print("⏸ 推迟发射 / Launch scrubbed")
