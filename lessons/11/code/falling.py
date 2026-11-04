# ⭐ 掉落的星星：ontimer 就是游戏的「心跳」 Falling star: ontimer is the game's heartbeat
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

star = turtle.Turtle()
star.shape("circle")
star.color("gold")
star.penup()
star.goto(0, 250)

SPEED = 8          # 每一拍掉几步 / how far it falls each beat
BEAT = 50          # 每拍几毫秒 / milliseconds per beat

def tick():
    star.sety(star.ycor() - SPEED)       # 往下掉 / fall down
    if star.ycor() < -250:               # 掉到底了？/ reached the bottom?
        star.goto(random.randint(-250, 250), 250)   # 回到顶上随机的位置 / back to the top
    screen.ontimer(tick, BEAT)           # 下一拍再叫我 / call me again next beat

tick()
print("星星在掉！点「■ 结束游戏」停下。 The star is falling! Click ■ End game to stop.")
