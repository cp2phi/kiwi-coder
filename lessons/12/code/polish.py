# ✨ 给项目加一个标题画面：星空 + 任务名 / Give your project a title screen: a starfield + the mission name
# 把 ___ 换成你的项目名字和昵称，运行看看。然后把这几行放进你的项目最前面！
# Replace ___ with your project name and nickname. Then put these lines at the top of your project!
# 星星用 stars 画，标题用 title_pen 写——都是新海龟，不会和你项目里的 pen、hud、booster 撞名。
# Stars use stars, the title uses title_pen — new turtles that won't clash with pen, hud or booster in your project.
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

stars = turtle.Turtle()             # 星空：留在背景里 / the starfield stays in the background
stars.hideturtle()
stars.speed(0)
stars.penup()
for i in range(60):
    stars.goto(random.randint(-290, 290), random.randint(-290, 290))
    stars.dot(random.randint(1, 3), "white")

title_pen = turtle.Turtle()         # 标题：3 秒后擦掉 / the title: wiped after 3 seconds
title_pen.speed(0)
title_pen.hideturtle()
title_pen.penup()

title_pen.goto(0, 60)
title_pen.color("gold")
title_pen.write("🚀 ___", align="center", font=("Arial", 32, "bold"))

title_pen.goto(0, 10)
title_pen.color("white")
title_pen.write("任务指挥 Flight director：___", align="center", font=("Arial", 18, "normal"))

title_pen.goto(0, -50)
title_pen.color("lightgreen")
title_pen.write("先点一下画布再玩！ Click the canvas first!", align="center", font=("Arial", 16, "normal"))

# 3 秒（3000 毫秒）后自动擦掉标题，露出你的项目 / wipe the title after 3 seconds (3000 ms)
screen.ontimer(title_pen.clear, 3000)
