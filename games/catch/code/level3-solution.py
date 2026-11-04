# 🍎 第 3 关：换个颜色 / Level 3: new colours
# 任务：把 FRUIT_COLOUR 和 BASKET_COLOUR 都换成别的颜色 / Task: change FRUIT_COLOUR and BASKET_COLOUR to new colours


import turtle
import random

# ===== 可以改的数字和颜色 / Numbers and colours you can change =====
SPEED = 5              # 水果下落的速度 / how fast the fruit falls
BASKET_STEP = 30       # 篮子每按一次移动多少 / how far the basket moves per key press
FRUIT_COLOUR = "gold"   # 水果的颜色 / fruit colour
BASKET_COLOUR = "green"  # 篮子的颜色 / basket colour
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
pen.goto(-280, 250)

score = 0
misses = 0
game_started = True

def show_score():
    pen.clear()
    pen.write(f"Score: {score}   Missed: {misses}/{MAX_MISSES}", font=("Arial", 16, "normal"))

def move_left():
    basket.setx(basket.xcor() - BASKET_STEP)

def move_right():
    basket.setx(basket.xcor() + BASKET_STEP)

def new_fruit():
    fruit.goto(random.randint(-250, 250), 280)

def tick():
    global score, misses
    fruit.sety(fruit.ycor() - SPEED)          # 水果往下掉 / fruit falls
    if fruit.distance(basket.xcor(), basket.ycor()) < 40:   # 接住了！/ caught it!
        score += 1
        new_fruit()
    elif fruit.ycor() < -280:                  # 掉到地上了 / hit the ground
        misses += 1
        new_fruit()
    show_score()
    if misses < MAX_MISSES:
        screen.ontimer(tick, 50)               # 50 毫秒后再来一次 / again in 50 ms
    else:
        pen.goto(-120, 0)
        pen.write("GAME OVER", font=("Arial", 28, "bold"))

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()
show_score()
tick()
