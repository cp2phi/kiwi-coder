# 🐢 海龟迷宫 第 9 关：过关检查（再用 4 个秘密迷宫考 solve()）/ Turtle Maze level 9: win check (tests solve() on 4 more secret mazes)
try:
    _has_fn = callable(solve)
except NameError:
    _has_fn = False


def _trouble():
    # 刚才那一趟出了什么问题？没问题就返回 None / what went wrong on that run? None if nothing
    if t.distance(_last[0], _last[1]) > 2:
        return "🚫 海龟被「瞬移」了！只能用 forward / left / right 和传感器。|🚫 The turtle was teleported! Only forward / left / right and the sensors are allowed."
    if crashed:
        return "💥 撞墙了！走之前先问 wall_ahead()。|💥 You hit a wall! Ask wall_ahead() before moving."
    if _tired:
        return "😵 海龟走了好远还没到——它在绕圈吗？试试「右手贴着墙走」：能右转就右转，不能就直走，再不能就左转。|😵 The turtle walked a long way and still isn't there — is it going in circles? Try 'keep your right hand on the wall': turn right if you can, else go straight, else turn left."
    if _cell_at(t.xcor(), t.ycor()) != goal_cell:
        return "🐢 还没到星星。solve() 里要用 while not at_goal(): 一直走到终点。|🐢 Not at the star yet. Inside solve(), use while not at_goal(): to keep going until the end."
    return None


if not _has_fn:
    print("__KC_HINT__ 🧩 这一关要写一个函数 def solve():，让它走出迷宫，然后调用 solve()。|🧩 This level needs a function def solve(): that gets through the maze — then call solve().")
elif _trouble() is not None:
    print("__KC_HINT__ " + _trouble())
else:
    _fail = None
    for _k in range(4):
        if _fail is None:
            _build()
            t.speed(0)
            try:
                _r = solve()
            except Exception as _e:
                _r = None
                _fail = "🔬 秘密迷宫 " + str(_k + 1) + " 里 solve() 出错了：" + str(_e) + "|🔬 solve() crashed in secret maze " + str(_k + 1) + ": " + str(_e)
            if _fail is None and _trouble() is not None:
                _fail = "🔬 秘密迷宫 " + str(_k + 1) + "：" + _trouble().split("|")[0] + "|🔬 Secret maze " + str(_k + 1) + ": " + _trouble().split("|")[1]
            _cells = int(round(_moved / CELL))
            if _fail is None and _r != _cells and _r != _moved:
                _fail = "🔢 秘密迷宫 " + str(_k + 1) + " 走了 " + str(_cells) + " 格，但 solve() return 的是 " + str(_r) + "。在循环里每走一格就数一下，最后 return 它。|🔢 Secret maze " + str(_k + 1) + " took " + str(_cells) + " cells, but solve() returned " + str(_r) + ". Count every cell you move inside the loop and return the count at the end."
    if _fail is None:
        t.dot(14, "gold")
        print("__KC_WIN__")
    else:
        print("__KC_HINT__ " + _fail)
