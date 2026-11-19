# 🛰️ 火星车 第 6 关：过关检查 / Mars Rover level 6: win check
def _kc_walk(cmds, c, r, d, cells):
    # 在没有石头的空地上假装开一遍，记下走过的格子 / pretend-drive on open ground and record the cells
    for ch in cmds:
        if ch == "F":
            c = c + _DX[d]
            r = r + _DY[d]
            cells.append((c, r))
        elif ch == "L":
            d = (d + 1) % 4
        elif ch == "R":
            d = (d + 3) % 4
    return [c, r, d]

try:
    _has = callable(drive) and callable(reverse_route)
except NameError:
    _has = False
if not _has:
    print("__KC_HINT__ 🧩 这一关要两个函数：def drive(route): 和 def reverse_route(route):（名字要一模一样）。|🧩 This level needs two functions: def drive(route): and def reverse_route(route): (exact names).")
else:
    _bad = ""
    _tests = []
    for _n in range(6):
        _tests.append(_kc_route()[0])
    _tests.append("FLFRFF")
    _tests.append("FFRRFLF")
    for _r in _tests:
        try:
            _back = reverse_route(_r)
        except Exception as _e:
            _bad = f"reverse_route(\"{_r}\") 出错了：{_e}|reverse_route(\"{_r}\") crashed: {_e}"
            break
        if type(_back) != type(""):
            _bad = f"reverse_route(\"{_r}\") 要交回一串指令（字符串），你的是 {repr(_back)}|reverse_route(\"{_r}\") should return a string of commands, yours gave {repr(_back)}"
            break
        _out = [(0, 0)]
        _e1 = _kc_walk(_r, 0, 0, 0, _out)
        _ret = []
        _e2 = _kc_walk(_back, _e1[0], _e1[1], _e1[2], _ret)
        _stray = False
        for _p in _ret:
            if _p not in _out:
                _stray = True
        if _e2[0] != 0 or _e2[1] != 0 or _stray:
            _bad = f"测试路线 \"{_r}\"：照着 reverse_route 交回的 \"{_back}\" 开，没有沿原路回到起点。|Test route \"{_r}\": driving your reverse_route answer \"{_back}\" does not retrace the route back to the start."
            break
    if _bad != "":
        _q = _bad.split("|")
        print(f"__KC_HINT__ 🧪 {_q[0]}|🧪 {_q[1]}")
    elif _crashed:
        print("__KC_HINT__ 💥 撞上了（看红点）。回程要原路返回：先掉头，再把路线倒过来走，左和右也要对调。|💥 Crash (see the red dot). Go home the way you came: turn around first, then drive the route backwards with left and right swapped.")
    elif len(_samples) > 0:
        print("__KC_HINT__ 🧪 路线终点的样本还没收。开完 drive(route) 以后要 collect()。|🧪 The sample at the end of the route isn't collected yet. collect() after drive(route).")
    elif (_pos[0], _pos[1]) != _base:
        print("__KC_HINT__ 🏠 样本收到了，可是没回到基地 H。用 drive(reverse_route(route)) 开回去。|🏠 Sample collected, but you're not back at base H. Drive home with drive(reverse_route(route)).")
    else:
        print("__KC_WIN__")
