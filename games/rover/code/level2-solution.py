# 第 2 关参考答案 / Level 2 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
for side in range(4):
    for step in range(10):
        if sample_here():
            collect()
        if rock_ahead():
            break
        move()
    turn_left()
