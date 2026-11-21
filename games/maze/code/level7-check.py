# 🐢 海龟迷宫 第 7 关：过关检查 / Turtle Maze level 7: win check
if t.distance(_last[0], _last[1]) > 2:
    print("__KC_HINT__ 🚫 海龟被「瞬移」了！这一关只能用 forward / left / right 和传感器。|🚫 The turtle was teleported! Only forward / left / right and the sensors are allowed here.")
elif crashed:
    print("__KC_HINT__ 💥 撞墙了！走之前先问 wall_ahead()：前面有墙就别走，先转弯。|💥 You hit a wall! Ask wall_ahead() before moving: if there is a wall in front, turn instead.")
elif _tired:
    print("__KC_HINT__ 😵 海龟走了好远好远还没到——它是不是在来回绕圈？撞墙的时候，先看看左边有没有墙，再决定往哪边转。|😵 The turtle walked a long way and still isn't there — is it going back and forth? When there's a wall ahead, check the left side first, then decide which way to turn.")
elif _cell_at(t.xcor(), t.ycor()) == goal_cell:
    t.dot(14, "gold")
    print("__KC_WIN__")
else:
    print("__KC_HINT__ 🐢 还没到星星。别忘了：迷宫每次都会变，所以不能数格子——用 while not at_goal(): 让海龟一直走，用 if 看路。|🐢 Not at the star yet. Remember: the maze changes every run, so counting cells won't work — use while not at_goal(): to keep going, and if to look around.")
