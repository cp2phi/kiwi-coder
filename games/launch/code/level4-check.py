# 🚀 发射控制 第 4 关：过关检查 / Launch Control level 4: win check
try:
    _has = callable(ready) and callable(count_no_go)
except NameError:
    _has = False
if not _has:
    print("__KC_HINT__ 🧩 要有两个函数：def ready(checks): 和 def count_no_go(checks):（名字要一模一样）。|🧩 You need two functions: def ready(checks): and def count_no_go(checks): (exact names).")
else:
    _bad_r = ""
    _bad_n = ""
    _passed = 0
    for _c in _kc_cases:
        _want_r = "NO GO" not in _c
        _want_n = 0
        for _x in _c:
            if _x == "NO GO":
                _want_n = _want_n + 1
        _ok = True
        # ① 测 ready / test ready
        _r = _kc_call(ready, _c)
        _m = ""
        if not _r[0]:
            _m = f"ready({_c}) 出错了：{_r[1]}|ready({_c}) crashed: {_r[1]}"
        elif _r[1] is not _want_r:
            if _r[1] == _want_r or str(_r[1]) == str(_want_r):
                _m = f"ready({_c}) 要 return {_want_r}（True / False，不加引号），不是 {repr(_r[1])}|ready({_c}) should return {_want_r} (True / False, no quotes), not {repr(_r[1])}"
            else:
                _m = f"ready({_c}) 应该是 {_want_r}，你的是 {_r[1]}|ready({_c}) should be {_want_r}, yours gave {_r[1]}"
        if _m != "":
            _ok = False
            if _bad_r == "":
                _bad_r = _m
        # ② 测 count_no_go / test count_no_go
        _n = _kc_call(count_no_go, _c)
        _m = ""
        if not _n[0]:
            _m = f"count_no_go({_c}) 出错了：{_n[1]}|count_no_go({_c}) crashed: {_n[1]}"
        elif _n[1] != _want_n:
            _m = f"count_no_go({_c}) 应该是 {_want_n}，你的是 {_n[1]}|count_no_go({_c}) should be {_want_n}, yours gave {_n[1]}"
        if _m != "":
            _ok = False
            if _bad_n == "":
                _bad_n = _m
        if _ok:
            _passed = _passed + 1
    _kc_print(f"🧪 隐藏测试 hidden tests: {_passed} / {len(_kc_cases)} ✅")
    _bad = _bad_r
    if _bad == "":
        _bad = _bad_n
    if _bad == "":
        print("__KC_WIN__")
    else:
        _p = _bad.split("|")
        print(f"__KC_HINT__ 🧪 测试没通过：{_p[0]}|🧪 A test failed: {_p[1]}")
