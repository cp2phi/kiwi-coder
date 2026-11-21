# 🚀 太空报数：% 余数 + elif 的顺序 Space Fizz: % remainder + the order of elif
# % 是「除完以后剩几」：7 % 3 → 1，9 % 3 → 0（0 = 刚好整除！）
# % means "what's left after dividing": 7 % 3 → 1, 9 % 3 → 0 (0 = divides exactly!)
for i in range(1, 16):
    if i % 15 == 0:                 # 3 和 5 都能整除 / divides by both 3 and 5
        print(f"{i} 🚀⭐ 火箭加星星！Rocket-star!")
    elif i % 3 == 0:                # 3 的倍数 / every 3rd number
        print(f"{i} 🚀")
    elif i % 5 == 0:                # 5 的倍数 / every 5th number
        print(f"{i} ⭐")
    else:
        print(i)
