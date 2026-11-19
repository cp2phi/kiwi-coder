# 🍎 接水果 第 8 关：过关检查（真的去玩一下你的函数）/ Fruit Catcher level 8: win check (actually plays your functions)
import turtle as _kt
import time as _time
def _kc8():
    global score, lives, game_over
    for _n in ["things", "fall", "is_bomb", "lives", "score", "game_over", "tick", "basket"]:
        if _n not in globals():
            print("__KC_HINT__ 还没有 " + _n + "。看看最上面的任务清单|There is no " + _n + " yet. Check the task list at the top")
            return False
    if not isinstance(things, list) or len(things) < 3:
        print("__KC_HINT__ things 要是一个列表，里面至少 3 个会掉的东西（用 for 循环 append make_thing()）|things must be a list with at least 3 falling things (use a for loop to append make_thing())")
        return False
    for _a in range(len(things)):
        if not hasattr(things[_a], "ycor"):
            print("__KC_HINT__ things 里放的要是海龟（make_thing() 做出来的），不能是数字或文字|things must hold turtles (made by make_thing()), not numbers or words")
            return False
        for _b in range(_a):
            if things[_a] is things[_b]:
                print("__KC_HINT__ things 里有两个其实是同一个海龟。每次都要叫一次 make_thing() 做新的|Two items in things are the same turtle. Call make_thing() each time to make a new one")
                return False
    _start = lives
    _kc_saved.append(_start)
    _f = _kt.Turtle()
    _f.hideturtle()
    _f.penup()
    _f.speed(0)
    _bx = basket.xcor()
    _by = basket.ycor()
    _cases = [
        ("red", True, 1, 0, "接到水果应该 +1 分、命不变|Catching a fruit should give +1 point and keep your lives"),
        ("black", True, 0, -1, "接到炸弹应该少 1 条命、不加分|Catching a bomb should cost 1 life and give no points"),
        ("red", False, 0, -1, "漏掉水果应该少 1 条命|Missing a fruit should cost 1 life"),
        ("black", False, 0, 0, "躲开炸弹（让它掉到地上）应该什么都不发生|Dodging a bomb (letting it hit the ground) should change nothing"),
    ]
    for _c in _cases:
        score = 0
        lives = 10
        game_over = False
        _f.color(_c[0])
        if _c[1]:
            _f.goto(_bx, _by + 10)          # 就在篮子上面 / right above the basket
        else:
            _f.goto(_bx + 200, -279)        # 离篮子很远，快到地上了 / far from the basket, about to hit the ground
        fall(_f)
        if score != _c[2] or lives != 10 + _c[3]:
            _p = _c[4].split("|")
            print("__KC_HINT__ " + _p[0] + "。现在分数变了 " + str(score) + "、命变了 " + str(lives - 10) + "|" + _p[1] + ". Right now the score changed by " + str(score) + " and lives by " + str(lives - 10))
            return False
        if _f.ycor() < 200:
            print("__KC_HINT__ 碰到篮子或者掉到地上以后，要用 new_thing(f) 把它放回天上|After touching the basket or the ground, put it back in the sky with new_thing(f)")
            return False
    # tick() 要让列表里每一个都往下掉 / tick() must make every thing in the list fall
    lives = _start
    score = 0
    game_over = True
    _time.sleep(0.2)
    _x = -240
    for _t in things:
        _t.color("red")
        _t.goto(_x, 200)
        _x = _x + 480 / len(things)
    game_over = False
    tick()
    for _t in things:
        if _t.ycor() >= 200:
            print("__KC_HINT__ tick() 只让一部分东西掉下来了。用 for f in things: 让每一个都 fall(f)|tick() only makes some of the things fall. Use for f in things: to make every one fall(f)")
            return False
    score = 0
    lives = _start
    for _t in things:
        _t.goto(_t.xcor(), 300 + 60 * things.index(_t))
    return True
_kc_saved = []
_kc_ok = _kc8()
if _kc_saved and not _kc_ok:
    score = 0
    lives = _kc_saved[0]
if _kc_ok:
    print("__KC_WIN__")
