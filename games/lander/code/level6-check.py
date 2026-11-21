# 🛬 火箭着陆 第 6 关：过关检查 / Rocket Lander level 6: win check
try:
    _has = callable(landings) and callable(veteran)
except NameError:
    _has = False
if not _has:
    print("__KC_HINT__ 🧩 要有两个函数：def landings(flights): 和 def veteran(counts):（名字要一模一样）。|🧩 You need two functions: def landings(flights): and def veteran(counts): (exact names).")
else:
    _tests = [[{"booster": "B-Kea", "landed": True}], [{"booster": "B-Tui", "landed": True}, {"booster": "B-Moa", "landed": False}, {"booster": "B-Tui", "landed": True}]]
    for _n in range(6):
        _tests.append(_kc_flights(random.randint(5, 20)))
    _bad = ""
    _passed = 0
    for _fl in _tests:
        _wc = _kc_land(_fl)
        _wv = _kc_vet(_wc)
        try:
            _c = landings(_kc_copy(_fl))
        except Exception as _e:
            _bad = f"landings(…) 出错了：{_e}|landings(…) crashed: {_e}"
            break
        if _c != _wc:
            _short = _fl
            if len(_fl) > 4:
                _short = str(_fl[0:3])[:-1] + ", …]"
            _bad = f"landings({_short}) 应该交回 {_wc}，你的是 {_c}。（只数 landed 是 True 的）|landings({_short}) should return {_wc}, yours gave {_c}. (Only count flights where landed is True.)"
            break
        try:
            _v = veteran(dict(_wc))
        except Exception as _e:
            _bad = f"veteran({_wc}) 出错了：{_e}|veteran({_wc}) crashed: {_e}"
            break
        if _v != _wv:
            _bad = f"veteran({_wc}) 应该是 {repr(_wv)}，你的是 {repr(_v)}|veteran({_wc}) should be {repr(_wv)}, yours gave {repr(_v)}"
            break
        _passed = _passed + 1
    _kc_print(f"🧪 隐藏测试 hidden tests: {_passed} / {len(_tests)} ✅")
    if _bad == "":
        print("__KC_WIN__")
    else:
        _q = _bad.split("|")
        print(f"__KC_HINT__ 🧪 测试没通过：{_q[0]}|🧪 A test failed: {_q[1]}")
