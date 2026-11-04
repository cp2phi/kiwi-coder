# ✨ 给项目加一个标题画面 / Give your project a title screen
# 把 ___ 换成你的项目名字和昵称，运行看看。然后把这几行放进你的项目最前面！
# Replace ___ with your project name and nickname. Then put these lines at the top of your project!
import turtle

screen = turtle.Screen()
screen.bgcolor("navy")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("gold")

pen.goto(0, 60)
pen.write("___ 的项目", align="center", font=("Arial", 32, "bold"))

pen.goto(0, 0)
pen.color("white")
pen.write("作者：___", align="center", font=("Arial", 18, "normal"))

pen.goto(0, -60)
pen.color("lightgreen")
pen.write("点一下画布，按方向键开始！", align="center", font=("Arial", 16, "normal"))
