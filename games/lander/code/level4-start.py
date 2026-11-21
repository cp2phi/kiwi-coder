# 🛬 第 4 关：试飞报告 / Level 4: test-flight report
# results 是 16 次试飞的落地速度（每次运行都会变）。速度 <= SAFE（4）= 安全着陆。
# results holds the touchdown speeds of 16 test flights (new every run). Speed <= SAFE (4) = safe landing.
# 最后三行要打印 / the last three lines must be:
#   Safe: 12/16         ← 安全的有几次 / how many were safe
#   Worst: 9            ← 最大的速度（试试自己用循环找）/ the biggest speed (try finding it yourself with a loop)
#   Best streak: 6      ← 最多「连续」安全几次 / the most safe landings in a row

safe = 0
for s in results:
    # TODO
    pass
print(f"Safe: {safe}/{len(results)}")

# TODO: Worst
# TODO: Best streak
