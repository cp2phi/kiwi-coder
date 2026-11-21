# 🔍 .strip() 和 .lower()：把乱七八糟的输入整理好 .strip() and .lower(): tidy messy input
# 先猜每一行打印什么，再运行！ Guess each line first, then run!

word = "  Rock  "
print("[" + word + "]")
print("[" + word.strip() + "]")          # 去掉两头的空格 / strip spaces off both ends
print("[" + word.lower() + "]")          # 全部变小写 / all lowercase
print("[" + word.strip().lower() + "]")  # 两个连着用 / both, one after the other
print("[" + word.strip().upper() + "]")  # 全部变大写 / all UPPERCASE

hello = "  Kia Ora  "
print("[" + hello.strip().lower() + "]") # 中间的空格呢？ what about the space in the middle?

answer = "YES"
answer.lower()                           # 🤔 这一行之后，answer 变了吗？ after this line, did answer change?
print(answer)
answer = answer.lower()                  # 要「存回去」才算！ you have to store it back!
print(answer)
