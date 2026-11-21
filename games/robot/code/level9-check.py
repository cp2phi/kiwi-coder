# 💎 宝石机器人 第 9 关：过关检查（再用 2 张秘密地图考 run()）/ Gem Robot level 9: win check (tests run() on 2 more secret maps)
try:
    _has_fn = callable(run)
except NameError:
    _has_fn = False


def _trouble():
    # 刚才那一趟出了什么问题？没问题就返回 None / what went wrong on that run? None if nothing
    if _tired:
        return "🔋 机器人做了太多动作，没电了——是不是有个循环停不下来？|🔋 The robot's battery ran out — is a loop never stopping?"
    if crashed:
        return "💥 机器人撞到石头或者走出格子了。是不是漏掉了小写字母，或者把 L 和 R 搞反了？|💥 The robot hit a rock or left the grid. Did you skip the lowercase letters, or mix up L and R?"
    if missed > 0:
        return "🙅 有 " + str(missed) + " 次 pick() 的地方没有宝石。只有 P 才捡！|🙅 " + str(missed) + " pick() calls happened where there was no gem. Only P means pick!"
    if len(gems) > 0:
        return "💎 还有 " + str(len(gems)) + " 颗宝石没捡。小写的 m、l、r、p 也是指令哦！|💎 " + str(len(gems)) + " gems left. Lowercase m, l, r, p are orders too!"
    return None


if not _has_fn:
    print("__KC_HINT__ 🧩 这一关要写一个函数 def run(orders):，让机器人照着指令字符串走，然后调用 run(orders)。|🧩 This level needs a function def run(orders): that makes the robot follow the orders string — then call run(orders).")
elif _trouble() is not None:
    print("__KC_HINT__ " + _trouble())
else:
    _fail = None
    for _k in range(2):
        if _fail is None:
            _make_world()
            _o = orders
            orders = ""
            _draw()
            t.speed(0)
            try:
                run(_o)
            except Exception as _e:
                _fail = "🔬 秘密地图 " + str(_k + 1) + " 的指令是 [" + _o + "]，run() 出错了：" + str(_e) + "|🔬 Secret map " + str(_k + 1) + " had orders [" + _o + "] and run() crashed: " + str(_e)
            if _fail is None and _trouble() is not None:
                _fail = "🔬 秘密地图 " + str(_k + 1) + " 的指令是 [" + _o + "]：" + _trouble().split("|")[0] + " 记得用参数 orders，不要只照着第一张地图写。|🔬 Secret map " + str(_k + 1) + " had orders [" + _o + "]: " + _trouble().split("|")[1] + " Remember to use the orders parameter, not the first map."
    if _fail is None:
        print("__KC_WIN__")
    else:
        print("__KC_HINT__ " + _fail)
