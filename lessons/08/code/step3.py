# ✊ 第 3 步：judge() 判断输赢 Step 3: judge() decides who wins
# 规则 Rules:  石头 赢 剪刀    剪刀 赢 布    布 赢 石头
#              rock beats scissors, scissors beat paper, paper beats rock
# 下面 6 个测试就是「说明书」：全部 ✅ 才算写对！
# The 6 tests below are the spec: all ✅ means you got it right!

def judge(me, computer):
    if me == computer:
        return "平"                     # tie
    # ✍️ TODO：你来写三种「赢」的情况（看规则表）/ you write the three "win" cases (see the table)

    return "输"                         # lose

# 🧪 测试小助手 / a little test helper
def test(me, computer, expected):
    result = judge(me, computer)
    if result == expected:
        print("✅", me, "vs", computer, "→", result)
    else:
        print("❌", me, "vs", computer, "→", result, " 应该是 / should be", expected)

test("石头", "剪刀", "赢")
test("剪刀", "布", "赢")
test("布", "石头", "赢")
test("石头", "布", "输")
test("剪刀", "石头", "输")
test("布", "布", "平")
