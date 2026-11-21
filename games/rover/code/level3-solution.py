# 第 3 关参考答案 / Level 3 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
while not at_base():
    if rock_ahead():
        turn_left()
        move()
        turn_right()
        move()
        while rock_right():
            move()
        turn_right()
        move()
        turn_left()
    else:
        move()
