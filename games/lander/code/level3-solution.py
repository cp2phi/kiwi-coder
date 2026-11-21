# 第 3 关参考答案 / Level 3 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
while not landed():
    allowed = height() // 10 + 2       # 越高，允许的速度越大 / the higher you are, the faster you may fall
    if speed() > allowed:
        step(True)
    else:
        step(False)
