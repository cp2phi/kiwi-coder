# 🐞 热身：这段程序生了 3 个 bug，把它治好！ Warm-up: this program has 3 bugs, cure it!
# test-expect-error: SyntaxError
# 目标：运行后要打印出 / Goal: it should print
#   猎鹰 9 号 加了 3 次燃料
#   可以发射！

rocket = "猎鹰 9 号"
fuel = 0

for i in range(3)
    fuel = fuel + 1

print(f"{rokcet} 加了 {fuel} 次燃料")

if fuel = 3:
    print("可以发射！")
