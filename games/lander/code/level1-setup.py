# 🛬 火箭着陆 第 1 关：关卡代码（隐藏）/ Rocket Lander level 1: hidden setup
import turtle
import random

# 记下孩子打印的每一行，检查的时候用 / remember every line the kid prints, for the check
_kc_print = print
_kc_buf = [""]
def print(*args, sep=" ", end="\n"):
    _kc_buf[0] = _kc_buf[0] + sep.join([str(a) for a in args]) + end
    _kc_print(*args, sep=sep, end=end)

def _kc_lines():
    return [_l.rstrip() for _l in _kc_buf[0].split("\n") if _l.strip() != ""]

_PLOT_DX = 8
_PLOT_TITLE = "📈 height 高度"
height = random.randint(150, 400)
speed = 0
g = random.randint(1, 2)
_h0 = height
_g = g

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

booster.goto(_BX, _kc_y(height))
_hud.write(f"height {height}   speed 0   g {g}", font=("Arial", 13, "bold"))
_kc_print(f"📡 height = {height}, speed = {speed}, g = {g}")
_kc_print("--------")
_boom = [False]

def draw(h):
    # 把助推器画在高度 h 的地方，图表上记一个点 / draw the booster at height h and add a point to the chart
    if h < 0:
        h = 0
    booster.goto(_BX, _kc_y(h))
    _kc_plot(h, 0.55)
    if h == 0 and not _boom[0]:
        _boom[0] = True
        booster.color("red")
        _w.goto(_BX, _DECK)
        _w.dot(40, "orangered")
        _hud.goto(_BX, _DECK + 40)
        _hud.color("orangered")
        _hud.write("💥", align="center", font=("Arial", 20, "bold"))
