# 🛰️ 火星车 第 2 关：关卡代码（隐藏，每次运行地图都不一样）/ Mars Rover level 2: hidden setup (new map every run)
import turtle
import random

_maze = False
_polys = []
N = 8
_SPEED = 6
_battery0 = 80
_start = (0, 0)
_dir0 = 0
_base = (0, 0)

# 场地大小是随机的，外面是悬崖 / the field has a random size; outside it are cliffs
_W = random.randint(4, 8)
_H = random.randint(4, 8)
_rocks = []
for _x in range(N):
    for _y in range(N):
        if _x >= _W or _y >= _H:
            _rocks.append((_x, _y))
_blocks = list(_rocks)
if _W < N or _H < N:
    _polys = [[(_W, 0), (N, 0), (N, N), (0, N), (0, _H), (_W, _H)]]

# 样本只放在场地的边上（起点除外）/ samples only on the edge of the field (not on the start)
_ring = []
for _x in range(_W):
    for _y in range(_H):
        if (_x == 0 or _y == 0 or _x == _W - 1 or _y == _H - 1) and (_x, _y) != (0, 0):
            _ring.append((_x, _y))
random.shuffle(_ring)
_samples = _ring[0:random.randint(3, 6)]

# ---------- 画地图 / draw the map ----------
# 每一笔海龟动作都要花时间，所以地图用尽量少的笔画画出来
# every turtle move takes a frame, so the map is drawn with as few strokes as possible
CELL = 480 // N
_O = -(CELL * N) // 2
_SAND = "#e8b384"
_WALL = "#6b3f22"

def _cx(c):
    return _O + CELL // 2 + c * CELL

def _cy(r):
    return _O + CELL // 2 + r * CELL

_w = turtle.Turtle()
_w.hideturtle()
_w.speed(0)
_w.penup()

if _maze:
    # 洞穴：背景是岩壁，空地画成一条条粗线（像熔岩管）/ cave: the background is rock, open cells are thick strokes (like lava tubes)
    turtle.Screen().bgcolor(_WALL)
    _w.color(_SAND)
    _w.pensize(CELL - 6)
    for _k in range(2):
        for _a in range(N):
            _b = 0
            while _b < N:
                if _k == 0:
                    _cell = (_b, _a)
                else:
                    _cell = (_a, _b)
                if _cell in _rocks:
                    _b = _b + 1
                    continue
                _e = _b
                while _e + 1 < N and (((_e + 1, _a) not in _rocks) if _k == 0 else ((_a, _e + 1) not in _rocks)):
                    _e = _e + 1
                if _e > _b:
                    if _k == 0:
                        _w.goto(_cx(_b), _cy(_a))
                        _w.pendown()
                        _w.goto(_cx(_e), _cy(_a))
                    else:
                        _w.goto(_cx(_a), _cy(_b))
                        _w.pendown()
                        _w.goto(_cx(_a), _cy(_e))
                    _w.penup()
                _b = _e + 1
