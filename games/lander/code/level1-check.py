# 🛬 火箭着陆 第 1 关：过关检查 / Rocket Lander level 1: win check
def _kc_fall(swap):
    h = _h0
    v = 0
    n = 0
    while True:
        n = n + 1
        if swap:
            h = h - v
            v = v + _g
        else:
            v = v + _g
            h = h - v
        if h <= 0:
            return [n, v]

_r = _kc_fall(False)
_want = f"Touchdown at tick {_r[0]}, speed {_r[1]}"
_got = _kc_lines()
_last = ""
if len(_got) > 0:
    _last = _got[-1]
_sw = _kc_fall(True)
if _last == _want:
    print("__KC_WIN__")
elif _last == "":
    print("__KC_HINT__ 🤔 什么都没打印。落地（height <= 0）的时候要打印 Touchdown at tick …, speed …|🤔 Nothing printed. When it lands (height <= 0), print Touchdown at tick …, speed …")
elif not _last.startswith("Touchdown at tick"):
    print(f"__KC_HINT__ 🔍 最后一行要长这样：Touchdown at tick 12, speed 12（用 f 字符串把 tick 和 speed 放进去）。你的是「{_last}」。|🔍 The last line should look like: Touchdown at tick 12, speed 12 (use an f-string with tick and speed). Yours is \"{_last}\".")
elif _last == f"Touchdown at tick {_sw[0]}, speed {_sw[1]}" and _sw[0] != _r[0]:
    print("__KC_HINT__ 🔁 顺序反了！每一拍要「先」让 speed 加 g，「再」让 height 减 speed。|🔁 Wrong order! Each tick: FIRST speed goes up by g, THEN height goes down by speed.")
else:
    print(f"__KC_HINT__ 🔍 这次应该是「{_want}」，你的是「{_last}」。检查：speed 每拍加的是 g（不是 1）；tick 从 1 开始数。|🔍 This time it should be \"{_want}\", yours is \"{_last}\". Check: speed grows by g each tick (not always 1); tick counts from 1.")
