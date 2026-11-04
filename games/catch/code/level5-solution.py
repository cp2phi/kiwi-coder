# 🍎 第 5 关参考答案：两个水果 / Level 5 solution: two fruits
import turtle
import random

SPEED = 5
BASKET_STEP = 30
FRUIT_COLOUR = "red"
BASKET_COLOUR = "brown"
MAX_MISSES = 3

screen = turtle.Screen()
screen.bgcolor("lightblue")

basket = turtle.Turtle()
basket.shape("square")
basket.color(BASKET_COLOUR)
basket.penup()
basket.speed(0)
basket.goto(0, -250)

# 把「做一个水果」打包成函数 / pack "make a fruit" into a function
def make_fruit(colour):
    f = turtle.Turtle()
    f.shape("circle")
    f.color(colour)
    f.penup()
    f.speed(0)
    f.goto(random.randint(-250, 250), random.randint(280, 500))
    return f

fruit = make_fruit(FRUIT_COLOUR)
fruit2 = make_fruit("gold")

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

def fall(f):
    global score, misses
    f.sety(f.ycor() - SPEED)
    if f.distance(basket.xcor(), basket.ycor()) < 40:
        score += 1
        f.goto(random.randint(-250, 250), 280)
    elif f.ycor() < -280:
        misses += 1
        f.goto(random.randint(-250, 250), 280)

def tick():
    fall(fruit)
    fall(fruit2)
    show_score()
    if misses < MAX_MISSES:
        screen.ontimer(tick, 50)
    else:
        pen.goto(-120, 0)
        pen.write("GAME OVER", font=("Arial", 28, "bold"))

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()
show_score()
tick()
