# 🏆 挑战：一朵花 Challenge: a flower
# 一个圆重复很多次，每次转一点点，就变成花瓣！ / A circle repeated, turning a little each time, becomes petals!
# 把 ___ 填好。提示：转的角度 × 次数 = 360 / Fill in ___. Hint: angle × times = 360
import turtle

t = turtle.Turtle()
t.speed(0)
t.color("hotpink")

for i in range(___):
    t.circle(70)          # 画一个圆 / draw a circle
    t.left(___)           # 转一点点 / turn a little

# 🌟 再加一个循环，在黑夜里画满星星？用 t.penup() t.goto(x, y) t.pendown() 到处跑
# 🌟 Add another loop to fill the sky with stars? Use t.penup() t.goto(x, y) t.pendown() to jump around
