# 第 6 关参考答案 / Level 6 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def is_go(reply):
    return reply.strip().lower() == "go"

def blockers(status):
    names = []
    for station in status:
        if not is_go(status[station]):
            names.append(station)
    return names

def director(status):
    names = blockers(status)
    if len(names) == 0:
        return "GO FOR LAUNCH"
    text = "HOLD: "
    for i in range(len(names)):
        if i > 0:
            text = text + ", "          # 第一个名字前面不加逗号 / no comma before the first name
        text = text + names[i]
    return text

print(blockers(status))
print(director(status))
