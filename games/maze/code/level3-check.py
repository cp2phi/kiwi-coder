# 🐢 海龟迷宫 第 3 关：过关检查 / Turtle Maze level 3: win check
if crashed:
    print("__KC_HINT__ 💥 撞墙了！看看红点在哪里：退回一点，转个弯再试试。|💥 You hit a wall! Look where the red dot is: back up a bit and turn, then try again.")
elif t.distance(goal[0], goal[1]) < 25:
    t.dot(14, "gold")
    print("__KC_WIN__")
else:
    _d = int(t.distance(goal[0], goal[1]))
    print("__KC_HINT__ 🐢 还差 " + str(_d) + " 步才到星星。海龟现在脸朝哪边？|🐢 " + str(_d) + " steps to the star. Which way is the turtle facing now?")
