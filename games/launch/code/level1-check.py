# 🚀 发射控制 第 1 关：过关检查 / Launch Control level 1: win check
_want = []
for _t in range(_start, 0, -1):
    if _t == _engines:
        _want.append(f"T-{_t} ENGINES ON")
    elif _t == _poll:
        _want.append(f"T-{_t} POLL")
    else:
        _want.append(f"T-{_t}")
_want.append("LIFTOFF!")
_got = _kc_lines()
if _got == _want:
    print("__KC_WIN__")
elif len(_got) > 0 and _got[0] == "T-10" and _start != 10:
    print(f"__KC_HINT__ 📡 今天要从 T-{_start} 开始，不是 T-10。别把数字写死，用变量 start！|📡 Today the count starts at T-{_start}, not T-10. Don't type the number — use the variable start!")
elif len(_got) > 1 and _got[0] == "T-1" and _got[1] == "T-2":
    print("__KC_HINT__ 🔁 你在往上数！倒计时要往下数：range(start, 0, -1)。|🔁 You're counting up! A countdown goes down: range(start, 0, -1).")
else:
    _i = 0
    while _i < len(_got) and _i < len(_want) and _got[_i] == _want[_i]:
        _i = _i + 1
    if _i >= len(_want):
        print(f"__KC_HINT__ 🤏 前 {len(_want)} 行都对了，可是后面多打印了「{_got[_i]}」。|🤏 The first {len(_want)} lines are right, but then you printed an extra line: \"{_got[_i]}\".")
    elif _i >= len(_got):
        print(f"__KC_HINT__ 🤏 前 {_i} 行都对，接下来少了一行「{_want[_i]}」。|🤏 The first {_i} lines are right, then this line is missing: \"{_want[_i]}\".")
    else:
        print(f"__KC_HINT__ 🔍 第 {_i + 1} 行应该是「{_want[_i]}」，你打印的是「{_got[_i]}」。|🔍 Line {_i + 1} should be \"{_want[_i]}\" but you printed \"{_got[_i]}\".")
