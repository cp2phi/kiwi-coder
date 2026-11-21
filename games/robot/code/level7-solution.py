# 第 7 关参考答案 / Level 7 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
for side in range(4):
    while front_is_clear():
        move()
        if gem_here():
            pick()
    turn_left()
