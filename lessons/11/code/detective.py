# 🔍 print 侦探：没有报错，但答案不对！ Print detective: no error, but the answer is wrong!
# 买了 3 样东西：3 元、5 元、2 元，一共应该是 10 元。
# Three things cost 3, 5 and 2 dollars. The total should be 10.
# 任务：在循环里面加一行 print("现在 total 是", total)，看看每一圈发生了什么
# Task: add print("now total is", total) inside the loop and watch each round

prices = [3, 5, 2]
total = 0

for price in prices:
    total = price

print(f"一共 {total} 元")
