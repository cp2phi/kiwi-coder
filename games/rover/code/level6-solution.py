# 第 6 关参考答案 / Level 6 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
print("route =", route)

def drive(route):
    for c in route:
        if c == "F":
            move()
        elif c == "L":
            turn_left()
        elif c == "R":
            turn_right()

def reverse_route(route):
    swap = {"F": "F", "L": "R", "R": "L"}
    back = "LL"                       # 先掉头 / turn around first
    for c in route[::-1]:             # 倒着读 / read it backwards
        back = back + swap[c]
    return back

drive(route)
collect()
drive(reverse_route(route))
