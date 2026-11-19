# 第 9 关参考答案（右手贴墙法）/ Level 9 solution (right-hand rule)
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def solve():
    steps = 0
    while not at_goal():
        if not wall_right():
            right(90)
            forward(60)
            steps += 1
        elif not wall_ahead():
            forward(60)
            steps += 1
        else:
            left(90)
    return steps

print("steps:", solve())