else:
    turtle.Screen().bgcolor(_SAND)
    # 格子线：来回画「之」字，笔画最少 / grid lines drawn as a zig-zag: fewest strokes
    _w.pensize(1)
    _w.color("#cf9563")
    _w.goto(_O, _O)
    _w.pendown()
    for _i in range(N + 1):
        if _i % 2 == 0:
            _w.goto(_O + N * CELL, _O + _i * CELL)
        else:
            _w.goto(_O, _O + _i * CELL)
        if _i < N:
            _w.goto(_w.xcor(), _O + (_i + 1) * CELL)
    _w.penup()
    _w.goto(_O, _O)
    _w.pendown()
    for _i in range(N + 1):
        if _i % 2 == 0:
            _w.goto(_O + _i * CELL, _O + N * CELL)
        else:
            _w.goto(_O + _i * CELL, _O)
        if _i < N:
            _w.goto(_O + (_i + 1) * CELL, _w.ycor())
    _w.penup()
    # 悬崖：一块一块填色的多边形（单位是格子）/ cliffs: filled polygons (corners in cell units)
    _w.color(_WALL)
    for _pg in _polys:
        _w.goto(_O + _pg[0][0] * CELL, _O + _pg[0][1] * CELL)
        _w.begin_fill()
        for _pt in _pg[1:]:
            _w.goto(_O + _pt[0] * CELL, _O + _pt[1] * CELL)
        _w.end_fill()
    for _rk in _rocks:
        if _rk not in _blocks:
            _w.goto(_cx(_rk[0]), _cy(_rk[1]))
            _w.dot(CELL * 3 // 4, "#8a5232")

for _s in _samples:
    _w.goto(_cx(_s[0]), _cy(_s[1]))
    _w.dot(CELL // 2, "mediumorchid")
    _w.dot(CELL // 5, "white")

if _base != None:
    _w.goto(_cx(_base[0]), _cy(_base[1]))
    _w.dot(CELL * 4 // 5, "white")
    _w.dot(CELL * 3 // 5, "royalblue")
    _w.goto(_cx(_base[0]), _cy(_base[1]) - CELL // 5)
    _w.color("white")
    _w.write("H", align="center", font=("Arial", CELL // 3, "bold"))

_hud = turtle.Turtle()
_hud.hideturtle()
_hud.speed(0)
_hud.penup()
if _maze:
    _hud.color("white")
else:
    _hud.color("#3b2416")
_hud.goto(_O, _O + N * CELL + 8)

# ---------- 火星车的状态 / rover state ----------
_collected = 0
_wasted = 0
_crashed = False
_flat = False
_bat = _battery0
_calls = 0
_LIMIT = 4000
_pos = [_start[0], _start[1]]
_dir = _dir0
_DX = [1, 0, -1, 0]
_DY = [0, 1, 0, -1]
_path = [(_start[0], _start[1])]

def _kc_show():
    _hud.clear()
    _hud.write(f"🔋 {_bat}    🧪 {_collected}", font=("Arial", 14, "bold"))

_kc_show()

t = turtle.Turtle()
t.shape("turtle")
t.color("white", "slategray")
t.pensize(3)
t.speed(0)
t.penup()
t.goto(_cx(_start[0]), _cy(_start[1]))
t.setheading(90 * _dir0)
t.pencolor("#fff3e0")
t.pendown()
t.speed(_SPEED)

def _kc_tick():
    # 安全带：命令太多（多半是 while 停不下来）就让程序停下
    # seatbelt: too many commands (usually a while loop that never stops) ends the program
    global _calls
    _calls = _calls + 1
    if _calls == _LIMIT:
        print("🛑 火星车发了 4000 个指令还没完——多半是 while 循环停不下来了。检查循环的条件！")
        print("🛑 The rover has run 4000 commands — your while loop probably never stops. Check its condition!")
    if _calls >= _LIMIT:
        raise RuntimeError("🛑 too many rover commands: is your while loop endless? / 指令太多：while 停不下来了？")

def _kc_blocked(c, r):
    return c < 0 or c >= N or r < 0 or r >= N or (c, r) in _rocks

def _kc_side(turn):
    d = (_dir + turn) % 4
    return _kc_blocked(_pos[0] + _DX[d], _pos[1] + _DY[d])

def move():
    global _crashed, _bat, _flat
    _kc_tick()
    if _crashed or _flat:
        return
    nc = _pos[0] + _DX[_dir]
    nr = _pos[1] + _DY[_dir]
    if _kc_blocked(nc, nr):
        _crashed = True
        t.dot(CELL // 3, "red")
        print("💥 撞到岩石或者开出地图了！看红点。/ Crashed into a rock or off the map! See the red dot.")
        return
    _pos[0] = nc
    _pos[1] = nr
    _path.append((nc, nr))
    _bat = _bat - 1
    t.goto(_cx(nc), _cy(nr))
    _kc_show()
    if _bat <= 0:
        _flat = True
        print("🪫 电池用完了，火星车停下了。/ Battery empty — the rover has stopped.")

def turn_left():
    global _dir
    _kc_tick()
    if _crashed or _flat:
        return
    _dir = (_dir + 1) % 4
    t.left(90)

def turn_right():
    global _dir
    _kc_tick()
    if _crashed or _flat:
        return
    _dir = (_dir + 3) % 4
    t.right(90)

# 撞车或没电 = 任务结束：传感器都说「挡住了」，at_base() 说 True，让 while 循环停下来，检查代码好告诉你发生了什么
# crash or flat battery = mission over: sensors all say "blocked" and at_base() says True,
# so while loops end and the check can explain what happened
def rock_ahead():
    _kc_tick()
    if _crashed or _flat:
        return True
    return _kc_side(0)

def rock_left():
    _kc_tick()
    if _crashed or _flat:
        return True
    return _kc_side(1)

def rock_right():
    _kc_tick()
    if _crashed or _flat:
        return True
    return _kc_side(3)

def sample_here():
    _kc_tick()
    if _crashed or _flat:
        return False
    return (_pos[0], _pos[1]) in _samples

def collect():
    global _collected, _wasted
    _kc_tick()
    if _crashed or _flat:
        return
    here = (_pos[0], _pos[1])
    if here in _samples:
        _samples.remove(here)
        _collected = _collected + 1
        t.dot(CELL // 2, "limegreen")
        _kc_show()
    else:
        _wasted = _wasted + 1
        t.dot(CELL // 5, "orangered")

def at_base():
    _kc_tick()
    if _crashed or _flat:
        return True
    return _base != None and _pos[0] == _base[0] and _pos[1] == _base[1]

def battery():
    _kc_tick()
    return _bat
