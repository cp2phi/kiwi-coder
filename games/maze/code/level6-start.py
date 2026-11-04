# 第 6 关：螺旋迷宫。规则：代码不能超过 6 行！/ Level 6: spiral maze. Rule: no more than 6 lines!
# 每一圈都比上一圈大 60 / each lap is 60 bigger than the last
for i in range(1, 5):
    forward(60 * i)
    left(90)
