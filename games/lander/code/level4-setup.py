# 🛬 火箭着陆 第 4 关：关卡代码（隐藏，每次数据都不一样）/ Rocket Lander level 4: hidden setup (new data every run)
import turtle
import random

# 记下孩子打印的每一行，检查的时候用 / remember every line the kid prints, for the check
_kc_print = print
_kc_buf = [""]
def print(*args, sep=" ", end="\n"):
    _kc_buf[0] = _kc_buf[0] + sep.join([str(a) for a in args]) + end
    _kc_print(*args, sep=sep, end=end)

def _kc_lines():
    return [_l.rstrip() for _l in _kc_buf[0].split("\n") if _l.strip() != ""]

SAFE = 4
_SAFE = SAFE
# 16 次试飞的落地速度（每次运行都不一样）/ touchdown speeds of 16 test flights (new every run)
results = []
for _i in range(16):
    if random.randint(1, 10) <= 7:
        results.append(random.randint(1, _SAFE))
    else:
        results.append(random.randint(_SAFE + 1, 12))
_res = list(results)

# 画一张柱状图：绿色 = 安全，红色 = 坠毁 / a bar chart: green = safe, red = crash
turtle.Screen().bgcolor("midnightblue")
_w = turtle.Turtle()
_w.hideturtle()
_w.speed(0)
_w.penup()
_w.pensize(1)
_w.color("gray")
_w.goto(-250, 200)
_w.pendown()
_w.goto(-250, -200)
_w.goto(260, -200)
_w.penup()
_w.color("limegreen")
_w.goto(-250, -200 + _SAFE * 30)
_w.pendown()
_w.goto(260, -200 + _SAFE * 30)
_w.penup()
_w.goto(264, -200 + _SAFE * 30 - 6)
_w.write("SAFE", font=("Arial", 10, "normal"))
_w.pensize(20)
for _i in range(len(_res)):
    if _res[_i] <= _SAFE:
        _w.color("limegreen")
    else:
        _w.color("tomato")
    _w.goto(-228 + _i * 30, -190)
    _w.pendown()
    _w.goto(-228 + _i * 30, -210 + _res[_i] * 30)
    _w.penup()
_w.color("white")
_w.goto(-250, 215)
_w.write("📊 16 test flights / 16 次试飞", font=("Arial", 13, "bold"))
_kc_print(f"📡 results = {results}")
_kc_print("--------")
