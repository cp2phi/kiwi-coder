# 🐞 病号 8：存钱罐（安静的 bug）/ Patient 8: the piggy bank (silent bugs)
# weeks_to_save(goal, per_week)：每周存 per_week 元，要几周才能存够 goal 元？
# weeks_to_save(goal, per_week): saving per_week dollars a week, how many weeks to reach goal dollars?
# 比如 goal=10, per_week=3：3 → 6 → 9 → 12，第 4 周就够了，所以答案是 4。
# e.g. goal=10, per_week=3: 3 → 6 → 9 → 12, enough after week 4, so the answer is 4.
# 3 只 bug，没有红框——看输出找！医院还会用秘密数字测试你的函数。
# 3 bugs, no red box — read the output! The hospital also tests your function with secret numbers.

def weeks_to_save(goal, per_week):
    saved = 0
    weeks = 0
    safety = 0      # 🛟 安全绳：防止循环停不下来，别删！/ safety rope: stops an endless loop. Don't delete it!
    while saved != goal and safety < 1000:
        saved = saved + per_week
        safety = safety + 1
    weeks = weeks + 1
    return saved

print(weeks_to_save(10, 5))   # 应该是 2 / should be 2
print(weeks_to_save(10, 3))   # 应该是 4 / should be 4
print(weeks_to_save(7, 7))    # 应该是 1 / should be 1
