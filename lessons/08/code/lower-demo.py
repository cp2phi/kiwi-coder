# 🔍 .lower() 和 .strip()：把乱七八糟的输入整理好 .lower() and .strip(): tidy messy input
# 先猜每一行打印什么，再运行！ Guess each line first, then run!

word = "  Rock  "
print("[" + word + "]")
print("[" + word.strip() + "]")          # 去掉两头的空格 / strip spaces off both ends
print("[" + word.lower() + "]")          # 全部变小写 / all lowercase
print("[" + word.strip().lower() + "]")  # 两个连着用 / both, one after the other
print("[" + word.strip().upper() + "]")  # 全部变大写 / all UPPERCASE

answer = "YES"
if answer.lower() == "yes":
    print("不管大小写，都算 yes！ Any capitals still count as yes!")
