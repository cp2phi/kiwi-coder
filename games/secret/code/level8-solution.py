# 🔐 第 8 关参考答案 / Level 8 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def decode(text):
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result = text[i] + result
    return result

print(decode("ipwbiqky"))
print(decode(secret))
