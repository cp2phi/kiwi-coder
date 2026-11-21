# 🐞 病号 9 参考答案 / Patient 9 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def count_birds(names):
    counts = {}
    for name in names:
        bird = name.strip().lower()
        if bird in counts:
            counts[bird] = counts[bird] + 1
        else:
            counts[bird] = 1
    return counts

def most_seen(counts):
    best = ""
    for bird in counts:
        if counts[bird] > counts.get(best, 0):
            best = bird
    return best

print(sightings)
counts = count_birds(sightings)
print(counts)
print("Most seen:", most_seen(counts))
