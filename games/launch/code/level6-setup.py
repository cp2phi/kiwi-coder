# 🚀 发射控制 第 6 关：关卡代码（隐藏）/ Launch Control level 6: hidden setup
import random

_kc_print = print

def _kc_messy(word):
    # 随机大小写 + 随机空格 / random capitals + random spaces
    s = ""
    for ch in word:
        if random.randint(0, 1) == 1:
            s = s + ch.upper()
        else:
            s = s + ch
    return " " * random.randint(0, 2) + s + " " * random.randint(0, 2)

_kc_stations = ["booster", "engines", "fuel", "weather", "range", "recovery", "comms"]

def _kc_status():
    # 随机挑几个岗位、随机顺序、随机回答 / random stations, random order, random replies
    names = list(_kc_stations)
    random.shuffle(names)
    d = {}
    nbad = random.randint(0, 3)
    for i in range(random.randint(4, 7)):
        if i < nbad and random.randint(0, 3) > 0:
            d[names[i]] = _kc_messy("no go")
        else:
            d[names[i]] = _kc_messy("go")
    keys = list(d.keys())
    random.shuffle(keys)
    d2 = {}
    for k in keys:
        d2[k] = d[k]
    return d2

# 今天的点名结果（每次运行都不一样）/ today's poll (different every run)
status = _kc_status()
_kc_print(f"📡 status = {status}")
_kc_print("--------")

_kc_tests = [{"booster": "go", "weather": "no go"}, {"range": " GO ", "fuel": "Go"}, {"comms": "No Go", "booster": "no go", "engines": "go"}]
for _n in range(8):
    _kc_tests.append(_kc_status())

def _kc_blockers(d):
    out = []
    for k in d:
        if d[k].strip().lower() != "go":
            out.append(k)
    return out

def _kc_director(d):
    b = _kc_blockers(d)
    if len(b) == 0:
        return "GO FOR LAUNCH"
    return "HOLD: " + ", ".join(b)

def _kc_copy(d):
    c = {}
    for k in d:
        c[k] = d[k]
    return c

def _kc_call(fn, arg):
    # 调用孩子的函数；出错也不要让检查代码崩掉 / call the kid's function without letting an error crash the check
    try:
        return [True, fn(_kc_copy(arg))]
    except Exception as e:
        return [False, str(e)]
