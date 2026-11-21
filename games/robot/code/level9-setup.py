# 💎 宝石机器人 第 9 关：关卡代码（随机地图 + 随机指令字符串）/ Gem Robot level 9: hidden setup (random map + random orders string)
import turtle
import random

_MAX_CALLS = 400
_start = (0, 0)
rocks = []
gems = []
orders = ""


def _make_world():
    # 随机走一条路线，把它写成指令字符串，再把字符串弄乱（大小写、空格、横线）
    # walk a random route, write it as an orders string, then mess the string up (case, spaces, dashes)
    global rocks, gems, orders
    x = 0
    y = 0
    d = 0
    plan = ""
    gem_list = []
    visited = {(0, 0): True}
    segs = random.randint(5, 7)
    for seg in range(segs):
        choices = []
        turns = [""]
        if seg > 0:
            turns = ["L", "R"]
        for turn in turns:
            nd = d
            if turn == "L":
                nd = (d + 1) % 4
            if turn == "R":
                nd = (d + 3) % 4
            room = 0
            while 0 <= x + _DX[nd] * (room + 1) < N and 0 <= y + _DY[nd] * (room + 1) < N:
                room = room + 1
            if room > 0:
                choices.append((turn, nd, room))
        turn, d, room = random.choice(choices)
        steps = random.randint(1, min(4, room))
        plan = plan + turn + "M" * steps
        for i in range(steps):
            x = x + _DX[d]
            y = y + _DY[d]
            visited[(x, y)] = True
        if (x, y) not in gem_list and (x, y) != (0, 0) and (random.random() < 0.8 or seg == segs - 1):
            plan = plan + "P"
            gem_list.append((x, y))
    if len(gem_list) < 3:
        return _make_world()
    rock_list = []
    while len(rock_list) < 7:
        c = random.randint(0, N - 1)
        r = random.randint(0, N - 1)
        if (c, r) not in visited and (c, r) not in rock_list:
            rock_list.append((c, r))
    messy = random.choice(["", " ", "  "])
    for ch in plan:
        if random.random() < 0.5:
            ch = ch.lower()
        messy = messy + ch
        k = random.random()
        if k < 0.25:
            messy = messy + " "
        elif k < 0.35:
            messy = messy + "-"
    messy = messy + random.choice(["", " ", "  "])
    rocks = rock_list
    gems = gem_list
    orders = messy
    return plan

N = 8
CELL = 60
_DX = [1, 0, -1, 0]
_DY = [0, 1, 0, -1]


def _cx(c):
    return -240 + 30 + c * CELL


def _cy(r):
    return -240 + 30 + r * CELL


_w = turtle.Turtle()
_w.hideturtle()
_w.speed(0)
_w.penup()

t = turtle.Turtle()
t.shape("turtle")
t.color("darkorange")
t.pensize(4)
t.speed(0)

collected = 0
crashed = False
missed = 0
_tired = False
_calls = 0
_pos = [0, 0]
_dir = 0


def _draw():
    # 画格子、石头、宝石，机器人回到起点 / draw the grid, rocks and gems; robot back to the start
    global collected, crashed, missed, _tired, _calls, _dir
    _w.clear()
    _w.pensize(1)
    _w.color("lightgray")
    for i in range(N + 1):
        _w.goto(-240, -240 + i * CELL)
        _w.pendown()
        _w.goto(240, -240 + i * CELL)
        _w.penup()
        _w.goto(-240 + i * CELL, -240)
        _w.pendown()
        _w.goto(-240 + i * CELL, 240)
        _w.penup()
    for rk in rocks:
        _w.goto(_cx(rk[0]), _cy(rk[1]))
        _w.dot(46, "dimgray")
        _w.dot(20, "gray")
    for g in gems:
        _w.goto(_cx(g[0]), _cy(g[1]))
        _w.dot(32, "deepskyblue")
        _w.dot(14, "white")
    collected = 0
    crashed = False
    missed = 0
    _tired = False
    _calls = 0
    _pos[0] = _start[0]
    _pos[1] = _start[1]
    _dir = 0
    t.penup()
    t.goto(_cx(_start[0]), _cy(_start[1]))
    t.setheading(0)
    t.clear()
    t.pendown()


def _tick():
    # 防止死循环：动作太多机器人就没电了 / guard against endless loops: too many actions and the battery runs out
    global _calls, _tired
    _calls = _calls + 1
    if _calls > _MAX_CALLS:
        _tired = True
    if _calls > _MAX_CALLS + 500:
        raise RuntimeError("机器人没电了，你的循环停不下来！点「↺ 还原」再想想。/ The robot's battery is flat - your loop never ends! Click Reset and rethink.")


def _free(c, r):
    return 0 <= c < N and 0 <= r < N and (c, r) not in rocks


def move():
    global crashed
    _tick()
    if crashed or _tired:
        return
    nc = _pos[0] + _DX[_dir]
    nr = _pos[1] + _DY[_dir]
    if not _free(nc, nr):
        crashed = True
        t.dot(20, "red")
        return
    _pos[0] = nc
    _pos[1] = nr
    t.goto(_cx(nc), _cy(nr))


def turn_left():
    global _dir
    _tick()
    if crashed or _tired:
        return
    _dir = (_dir + 1) % 4
    t.left(90)


def turn_right():
    global _dir
    _tick()
    if crashed or _tired:
        return
    _dir = (_dir + 3) % 4
    t.right(90)


def pick():
    global collected, missed
    _tick()
    if crashed or _tired:
        return
    here = (_pos[0], _pos[1])
    if here in gems:
        gems.remove(here)
        collected = collected + 1
        t.dot(32, "gold")
    else:
        missed = missed + 1


# 🆕 传感器 / sensors
def front_is_clear():
    _tick()
    if crashed or _tired:
        return False
    return _free(_pos[0] + _DX[_dir], _pos[1] + _DY[_dir])


def gem_here():
    _tick()
    if crashed or _tired:
        return False
    return (_pos[0], _pos[1]) in gems


_plan = _make_world()
_draw()
t.speed(6)
