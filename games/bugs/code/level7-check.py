# 🐞 虫虫医院 病号 7：检查（用规则自己算一遍，再和你的比）/ Bug Hospital patient 7: check (works it out from the rules and compares)
def _grade(s):
    if s >= 90:
        return "A"
    if s >= 70:
        return "B"
    if s >= 50:
        return "C"
    return "F"


_want = []
_want_pass = 0
for _s in _scores:
    _want.append(_grade(_s))
    if _s >= 50:
        _want_pass = _want_pass + 1
try:
    _g = grades
    _p = passed
except NameError:
    _g = None
    _p = None
if _g is None:
    print("__KC_HINT__ 🩺 病人的 grades 或 passed 不见了！别删掉这两个变量。|🩺 The patient's grades or passed has gone missing! Don't delete those two variables.")
elif _g != _want:
    _i = 0
    while _i < len(_want) and _i < len(_g) and _g[_i] == _want[_i]:
        _i = _i + 1
    if _i < len(_want) and _i < len(_g):
        print("__KC_HINT__ 🔍 分数 " + str(_scores[_i]) + " 应该是 " + _want[_i] + "，可是程序给了 " + str(_g[_i]) + "。电脑从上往下检查 if / elif，碰到第一个 True 就停下——顺序对吗？边界上的分数（比如正好 90）呢？|🔍 A score of " + str(_scores[_i]) + " should be " + _want[_i] + ", but the program gave " + str(_g[_i]) + ". The computer checks if / elif from the top and stops at the first True — is the order right? What about scores right on the edge (like exactly 90)?")
    else:
        print("__KC_HINT__ 🔍 grades 里应该有 " + str(len(_want)) + " 个等级，你的有 " + str(len(_g)) + " 个。|🔍 grades should hold " + str(len(_want)) + " grades; yours has " + str(len(_g)) + ".")
elif _p != _want_pass:
    print("__KC_HINT__ 🔍 等级都对了！但是 passed 应该是 " + str(_want_pass) + "，程序算出来是 " + str(_p) + "。passed = 0 这一行，每次循环都会跑一遍吗？|🔍 The grades are all right! But passed should be " + str(_want_pass) + " and the program got " + str(_p) + ". Does the line passed = 0 run again on every loop?")
else:
    print("__KC_WIN__")
