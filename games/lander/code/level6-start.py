# 🛬 第 6 关：助推器机队 / Level 6: the booster fleet
# flights 是一年的飞行记录，每一次飞行是一个字典（每次运行都会变）：
# flights is a year of flights; each flight is a dictionary (new every run):
#   {"booster": "B-Kea", "landed": True}     ← 哪枚助推器 / which booster;  有没有成功落回来 / did it land back safely
print(flights[0])
print(flights[1])

def landings(flights):
    # TODO: 交回一个字典：助推器名字 → 成功落地几次（landed 是 False 的不算）
    # TODO: return a dictionary: booster name → how many safe landings (skip landed False)
    counts = {}
    return counts

def veteran(counts):
    # TODO: 交回落地次数最多的那个名字 / return the name with the most landings
    return ""

counts = landings(flights)
print(counts)
print("🏅 Veteran:", veteran(counts))
