# 🚀 第 2 关：Go / No-Go 天气窗口 / Level 2: Go / No-Go weather windows
# 窗口 i 的天气是 wind[i]、storm[i]、temp[i]（三个列表，每次运行都会变）
# Window i's weather is wind[i], storm[i], temp[i] (three lists that change every run)
# 规则（按这个顺序看）/ rules (check in this order):
#   storm 是 True → NO GO storm     wind > 40 → NO GO wind     temp < 0 → NO GO cold     否则 otherwise → GO
# 最后一行 / last line:  LAUNCH in window N（第一个 GO 的窗口 / the first GO window）或者 or  SCRUB

for i in range(len(wind)):
    if storm[i]:
        print(f"Window {i + 1}: NO GO storm")
    else:
        print(f"Window {i + 1}: GO")

# TODO 1: 加上风和冷的规则 / add the wind and cold rules
# TODO 2: 记住第一个 GO 的窗口，在循环外面打印最后一行 / remember the first GO window; print the last line after the loop
