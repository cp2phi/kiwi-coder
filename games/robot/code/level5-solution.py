# 第 5 关参考答案 / Level 5 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def grab_row():
    for i in range(5):
        move()
        pick()

grab_row()
turn_left()
move()
move()
turn_left()
grab_row()
turn_right()
move()
move()
turn_right()
grab_row()
