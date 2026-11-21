# 第 7 关参考答案 / Level 7 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
while not at_goal():
    if not wall_ahead():
        forward(60)
    elif not wall_left():
        left(90)
    else:
        right(90)
