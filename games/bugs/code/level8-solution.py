# 🐞 病号 8 参考答案 / Patient 8 solution
# test-skip: 要和 check 拼起来跑（已用 Playwright 验证过关）
def weeks_to_save(goal, per_week):
    saved = 0
    weeks = 0
    safety = 0
    while saved < goal and safety < 1000:
        saved = saved + per_week
        safety = safety + 1
        weeks = weeks + 1
    return weeks

print(weeks_to_save(10, 5))
print(weeks_to_save(10, 3))
print(weeks_to_save(7, 7))
