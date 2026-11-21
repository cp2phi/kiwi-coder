# 第 1 关参考答案 / Level 1 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
for leg in range(3):
    for step in range(10):
        if rock_ahead():
            break
        move()
    drill()
    turn_left()
