# 🔐 第 7 关参考答案 / Level 7 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
print("secret:", secret)
print("key:", key)

answer = ""
for c in secret:
    if c == " ":
        answer = answer + " "
    else:
        n = ord(c) - ord("a")
        n = (n - key) % 26
        answer = answer + chr(n + ord("a"))
print(answer)
