# 🛬 火箭着陆 第 6 关：关卡代码（隐藏，每次数据都不一样）/ Rocket Lander level 6: hidden setup (new data every run)
import random

_kc_print = print
_kc_names = ["B-Kea", "B-Tui", "B-Weka", "B-Kiwi", "B-Ruru", "B-Moa"]

def _kc_land(fl):
    c = {}
    for f in fl:
        if f["landed"]:
            c[f["booster"]] = c.get(f["booster"], 0) + 1
    return c

def _kc_vet(c):
    best = ""
    for k in c:
        if best == "" or c[k] > c[best]:
            best = k
    return best

def _kc_unique_max(c):
    if len(c) == 0:
        return False
    top = c[_kc_vet(c)]
    n = 0
    for k in c:
        if c[k] == top:
            n = n + 1
    return n == 1

def _kc_flights(n):
    # 随机的飞行记录，保证「飞得最多」的只有一枚 / random flight log with exactly one top booster
    while True:
        k = random.randint(3, 6)
        names = list(_kc_names)
        random.shuffle(names)
        names = names[0:k]
        fl = []
        for i in range(n):
            fl.append({"booster": random.choice(names), "landed": random.randint(1, 100) <= 85})
        if _kc_unique_max(_kc_land(fl)):
            return fl

def _kc_copy(fl):
    out = []
    for f in fl:
        out.append({"booster": f["booster"], "landed": f["landed"]})
    return out

# 我们假想的助推器机队这一年的飞行记录（每次运行都不一样）/ our pretend fleet's flight log for the year (new every run)
flights = _kc_flights(16)
_kc_print(f"📡 {len(flights)} flights, e.g. flights[0] = {flights[0]}")
_kc_print("--------")
