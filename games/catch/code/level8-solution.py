# 🍎 第 8 关参考答案：小心炸弹！/ Level 8 solution: watch out for bombs!
import turtle
import random

SPEED = 5
BASKET_STEP = 30
BASKET_COLOUR = "brown"
MAX_LIVES = 3
KINDS = ["red", "gold", "limegreen", "black"]   # black = 炸弹 / bomb（4 个里 1 个是炸弹 / 1 in 4 is a bomb）
HOW_MANY = 3                                    # 同时掉几个 / how many fall at once

screen = turtle.Screen()
screen.bgcolor("lightblue")

basket = turtle.Turtle()
basket.shape("square")
basket.color(BASKET_COLOUR)
basket.penup()
basket.speed(0)
basket.goto(0, -250)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

score = 0
lives = MAX_LIVES
game_over = False

def is_bomb(f):
    return f.pencolor() == "black"

def new_thing(f):
    # 随机换一种（可能是炸弹），放回天上 / pick a random kind (maybe a bomb) and put it back in the sky
    f.color(random.choice(KINDS))
    f.goto(random.randint(-250, 250), random.randint(280, 500))

def make_thing():
    f = turtle.Turtle()
    f.shape("circle")
    f.penup()
    f.speed(0)
    new_thing(f)
    return f

things = []
for i in range(HOW_MANY):
    things.append(make_thing())

def show_score():
    pen.clear()
    pen.goto(-280, 250)
    pen.write(f"Score: {score}   Lives: {lives}", font=("Arial", 16, "normal"))

def show_game_over():
    pen.goto(-160, 0)
    pen.write("GAME OVER", font=("Arial", 28, "bold"))
    pen.goto(-160, -40)
    pen.write("按空格再来一局 / Space = play again", font=("Arial", 14, "normal"))

def move_left():
    basket.setx(basket.xcor() - BASKET_STEP)

def move_right():
    basket.setx(basket.xcor() + BASKET_STEP)

def lose_life():
    global lives, game_over
    lives = lives - 1
    if lives <= 0:
        game_over = True

def fall(f):
    global score
    f.sety(f.ycor() - SPEED)
    if f.distance(basket.xcor(), basket.ycor()) < 40:   # 碰到篮子 / touched the basket
        if is_bomb(f):
            lose_life()          # 接到炸弹：少一条命 / caught a bomb: lose a life
        else:
            score += 1           # 接到水果：加分 / caught a fruit: +1
        new_thing(f)
    elif f.ycor() < -280:                              # 掉到地上 / hit the ground
        if not is_bomb(f):
            lose_life()          # 漏掉水果才扣命；躲开炸弹没事 / only a missed fruit costs a life; dodging a bomb is fine
        new_thing(f)

def tick():
    if game_over:
        return
    for f in things:             # 每一个都掉一步 / every thing falls one step
        fall(f)
    show_score()
    if game_over:
        show_game_over()
    else:
        screen.ontimer(tick, 50)

def restart():
    global score, lives, game_over
    if not game_over:
        return
    score = 0
    lives = MAX_LIVES
    game_over = False
    for f in things:
        new_thing(f)
    show_score()
    tick()

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(restart, "space")
screen.listen()
show_score()
tick()
