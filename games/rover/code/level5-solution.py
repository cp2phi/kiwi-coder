# 第 5 关参考答案 / Level 5 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def sweep_row():
    if sample_here():
        collect()
    while not rock_ahead():
        move()
        if sample_here():
            collect()

def u_turn(side):
    if side == "left":
        turn_left()
    else:
        turn_right()
    if rock_ahead():
        return False          # 上面没有排了：扫完了 / no more rows: finished
    move()
    if side == "left":
        turn_left()
    else:
        turn_right()
    return True

side = "left"
sweep_row()
while u_turn(side):
    sweep_row()
    if side == "left":
        side = "right"
    else:
        side = "left"
