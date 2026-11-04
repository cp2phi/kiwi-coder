# test-input: 去南极看企鹅 | 学会滑板 | 养一只狗
# 🌠 愿望清单：用 append() 往列表里加东西 / Wish list: add things with append()

wishes = []                                  # 一开始是空的 / starts empty

for i in range(3):
    w = input("说一个愿望 / Tell me a wish: ")
    wishes.append(w)                         # 放进列表的最后 / add to the end

print(f"你一共有 {len(wishes)} 个愿望 / You have {len(wishes)} wishes:")
for i in range(len(wishes)):
    print(f"{i + 1}. {wishes[i]}")
