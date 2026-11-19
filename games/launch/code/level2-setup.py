# 🚀 发射控制 第 2 关：关卡代码（隐藏）/ Launch Control level 2: hidden setup
import random

# 记下孩子打印的每一行，检查的时候用 / remember every line the kid prints, for the check
_kc_print = print
_kc_buf = [""]
def print(*args, sep=" ", end="\n"):
    _kc_buf[0] = _kc_buf[0] + sep.join([str(a) for a in args]) + end
    _kc_print(*args, sep=sep, end=end)

def _kc_lines():
    return [_l.rstrip() for _l in _kc_buf[0].split("\n") if _l.strip() != ""]

def _kc_verdict(s, w, c):
    if s:
        return "NO GO storm"
    elif w > 40:
        return "NO GO wind"
    elif c < 0:
        return "NO GO cold"
    return "GO"

# 六个发射窗口的天气（每次运行都不一样）/ weather for six launch windows (different every run)
_bad_day = random.randint(1, 5) == 1
wind = []
storm = []
temp = []
for _i in range(6):
    _s = random.randint(1, 5) == 1
    _w = random.randint(5, 60)
    _c = random.randint(-6, 25)
    while _bad_day and _kc_verdict(_s, _w, _c) == "GO":
        _s = random.randint(1, 3) == 1
        _w = random.randint(5, 60)
        _c = random.randint(-8, 20)
    wind.append(_w)
    storm.append(_s)
    temp.append(_c)
_wind = list(wind)
_storm = list(storm)
_temp = list(temp)
_kc_print(f"📡 wind  = {wind}")
_kc_print(f"📡 storm = {storm}")
_kc_print(f"📡 temp  = {temp}")
_kc_print("--------")
