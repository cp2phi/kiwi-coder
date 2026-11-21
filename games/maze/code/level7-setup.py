# 🐢 海龟迷宫 第 7 关：关卡代码（每次随机一条走廊 + 传感器）/ Turtle Maze level 7: hidden setup (a random corridor every run + sensors)
import turtle
import random
import math

CELL = 60
_N = 9
_DX = [1, 0, -1, 0]
_DY = [0, 1, 0, -1]


def _cx(c):
    return -240 + c * CELL


def _cy(r):
    return -240 + r * CELL


def _inside(c, r):
    return 0 <= c < _N and 0 <= r < _N


# 随机走廊：一条不会碰到自己的弯弯曲曲的路，左转右转都有
# random corridor: a winding path that never touches itself, with both left and right turns
def _make_path():
    while True:
        r0 = random.randint(1, 7)
        path = [(0, r0), (1, r0)]
        used = {(0, r0): True, (1, r0): True}
        d = 0
        lefts = 0
        rights = 0
        target = random.randint(16, 24)
        while len(path) < target:
            cur = path[-1]
            options = []
            for turn in [0, 0, 1, 3]:
                nd = (d + turn) % 4
                n = (cur[0] + _DX[nd], cur[1] + _DY[nd])
                if not _inside(n[0], n[1]) or n in used:
                    continue
                ok = True
                for k in range(4):
                    m = (n[0] + _DX[k], n[1] + _DY[k])
                    if m != cur and m in used:
                        ok = False
                if ok:
                    options.append(turn)
            if len(options) == 0:
                break
            turn = random.choice(options)
            if turn == 1:
                lefts = lefts + 1
            if turn == 3:
                rights = rights + 1
            d = (d + turn) % 4
            n = (cur[0] + _DX[d], cur[1] + _DY[d])
            path.append(n)
            used[n] = True
        if len(path) >= 13 and lefts >= 2 and rights >= 2:
            return path


_path = _make_path()
_open = {}
for _p in _path:
    _open[_p] = True
goal_cell = _path[-1]
goal = (_cx(goal_cell[0]), _cy(goal_cell[1]))
start = (_cx(_path[0][0]), _cy(_path[0][1]))

_w = turtle.Turtle()
_w.hideturtle()
_w.speed(0)
_w.penup()


def _rect(x1, y1, x2, y2, color):
    _w.goto(x1, y1)
    _w.setheading(0)
    _w.pendown()
    _w.color(color)
    _w.fillcolor(color)
    _w.begin_fill()
    _w.goto(x2, y1)
    _w.goto(x2, y2)
    _w.goto(x1, y2)
    _w.goto(x1, y1)
    _w.end_fill()
    _w.penup()


# 先把整块涂成墙，再挖出走廊 / paint everything as wall, then carve the corridor
_rect(-270, -270, 270, 270, "slategray")
for _p in _path:
    _rect(_cx(_p[0]) - 30, _cy(_p[1]) - 30, _cx(_p[0]) + 30, _cy(_p[1]) + 30, "white")

# 终点：金色星星 / goal: a gold star
_w.goto(goal[0], goal[1])
_w.dot(40, "gold")
_w.goto(goal[0] - 15, goal[1] - 5)
_w.setheading(0)
_w.pendown()
_w.color("darkorange")
_w.fillcolor("darkorange")
_w.begin_fill()
for _i in range(5):
    _w.forward(30)
    _w.right(144)
_w.end_fill()
_w.penup()

# 起点：绿点 / start: a green dot
_w.goto(start[0], start[1])
_w.dot(20, "limegreen")

t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen")
t.pensize(3)
t.speed(0)
t.penup()
t.goto(start[0], start[1])
t.setheading(0)
t.pendown()
t.speed(8)

crashed = False
_tired = False
_moved = 0
_calls = 0
_max_moved = len(_path) * CELL + 900
_last = (start[0], start[1])


def _cell_at(x, y):
    return (int(math.floor((x + 270) / CELL)), int(math.floor((y + 270) / CELL)))


def _hit(x, y):
    return _cell_at(x, y) not in _open


def _tick():
    # 防止死循环：海龟累了就停下；还在一直叫它就报错
    # guard against endless loops: a tired turtle stops; if it is still being called, raise an error
    global _calls
    _calls = _calls + 1
    if _calls > 4000:
        raise RuntimeError("海龟累坏了，你的循环停不下来！点「↺ 还原」再想想。/ The turtle is exhausted - your loop never ends! Click Reset and rethink.")


def _go(n):
    global crashed, _moved, _tired, _last
    _tick()
    if crashed or _tired:
        return
    left_over = abs(n)
    while left_over > 0 and not crashed:
        step = left_over
        if step > 5:
            step = 5
        if n >= 0:
            t.forward(step)
        else:
            t.backward(step)
        left_over = left_over - step
        _moved = _moved + step
        if _hit(t.xcor(), t.ycor()):
            crashed = True
            t.dot(18, "red")
    _last = (t.xcor(), t.ycor())
    if _moved > _max_moved:
        _tired = True


def forward(n):
    _go(n)


def backward(n):
    _go(-n)


def left(a):
    _tick()
    if not crashed and not _tired:
        t.left(a)


def right(a):
    _tick()
    if not crashed and not _tired:
        t.right(a)


def _dir():
    return int(round(t.heading() / 90.0)) % 4


def _blocked(turn):
    _tick()
    if crashed or _tired:
        return True
    here = _cell_at(t.xcor(), t.ycor())
    d = (_dir() + turn) % 4
    return (here[0] + _DX[d], here[1] + _DY[d]) not in _open


# 🆕 传感器 / sensors
def wall_ahead():
    return _blocked(0)


def wall_left():
    return _blocked(1)


def wall_right():
    return _blocked(3)


def at_goal():
    _tick()
    if crashed or _tired:
        return True
    return _cell_at(t.xcor(), t.ycor()) == goal_cell
