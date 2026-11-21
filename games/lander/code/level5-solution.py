# 第 5 关参考答案 / Level 5 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def brake_distance(v):
    d = 0
    while v > 2:
        v = v - 2
        d = d + v
    return d

def autopilot(h, v, fuel):
    # 如果这一拍不点火，下一拍就太晚了吗？/ if I don't burn now, will it be too late next tick?
    return v > 2 and brake_distance(v + 1) + v + 1 >= h

print(brake_distance(10), "← 应该是 should be 20")
print(brake_distance(7), "← 应该是 should be 9")
fly(autopilot)
