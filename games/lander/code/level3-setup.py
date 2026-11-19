# 🛬 火箭着陆 第 3 关：关卡代码（隐藏，每次都不一样）/ Rocket Lander level 3: hidden setup (different every run)
import turtle
import random

_PLOT_DX = 2
_PLOT_TITLE = "📈 speed 速度"
_FLIGHTS = 3

def _kc_scenario():
    # 更高、已经在往下掉、燃料很少 / higher, already falling, very little fuel
    return [random.randint(250, 450), random.randint(0, 8), random.randint(16, 20)]

# ---------- 物理规则（游戏里的简化版）/ the physics (simplified for the game) ----------
# 每一拍 / every tick:  speed 加 G（重力）→ 点火的话 speed 减 THRUST、燃料减 1 → height 减 speed
#                        speed + G (gravity) → if the engine is on: speed - THRUST, fuel - 1 → height - speed
# speed 是往下的速度：正数 = 往下掉，负数 = 往上飞 / speed is downward: positive = falling, negative = going up
G = 1
THRUST = 3
SAFE = 4
_G = G
_TH = THRUST
_SAFE = SAFE

# ---------- 画场景（笔画越少越快）/ draw the scene (fewer strokes = faster) ----------
_HMAX = 500
_DECK = -220
_BX = -170
_PX = 10
_PY = -150
_S = 470 / _HMAX

turtle.Screen().bgcolor("midnightblue")
_w = turtle.Turtle()
_w.hideturtle()
_w.speed(0)
_w.penup()
for _st in [(-260, 230), (-60, 250), (150, 210), (240, 120), (-230, 60), (120, 245), (-110, 160)]:
    _w.goto(_st[0], _st[1])
    _w.dot(3, "white")
# 大海 + 无人船 / the sea + the drone ship
_w.color("steelblue")
_w.goto(-300, -300)
_w.begin_fill()
_w.goto(300, -300)
_w.goto(300, _DECK - 8)
_w.goto(-300, _DECK - 8)
_w.end_fill()
_w.color("lightgray")
_w.pensize(12)
_w.goto(_BX - 40, _DECK - 6)
_w.pendown()
_w.goto(_BX + 40, _DECK - 6)
_w.penup()
# 右边的小图表 / the little chart on the right
_w.pensize(1)
_w.color("gray")
_w.goto(_PX, _PY + 300)
_w.pendown()
_w.goto(_PX, _PY)
_w.goto(_PX + 270, _PY)
_w.penup()
_w.color("white")
_w.goto(_PX + 4, _PY + 285)
_w.write(_PLOT_TITLE, font=("Arial", 11, "normal"))

_plot = turtle.Turtle()
_plot.hideturtle()
_plot.speed(0)
_plot.penup()
_plot.pensize(2)
_plot.color("deepskyblue")
_plot_n = 0

def _kc_plot(value, scale):
    global _plot_n
    x = _PX + _plot_n * _PLOT_DX
    if x > _PX + 270:
        return
    y = _PY + value * scale
    if y > _PY + 280:
        y = _PY + 280
    if y < _PY - 60:
        y = _PY - 60
    _plot.goto(x, y)
    _plot.pendown()
    _plot_n = _plot_n + 1

_hud = turtle.Turtle()
_hud.hideturtle()
_hud.speed(0)
_hud.penup()
_hud.color("white")
_hud.goto(-280, 262)

booster = turtle.Turtle()
booster.shape("triangle")
booster.color("white")
booster.setheading(90)
booster.penup()
booster.speed(0)

def _kc_y(h):
    y = _DECK + 10 + h * _S
    if y > 280:
        y = 280
    return y

# ---------- 助推器的指令 / booster commands ----------
_flight = 1
_ok_count = 0
_sc = _kc_scenario()
_h = _sc[0]
_v = _sc[1]
_f = _sc[2]
_fs = _f
_tick = 0
_done = False
_touch = None
_calls = 0
_LIMIT = 6000
booster.goto(_BX, _kc_y(_h))

