# 🍎 接水果 第 9 关：过关检查（真的去玩一下你的函数）/ Fruit Catcher level 9: win check (actually plays your functions)
import turtle as _kt
import time as _time
def _kc9():
    global score, lives, game_over, combo
    for _n in ["speed_for", "combo", "fall", "score", "lives", "game_over", "basket", "tick"]:
        if _n not in globals():
            print("__KC_HINT__ 还没有 " + _n + "。看看最上面的任务清单|There is no " + _n + " yet. Check the task list at the top")
            return False
    # ① speed_for 的规律 / the speed_for rule
    _table = [[0, 5], [4, 5], [5, 6], [9, 6], [10, 7], [23, 9], [34, 11], [35, 12], [36, 12], [50, 12], [1000, 12]]
    for _row in _table:
        _got = speed_for(_row[0])
        if _got != _row[1]:
            print("__KC_HINT__ speed_for(" + str(_row[0]) + ") 应该是 " + str(_row[1]) + "，你的函数交回了 " + str(_got) + "|speed_for(" + str(_row[0]) + ") should be " + str(_row[1]) + ", but your function returned " + str(_got))
            return False
    _start = lives
    _kc_saved.append(_start)
    # 先让游戏暂停，测试的时候别的东西不会乱动 / pause the game first so nothing else moves during the tests
    game_over = True
    _time.sleep(0.2)
    _f = _kt.Turtle()
    _f.hideturtle()
    _f.penup()
    _f.speed(0)
    _bx = basket.xcor()
    _by = basket.ycor()
    # ② fall 用 speed_for / fall uses speed_for
    lives = 10
    game_over = False
    for _s in [0, 23]:
        score = _s
        _f.color("red")
        _f.goto(_bx + 200, 100)
        fall(_f)
        if abs((100 - _f.ycor()) - speed_for(_s)) > 0.01:
            print("__KC_HINT__ 分数是 " + str(_s) + " 的时候，水果一步应该掉 " + str(speed_for(_s)) + "，但它掉了 " + str(100 - _f.ycor()) + "。fall(f) 里要用 speed_for(score)|With a score of " + str(_s) + " a fruit should fall " + str(speed_for(_s)) + " per step, but it fell " + str(100 - _f.ycor()) + ". Use speed_for(score) in fall(f)")
            return False
    # ③④ 连击 / combos
    score = 0
    lives = 10
    combo = 0
    # [颜色, 接住?, 之后的分数, 之后的命, 之后的连击, 中文说明, English]
    _steps = [
        ["red", True, 1, 10, 1, "接住第 1 个水果", "catching the 1st fruit"],
        ["red", True, 2, 10, 2, "连续接住第 2 个", "catching a 2nd in a row"],
        ["red", True, 4, 10, 3, "连续接住第 3 个（combo 到 3，算 2 分）", "catching a 3rd in a row (combo reaches 3, worth 2)"],
        ["red", True, 6, 10, 4, "连续接住第 4 个（还是 2 分）", "catching a 4th in a row (still worth 2)"],
        ["red", False, 6, 9, 0, "漏掉一个水果（少 1 命，combo 归 0）", "missing a fruit (lose 1 life, combo back to 0)"],
        ["red", True, 7, 9, 1, "漏掉以后再接住 1 个", "catching one after the miss"],
        ["red", True, 8, 9, 2, "再接住 1 个", "catching one more"],
        ["black", False, 8, 9, 2, "躲开一个炸弹（combo 不变）", "dodging a bomb (combo stays)"],
        ["red", True, 10, 9, 3, "躲开炸弹后接住水果（combo 到 3，算 2 分）", "catching a fruit after dodging (combo reaches 3, worth 2)"],
        ["black", True, 10, 8, 0, "接到炸弹（少 1 命，combo 归 0）", "catching a bomb (lose 1 life, combo back to 0)"],
        ["red", True, 11, 8, 1, "接到炸弹以后再接住水果", "catching a fruit after the bomb"],
    ]
    for _st in _steps:
        _f.color(_st[0])
        if _st[1]:
            _f.goto(_bx, _by + 10)
        else:
            _f.goto(_bx + 200, -279)
        fall(_f)
        if score != _st[2] or lives != _st[3] or combo != _st[4]:
            print("__KC_HINT__ 测试：" + _st[5] + "之后，应该是 score = " + str(_st[2]) + "、lives = " + str(_st[3]) + "、combo = " + str(_st[4]) + "；你的是 score = " + str(score) + "、lives = " + str(lives) + "、combo = " + str(combo) + "|Test: after " + _st[6] + " it should be score = " + str(_st[2]) + ", lives = " + str(_st[3]) + ", combo = " + str(_st[4]) + "; yours is score = " + str(score) + ", lives = " + str(lives) + ", combo = " + str(combo))
            return False
    return True
_kc_saved = []
_kc_ok = _kc9()
if _kc_saved:
    # 测试完了（不管过没过）：新的一局，重新启动心跳 / tests done (pass or not): a fresh game, restart the heartbeat
    score = 0
    combo = 0
    lives = _kc_saved[0]
    game_over = False
    tick()
if _kc_ok:
    print("__KC_WIN__")
