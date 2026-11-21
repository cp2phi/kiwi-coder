# 第 4 关参考答案 / Level 4 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def ready(checks):
    for c in checks:
        if c != "GO":
            return False       # 发现一个不行就够了 / one bad check is enough
    return True                # 全部看完都没问题 / looked at all of them: all fine

def count_no_go(checks):
    count = 0
    for c in checks:
        if c == "NO GO":
            count = count + 1
    return count

print(ready(["GO", "GO", "GO"]), "← 应该是 should be True")
print(ready(["GO", "NO GO", "GO"]), "← 应该是 should be False")
print(count_no_go(["NO GO", "GO", "NO GO"]), "← 应该是 should be 2")
