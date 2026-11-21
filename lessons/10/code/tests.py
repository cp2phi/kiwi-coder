# test-expect-error: AssertionError
# 🧪 让电脑帮你检查：assert  Let the computer check for you: assert
# 三个太空项目里各拿一个「纯函数」：只吃数字、吐出答案，不碰海龟——最好测！
# One "pure function" from each space project: numbers in, answer out, no turtles — the easiest kind to test!

def is_safe_landing(speed, drift):      # 🚀 着陆安全吗？速度 ≤ 2 而且离中心 ≤ 40 / safe landing? speed ≤ 2 and drift ≤ 40
    return speed <= 2 and drift <= 40

def keep_inside(x):                     # ☄️ 别飞出画布 / don't fly off the screen
    if x > 270:
        return 270
    elif x < -270:
        return -270
    return x

def all_systems_go(checks):             # 🛰️ 每个系统都是 GO 吗？/ is every system GO?
    for system in checks:
        if checks[system] != "GO":
            return False
    return True

# 一排测试 / a row of tests
assert is_safe_landing(1, 10) == True,  "又慢又准 = 安全 / slow and centred = safe"
assert is_safe_landing(5, 10) == False, "太快 = 不安全 / too fast = unsafe"
assert is_safe_landing(2, 40) == True,  "刚好在边上也算安全 / exactly on the limit is still safe"
assert keep_inside(0) == 0,             "在中间不用动 / in the middle: no change"
assert keep_inside(-400) == -270,       "飞出左边要拉回来 / pulled back from the left"
assert all_systems_go({"燃料 fuel": "GO", "天气 weather": "GO"}) == True,     "全部 GO / all GO"
assert all_systems_go({"燃料 fuel": "GO", "天气 weather": "NO-GO"}) == False, "有一个 NO-GO 就不能发射 / one NO-GO = no launch"

# 🐞 下面这个测试会失败——故意的！读报错，再想想：是函数错了，还是测试错了？
# 🐞 This test fails on purpose! Read the error, then ask: is the function wrong, or the test?
assert keep_inside(300) == 300, "飞到 300 应该被拉回 270 —— 咦，这个测试写对了吗？/ 300 should be pulled back to 270 — is this test right?"

print("✅ 所有测试都通过了！/ All tests passed!")
