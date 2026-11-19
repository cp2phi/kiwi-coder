# 🚀 发射控制 第 2 关：过关检查 / Launch Control level 2: win check
_want = []
_first = 0
for _i in range(len(_wind)):
    _v = _kc_verdict(_storm[_i], _wind[_i], _temp[_i])
    _want.append(f"Window {_i + 1}: {_v}")
    if _v == "GO" and _first == 0:
        _first = _i + 1
if _first > 0:
    _want.append(f"LAUNCH in window {_first}")
else:
    _want.append("SCRUB")
_got = _kc_lines()
if _got == _want:
    print("__KC_WIN__")
else:
    _i = 0
    while _i < len(_got) and _i < len(_want) and _got[_i] == _want[_i]:
        _i = _i + 1
    if _i >= len(_want):
        print(f"__KC_HINT__ 🤏 前 {len(_want)} 行都对了，可是后面多打印了「{_got[_i]}」。只在循环外面打印最后那一行哦。|🤏 The first {len(_want)} lines are right, but then there's an extra line: \"{_got[_i]}\". Print the last line once, after the loop.")
    elif _i >= len(_got):
        print(f"__KC_HINT__ 🤏 前 {_i} 行都对，接下来少了一行「{_want[_i]}」。|🤏 The first {_i} lines are right, then this line is missing: \"{_want[_i]}\".")
    elif _i < len(_wind) and _storm[_i] and (_wind[_i] > 40 or _temp[_i] < 0) and _got[_i] != _want[_i]:
        print(f"__KC_HINT__ ⛈️ 窗口 {_i + 1} 又有雷暴又有别的问题。规则是先看雷暴——elif 的顺序很重要！|⛈️ Window {_i + 1} has a storm AND another problem. The rule checks the storm first — the order of your elifs matters!")
    elif _i < len(_wind) and _wind[_i] > 40 and _temp[_i] < 0 and _got[_i] != _want[_i]:
        print(f"__KC_HINT__ 💨 窗口 {_i + 1} 风大又冷。规则是先看风，再看冷——检查一下 elif 的顺序。|💨 Window {_i + 1} is windy AND cold. Wind is checked before cold — check the order of your elifs.")
    elif _i == len(_wind) and _first == 0:
        print("__KC_HINT__ 🌧️ 今天一个 GO 的窗口都没有，最后一行应该打印 SCRUB（取消发射）。多运行几次，两种情况都要测到！|🌧️ No GO window at all today, so the last line should be SCRUB. Run it a few times — test both cases!")
    elif _i == len(_wind):
        print(f"__KC_HINT__ 🔍 最后一行应该是「{_want[-1]}」——要找的是「第一个」GO 的窗口。|🔍 The last line should be \"{_want[-1]}\" — you want the FIRST GO window.")
    else:
        print(f"__KC_HINT__ 🔍 第 {_i + 1} 行应该是「{_want[_i]}」，你打印的是「{_got[_i]}」。|🔍 Line {_i + 1} should be \"{_want[_i]}\" but you printed \"{_got[_i]}\".")
