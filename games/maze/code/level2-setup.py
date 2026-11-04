# 🐢 海龟迷宫 第 2 关：关卡代码（画迷宫、定义指令）/ Turtle Maze level 2: hidden setup
import turtle

walls = [(-260, -215, 165, -200), (-260, -100, 50, -85), (150, -215, 165, 185), (35, -85, 50, 185), (35, 170, 165, 185), (-275, -215, -260, -85)]
start = (-200, -150)
goal = (100, 120)

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

for _wall in walls:
    _rect(_wall[0], _wall[1], _wall[2], _wall[3], "slategray")

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
t.speed(7)

crashed = False

def _hit(x, y):
    if abs(x) > 295 or abs(y) > 295:
        return True
    for _wl in walls:
        if _wl[0] <= x <= _wl[2] and _wl[1] <= y <= _wl[3]:
            return True
    return False

def _go(n):
    global crashed
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

def forward(n):
    _go(n)

def backward(n):
    _go(-n)

def left(a):
    if not crashed:
        t.left(a)

def right(a):
    if not crashed:
        t.right(a)
