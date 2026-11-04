# 💎 宝石机器人 第 5 关：关卡代码（画格子、放宝石、定义指令）/ Gem Robot level 5: hidden setup
import turtle

N = 8
CELL = 60
rocks = []
gems = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]
_start = (0, 1)

def _cx(c):
    return -240 + 30 + c * CELL

def _cy(r):
    return -240 + 30 + r * CELL

_w = turtle.Turtle()
_w.hideturtle()
_w.speed(0)
_w.penup()
_w.pensize(1)
_w.color("lightgray")
for _i in range(N + 1):
    _w.goto(-240, -240 + _i * CELL)
    _w.pendown()
    _w.goto(240, -240 + _i * CELL)
    _w.penup()
    _w.goto(-240 + _i * CELL, -240)
    _w.pendown()
    _w.goto(-240 + _i * CELL, 240)
    _w.penup()

for _rk in rocks:
    _w.goto(_cx(_rk[0]), _cy(_rk[1]))
    _w.dot(46, "dimgray")
    _w.dot(20, "gray")

for _g in gems:
    _w.goto(_cx(_g[0]), _cy(_g[1]))
    _w.dot(32, "deepskyblue")
    _w.dot(14, "white")

collected = 0
crashed = False
missed = 0
_pos = [_start[0], _start[1]]
_dir = 0
_DX = [1, 0, -1, 0]
_DY = [0, 1, 0, -1]

t = turtle.Turtle()
t.shape("turtle")
t.color("darkorange")
t.pensize(4)
t.speed(0)
t.penup()
t.goto(_cx(_start[0]), _cy(_start[1]))
t.setheading(0)
t.pendown()
t.speed(6)

def move():
    global crashed
    if crashed:
        return
    nc = _pos[0] + _DX[_dir]
    nr = _pos[1] + _DY[_dir]
    if nc < 0 or nc >= N or nr < 0 or nr >= N or (nc, nr) in rocks:
        crashed = True
        t.dot(20, "red")
        return
    _pos[0] = nc
    _pos[1] = nr
    t.goto(_cx(nc), _cy(nr))

def turn_left():
    global _dir
    if crashed:
        return
    _dir = (_dir + 1) % 4
    t.left(90)

def turn_right():
    global _dir
    if crashed:
        return
    _dir = (_dir + 3) % 4
    t.right(90)

def pick():
    global collected, missed
    if crashed:
        return
    here = (_pos[0], _pos[1])
    if here in gems:
        gems.remove(here)
        collected = collected + 1
        t.dot(32, "gold")
    else:
        missed = missed + 1
