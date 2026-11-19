# 🐞 病号 7 参考答案 / Patient 7 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
grades = []
passed = 0
for s in scores:
    if s >= 90:
        grades.append("A")
    elif s >= 70:
        grades.append("B")
    elif s >= 50:
        grades.append("C")
    else:
        grades.append("F")
    if s >= 50:
        passed = passed + 1

print("scores:", scores)
print("grades:", grades)
print("passed:", passed)
