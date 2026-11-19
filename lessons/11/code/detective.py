# 🔍 print 侦探：没有报错，但答案不对！ Print detective: no error, but the answer is wrong!
# 助推器有 100 份燃料，点了 3 次火，分别用掉 30、25、20。最后应该剩 25。
# The booster has 100 fuel and burns 3 times: 30, 25 and 20. It should have 25 left.
# 任务：在循环里面加一行 print("现在 fuel 是", fuel)，看看每一圈发生了什么
# Task: add print("now fuel is", fuel) inside the loop and watch each round

burns = [30, 25, 20]
fuel = 100

for burn in burns:
    fuel = 100 - burn

print(f"剩余燃料 {fuel}")
