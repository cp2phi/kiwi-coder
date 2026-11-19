# 🐞 虫虫医院 病号 8：检查（用秘密数字测试函数）/ Bug Hospital patient 8: check (tests the function with secret numbers)
import random as _random

try:
    _has_fn = callable(weeks_to_save)
except NameError:
    _has_fn = False

if not _has_fn:
    print("__KC_HINT__ 🩺 函数 weeks_to_save 不见了！别删掉它，也别改名字。|🩺 The function weeks_to_save has gone missing! Don't delete or rename it.")
else:
    _cases = [(10, 5), (10, 3), (7, 7)]
    for _k in range(4):
        _cases.append((_random.randint(20, 300), _random.randint(3, 40)))
    _bad = []
    for _c in _cases:
        _want = (_c[0] + _c[1] - 1) // _c[1]
        try:
            _got = weeks_to_save(_c[0], _c[1])
        except Exception as _x:
            _got = "error: " + str(_x)
        if _got != _want:
            _bad.append((_c[0], _c[1], _want, _got))
    if len(_bad) == 0:
        print("__KC_WIN__")
    else:
        # 找出最能说明问题的那个例子 / pick the example that best shows the problem
        _b = _bad[0]
        _why = 0
        for _x in _bad:
            if _why == 0 and _x[3] is None:
                _b = _x
                _why = 1
        for _x in _bad:
            if _why == 0 and type(_x[3]) == int and _x[3] >= 900:
                _b = _x
                _why = 2
        for _x in _bad:
            if _why == 0 and type(_x[3]) == int and _x[3] == _x[2] * _x[1]:
                _b = _x
                _why = 3
        for _x in _bad:
            if _why == 0 and _x[3] == 1:
                _b = _x
                _why = 4
        _zh = "🔬 检查员试了 weeks_to_save(" + str(_b[0]) + ", " + str(_b[1]) + ")：应该是 " + str(_b[2]) + " 周，函数给了 " + str(_b[3]) + "。"
        _en = "🔬 The inspector tried weeks_to_save(" + str(_b[0]) + ", " + str(_b[1]) + "): it should be " + str(_b[2]) + " weeks, the function gave " + str(_b[3]) + "."
        if _why == 1:
            _zh = _zh + "函数什么都没交出来——少了 return？"
            _en = _en + " The function handed back nothing — missing a return?"
        elif _why == 2:
            _zh = _zh + "这么大？循环自己停不下来，是安全绳把它拉住的。用手算一下：saved 是 3、6、9、12……会正好等于 10 吗？"
            _en = _en + " That big? The loop never stopped by itself — the safety rope caught it. Work it out by hand: saved goes 3, 6, 9, 12… does it ever equal exactly 10?"
        elif _why == 3:
            _zh = _zh + "这个数是「存了多少钱」，不是「过了几周」。看看 return 后面写的是什么。"
            _en = _en + " That number is how much money was saved, not how many weeks passed. Look at what comes after return."
        elif _why == 4:
            _zh = _zh + "周数总是 1？weeks = weeks + 1 这一行在循环里面吗？看看缩进。"
            _en = _en + " Always 1 week? Is the line weeks = weeks + 1 inside the loop? Check the indentation."
        print("__KC_HINT__ " + _zh + "|" + _en)
