# 🌀 一直画到边上为止 / Keep drawing until the edge
# while 不只能数数：这里是「海龟离中间还不到 250 就继续」
# while isn't just for counting: here it's "keep going while the turtle is less than 250 from the middle"
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.color("deepskyblue")

step = 5
while t.distance(0, 0) < 250:
    t.forward(step)
    t.left(30)
    step = step + 2      # 每次走得更远一点 / go a little further each time

t.write("到边上了！Made it!", font=("Arial", 16, "bold"))
