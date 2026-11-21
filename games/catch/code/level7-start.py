# 🍎 第 7 关：生命值 + 再来一局 / Level 7: lives + play again
# 任务 / Task:
#   ① 把 misses 换成 lives（命），一开始 3 条，漏掉一个水果就少 1 条 / swap misses for lives: start with 3, lose 1 for each missed fruit
#   ② 写 lose_life()：命少 1；命到 0 的时候 game_over = True / write lose_life(): one less life; at 0 lives set game_over = True
#   ③ game_over 以后水果不再掉 / after game_over nothing falls
#   ④ 写 restart()，按空格调用：只有游戏结束时才重新开始（分数归 0、命回满、水果重新掉）/ write restart(), called by space: only when the game is over, start again (score 0, full lives, fruit falling again)


import turtle
import random

# ===== 可以改的数字和颜色 / Numbers and colours you can change =====
SPEED = 5              # 水果下落的速度 / how fast the fruit falls
BASKET_STEP = 30       # 篮子每按一次移动多少 / how far the basket moves per key press
FRUIT_COLOUR = "red"   # 水果的颜色 / fruit colour
BASKET_COLOUR = "brown"  # 篮子的颜色 / basket colour
MAX_MISSES = 3         # 漏掉几个就结束 / misses before game over

screen = turtle.Screen()
screen.bgcolor("lightblue")

# 篮子 / the basket
basket = turtle.Turtle()
basket.shape("square")
basket.color(BASKET_COLOUR)
basket.penup()
basket.speed(0)
basket.goto(0, -250)

# 水果 / the fruit
fruit = turtle.Turtle()
fruit.shape("circle")
fruit.color(FRUIT_COLOUR)
fruit.penup()
fruit.speed(0)
fruit.goto(random.randint(-250, 250), 280)

# 写分数的笔 / the pen that writes the score
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

score = 0
misses = 0

def show_score():
    pen.clear()
    pen.goto(-280, 250)
    pen.write(f"Score: {score}   Missed: {misses}/{MAX_MISSES}", font=("Arial", 16, "normal"))

def move_left():
    basket.setx(basket.xcor() - BASKET_STEP)

def move_right():
    basket.setx(basket.xcor() + BASKET_STEP)

def new_fruit(f):
    f.goto(random.randint(-250, 250), 280)

# 一个水果往下掉一步，再看看接住了没有、掉地上没有 / one fruit falls one step, then: caught? hit the ground?
def fall(f):
    global score, misses
    f.sety(f.ycor() - SPEED)
    if f.distance(basket.xcor(), basket.ycor()) < 40:   # 接住了！/ caught it!
        score += 1
        new_fruit(f)
    elif f.ycor() < -280:                              # 掉到地上了 / hit the ground
        misses += 1
        new_fruit(f)

def tick():
    fall(fruit)
    show_score()
    if misses < MAX_MISSES:
        screen.ontimer(tick, 50)               # 50 毫秒后再来一次 / again in 50 ms
    else:
        pen.goto(-120, 0)
        pen.write("GAME OVER", font=("Arial", 28, "bold"))

# TODO: def lose_life():

# TODO: def restart():

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
# TODO: 按空格 → restart / space → restart
screen.listen()
show_score()
tick()
