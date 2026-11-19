# 🚀 发射控制 第 1 关：关卡代码（隐藏）/ Launch Control level 1: hidden setup
import random

# 记下孩子打印的每一行，检查的时候用 / remember every line the kid prints, for the check
_kc_print = print
_kc_buf = [""]
def print(*args, sep=" ", end="\n"):
    _kc_buf[0] = _kc_buf[0] + sep.join([str(a) for a in args]) + end
    _kc_print(*args, sep=sep, end=end)

def _kc_lines():
    return [_l.rstrip() for _l in _kc_buf[0].split("\n") if _l.strip() != ""]

start = random.randint(9, 20)
engines = random.randint(2, 5)
poll = random.randint(engines + 2, start - 1)
_start = start
_engines = engines
_poll = poll
_kc_print(f"📡 start = {start}, poll = {poll}, engines = {engines}")
_kc_print("--------")
