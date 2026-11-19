# ☄️ 参考答案 B：陨石大躲避 v1（3 个必做功能都做好了）Reference B: Asteroid Dodger v1 (all 3 must-haves done)
# 给老师看的 / for the teacher
# 玩法：先点一下画布。用 ← → 开飞船，躲开掉下来的陨石！每躲过一颗得 1 分。
# How to play: click the canvas first. Fly the ship with ← → and dodge the falling asteroids! 1 point per asteroid dodged.
import turtle
import random

# ===== 设置 settings（改这些数字最好玩！/ the most fun numbers to change!）=====
SHIP_STEP = 30        # 飞船每按一次移动多少 / how far the ship moves per key press
ROCK_COUNT = 3        # 同时有几颗陨石 / how many asteroids at once
START_SPEED = 3       # 陨石一开始的速度 / starting asteroid speed
MAX_SPEED = 10        # 陨石最快多快 / top asteroid speed
EDGE = 270            # 飞船最远能到哪 / how far out the ship may go
LIVES = 3             # 几条命 / number of lives

# ===== 纯函数 pure functions：只算数字，不碰海龟 → 最好测试 / numbers only, no turtles → easy to test =====
def hit(ax, ay, bx, by):                # 两个东西撞上了吗？/ have two things crashed?
    return abs(ax - bx) < 25 and abs(ay - by) < 25     # abs() 去掉负号 / abs() drops the minus sign

def keep_inside(x):                     # 不让飞船飞出画布 / keep the ship on the screen
    if x > EDGE:
        return EDGE
    elif x < -EDGE:
        return -EDGE
    return x

def speed_for(score):                   # 分数越高，陨石越快 / the higher the score, the faster the rocks
    speed = START_SPEED + score / 10
    if speed > MAX_SPEED:
        return MAX_SPEED
    return speed

def test():                             # 🧪 小测试：开始前先检查 / tiny tests before we start
    assert hit(0, 0, 10, 10) == True, "离得很近 = 撞上 / very close = crash"
    assert hit(0, 0, 100, 0) == False, "离得很远 = 没撞 / far apart = safe"
    assert keep_inside(0) == 0
    assert keep_inside(400) == EDGE, "飞出右边要拉回来 / pulled back from the right"
    assert keep_inside(-400) == -EDGE, "飞出左边要拉回来 / pulled back from the left"
    assert keep_inside(EDGE) == EDGE, "刚好在边上不用动 / exactly on the edge stays"
    assert speed_for(0) == START_SPEED
    assert speed_for(20) == START_SPEED + 2
    assert speed_for(1000) == MAX_SPEED, "再快也有上限 / there's a top speed"

# ===== 画面 the scene =====
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()                   # 画星星 / draws the stars
pen.hideturtle()
pen.speed(0)
pen.penup()
for i in range(40):
    pen.goto(random.randint(-290, 290), random.randint(-290, 290))
    pen.dot(random.randint(1, 3), "white")

ship = turtle.Turtle()                  # 飞船 / the ship
ship.shape("triangle")
ship.color("deepskyblue")
ship.setheading(90)
ship.penup()
ship.speed(0)
ship.goto(0, -250)

def make_rock():                        # 做一颗陨石，放在画布上面 / make one asteroid above the screen
    rock = turtle.Turtle()
    rock.shape("circle")
    rock.color("sienna")
    rock.penup()
    rock.speed(0)
    rock.goto(random.randint(-EDGE, EDGE), random.randint(300, 600))
    return rock

rocks = []                              # 所有陨石放在一个列表里 / all asteroids in one list
for i in range(ROCK_COUNT):
    rocks.append(make_rock())

hud = turtle.Turtle()                   # 写分数的笔 / the pen for the score
hud.hideturtle()
hud.speed(0)
hud.penup()
hud.color("white")

# ===== 记住的数字 what the game remembers =====
score = 0
lives = LIVES

def show_hud():
    hud.clear()
    hud.goto(-280, 260)
    hud.write(f"分数 score {score}   命 lives {lives}", font=("Arial", 14, "normal"))

def go_left():                          # ← 键 / left key
    ship.setx(keep_inside(ship.xcor() - SHIP_STEP))

def go_right():                         # → 键 / right key
    ship.setx(keep_inside(ship.xcor() + SHIP_STEP))

def tick():                             # 游戏心跳：每 50 毫秒一次 / the game heartbeat, every 50 ms
    global score, lives
    speed = speed_for(score)
    for rock in rocks:                          # 每一颗陨石都动一下 / move every asteroid
        rock.sety(rock.ycor() - speed)
        if rock.ycor() < -300:                  # 躲过了一颗！/ dodged one!
            score = score + 1
            rock.goto(random.randint(-EDGE, EDGE), random.randint(300, 450))
        if hit(ship.xcor(), ship.ycor(), rock.xcor(), rock.ycor()):    # 撞上了！/ crash!
            lives = lives - 1
            rock.goto(random.randint(-EDGE, EDGE), random.randint(300, 450))
    show_hud()
    if lives > 0:
        screen.ontimer(tick, 50)                # 还有命：下一拍 / lives left: next beat
    else:
        hud.goto(0, 0)
        hud.color("red")
        hud.write(f"GAME OVER  分数 score {score}", align="center", font=("Arial", 26, "bold"))

test()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.listen()
tick()
