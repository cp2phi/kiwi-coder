# 🐢 海龟迷宫 第 8 关：关卡代码（城堡的牙齿，高度每次随机）/ Turtle Maze level 8: hidden setup (castle teeth with random heights)
import turtle
import random
import math

GAP = 50
_W = 15
heights = []
for _i in range(5):
    heights.append(random.choice([40, 80, 120, 160]))

# 走廊的中心线：每颗牙齿 = 上 h → 右 50 → 下 h → 右 50
# corridor centre line: each tooth = up h → right 50 → down h → right 50
start = (-250, -150)
_pts = [start]
_x = start[0]
for _h in heights:
    _pts.append((_x, start[1] + _h))
    _pts.append((_x + GAP, start[1] + _h))
    _pts.append((_x + GAP, start[1]))
    _pts.append((_x + 2 * GAP, start[1]))
    _x = _x + 2 * GAP
goal = (_x, start[1])

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


# 先涂一块墙，再用白色粗笔「挖」出走廊 / paint a block of wall, then carve the corridor with a thick white pen
_rect(-285, -195, 285, 45, "slategray")
for _i in range(len(_pts) - 1):
    _a = _pts[_i]
    _b = _pts[_i + 1]
    _rect(min(_a[0], _b[0]) - _W, min(_a[1], _b[1]) - _W, max(_a[0], _b[0]) + _W, max(_a[1], _b[1]) + _W, "white")

# 终点：金色星星 / goal: a gold star
_w.goto(goal[0], goal[1])
_w.dot(26, "gold")
_w.goto(goal[0] - 10, goal[1] - 3)
_w.setheading(0)
_w.pendown()
_w.color("darkorange")
_w.fillcolor("darkorange")
_w.begin_fill()
for _i in range(5):
    _w.forward(20)
    _w.right(144)
_w.end_fill()
_w.penup()

# 起点：绿点 / start: a green dot
_w.goto(start[0], start[1])
_w.dot(16, "limegreen")

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
_last = (start[0], start[1])
_calls = 0
# 检查的时候用的「假想海龟」（不动真的海龟）/ an imaginary turtle used by the check (the real one stays put)
_virtual = False
_vx = 0.0
_vy = 0.0
_vh = 0.0
_vtop = 0.0


def _seg_dist(px, py, a, b):
    if a[0] == b[0]:
        lo = min(a[1], b[1])
        hi = max(a[1], b[1])
        dy = 0
        if py < lo:
            dy = lo - py
        if py > hi:
            dy = py - hi
        return math.sqrt((px - a[0]) ** 2 + dy ** 2)
    lo = min(a[0], b[0])
    hi = max(a[0], b[0])
    dx = 0
    if px < lo:
        dx = lo - px
    if px > hi:
        dx = px - hi
    return math.sqrt(dx ** 2 + (py - a[1]) ** 2)


def _hit(x, y):
    for _i in range(len(_pts) - 1):
        if _seg_dist(x, y, _pts[_i], _pts[_i + 1]) <= _W:
            return False
    return True


def _tick():
    global _calls
    _calls = _calls + 1
    if _calls > 5000:
        raise RuntimeError("海龟累坏了，你的循环停不下来！点「↺ 还原」再想想。/ The turtle is exhausted - your loop never ends! Click Reset and rethink.")


def _go(n):
    global crashed, _last, _vx, _vy, _vtop
    _tick()
    if _virtual:
        _vx = _vx + n * math.cos(math.radians(_vh))
        _vy = _vy + n * math.sin(math.radians(_vh))
        if _vy > _vtop:
            _vtop = _vy
        return
    if crashed:
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
        if _hit(t.xcor(), t.ycor()):
            crashed = True
            t.dot(18, "red")
    _last = (t.xcor(), t.ycor())


def forward(n):
    _go(n)


def backward(n):
    _go(-n)


def left(a):
    global _vh
    _tick()
    if _virtual:
        _vh = _vh + a
    elif not crashed:
        t.left(a)


def right(a):
    global _vh
    _tick()
    if _virtual:
        _vh = _vh - a
    elif not crashed:
        t.right(a)
