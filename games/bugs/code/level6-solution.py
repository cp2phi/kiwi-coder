def double(n):
    return n * 2

count = 1
total = 0
while count <= 3:
    total = total + double(count)
    count += 1
print("Total:", total)
