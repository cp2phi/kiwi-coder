# 第 9 关：国际象棋棋盘——6 行 × 6 列，每格 40 / Level 9: a chessboard: 6 rows × 6 columns, each square 40
# 棋盘左下角在 (-120, -120)；最左下那一格是涂满的，然后涂满 / 空着轮流来 / the bottom-left corner is (-120, -120); the bottom-left square is filled, then filled / empty take turns
# 起始代码有一个会画「一格」的函数，但它还不会决定涂不涂 / the starter has a function that draws one square, but it can't decide whether to fill yet
import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("black", "crimson")    # 线是黑色，涂的颜色是红色 / black lines, crimson fill

def square(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()              # 开始涂色 / start filling
    for k in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()                # 涂好了 / done filling

# 现在只画了左下角那一格 / right now only the bottom-left square is drawn
square(-120, -120, 40)
