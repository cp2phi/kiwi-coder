# test-input: 去火星 | 学会滑板 | 去火星 | 养一只狗
# 🌠 愿望清单：在循环里一个一个加进列表 / Wish list: build a list one item at a time in a loop

wishes = []                                  # 一开始是空的 / starts empty

for i in range(4):
    w = input("说一个愿望 / Tell me a wish: ")
    wishes.append(w)                         # 放进列表的最后 / add to the end

print(f"你一共有 {len(wishes)} 个愿望 / You have {len(wishes)} wishes:")
for i in range(len(wishes)):
    print(f"{i + 1}. {wishes[i]}")
