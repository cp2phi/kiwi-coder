# 第 8 关参考答案 / Level 8 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
print(heights)

def tooth(h):
    left(90)
    forward(h)
    right(90)
    forward(50)
    right(90)
    forward(h)
    left(90)
    forward(50)

for h in heights:
    tooth(h)
