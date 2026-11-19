# 🔁 热身：函数 + 列表 + random  Warm-up: functions + lists + random
# test-input: 3
# pick_many(n) 要「交回」一个装着 n 个随机水果的列表（第 7 课的「交回列表」！）
# pick_many(n) should return a list of n random fruits (Lesson 7's "return a list"!)
import random

fruits = ["kiwi", "feijoa", "apple", "mango"]

def pick_many(n):
    basket = []
    for i in range(n):
        ___                  # 👈 一行：往篮子里放一个随机水果 / one line: put a random fruit in the basket
    return basket

times = int(input("要几个？ how many? "))
my_basket = pick_many(times)
print(my_basket)
print("一共 / in total:", len(my_basket))
