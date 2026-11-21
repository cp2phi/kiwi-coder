# ☄️ 掉落的陨石：ontimer 就是游戏的「心跳」 Falling asteroid: ontimer is the game's heartbeat
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

rock = turtle.Turtle()
rock.shape("circle")
rock.color("sienna")
rock.penup()
rock.goto(0, 250)

SPEED = 8          # 每一拍掉几步 / how far it falls each beat
BEAT = 50          # 每拍几毫秒 / milliseconds per beat

def tick():
    rock.sety(rock.ycor() - SPEED)       # ① 往下掉 / fall down
    if rock.ycor() < -250:               # ② 掉到底了？/ reached the bottom?
        rock.goto(random.randint(-250, 250), 250)   # 回到顶上随机的位置 / back to a random spot at the top
    screen.ontimer(tick, BEAT)           # ③ 下一拍再叫我 / call me again next beat

tick()
print("陨石在掉！点「■ 结束游戏」停下。 The asteroid is falling! Click ■ End game to stop.")
