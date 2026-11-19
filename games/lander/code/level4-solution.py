# 第 4 关参考答案 / Level 4 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
safe = 0
worst = 0
streak = 0          # 现在连着几次安全 / safe in a row right now
best = 0            # 最长的一串 / the longest run so far
for s in results:
    if s > worst:
        worst = s
    if s <= SAFE:
        safe = safe + 1
        streak = streak + 1
        if streak > best:
            best = streak
    else:
        streak = 0
print(f"Safe: {safe}/{len(results)}")
print(f"Worst: {worst}")
print(f"Best streak: {best}")
