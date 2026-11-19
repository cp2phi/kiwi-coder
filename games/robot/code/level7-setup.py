# 💎 宝石机器人 第 7 关：关卡代码（房间大小和宝石每次随机）/ Gem Robot level 7: hidden setup (random room size and gems every run)
import turtle
import random

_MAX_CALLS = 300
_start = (0, 0)
room_w = random.randint(4, 8)
room_h = random.randint(4, 8)
if room_w == 8 and room_h == 8:
    room_h = 7
# 房间外面全是石头 / everything outside the room is rock
rocks = []
for _c in range(8):
    for _r in range(8):
        if _c >= room_w or _r >= room_h:
            rocks.append((_c, _r))
# 宝石只在靠墙的一圈格子上 / gems only on the cells along the walls
_ring = []
for _c in range(room_w):
    for _r in range(room_h):
        if _c == 0 or _r == 0 or _c == room_w - 1 or _r == room_h - 1:
            _ring.append((_c, _r))
gems = random.sample(_ring, random.randint(4, 7))

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


_draw()
t.speed(6)
