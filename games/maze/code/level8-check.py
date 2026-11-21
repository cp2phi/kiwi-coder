# 🐢 海龟迷宫 第 8 关：过关检查 / Turtle Maze level 8: win check
try:
    _has_fn = callable(tooth)
except NameError:
    _has_fn = False


def _test_tooth(k):
    # 用「假想海龟」测一下 tooth(k)：应该向右挪 100、最高到 k、最后还是脸朝右
    # test tooth(k) on the imaginary turtle: it should end 100 to the right, reach height k, and face right again
    global _virtual, _vx, _vy, _vh, _vtop
    _virtual = True
    _vx = 0.0
    _vy = 0.0
    _vh = 0.0
    _vtop = 0.0
    try:
        tooth(k)
    except Exception:
        _virtual = False
        return False
    _virtual = False
    h = _vh % 360
    facing_right = h < 1 or h > 359
    return abs(_vx - 2 * GAP) < 1 and abs(_vy) < 1 and abs(_vtop - k) < 1 and facing_right


if not _has_fn:
    print("__KC_HINT__ 🧩 这一关要先用 def 教海龟画一颗牙齿：def tooth(h):，再用它走完所有牙齿。|🧩 This level needs a trick taught with def first: def tooth(h):, then use it for every tooth.")
elif t.distance(_last[0], _last[1]) > 2:
    print("__KC_HINT__ 🚫 海龟被「瞬移」了！这一关只能用 forward / left / right。|🚫 The turtle was teleported! Only forward / left / right are allowed here.")
elif crashed:
    print("__KC_HINT__ 💥 撞墙了！看红点在第几颗牙齿。是 tooth(h) 里面哪一步错了，还是高度用错了？先只调用一次 tooth(heights[0]) 试试。|💥 You hit a wall! Which tooth has the red dot? Is one step inside tooth(h) wrong, or the height? Try calling tooth(heights[0]) just once first.")
elif t.distance(goal[0], goal[1]) >= 20:
    _d = int(t.distance(goal[0], goal[1]))
    print("__KC_HINT__ 🐢 还差 " + str(_d) + " 步才到星星。一共有 " + str(len(heights)) + " 颗牙齿——每一颗都走了吗？试试 for h in heights:|🐢 " + str(_d) + " steps to the star. There are " + str(len(heights)) + " teeth — did you do every one? Try for h in heights:")
elif not (_test_tooth(random.randint(20, 35)) and _test_tooth(random.randint(90, 140))):
    print("__KC_HINT__ 🔬 检查员用别的高度测了你的 tooth(h)，结果不对。tooth 里面是不是写死了数字？向上、向下都要走 h 步，最后脸要朝右。|🔬 The inspector tested your tooth(h) with other heights and it went wrong. Did you put a fixed number inside tooth? Go up h and down h, and end facing right.")
else:
    t.dot(14, "gold")
    print("__KC_WIN__")
