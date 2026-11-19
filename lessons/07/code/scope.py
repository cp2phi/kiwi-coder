# 🔍 函数里的变量只住在函数里 Variables inside a function only live inside it
# 先猜：最后三行会打印什么？ Guess first: what do the last three lines print?

def boost(fuel):
    fuel = fuel * 2       # 这个 fuel 是函数自己的「本地」变量 / this fuel is the function's own local variable
    return fuel + 1

fuel = 3
x = boost(fuel)
y = boost(x)
print("fuel:", fuel)      # 外面的 fuel 变了吗？ did the outside fuel change?
print("x:", x)
print("y:", y)
