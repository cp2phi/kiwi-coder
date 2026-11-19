# 🔐 第 9 关参考答案 / Level 9 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
print(code_book)
print("[" + secret + "]")

def decode(text, book):
    # 先把密码本反过来：密码字母 → 真字母 / flip the book first: secret letter → real letter
    back = {}
    for real in book:
        back[book[real]] = real
    result = ""
    for c in text.strip().lower():
        if c in back:
            result = result + back[c]
        else:
            result = result + c
    return result

print(decode(secret, code_book))