_msg = turtle.Turtle()
_msg.hideturtle()
_msg.speed(0)
_msg.penup()
_msg.goto(_BX, _DECK + 40)

def _kc_hud():
    _hud.clear()
    _hud.write(f"🚀 {_flight}/{_FLIGHTS}   height {_h}   speed {_v}   fuel {_f}", font=("Arial", 13, "bold"))

_kc_hud()

def _kc_tick():
    # 安全带：命令太多（多半是循环里有一条路没有 step）就让程序停下
    # seatbelt: too many commands (usually a path through the loop with no step) ends the program
    global _calls
    _calls = _calls + 1
    if _calls == _LIMIT:
        print("🛑 发了好几千个指令还没落地——是不是循环里有一条路没有调用 step()？")
        print("🛑 Thousands of commands and still not down — is there a path through your loop that never calls step()?")
    if _calls >= _LIMIT:
        raise RuntimeError("🛑 too many booster commands: does every loop call step()? / 指令太多：每一圈都有 step() 吗？")

def _kc_touchdown(v):
    global _done, _ok_count, _flight, _h, _v, _f, _fs, _plot_n
    _msg.clear()
    if v > _SAFE:
        _done = True
        booster.color("red")
        _w.goto(_BX, _DECK)
        _w.dot(40, "orangered")
        _msg.color("orangered")
        _msg.write(f"💥 CRASH  speed {v}", align="center", font=("Arial", 14, "bold"))
        return
    _ok_count = _ok_count + 1
    _msg.color("lime")
    _msg.write(f"✅ #{_flight} LANDED  speed {v}", align="center", font=("Arial", 14, "bold"))
    if _flight >= _FLIGHTS:
        _done = True
        return
    # 下一枚助推器来了！/ here comes the next booster!
    _flight = _flight + 1
    sc = _kc_scenario()
    _h = sc[0]
    _v = sc[1]
    _f = sc[2]
    _fs = _f
    booster.goto(_BX, _kc_y(_h))
    _plot.clear()
    _plot.penup()
    _plot_n = 0

def step(burn):
    # 走一拍：burn 是 True 就点火，False 就不点 / one tick: burn True = engine on, False = engine off
    global _h, _v, _f, _tick, _touch
    _kc_tick()
    if _done:
        return
    on = False
    if burn and _f > 0:
        on = True
    _v = _v + _G
    if on:
        _v = _v - _TH
        _f = _f - 1
    _h = _h - _v
    _tick = _tick + 1
    # 图表上：橙色 = 点火，蓝色 = 没点火 / on the chart: orange = engine on, blue = engine off
    if on:
        _plot.color("orange")
    else:
        _plot.color("deepskyblue")
    if _h <= 0:
        _h = 0
        _touch = _v
        booster.goto(_BX, _kc_y(0))
        _kc_touchdown(_v)
        _kc_hud()
        return
    booster.goto(_BX, _kc_y(_h))
    _kc_plot(_v, 5)
    if _tick % 6 == 0:
        _kc_hud()

def height():
    _kc_tick()
    return _h

def speed():
    _kc_tick()
    return _v

def fuel():
    _kc_tick()
    return _f

def landed():
    _kc_tick()
    return _done

def _kc_sim(h, v, f, pilot):
    # 不画图，悄悄飞一次，交回落地速度（出错 / 飞太久 → 999）
    # fly once quietly without drawing; return the touchdown speed (error / too long → 999)
    for i in range(600):
        try:
            b = pilot(h, v, f)
        except Exception:
            return 999
        v = v + _G
        if b and f > 0:
            v = v - _TH
            f = f - 1
        h = h - v
        if h <= 0:
            return v
    return 999

# 图表上的 SAFE 线 / the SAFE line on the chart
_w.color("limegreen")
_w.goto(_PX, _PY + _SAFE * 5)
_w.pendown()
_w.goto(_PX + 270, _PY + _SAFE * 5)
_w.penup()
_w.goto(_PX + 230, _PY + _SAFE * 5 + 3)
_w.write("SAFE", font=("Arial", 9, "normal"))
