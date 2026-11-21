# 🚀 发射控制 第 6 关：过关检查 / Launch Control level 6: win check
try:
    _has = callable(blockers) and callable(director)
except NameError:
    _has = False
if not _has:
    print("__KC_HINT__ 🧩 要有两个函数：def blockers(status): 和 def director(status):（名字要一模一样）。|🧩 You need two functions: def blockers(status): and def director(status): (exact names).")
else:
    _bad = ""
    _passed = 0
    for _d in _kc_tests:
        _wb = _kc_blockers(_d)
        _wd = _kc_director(_d)
        _r = _kc_call(blockers, _d)
        _s = _kc_call(director, _d)
        _m = ""
        if not _r[0]:
            _m = f"blockers({_d}) 出错了：{_r[1]}|blockers({_d}) crashed: {_r[1]}"
        elif _r[1] != _wb:
            _m = f"blockers({_d}) 应该交回 {_wb}，你的是 {repr(_r[1])}|blockers({_d}) should return {_wb}, yours gave {repr(_r[1])}"
        elif not _s[0]:
            _m = f"director({_d}) 出错了：{_s[1]}|director({_d}) crashed: {_s[1]}"
        elif _s[1] != _wd:
            _m = f"director({_d}) 应该交回 {repr(_wd)}，你的是 {repr(_s[1])}|director({_d}) should return {repr(_wd)}, yours gave {repr(_s[1])}"
        else:
            _passed = _passed + 1
        if _m != "" and _bad == "":
            _bad = _m
    _kc_print(f"🧪 隐藏测试 hidden tests: {_passed} / {len(_kc_tests)} ✅")
    if _bad == "":
        print("__KC_WIN__")
    else:
        _q = _bad.split("|")
        print(f"__KC_HINT__ 🧪 测试没通过：{_q[0]}|🧪 A test failed: {_q[1]}")
