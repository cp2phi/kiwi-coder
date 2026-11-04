secret = "ljxj"

result = ""
for c in secret:
    result = result + chr(ord(c) - 1)
print(result)
