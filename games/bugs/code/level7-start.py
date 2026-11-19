# 🐞 病号 7：成绩单（安静的 bug）/ Patient 7: the report card (silent bugs)
# 这次没有红框！程序能跑，但是答案是错的。有 3 只 bug。
# No red box this time! The program runs, but the answers are wrong. There are 3 bugs.
# 规则 / rules:  90 及以上 A，70–89 B，50–69 C，50 以下 F；50 及以上算及格（passed）
#                90 and up = A, 70–89 = B, 50–69 = C, under 50 = F; 50 and up counts as passed
# scores 是医院每次随机给的分数 / scores are random every run (the hospital gives them)

grades = []
for s in scores:
    passed = 0
    if s >= 50:
        grades.append("C")
    elif s >= 70:
        grades.append("B")
    elif s > 90:
        grades.append("A")
    else:
        grades.append("F")
    if s >= 50:
        passed = passed + 1

print("scores:", scores)
print("grades:", grades)
print("passed:", passed)
