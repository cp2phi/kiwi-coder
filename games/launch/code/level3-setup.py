# 🚀 发射控制 第 3 关：关卡代码（隐藏）/ Launch Control level 3: hidden setup
import random

# 记下孩子打印的每一行，检查的时候用 / remember every line the kid prints, for the check
_kc_print = print
_kc_buf = [""]
def print(*args, sep=" ", end="\n"):
    _kc_buf[0] = _kc_buf[0] + sep.join([str(a) for a in args]) + end
    _kc_print(*args, sep=sep, end=end)

def _kc_lines():
    return [_l.rstrip() for _l in _kc_buf[0].split("\n") if _l.strip() != ""]

fuel = random.randint(30, 90)
burn = random.randint(5, 9)
boost = random.randint(2, 4)
_fuel = fuel
_burn = burn
_boost = boost
_kc_print(f"📡 fuel = {fuel}, burn = {burn}, boost = {boost}, target = 100")
_kc_print("--------")
