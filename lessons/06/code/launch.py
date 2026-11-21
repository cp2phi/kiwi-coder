# 🚀 旗子变量：一直等到天气好才发射 / A flag variable: wait for good weather to launch
# 这些天气规则是我们为游戏编的 / these weather rules are made up for our game
import random

launched = False                             # 🚩 旗子：还没发射 / the flag: not launched yet
day = 0

while not launched:                          # 只要还没发射，就再等一天 / while not launched, wait another day
    day += 1
    wind = random.randint(0, 60)             # 风速 km/h / wind speed km/h
    rain = random.randint(1, 4) == 1         # 比较的结果 True / False 也能放进盒子！/ a comparison's True / False can go in a box!
    print(f"第 {day} 天 Day {day}: 风 wind {wind} km/h, 下雨 rain: {rain}")

    if wind < 30 and not rain:
        print("   ✅ GO! 发射！/ Launch!")
        launched = True                      # 🚩 举旗：循环下次检查时就停了 / raise the flag: the loop stops at the next check
    else:
        print("   ⛔ NO GO，明天再试 / try again tomorrow")

print(f"🚀 第 {day} 天终于发射了！/ Launched on day {day}!")
