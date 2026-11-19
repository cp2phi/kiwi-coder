# 🛬 火箭着陆 第 4 关：过关检查 / Rocket Lander level 4: win check
_safe = 0
_worst = 0
_best = 0
_run = 0
for _x in _res:
    if _x > _worst:
        _worst = _x
    if _x <= _SAFE:
        _safe = _safe + 1
        _run = _run + 1
        if _run > _best:
            _best = _run
    else:
        _run = 0
_want = [f"Safe: {_safe}/{len(_res)}", f"Worst: {_worst}", f"Best streak: {_best}"]
_got = _kc_lines()
_last = _got[-3:]
while len(_last) < 3:
    _last = [""] + _last
if _last == _want:
    print("__KC_WIN__")
elif _last[0] != _want[0]:
    print(f"__KC_HINT__ 🔍 倒数第 3 行应该是「{_want[0]}」，你的是「{_last[0]}」。速度 <= SAFE（4）才算安全。|🔍 The third-last line should be \"{_want[0]}\", yours is \"{_last[0]}\". Speed <= SAFE (4) counts as safe.")
elif _last[1] != _want[1]:
    print(f"__KC_HINT__ 🔍 倒数第 2 行应该是「{_want[1]}」，你的是「{_last[1]}」。用一个变量记住「到现在为止最大的」，遇到更大的就换掉它。|🔍 The second-last line should be \"{_want[1]}\", yours is \"{_last[1]}\". Keep a variable for \"the biggest so far\" and replace it when you meet a bigger one.")
else:
    print(f"__KC_HINT__ 🔍 最后一行应该是「{_want[2]}」，你的是「{_last[2]}」。数「现在连着几次安全」：安全就 +1，坠毁就变回 0；再记住它最大到过几。|🔍 The last line should be \"{_want[2]}\", yours is \"{_last[2]}\". Count \"safe in a row right now\": +1 when safe, back to 0 on a crash; and remember the biggest it ever got.")
