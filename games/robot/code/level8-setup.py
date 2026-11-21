# 💎 宝石机器人 第 8 关：关卡代码（田地大小和宝石每次随机）/ Gem Robot level 8: hidden setup (random field size and gems every run)
import turtle
import random

_MAX_CALLS = 600
_start = (0, 0)
field_w = random.randint(4, 8)
field_h = random.randint(3, 8)
rocks = []
_field = []
for _c in range(8):
    for _r in range(8):
        if _c >= field_w or _r >= field_h:
            rocks.append((_c, _r))
        else:
            _field.append((_c, _r))
gems = random.sample(_field, max(5, len(_field) // 3))

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
t.speed(7)
