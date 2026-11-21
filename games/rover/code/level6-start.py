# 🛰️ 第 6 关：原路返回 / Level 6: retrace the route
# route 是一串指令，比如 "FFLFRFF"：F 往前一格，L 左转，R 右转（每次运行都不一样，看输出）
# route is a string of commands like "FFLFRFF": F = forward one cell, L = turn left, R = turn right (new every run — see the output)
# 任务：照 route 开到样本那里 → collect() → 沿原路开回基地 H（路旁有石头，抄近路会撞！）
# Job: follow route to the sample → collect() → retrace the route back to base H (rocks beside the road: shortcuts crash!)
print("route =", route)

def drive(route):
    # TODO: 一个字母一个字母地读，F → move()，L → turn_left()，R → turn_right()
    # TODO: read one letter at a time: F → move(), L → turn_left(), R → turn_right()
    pass

def reverse_route(route):
    # TODO: 交回回家的路线：先掉头 "LL"，再把 route 倒过来，L 和 R 对调（用字典！）
    # TODO: return the route home: turn around "LL" first, then route backwards with L and R swapped (use a dictionary!)
    swap = {"F": "F", "L": "R", "R": "L"}
    back = "LL"
    return back

drive(route)
collect()
drive(reverse_route(route))
