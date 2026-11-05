# 第 5 关：彩虹方形螺旋 / Level 5: a rainbow square spiral
# 60 圈，第 i 圈走 i * 4 步，每次左转 91 度 / 60 turns, step i goes i * 4, turn left 91 each time
# 颜色不算分，但很好看！/ colours don't count for the score, but they look great!
import turtle
t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "gold", "green", "blue", "purple"]

for i in range(60):
    t.color(colors[i % 6])
    t.forward(___)
    t.left(___)
