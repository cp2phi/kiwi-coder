# ⌨️ 用方向键开飞船 / Fly a spaceship with the arrow keys
# 先点 ▶ 运行，再点一下画布，然后按 ← → ↑ ↓
# Click ▶ Run, then click the canvas, then press ← → ↑ ↓
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

ship = turtle.Turtle()
ship.shape("triangle")
ship.color("deepskyblue")
ship.pencolor("white")
ship.speed(0)

STEP = 20        # 每按一次飞多远 / how far each press

def go_left():
    ship.setheading(180)
    ship.forward(STEP)

def go_right():
    ship.setheading(0)
    ship.forward(STEP)

def go_up():
    ship.setheading(90)
    ship.forward(STEP)

def go_down():
    ship.setheading(270)
    ship.forward(STEP)

# 把按键和函数「绑」在一起 / tie each key to a function
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.listen()           # 开始听键盘 / start listening

print("点一下画布，然后按方向键！ Click the canvas, then press the arrow keys!")
