# 第 1 关参考答案 / Level 1 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
for t in range(start, 0, -1):
    if t == engines:
        print(f"T-{t} ENGINES ON")
    elif t == poll:
        print(f"T-{t} POLL")
    else:
        print(f"T-{t}")
print("LIFTOFF!")
