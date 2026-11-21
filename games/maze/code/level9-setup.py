# 🐢 海龟迷宫 第 9 关：关卡代码（真正的迷宫：有岔路和死胡同，每次随机）/ Turtle Maze level 9: hidden setup (a real maze with branches and dead ends, random every run)
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


# 用「挖洞法」生成迷宫：5×5 个房间，房间之间挖通道 / carve a maze: 5×5 rooms joined by passages
def _make_maze():
    opened = {(0, 0): True}
    stack = [(0, 0)]
    seen = {(0, 0): True}
    while len(stack) > 0:
        cur = stack[-1]
        nbrs = []
        for k in range(4):
            n = (cur[0] + _DX[k], cur[1] + _DY[k])
            if 0 <= n[0] < 5 and 0 <= n[1] < 5 and n not in seen:
                nbrs.append(n)
        if len(nbrs) == 0:
            stack.pop()
        else:
            n = random.choice(nbrs)
            seen[n] = True
            opened[(n[0] * 2, n[1] * 2)] = True
            opened[(cur[0] + n[0], cur[1] + n[1])] = True
            stack.append(n)
    # 再多挖几个洞，迷宫里就有了「圈」/ knock out a few more walls so the maze has loops
    extra = 0
    while extra < 5:
        c = random.randint(0, 8)
        r = random.randint(0, 8)
        if (c + r) % 2 == 1 and (c, r) not in opened:
            opened[(c, r)] = True
            extra = extra + 1
    return opened


_w = turtle.Turtle()
_w.hideturtle()
_w.speed(0)
_w.penup()

t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen")
t.pensize(3)
t.speed(0)

start = (_cx(0), _cy(0))
goal_cell = (8, 8)
goal = (_cx(8), _cy(8))
_open = {}
crashed = False
_tired = False
_moved = 0
_calls = 0
_max_moved = 0
_last = (start[0], start[1])


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


def _build():
    # 换一个新迷宫，海龟回到起点 / make a new maze and put the turtle back at the start
    global _open, crashed, _tired, _moved, _calls, _max_moved, _last
    _open = _make_maze()
    _w.clear()
    _rect(-270, -270, 270, 270, "slategray")
    for p in _open:
        _rect(_cx(p[0]) - 30, _cy(p[1]) - 30, _cx(p[0]) + 30, _cy(p[1]) + 30, "white")
    _w.goto(goal[0], goal[1])
    _w.dot(40, "gold")
    _w.goto(goal[0] - 15, goal[1] - 5)
    _w.setheading(0)
    _w.pendown()
    _w.color("darkorange")
    _w.fillcolor("darkorange")
    _w.begin_fill()
    for i in range(5):
        _w.forward(30)
        _w.right(144)
    _w.end_fill()
    _w.penup()
    _w.goto(start[0], start[1])
    _w.dot(20, "limegreen")
    t.penup()
    t.goto(start[0], start[1])
    t.setheading(0)
    t.clear()
    t.pendown()
    crashed = False
    _tired = False
    _moved = 0
    _calls = 0
    _max_moved = (len(_open) + 10) * CELL * 2
    _last = (start[0], start[1])


_build()
t.speed(10)


def _cell_at(x, y):
    return (int(math.floor((x + 270) / CELL)), int(math.floor((y + 270) / CELL)))


def _hit(x, y):
    return _cell_at(x, y) not in _open


def _tick():
    # 防止死循环 / guard against endless loops
    global _calls
    _calls = _calls + 1
    if _calls > 8000:
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


# 传感器 / sensors
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
