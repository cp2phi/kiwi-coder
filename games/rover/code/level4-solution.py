# 第 4 关参考答案 / Level 4 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
while not at_base():
    if not rock_right():
        turn_right()
        move()
    elif not rock_ahead():
        move()
    else:
        turn_left()
