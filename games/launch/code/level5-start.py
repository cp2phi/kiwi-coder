# 🚀 第 5 关：无线电点名 / Level 5: radio poll
# 每个岗位用无线电回答 "go" 或 "no go"，可是大小写乱七八糟，前后还有空格：" Go"、"NO GO "……
# Every station radios back "go" or "no go", but with messy capitals and extra spaces: " Go", "NO GO "...

def is_go(reply):
    # TODO: 先整理一下 reply（strip、lower），再判断 / tidy reply up first (strip, lower), then decide
    return reply == "go"

def poll(replies):
    # TODO: 用 is_go 数一数有几个不是 go / use is_go to count the ones that aren't go
    # 全是 go → "GO FOR LAUNCH"；否则 → "HOLD: 2 NO GO"（数字是不是 go 的个数）
    # all go → "GO FOR LAUNCH"; otherwise → "HOLD: 2 NO GO" (the number of non-go replies)
    return "GO FOR LAUNCH"

# 🧪 自己的小测试 / your own little tests
print(is_go(" GO "), "← 应该是 should be True")
print(is_go("No Go"), "← 应该是 should be False")
print(poll(["go", " No Go", "GO "]), "← 应该是 should be HOLD: 1 NO GO")
