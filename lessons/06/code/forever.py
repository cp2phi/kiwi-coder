# ♾️ 这个程序想永远跑下去…… / This program wants to run forever…
# while True 永远是 True，所以永远不停。只有 break 能救它。
# while True is always True, so it never stops. Only break can save it.
count = 0

while True:
    count = count + 1
    print("我停不下来！I can't stop!", count)
    if count == 10:
        break           # 🛑 跳出循环 / jump out of the loop

print("呼～ break 救了我 / Phew, break saved me")

# 试试：把 if 和 break 那两行删掉，运行，再点红色的「■ 停下」
# Try: delete the if and break lines, run it, then click the red "■ Stop"
