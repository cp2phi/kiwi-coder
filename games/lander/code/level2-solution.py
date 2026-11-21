# 第 2 关参考答案 / Level 2 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
for i in range(1000):
    if landed():
        break
    if speed() > 2:
        step(True)
    else:
        step(False)
