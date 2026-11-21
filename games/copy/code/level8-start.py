# 第 8 关：多边形排排队 / Level 8: polygon parade
# 三角形、正方形、五边形、六边形、七边形，边长都是 45 / triangle, square, pentagon, hexagon, heptagon, all with sides of 45
# 第一个从 (-255, -40) 开始，后面每个往右挪 115 / the first starts at (-255, -40), each next one starts 115 further right
# 起始代码只画了三角形。找规律：边数变了，什么跟着变？/ The starter only draws the triangle. Spot the pattern: when the number of sides changes, what else changes?
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

t.penup()
t.goto(-255, -40)
t.pendown()
for k in range(3):
    t.forward(45)
    t.left(120)
