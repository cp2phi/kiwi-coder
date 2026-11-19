# 🚀 第 4 关：修好 ready() / Level 4: fix ready()
# 上一个工程师写的 ready()：所有检查都是 "GO" 才交回 True。可是它有个 bug……
# The last engineer's ready(): it should return True only if EVERY check is "GO". But it has a bug...
def ready(checks):
    for c in checks:
        if c == "GO":
            return True
        else:
            return False

# 新任务：数一数有几个 "NO GO" / new job: count how many "NO GO" there are
def count_no_go(checks):
    return 0

# 🧪 自己的小测试 / your own little tests
print(ready(["GO", "GO", "GO"]), "← 应该是 should be True")
print(ready(["GO", "NO GO", "GO"]), "← 应该是 should be False")
print(count_no_go(["NO GO", "GO", "NO GO"]), "← 应该是 should be 2")
