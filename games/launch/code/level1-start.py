# 🚀 第 1 关：倒计时 / Level 1: countdown
# start、poll、engines 每次运行都会变（看输出最上面那行 📡）
# start, poll and engines change on every run (see the 📡 line at the top of the output)
# 要打印 / print:  T-start ... T-1，最后 LIFTOFF!
#   T-poll 那一行写成 / the T-poll line reads:        T-7 POLL
#   T-engines 那一行写成 / the T-engines line reads:  T-3 ENGINES ON
# 下面是昨天的程序：从 1 数到 10，方向反了，还写死了 10 🙈
# Below is yesterday's program: it counts 1 to 10 — wrong way round, and 10 is typed in 🙈

for t in range(1, 11):
    print(f"T-{t}")
print("LIFTOFF!")
