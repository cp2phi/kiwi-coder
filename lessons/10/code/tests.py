# test-expect-error: AssertionError
# 🧪 让电脑帮你检查：assert  Let the computer check for you: assert
# assert 后面的话必须是 True，否则程序立刻报错——这就是「测试」
# What comes after assert must be True, or the program stops with an error — that's a "test"

def add(a, b):
    return a + b

def double(n):
    return n + n          # 两倍 = 自己加自己 / double = add it to itself

# 一串测试 / a row of tests
assert add(2, 3) == 5,      "2 + 3 应该是 5"
assert add(10, -4) == 6,    "10 - 4 应该是 6"
assert double(4) == 8,      "4 的两倍应该是 8"
assert double(0) == 0,      "0 的两倍应该是 0"
assert double(-3) == -6,    "-3 的两倍应该是 -6"
assert double(2.5) == 5,    "2.5 的两倍应该是 5"
assert double(3) == 6,      "3 的两倍应该是 6"

# 🐞 下面这个测试会失败——故意的！读一读报错，再想想怎么改
# 🐞 This test fails on purpose! Read the error, then decide what to fix
assert double(5) == 11,     "5 的两倍应该是 10 —— 咦，这个测试写对了吗？"

print("✅ 所有测试都通过了！/ All tests passed!")
