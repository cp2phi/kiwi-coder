# 第 5 关参考答案 / Level 5 solution
# test-skip: 要和 setup/check 拼起来跑（已用 Playwright 验证过关）
def is_go(reply):
    return reply.strip().lower() == "go"

def poll(replies):
    no_go = 0
    for r in replies:
        if not is_go(r):
            no_go = no_go + 1
    if no_go == 0:
        return "GO FOR LAUNCH"
    return f"HOLD: {no_go} NO GO"

print(is_go(" GO "), "← 应该是 should be True")
print(is_go("No Go"), "← 应该是 should be False")
print(poll(["go", " No Go", "GO "]), "← 应该是 should be HOLD: 1 NO GO")
