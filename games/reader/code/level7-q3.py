total = 0
for i in range(1, 4):
    for j in range(1, 4):
        if j == i:
            break
        total = total + j
print(total)
