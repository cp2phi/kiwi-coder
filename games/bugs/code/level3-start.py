# test-expect-error: SyntaxError
# 🐞 病号 3：if 生病了 / Patient 3: a sick if
# 应该打印：/ It should print:
#   Year 6!
#   Done

age = 11
if age = 11
    print("Year 6!")
else:
    print("Not Year 6")
print("Done")
