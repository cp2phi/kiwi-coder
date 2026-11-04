# 💎 宝石机器人 第 5 关：过关检查 / Gem Robot level 5: win check
try:
    _has_fn = callable(grab_row)
except NameError:
    _has_fn = False
if not _has_fn:
    print("__KC_HINT__ 🧩 这一关要先用 def 教机器人一招：写 def grab_row():，再用它来走。|🧩 This level needs a trick taught with def first: write def grab_row(): and then use it.")
elif crashed:
    print("__KC_HINT__ 💥 机器人撞到石头或者走出格子了（红点的地方）。数一数格子，少走一步试试？|💥 The robot hit a rock or left the grid (see the red dot). Count the cells: try one move fewer?")
elif len(gems) == 0:
    print("__KC_WIN__")
else:
    _msg = "💎 还有 " + str(len(gems)) + " 颗宝石没捡。"
    _msg_en = "💎 " + str(len(gems)) + " gems left."
    if missed > 0:
        _msg = _msg + " 有 " + str(missed) + " 次 pick() 的地方其实没有宝石哦。"
        _msg_en = _msg_en + " " + str(missed) + " pick() happened where there was no gem."
    else:
        _msg = _msg + " 走到宝石上面要记得 pick()！"
        _msg_en = _msg_en + " Remember to pick() when you are on a gem!"
    print("__KC_HINT__ " + _msg + "|" + _msg_en)
