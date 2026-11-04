# 🔁 热身：函数 + 列表 + random 还记得吗？ Warm-up: functions + lists + random?
# test-input: 3
# 填好 ___，让招式「交回」一个随机的水果，然后打印 3 次
# Fill in ___ so the trick returns a random fruit, then print it 3 times
import random

fruits = ["kiwi", "feijoa", "apple", "mango"]

def pick():
    return ___.choice(fruits)      # 哪个工具箱有 choice？ which toolbox has choice?

times = int(input("要几个？ how many? "))
for i in range(___):               # 用上面的变量 / use the variable above
    print(pick())
