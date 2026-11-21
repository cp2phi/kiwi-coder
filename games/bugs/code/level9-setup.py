# 🐞 虫虫医院 病号 9：隐藏代码（每次随机的观鸟记录）/ Bug Hospital patient 9: hidden setup (random bird sightings every run)
import random

_birds = ["kiwi", "tui", "kea", "weka", "pukeko", "fantail"]


def _messy(b):
    # 观鸟的人写字很乱：大小写不一样，前后还有空格 / the bird-watchers write messily: mixed capitals, extra spaces
    k = random.randint(0, 4)
    if k == 0:
        return b
    if k == 1:
        return b.upper()
    if k == 2:
        return b[0].upper() + b[1:]
    if k == 3:
        return " " + b
    return b + "  "


def _count(names):
    counts = {}
    for n in names:
        b = n.strip().lower()
        counts[b] = counts.get(b, 0) + 1
    return counts


def _top(counts):
    best = ""
    for b in counts:
        if counts[b] > counts.get(best, 0):
            best = b
    return best


def _make_list():
    # 保证「看到最多的鸟」只有一种 / make sure only one bird is the most seen
    while True:
        chosen = random.sample(_birds, 4)
        names = []
        for i in range(random.randint(9, 13)):
            names.append(_messy(random.choice(chosen)))
        c = _count(names)
        top = _top(c)
        ties = 0
        for b in c:
            if c[b] == c[top]:
                ties = ties + 1
        if ties == 1:
            return names


sightings = _make_list()
_sightings = sightings[:]
