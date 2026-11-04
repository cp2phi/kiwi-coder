# 第 6 关参考答案 / Level 6 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
for i in range(1, 5):
    forward(60 * i)
    left(90)
    forward(60 * i)
    left(90)
