# 第 6 关参考答案 / Level 6 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def go(n):
    for i in range(n):
        move()

go(3)
pick()
turn_left()
go(3)
pick()
turn_left()
go(3)
pick()
turn_right()
go(3)
pick()
turn_right()
go(6)
pick()
turn_right()
go(4)
pick()
