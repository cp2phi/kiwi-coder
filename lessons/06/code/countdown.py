# 🚀 倒计时：while = 条件还是 True 就一直重复 / Countdown: while = keep repeating while the condition is True
n = 5

while n > 0:        # 没到 0 就继续 / keep going until 0
    print(n)
    n = n - 1       # 每次减 1 —— 少了这行会怎样？/ take 1 away each time — what if this line is missing?

print("🚀 发射！Blast off!")
