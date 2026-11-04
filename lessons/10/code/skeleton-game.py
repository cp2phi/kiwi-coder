# 🎮 项目骨架：接星星游戏  Project skeleton: Catch the Stars
# 作者 By：（昵称 nickname）
# 玩法：先点一下画布，用 ← → 移动篮子，接住掉下来的星星 ⭐
# How to play: click the canvas, move the basket with ← →, catch the falling star ⭐
import turtle
import random

# ----- 设置 settings（改这些数字最好玩！/ the most fun numbers to change!）-----
SPEED = 4            # 星星下落速度 / how fast the star falls
STEP = 40            # 篮子每次移动多少 / how far the basket moves
screen = turtle.Screen()
screen.bgcolor("navy")
screen.title("接星星")

# ----- 篮子 basket -----
basket = turtle.Turtle()
basket.speed(0)                          # 最快，不要慢吞吞 / fastest, no waiting
basket.shape("square")
basket.color("orange")
basket.penup()
basket.goto(0, -250)

# ----- 星星 star -----
star = turtle.Turtle()
star.speed(0)
star.shape("circle")
star.color("gold")
star.penup()
star.goto(random.randint(-250, 250), 280)

# ----- 记分 score -----
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.color("white")

def test():                                  # 🧪 小测试：开始前先检查 / tiny tests before we start
    assert SPEED > 0, "速度要大于 0"
    assert -300 < basket.xcor() < 300, "篮子要在画布里"

def go_left():                               # ← 键 / left key
    basket.setx(basket.xcor() - STEP)

def go_right():                              # → 键 / right key
    basket.setx(basket.xcor() + STEP)

def tick():                                  # 游戏循环：每 30 毫秒跑一次 / game loop every 30 ms
    global score
    star.sety(star.ycor() - SPEED)           # 星星往下掉 / star falls
    if star.distance(basket) < 30:           # 接住了！/ caught it!
        score = score + 1
        star.goto(random.randint(-250, 250), 280)
    if star.ycor() < -300:                   # 掉到底了 / fell off the bottom
        star.goto(random.randint(-250, 250), 280)
        # TODO: 加分功能：漏接扣分或减命 / lose a point or a life
    pen.clear()
    pen.write(f"分数 Score: {score}", align="center", font=("Arial", 18, "bold"))
    screen.ontimer(tick, 30)

test()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.listen()
tick()
# TODO: 必做功能 2：星星越来越快 / star gets faster   必做功能 3：到 10 分显示「你赢了」/ "You win" at 10
