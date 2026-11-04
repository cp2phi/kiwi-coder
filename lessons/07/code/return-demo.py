# ✨ 例 4：return = 招式做完「交回」一个结果 Example 4: return = the trick hands back a result
# 先猜每一行会打印什么，再运行！ Guess what each line prints, then run!

def double(n):
    return n * 2          # 把 n 的两倍交回去 / hand back twice n

def is_big(n):
    return n > 100        # 交回 True 或 False / hands back True or False

def greet(name):
    return f"Kia ora, {name}!"

print(double(5))
print(double(21))

answer = double(50)       # 交回来的结果可以存进变量 / the result can go in a variable
print(answer)

if is_big(answer):
    print(answer, "是个大数字 / is a big number")
else:
    print(answer, "是个小数字 / is a small number")

print(greet("Kiwi"))
print(greet("海龟"))
