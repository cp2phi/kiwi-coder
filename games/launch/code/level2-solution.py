# 第 2 关参考答案 / Level 2 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
first = 0                      # 0 = 还没找到 GO / no GO window found yet
for i in range(len(wind)):
    if storm[i]:
        print(f"Window {i + 1}: NO GO storm")
    elif wind[i] > 40:
        print(f"Window {i + 1}: NO GO wind")
    elif temp[i] < 0:
        print(f"Window {i + 1}: NO GO cold")
    else:
        print(f"Window {i + 1}: GO")
        if first == 0:
            first = i + 1

if first > 0:
    print(f"LAUNCH in window {first}")
else:
    print("SCRUB")
