# test-input: 2
# 🛰️ 项目骨架 C：任务控制中心  Project skeleton C: Mission Control
# 作者 By：（昵称 nickname）
# 玩法：选载荷 → 系统 GO / NO-GO 检查 → 点一下画布，按空格发射 → 看火箭飞上轨道
# How to play: pick a payload → GO / NO-GO poll → click the canvas, press space to launch → watch the rocket reach orbit
import turtle
import random

# ===== 设置 settings =====
EARTH_Y = -60         # 地球中心的高度 / height of the Earth's centre
EARTH_R = 110         # 地球半径 / Earth's radius
SEPARATION = 120      # 飞到这个高度（y），一级和二级分离 / stage separation at this height (y)
ORBIT = 200           # 飞到这个高度（y）就入轨 / reach this height (y) = orbit
ACCEL = 0.05          # 每一拍加速多少 / how much faster every beat
PAYLOADS = {"1": "🛰️ 通信卫星 satellite", "2": "👩‍🚀 宇航员 crew", "3": "🤖 火星车 rover"}

# ===== 纯函数 pure functions：只算数字和字典，不碰海龟 → 最好测试 / no turtles → easy to test =====
def read_sensors():                     # 假装读传感器（随机）/ pretend sensor readings (random)
    return {
        "fuel": random.randint(94, 100),            # 燃料加满了百分之几 / fuel %
        "wind": random.randint(0, 34),              # 风速 km/h / wind speed
        "engines": random.choice([9, 9, 9, 8]),     # 9 台发动机里几台正常 / how many of 9 engines are OK
    }

def go_or_nogo(ok):                     # True → "GO"，False → "NO-GO"
    if ok:
        return "GO"
    return "NO-GO"

def poll(readings):                     # 发射前的 GO / NO-GO 轮询（我们自己定的规则）/ the pre-launch poll (our own rules)
    checks = {}
    checks["燃料 fuel"] = go_or_nogo(readings["fuel"] >= 95)
    checks["天气 weather"] = go_or_nogo(readings["wind"] <= 30)
    checks["发动机 engines"] = go_or_nogo(readings["engines"] == 9)
    return checks

def all_systems_go(checks):             # 每个系统都是 GO 吗？/ is every system GO?
    # TODO 必做 1：用 for 看每一个系统：有一个不是 "GO" 就 return False；全部看完 return True
    #      must-have 1: loop over the systems: any one not "GO" → return False; after the loop → return True
    return True                         # 先假装永远 GO / pretend it's always GO for now

def stage_for(height):                  # 现在是第几级在推？/ which stage is pushing now?
    # TODO 必做 3：height 比 SEPARATION 小 → 1，否则 → 2 / must-have 3: below SEPARATION → 1, otherwise → 2
    return 1

def test():                             # 🧪 小测试：开始前先检查 / tiny tests before we start
    assert go_or_nogo(True) == "GO"
    assert go_or_nogo(False) == "NO-GO"
    assert poll({"fuel": 100, "wind": 50, "engines": 9})["天气 weather"] == "NO-GO", "大风不能发射 / too windy"
    # TODO 必做 1：写好 all_systems_go 以后，删掉下面 2 行前面的 # / remove the # when all_systems_go is written
    # assert all_systems_go({"燃料 fuel": "GO", "天气 weather": "GO"}) == True
    # assert all_systems_go({"燃料 fuel": "GO", "天气 weather": "NO-GO"}) == False, "一个 NO-GO 就不行 / one NO-GO = no launch"
    # TODO 必做 3：写好 stage_for 以后，删掉下面 2 行前面的 # / remove the # when stage_for is written
    # assert stage_for(0) == 1
    # assert stage_for(SEPARATION + 1) == 2

# ===== 任务日志 the mission log =====
log = []                                # 发生过的事，按顺序 / what happened, in order
beats = 0                               # 起飞后过了几拍（每拍 0.05 秒）/ beats since liftoff (0.05 s each)

def log_event(text):                    # 记一条日志 / write one log line
    line = f"T+{round(beats * 0.05, 1)}s  {text}"
    log.append(line)
    print(line)

def print_log():                        # 打印整本日志 / print the whole log
    print("\n📜 任务日志 Mission log")
    for line in log:
        print("   " + line)

