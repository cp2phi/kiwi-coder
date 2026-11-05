# 🔺 两个变量画图形  Two variables, one shape
# 把 ___ 填好：side 是边长，turn 是每次转的角度  Fill in the blanks: side = length, turn = angle each time
# 提示：三角形每次转 120，正方形转 90  Hint: a triangle turns 120, a square turns 90

import turtle

t = turtle.Turtle()
t.color("orange")
t.pensize(4)

side = 80
turn = ___

t.forward(side)
t.left(turn)
t.forward(side)
t.left(turn)
t.forward(side)
t.left(turn)
t.forward(side)
t.left(turn)
