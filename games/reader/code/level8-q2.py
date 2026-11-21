def grow(x):
    x = x + 10
    return x

x = 5
y = grow(grow(x))
print(x, y)
