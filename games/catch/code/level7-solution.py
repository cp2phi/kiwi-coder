# 🍎 第 7 关参考答案：生命值 + 再来一局 / Level 7 solution: lives + play again
import turtle
import random

SPEED = 5
BASKET_STEP = 30
FRUIT_COLOUR = "red"
BASKET_COLOUR = "brown"
MAX_LIVES = 3          # 一开始有几条命 / lives at the start

screen = turtle.Screen()
screen.bgcolor("lightblue")

basket = turtle.Turtle()
basket.shape("square")
basket.color(BASKET_COLOUR)
basket.penup()
basket.speed(0)
basket.goto(0, -250)

fruit = turtle.Turtle()
fruit.shape("circle")
fruit.color(FRUIT_COLOUR)
fruit.penup()
fruit.speed(0)
fruit.goto(random.randint(-250, 250), 280)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

score = 0
lives = MAX_LIVES
game_over = False

def show_score():
    pen.clear()
    pen.goto(-280, 250)        # 每次都先回到左上角 / always go back to the top-left first
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

def new_fruit(f):
    f.goto(random.randint(-250, 250), 280)

def lose_life():
    global lives, game_over
    lives = lives - 1
    if lives <= 0:
        game_over = True       # 没命了 / out of lives

def fall(f):
    global score
    f.sety(f.ycor() - SPEED)
    if f.distance(basket.xcor(), basket.ycor()) < 40:
        score += 1
        new_fruit(f)
    elif f.ycor() < -280:
        lose_life()
        new_fruit(f)

def tick():
    if game_over:
        return                 # 游戏结束了：什么都不做，也不再约下一次 / game over: do nothing, don't book the next tick
    fall(fruit)
    show_score()
    if game_over:
        show_game_over()       # 这一下刚好没命了 / we just ran out of lives
    else:
        screen.ontimer(tick, 50)

def restart():
    global score, lives, game_over
    if not game_over:
        return                 # 游戏还在进行：按空格不算数 / game still running: space does nothing
    score = 0
    lives = MAX_LIVES
    game_over = False
    new_fruit(fruit)
    show_score()
    tick()                     # 重新启动心跳 / start the heartbeat again

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(restart, "space")
screen.listen()
show_score()
tick()
