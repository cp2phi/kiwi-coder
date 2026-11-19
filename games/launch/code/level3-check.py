# 🚀 发射控制 第 3 关：过关检查 / Launch Control level 3: win check
_f = _fuel
_tk = 0
_sp = 0
_al = 0
while _f >= _burn and _al < 100:
    _f = _f - _burn
    _sp = _sp + _boost
    _al = _al + _sp
    _tk = _tk + 1
if _al >= 100:
    _want = f"SPACE at T+{_tk}, altitude {_al}, fuel {_f}"
else:
    _want = f"OUT OF FUEL at T+{_tk}, altitude {_al}, fuel {_f}"
_got = _kc_lines()
_last = ""
if len(_got) > 0:
    _last = _got[-1]
if _last == _want:
    print("__KC_WIN__")
elif _last == "":
    print("__KC_HINT__ 🤔 什么都没打印。循环结束以后要打印结果那一行。|🤔 Nothing was printed. Print the result line after the loop.")
elif _al >= 100 and _last.startswith("OUT OF FUEL"):
    print(f"__KC_HINT__ 🚀 这次其实到太空了（{_want}）！循环里要停在两种情况：没燃料了，或者 altitude 到 100 了——用 and 把两个条件连起来；循环后用 if 判断是哪一种。|🚀 This flight actually reached space ({_want})! The loop should stop for two reasons: out of fuel, or altitude reached 100 — join the conditions with and; after the loop, use if to tell which happened.")
elif _al < 100 and _last.startswith("SPACE"):
    print(f"__KC_HINT__ ⛽ 这次燃料不够，到不了 100（{_want}）。循环后判断 altitude 有没有到 100。|⛽ Not enough fuel to reach 100 this time ({_want}). After the loop, check whether altitude reached 100.")
else:
    print(f"__KC_HINT__ 🔍 最后一行应该是「{_want}」，你的是「{_last}」。检查每一步的顺序：先减燃料，speed 加 boost，altitude 加 speed，tick 加 1。|🔍 The last line should be \"{_want}\" but yours is \"{_last}\". Check the order inside each step: fuel minus burn, speed plus boost, altitude plus speed, tick plus 1.")
