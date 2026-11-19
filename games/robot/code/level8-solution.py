# 第 8 关参考答案 / Level 8 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def sweep_row():
    if gem_here():
        pick()
    while front_is_clear():
        move()
        if gem_here():
            pick()

def turn(side):
    if side == "left":
        turn_left()
    else:
        turn_right()

def next_row(side):
    turn(side)
    if not front_is_clear():
        return False
    move()
    turn(side)
    return True

side = "left"
sweep_row()
while next_row(side):
    sweep_row()
    if side == "left":
        side = "right"
    else:
        side = "left"
