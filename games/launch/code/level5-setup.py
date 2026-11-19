# 🚀 发射控制 第 5 关：关卡代码（隐藏）/ Launch Control level 5: hidden setup
import random

_kc_print = print

def _kc_messy(word):
    # 把 "go" / "no go" 变成乱七八糟的样子：随机大小写 + 随机空格
    # make "go" / "no go" messy: random capitals + random spaces
    s = ""
    for ch in word:
        if random.randint(0, 1) == 1:
            s = s + ch.upper()
        else:
            s = s + ch
    return " " * random.randint(0, 2) + s + " " * random.randint(0, 2)

# is_go 的测试：固定几个难的 + 随机的 / tests for is_go: some tricky fixed ones + random ones
_kc_words = ["go", "GO", " Go ", "gO  ", "no go", "NO GO", " No Go", "no go  ", "No go"]
for _n in range(8):
    _kc_words.append(_kc_messy(random.choice(["go", "no go"])))

# poll 的测试 / tests for poll
_kc_polls = []
for _n in range(8):
    _p = []
    _bad = random.randint(0, 2)
    for _k in range(random.randint(3, 7)):
        _p.append(_kc_messy("go"))
    for _k in range(_bad):
        _p[random.randint(0, len(_p) - 1)] = _kc_messy("no go")
    _kc_polls.append(_p)
_kc_polls.append([_kc_messy("no go"), _kc_messy("no go"), _kc_messy("go")])

def _kc_is_go(r):
    return r.strip().lower() == "go"

def _kc_call(fn, arg):
    # 调用孩子的函数；出错也不要让检查代码崩掉 / call the kid's function without letting an error crash the check
    try:
        return [True, fn(arg)]
    except Exception as e:
        return [False, str(e)]