# ===== 画面 the scene =====
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()                   # 画地球 / draws the Earth
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(0, EARTH_Y - EARTH_R)
pen.color("royalblue")
pen.begin_fill()
pen.circle(EARTH_R)
pen.end_fill()

rocket = turtle.Turtle()                # 火箭（二级 + 载荷）/ the rocket (second stage + payload)
rocket.shape("triangle")
rocket.color("white")
rocket.setheading(90)
rocket.penup()
rocket.speed(0)
rocket.goto(0, EARTH_Y + EARTH_R + 22)

booster = turtle.Turtle()               # 一级助推器 / the first-stage booster
booster.shape("square")
booster.color("gray")
booster.penup()
booster.speed(0)
booster.goto(0, rocket.ycor() - 20)

hud = turtle.Turtle()                   # 仪表盘 / the dashboard
hud.hideturtle()
hud.speed(0)
hud.penup()
hud.color("white")

vy = 0                                  # 往上的速度 / upward speed
in_orbit = False                        # 到轨道了吗？/ in orbit yet?

def show_hud():
    hud.clear()
    hud.goto(-280, 260)
    hud.write(f"高度 altitude {int(rocket.ycor())}   速度 speed {round(vy, 1)}", font=("Arial", 14, "normal"))

def fly():                              # 飞行心跳：每 50 毫秒一次 / the flight heartbeat, every 50 ms
    global vy, beats, in_orbit
    beats = beats + 1
    if in_orbit:                                # 已经在轨道上：绕着地球转 / in orbit: circle the Earth
        rocket.circle(ORBIT - EARTH_Y, 2)
    elif rocket.ycor() < ORBIT:                 # 还在往上飞 / still climbing
        vy = vy + ACCEL
        rocket.sety(rocket.ycor() + vy)
        booster.goto(rocket.xcor(), rocket.ycor() - 20)     # 一级还连着 / stage 1 still attached
        # TODO 必做 3：用 stage_for 看高度：变成第 2 级时，记一条「一二级分离」日志（只记一次！），
        #      之后 booster 不再跟着火箭，而是往下掉
        #      must-have 3: use stage_for: when it becomes stage 2, log "stage separation" (only once!),
        #      then the booster stops following the rocket and falls instead
        show_hud()
    else:                                       # 刚刚到轨道 / just reached orbit
        in_orbit = True
        rocket.setheading(180)
        rocket.pencolor("lightgray")
        rocket.pendown()                        # 画出轨道 / draw the orbit
        log_event(f"入轨！Orbit! {payload}")
        print_log()
    screen.ontimer(fly, 50)

def launch():                           # 空格键：发射！/ space key: launch!
    log_event("点火，起飞！Liftoff!")
    fly()
    # TODO 必做 2：先倒数 T-10 … T-0（用 ontimer，每 0.5 秒一个数，写在画布中间），倒数完才 fly()；
    #      按两次空格也只能发射一次
    #      must-have 2: count down T-10 … T-0 first (ontimer, one number every 0.5 s, in the middle of the canvas),
    #      then fly(); pressing space twice must still launch only once

# ===== 主程序 main program =====
test()
show_hud()
print("🛰️ 任务控制中心 Mission Control")
for key in PAYLOADS:
    print(f"   {key}  {PAYLOADS[key]}")
choice = input("今天发射什么？输入 1、2 或 3 / What are we launching? Type 1, 2 or 3: ")
payload = PAYLOADS.get(choice.strip(), PAYLOADS["1"])
log_event(f"载荷 payload: {payload}")

print("\n📋 GO / NO-GO:")
checks = poll(read_sensors())
for system in checks:
    print(f"   {system}: {checks[system]}")
# TODO 必做 1：用 all_systems_go(checks) 决定：全部 GO 才能发射；否则打印「🛑 推迟发射 SCRUB」，不能按空格发射
#      must-have 1: use all_systems_go(checks): launch only if all GO; otherwise print "🛑 SCRUB" and space does nothing
print("\n✅ 点一下画布，按空格键发射！/ Click the canvas, then press space to launch!")
screen.onkey(launch, "space")
screen.listen()
