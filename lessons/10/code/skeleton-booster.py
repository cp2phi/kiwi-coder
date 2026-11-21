# 🚀 项目骨架 A：助推器回家  Project skeleton A: Bring the Booster Home
# 作者 By：（昵称 nickname）
# 玩法：先点一下画布。按 ↑ 点火减速，让助推器慢慢落在无人船的甲板上！
# How to play: click the canvas first. Press ↑ to fire the engine and slow down. Land softly on the drone ship's deck!
# 灵感：SpaceX 猎鹰 9 号的一级助推器会自己飞回来，降落在海上的无人船上，下次再用。
# Inspired by SpaceX's Falcon 9 first-stage boosters, which fly back, land on a drone ship at sea, and fly again.
import turtle
import random

# ===== 设置 settings（改这些数字最好玩！/ the most fun numbers to change!）=====
GRAVITY = 0.05        # 重力：每一拍往下快一点点 / gravity: a little faster downwards every beat
THRUST = 0.6          # 按一次 ↑ 往上推多少 / how much one ↑ press pushes up
START_FUEL = 30       # 一开始能点几次火 / how many burns of fuel at the start
MAX_SPEED = 2         # 落地速度不超过它才安全 / land at this speed or slower to be safe
PAD_HALF = 40         # 甲板宽度的一半 / half the width of the deck
DECK_Y = -230         # 甲板的高度 / height of the deck
SHIP_X = 0            # 无人船在哪里 / where the drone ship is

# ===== 纯函数 pure functions：只算数字，不碰海龟 → 最好测试 / numbers only, no turtles → easy to test =====
def use_fuel(fuel):                     # 点一次火用掉 1 份燃料，最少是 0 / one burn uses 1 fuel, never below 0
    if fuel > 0:
        return fuel - 1
    return 0

def is_safe_landing(speed, drift):      # speed = 落地时往下的速度 / downward speed at touchdown
    # drift = 离甲板中心多远 / how far from the middle of the deck
    # TODO 必做 3：speed ≤ MAX_SPEED 而且 drift ≤ PAD_HALF 才安全（用 and）
    #      must-have 3: safe only if speed ≤ MAX_SPEED and drift ≤ PAD_HALF (use and)
    return True                         # 先假装永远安全 / pretend it's always safe for now

def test():                             # 🧪 小测试：开始前先检查 / tiny tests before we start
    assert use_fuel(10) == 9, "点一次火少 1 份燃料 / one burn uses 1 fuel"
    assert use_fuel(0) == 0, "没油了不能变成负数 / fuel can't go negative"
    # TODO 必做 3：写好 is_safe_landing 以后，删掉下面 3 行最前面的 # / when is_safe_landing is written, remove the # from these 3 lines
    # assert is_safe_landing(1, 10) == True,  "又慢又准 = 安全 / slow and centred = safe"
    # assert is_safe_landing(5, 10) == False, "太快 = 不安全 / too fast = unsafe"
    # assert is_safe_landing(1, 80) == False, "没落在甲板上 = 不安全 / missed the deck = unsafe"

# ===== 画面 the scene =====
screen = turtle.Screen()
screen.bgcolor("midnightblue")

pen = turtle.Turtle()                   # 画海和船 / draws the sea and the ship
pen.hideturtle()
pen.speed(0)
pen.penup()

def draw_box(x, y, width, height, colour):      # 画一个实心长方形，(x, y) 是左上角 / a filled box; (x, y) = top-left
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(colour)
    pen.begin_fill()
    for i in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

draw_box(-300, DECK_Y - 12, 600, 60, "steelblue")             # 大海 / the sea
draw_box(SHIP_X - PAD_HALF, DECK_Y, PAD_HALF * 2, 12, "gray")  # 无人船 / the drone ship

booster = turtle.Turtle()               # 助推器 / the booster
booster.shape("triangle")
booster.color("white")
booster.setheading(90)                  # 头朝上 / nose up
booster.penup()
booster.speed(0)
booster.goto(random.randint(-200, 200), 250)

hud = turtle.Turtle()                   # 写仪表盘的笔 / the pen for the dashboard
hud.hideturtle()
hud.speed(0)
hud.penup()
hud.color("white")

# ===== 记住的数字 what the game remembers =====
vy = -1                                 # 上下速度：正 = 往上，负 = 往下 / up-down velocity: + up, − down
vx = 0                                  # 左右速度 / left-right velocity
fuel = START_FUEL

def show_hud():                         # 左上角的仪表盘 / the dashboard, top left
    hud.clear()
    hud.goto(-280, 260)
    hud.write(f"高度 height {int(booster.ycor() - DECK_Y)}   速度 speed {round(-vy, 1)}", font=("Arial", 14, "normal"))
    # TODO 必做 1：把燃料 fuel 也写出来 / must-have 1: show the fuel too

def engine():                           # ↑ 键：点火，往上推 / ↑ key: fire the engine, push up
    global vy
    vy = vy + THRUST
    # TODO 必做 1：用 use_fuel 扣燃料；fuel 是 0 的时候不能点火（要 global fuel）
    #      must-have 1: use_fuel to spend fuel; no burning when fuel is 0 (needs global fuel)

# TODO 必做 2：写 go_left() 和 go_right()：侧面的小推进器让 vx 变一点点（要 global vx）
#      must-have 2: write go_left() and go_right(): small side thrusters change vx a little (needs global vx)

def touchdown():                        # 碰到甲板的高度了 / reached the deck
    speed = round(-vy, 1)
    drift = abs(booster.xcor() - SHIP_X)        # abs() 去掉负号 / abs() drops the minus sign
    hud.goto(0, 0)
    hud.write(f"触地 Touchdown!  speed {speed}  drift {int(drift)}", align="center", font=("Arial", 18, "bold"))
    # TODO 必做 3：用 is_safe_landing(speed, drift) 判断：成功写绿色的「着陆成功」，失败把助推器变红写「坠毁」
    #      must-have 3: use is_safe_landing(speed, drift): green "Landed!" on success; red booster + "Crashed" on failure

def tick():                             # 游戏心跳：每 50 毫秒一次 / the game heartbeat, every 50 ms
    global vy
    vy = vy - GRAVITY                           # 重力让它越落越快 / gravity makes it fall faster
    booster.sety(booster.ycor() + vy)           # 上下动 / move up or down
    booster.setx(booster.xcor() + vx)           # 左右飘 / drift left or right
    show_hud()
    if booster.ycor() <= DECK_Y + 10:           # 到甲板了吗？/ at the deck?
        touchdown()                             # 到了：不再约下一拍，游戏停 / yes: no next beat, game stops
    else:
        screen.ontimer(tick, 50)                # 没到：50 毫秒后再来 / no: again in 50 ms

test()
screen.onkey(engine, "Up")
screen.listen()
tick()
