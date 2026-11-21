# 🚀 发射控制 第 4 关：关卡代码（隐藏）/ Launch Control level 4: hidden setup
import random

_kc_print = print

# 准备一批隐藏的测试清单（每次运行都不一样）/ a batch of hidden test lists (different every run)
_kc_cases = [["GO"], ["NO GO"], ["GO", "GO", "GO"], ["GO", "NO GO", "GO"], ["NO GO", "GO", "GO"], ["GO", "GO", "NO GO"], ["NO GO", "NO GO"]]
for _n in range(8):
    _c = []
    for _k in range(random.randint(3, 8)):
        if random.randint(1, 4) == 1:
            _c.append("NO GO")
        else:
            _c.append("GO")
    _kc_cases.append(_c)
_c = []
for _k in range(random.randint(4, 8)):
    _c.append("GO")
_kc_cases.append(_c)

def _kc_call(fn, arg):
    # 调用孩子的函数；出错也不要让检查代码崩掉 / call the kid's function without letting an error crash the check
    try:
        return [True, fn(list(arg))]
    except Exception as e:
        return [False, str(e)]
