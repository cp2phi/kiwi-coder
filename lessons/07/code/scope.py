# 🔍 函数里的变量只住在函数里 Variables inside a function only live inside it
# 先猜：最后会打印什么？ Guess first: what prints at the end?

def make_bigger(n):
    n = n * 10            # 这个 n 是函数里面的「本地」n / this n is the function's own local n
    print("函数里面 inside:", n)
    return n

n = 7
result = make_bigger(n)
print("函数外面 outside:", n)       # 外面的 n 变了吗？ did the outside n change?
print("交回来的 returned:", result)
