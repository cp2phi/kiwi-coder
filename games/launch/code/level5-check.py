# 🚀 发射控制 第 5 关：过关检查 / Launch Control level 5: win check
try:
    _has = callable(is_go) and callable(poll)
except NameError:
    _has = False
if not _has:
    print("__KC_HINT__ 🧩 要有两个函数：def is_go(reply): 和 def poll(replies):（名字要一模一样）。|🧩 You need two functions: def is_go(reply): and def poll(replies): (exact names).")
else:
    _bad = ""
    _passed = 0
    _total = len(_kc_words) + len(_kc_polls)
    for _w in _kc_words:
        _want = _kc_is_go(_w)
        _r = _kc_call(is_go, _w)
        if not _r[0]:
            _m = f"is_go({repr(_w)}) 出错了：{_r[1]}|is_go({repr(_w)}) crashed: {_r[1]}"
        elif _r[1] is not _want:
            _m = f"is_go({repr(_w)}) 应该是 {_want}，你的是 {repr(_r[1])}|is_go({repr(_w)}) should be {_want}, yours gave {repr(_r[1])}"
            if _r[1] == True and "no" in _w.lower():
                _m = f"is_go({repr(_w)}) 应该是 False——小心！\"no go\" 里面也藏着 \"go\" 这两个字母，所以不能只问 in。|is_go({repr(_w)}) should be False — careful! \"no go\" also contains the letters \"go\", so 'in' isn't enough."
        else:
            _m = ""
            _passed = _passed + 1
        if _m != "" and _bad == "":
            _bad = _m
    for _p in _kc_polls:
        _n = 0
        for _x in _p:
            if not _kc_is_go(_x):
                _n = _n + 1
        if _n == 0:
            _want = "GO FOR LAUNCH"
        else:
            _want = f"HOLD: {_n} NO GO"
        _r = _kc_call(poll, list(_p))
        if not _r[0]:
            _m = f"poll({_p}) 出错了：{_r[1]}|poll({_p}) crashed: {_r[1]}"
        elif _r[1] != _want:
            _m = f"poll({_p}) 应该交回 {repr(_want)}，你的是 {repr(_r[1])}|poll({_p}) should return {repr(_want)}, yours gave {repr(_r[1])}"
        else:
            _m = ""
            _passed = _passed + 1
        if _m != "" and _bad == "":
            _bad = _m
    _kc_print(f"🧪 隐藏测试 hidden tests: {_passed} / {_total} ✅")
    if _bad == "":
        print("__KC_WIN__")
    else:
        _q = _bad.split("|")
        print(f"__KC_HINT__ 🧪 测试没通过：{_q[0]}|🧪 A test failed: {_q[1]}")
