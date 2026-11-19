# 第 9 关参考答案 / Level 9 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
print("[" + orders + "]")

def run(orders):
    actions = {"m": move, "l": turn_left, "r": turn_right, "p": pick}
    for c in orders.lower():
        if c in actions:
            actions[c]()

run(orders)
