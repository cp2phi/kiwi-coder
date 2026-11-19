# 🔁 热身：上节课的列表 + in + append / Warm-up: lists + in + append from last lesson
import random

planets = ["Mercury", "Venus", "Earth", "Mars"]
visited = []                                # 去过的行星 / planets visited so far

for i in range(3):
    p = random.choice(planets)
    if p in visited:
        print(f"🔁 {p} 去过了 / already visited")
    else:
        visited.append(p)
        print(f"🚀 飞往 Flying to {p}")

print(f"去过 {len(visited)} 颗 / visited {len(visited)}: {visited}")
