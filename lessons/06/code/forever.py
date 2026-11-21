# test-input: 发射成功 | 看到了月亮 | end
# ♾️ while True + break：太空日志 / while True + break: space log
# 不知道你要写几条日志，所以「永远重复」，直到你输入 end
# We don't know how many entries you'll write, so "repeat forever" until you type end
log = []

while True:
    entry = input("📝 写一条日志（输入 end 结束）/ Log entry (type end to finish): ")
    if entry == "end":
        break                   # 🛑 跳出循环 / jump out of the loop
    log.append(entry)

print(f"📒 一共 {len(log)} 条日志 / {len(log)} entries:")
for e in log:
    print("  -", e)
