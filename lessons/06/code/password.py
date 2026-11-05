# test-input: kiwi | 12
# 🔐 秘密基地的门：and / or / not / The secret base door: and / or / not
password = input("密码 Password: ")
age = int(input("年龄 Age: "))

if password == "kiwi" and age >= 10:          # 两个都要对 / both must be true
    print("✅ 欢迎进入秘密基地！Welcome to the secret base!")
elif password == "kiwi" and not age >= 10:    # not：把 True 变 False / not flips True and False
    print("🙅 密码对了，但你还太小 / Right password, but too young")
else:
    print("❌ 密码错误 / Wrong password")

if age < 6 or age > 99:                       # 只要一个对就行 / just one needs to be true
    print("🤔 这个年龄……真的吗？/ That age… really?")
