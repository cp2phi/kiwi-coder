def check(n):
    for i in range(2, n):
        if n % i == 0:
            return "no"
    return "yes"

print(check(7), check(9), check(2))
