# 第 1 关参考答案 / Level 1 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
for tick in range(1, 60):
    speed = speed + g
    height = height - speed
    draw(height)
    if height <= 0:
        print(f"Touchdown at tick {tick}, speed {speed}")
        break
