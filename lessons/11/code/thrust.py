# 🚀 会变的速度：重力 + 点火 / Speed that changes: gravity + thrust
# 先运行，再点一下画布。按 ↑ 点火，试试让火箭悬停在半空！
# Run it, then click the canvas. Press ↑ to fire the engine — can you make the rocket hover?
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

rocket = turtle.Turtle()
rocket.shape("triangle")
rocket.color("white")
rocket.setheading(90)
rocket.penup()
rocket.speed(0)
rocket.goto(0, 200)

info = turtle.Turtle()
info.hideturtle()
info.penup()
info.color("white")
info.goto(-280, 260)

GRAVITY = 0.1     # 每一拍，重力让速度往下变多少 / how much gravity changes the speed each beat
THRUST = 1        # 按一次 ↑，速度往上变多少 / how much one ↑ press changes the speed
vy = 0            # 速度：正 = 往上，负 = 往下 / velocity: + up, − down

def engine():                         # ↑ 键 / ↑ key
    global vy
    vy = vy + THRUST

def tick():
    global vy
    vy = vy - GRAVITY                 # ① 重力改「速度」/ gravity changes the VELOCITY
    rocket.sety(rocket.ycor() + vy)   # ② 速度改「位置」/ velocity changes the POSITION
    if rocket.ycor() < -280:          # 到地面了：停在地上 / hit the ground: stay there
        rocket.sety(-280)
        vy = 0
    info.clear()
    info.write(f"速度 vy = {round(vy, 1)}", font=("Arial", 16, "normal"))
    screen.ontimer(tick, 50)

screen.onkey(engine, "Up")
screen.listen()
tick()
