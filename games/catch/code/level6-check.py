_ok = True
try:
    bonus
except NameError:
    _ok = False
    print("__KC_HINT__ 还没有叫 bonus 的函数（def bonus():）|There is no function called bonus yet (def bonus():)")
try:
    if len(FRUITS) < 3:
        _ok = False
        print("__KC_HINT__ FRUITS 列表里要至少 3 种颜色|The FRUITS list needs at least 3 colours")
except NameError:
    _ok = False
    print("__KC_HINT__ 还没有叫 FRUITS 的列表|There is no list called FRUITS yet")
if _ok:
    print("__KC_WIN__")
