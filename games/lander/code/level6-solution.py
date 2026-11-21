# 第 6 关参考答案 / Level 6 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def landings(flights):
    counts = {}
    for f in flights:
        if f["landed"]:
            name = f["booster"]
            counts[name] = counts.get(name, 0) + 1
    return counts

def veteran(counts):
    best = ""
    for name in counts:
        if best == "" or counts[name] > counts[best]:
            best = name
    return best

counts = landings(flights)
print(counts)
print("🏅 Veteran:", veteran(counts))
