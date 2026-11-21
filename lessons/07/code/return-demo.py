# ✨ 例 4：return = 招式做完「交回」一个结果 Example 4: return = the trick hands back a result
# 先在纸上写下每一行会打印什么，再运行！ Write down what each line prints first, then run!

def double(n):
    return n * 2          # 把 n 的两倍交回去 / hand back twice n

def is_big(n):
    return n > 100        # 交回 True 或 False / hands back True or False

def bigger(a, b):
    if a > b:
        return a          # return 之后，招式马上结束 / after return, the trick ends at once
    return b

print(double(5))
answer = double(double(30))      # 先算里面的，再算外面的 / inside first, then outside
print(answer)
print(is_big(answer))

if is_big(double(40)):           # 交回的 True / False 直接放进 if / the True / False goes straight into the if
    print("80 很大 / 80 is big")
else:
    print("80 不大 / 80 is not big")

print(bigger(7, 12), bigger(double(7), 12))
