# test-input: 1
# test-expect-error: TypeError
# 📜 读报错进阶：标红的那一行，不一定是 bug 住的那一行！ Advanced: the red line isn't always where the bug lives!
# 先运行（随便输一个数，比如 1），读报错，再顺着「这个值是从哪来的？」往回找。
# Run it (type any number, e.g. 1), read the error, then follow "where did this value come from?" backwards.

def is_safe_landing(speed, drift):
    return speed <= 2 and drift <= 40          # ← 报错会标在这里 / the error points here

drift = 10
speed = input("落地速度是多少？/ Landing speed? ")
if is_safe_landing(speed, drift):              # ← speed 是从这里交进去的 / speed is handed over here
    print("🎉 安全着陆！/ Safe landing!")
else:
    print("💥 太快了！/ Too fast!")
