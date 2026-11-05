# 🍎 第 6 关参考答案：金色水果 3 分 / Level 6 solution: gold fruit = 3 points
import turtle
import random

SPEED = 5
BASKET_STEP = 30
FRUITS = ["red", "gold", "purple"]   # 水果颜色列表 / list of fruit colours
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

fruit = turtle.Turtle()
fruit.shape("circle")
fruit.penup()
fruit.speed(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.goto(-280, 250)

score = 0
misses = 0

def new_fruit():
    fruit.color(random.choice(FRUITS))        # 每次随机一种颜色 / a random colour each time
    fruit.goto(random.randint(-250, 250), 280)

def bonus():
    # 金色水果值 3 分，其他 1 分 / gold is worth 3 points, others 1
    if fruit.pencolor() == "gold":
        return 3
    return 1

def show_score():
    pen.clear()
    pen.write(f"Score: {score}   Missed: {misses}/{MAX_MISSES}", font=("Arial", 16, "normal"))

def move_left():
    basket.setx(basket.xcor() - BASKET_STEP)

def move_right():
    basket.setx(basket.xcor() + BASKET_STEP)

def tick():
    global score, misses
    fruit.sety(fruit.ycor() - SPEED)
    if fruit.distance(basket.xcor(), basket.ycor()) < 40:
        score += bonus()
        new_fruit()
    elif fruit.ycor() < -280:
        misses += 1
        new_fruit()
    show_score()
    if misses < MAX_MISSES:
        screen.ontimer(tick, 50)
    else:
        pen.goto(-120, 0)
        pen.write("GAME OVER", font=("Arial", 28, "bold"))

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()
new_fruit()
show_score()
tick()
