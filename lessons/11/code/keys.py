# ⌨️ 用方向键控制海龟 / Move the turtle with the arrow keys
# 先点 ▶ 运行，再点一下画布，然后按 ← → ↑ ↓
# Click ▶ Run, then click the canvas, then press ← → ↑ ↓
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pensize(3)
t.speed(0)

STEP = 20        # 每次走几步 / how far each press

def go_left():
    t.setheading(180)
    t.forward(STEP)

def go_right():
    t.setheading(0)
    t.forward(STEP)

def go_up():
    t.setheading(90)
    t.forward(STEP)

def go_down():
    t.setheading(270)
    t.forward(STEP)

# 把按键和函数「绑」在一起 / tie each key to a function
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.listen()           # 开始听键盘 / start listening

print("点一下画布，然后按方向键！ Click the canvas, then press the arrow keys!")
