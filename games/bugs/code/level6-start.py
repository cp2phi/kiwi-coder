# test-expect-error: TypeError
# 🐞 病号 6：两个 bug 的重病号 / Patient 6: a serious case with two bugs
# 应该打印：/ It should print:
#   Total: 12
# （2 + 4 + 6 = 12）小心：治好第一个 bug 以后，程序可能停不下来——点「■ 停下」，再找第二个！
# Careful: after you fix the first bug, the program might never stop — click "■ Stop" and find bug number two!

def double(n):
    n * 2

count = 1
total = 0
while count <= 3:
    total = total + double(count)
print("Total:", total)
