# 🍎 第 8 关：小心炸弹！/ Level 8: watch out for bombs!
# 这是第 7 关的答案。现在要同时掉 3 个东西，而且有的是炸弹（黑色）/ This is level 7's answer. Now 3 things fall at once, and some are bombs (black)
# 任务 / Task:
#   ① 做一个列表 things，用循环放进 3 个 make_thing() / make a list things and use a loop to put 3 make_thing() in it
#   ② tick() 里让 things 里的每一个都 fall / in tick(), make every thing in things fall
#   ③ 改 fall(f)，四种情况四种结果 / change fall(f): four cases, four results
#        接到水果 +1 分 · 接到炸弹 -1 命 · 漏掉水果 -1 命 · 躲开炸弹 没事
#        catch a fruit +1 point · catch a bomb -1 life · miss a fruit -1 life · dodge a bomb nothing happens
#   ④ restart() 里把每一个都放回天上 / in restart(), put every thing back in the sky


import turtle
import random

SPEED = 5
BASKET_STEP = 30
BASKET_COLOUR = "brown"
MAX_LIVES = 3
KINDS = ["red", "gold", "limegreen", "black"]   # black = 炸弹 / bomb（4 个里 1 个是炸弹 / 1 in 4 is a bomb）

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

# 是炸弹吗？/ is it a bomb?
def is_bomb(f):
    return f.pencolor() == "black"

# 随机换一种（可能是炸弹），放回天上 / pick a random kind (maybe a bomb) and put it back in the sky
def new_thing(f):
    f.color(random.choice(KINDS))
    f.goto(random.randint(-250, 250), random.randint(280, 500))

# 做一个会掉的东西 / make one falling thing
def make_thing():
    f = turtle.Turtle()
    f.shape("circle")
    f.penup()
    f.speed(0)
    new_thing(f)
    return f

fruit = make_thing()
# TODO ①: things = …

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
        score += 1               # TODO ③: 炸弹呢？/ what about bombs?
        new_thing(f)
    elif f.ycor() < -280:                              # 掉到地上 / hit the ground
        lose_life()              # TODO ③: 炸弹呢？/ what about bombs?
        new_thing(f)

def tick():
    if game_over:
        return
    fall(fruit)                  # TODO ②
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
    new_thing(fruit)             # TODO ④
    show_score()
    tick()

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(restart, "space")
screen.listen()
show_score()
tick()
