# ✨ 给项目加一个标题画面 / Give your project a title screen
# 把 ___ 换成你的项目名字和昵称，运行看看。然后把这几行放进你的项目最前面！
# Replace ___ with your project name and nickname. Then put these lines at the top of your project!
# 标题用一只新海龟 title_pen 来写，不会和你项目里的 pen、t、basket 撞名。
# The title uses a new turtle, title_pen, so it won't clash with pen, t or basket in your project.
import turtle

screen = turtle.Screen()
screen.bgcolor("navy")

title_pen = turtle.Turtle()
title_pen.speed(0)
title_pen.hideturtle()
title_pen.penup()

title_pen.goto(0, 60)
title_pen.color("gold")
title_pen.write("___ 的项目", align="center", font=("Arial", 32, "bold"))

title_pen.goto(0, 0)
title_pen.color("white")
title_pen.write("作者 by：___", align="center", font=("Arial", 18, "normal"))

title_pen.goto(0, -60)
title_pen.color("lightgreen")
title_pen.write("先点一下画布再玩！ Click the canvas first!", align="center", font=("Arial", 16, "normal"))

# 3 秒（3000 毫秒）后自动擦掉标题，露出你的项目 / wipe the title after 3 seconds (3000 ms)
screen.ontimer(title_pen.clear, 3000)
