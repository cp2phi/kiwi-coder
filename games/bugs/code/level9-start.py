# test-expect-error: KeyError
# 🐞 病号 9：观鸟记录（3 只 bug）/ Patient 9: the bird count (3 bugs)
# sightings 是观鸟的人随手记下的鸟名，每次运行都不一样（大小写乱、前后有空格）。
# sightings is a list of bird names the bird-watchers jotted down — different every run (messy capitals and spaces).
# count_birds 应该数出每种鸟见了几次（名字要洗干净：小写、没空格）；most_seen 应该找出见得最多的鸟。
# count_birds should count each bird (with clean names: lowercase, no spaces); most_seen should find the most-seen bird.
# 第一只 bug 会出红框，另外两只是安静的。医院还会用 2 份秘密记录测试你的函数。
# The first bug shows a red box; the other two are silent. The hospital also tests your functions with 2 secret lists.

def count_birds(names):
    counts = {}
    for name in names:
        bird = name
        if bird in counts:
            counts[bird] = 1
        else:
            counts[bird] = counts[bird] + 1
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
