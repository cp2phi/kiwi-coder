# 第 4 关参考答案 / Level 4 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
for side in range(4):
    for step in range(5):
        move()
    pick()
    turn_left()
