# 🛬 火箭着陆 第 5 关：过关检查 / Rocket Lander level 5: win check
try:
    _has = callable(brake_distance) and callable(autopilot)
except NameError:
    _has = False
if not _has:
    print("__KC_HINT__ 🧩 要有两个函数：def brake_distance(v): 和 def autopilot(h, v, fuel):（名字要一模一样）。|🧩 You need two functions: def brake_distance(v): and def autopilot(h, v, fuel): (exact names).")
else:
    _bad = ""
    for _x in [0, 1, 2, 3, 4, 5, 6, 7, 10, 13, 20, random.randint(21, 40)]:
        try:
            _y = brake_distance(_x)
        except Exception as _e:
            _bad = f"brake_distance({_x}) 出错了：{_e}|brake_distance({_x}) crashed: {_e}"
            break
        if _y != _kc_bd(_x):
            _bad = f"brake_distance({_x}) 应该是 {_kc_bd(_x)}，你的是 {_y}|brake_distance({_x}) should be {_kc_bd(_x)}, yours gave {_y}"
            break
    _ok = 0
    _fail = ""
    for _n in range(12):
        _s = _kc_scenario()
        _t = _kc_sim(_s[0], _s[1], _s[2], autopilot)
        if _t <= _SAFE:
            _ok = _ok + 1
        elif _fail == "":
            if _t == 999:
                _fail = f"从 h={_s[0]}, v={_s[1]}, fuel={_s[2]} 出发：一直没落地（或者出错了）|starting at h={_s[0]}, v={_s[1]}, fuel={_s[2]}: never landed (or crashed with an error)"
            else:
                _fail = f"从 h={_s[0]}, v={_s[1]}, fuel={_s[2]} 出发：落地速度 {_t}|starting at h={_s[0]}, v={_s[1]}, fuel={_s[2]}: touchdown speed {_t}"
    print(f"🧪 隐藏试飞 hidden test flights: {_ok} / 12 ✅")
    if _bad != "":
        _q = _bad.split("|")
        print(f"__KC_HINT__ 🧮 {_q[0]}|🧮 {_q[1]}")
    elif _fail != "":
        _q = _fail.split("|")
        print(f"__KC_HINT__ 💥 有一次隐藏试飞没成功，{_q[0]}。在纸上算一算这种情况，再改 autopilot。|💥 A hidden test flight failed, {_q[1]}. Work through that case on paper, then fix autopilot.")
    elif not _done:
        print("__KC_HINT__ 👀 隐藏试飞全过了！最后加一行 fly(autopilot)，让大家看着它落地。|👀 All hidden test flights passed! Add fly(autopilot) at the end so everyone can watch it land.")
    elif _touch > _SAFE:
        print(f"__KC_HINT__ 💥 这次看得见的飞行落地速度是 {_touch}。|💥 The flight you watched touched down at speed {_touch}.")
    else:
        print("__KC_WIN__")
