# 第 9 关参考答案 / Level 9 solution
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("black", "crimson")

def square(x, y, size, filled):
    t.penup()
    t.goto(x, y)
    t.pendown()
    if filled:                  # 只有要涂的格子才涂 / only fill when asked
        t.begin_fill()
    for k in range(4):
        t.forward(size)
        t.left(90)
    if filled:
        t.end_fill()

for row in range(6):            # 第几行（从下往上）/ which row (bottom to top)
    for col in range(6):        # 第几列（从左往右）/ which column (left to right)
        x = -120 + col * 40
        y = -120 + row * 40
        filled = (row + col) % 2 == 0   # 行 + 列是双数就涂 / fill when row + column is even
        square(x, y, 40, filled)
