# 第 9 关：迷宫大师 / Level 9: maze master
# 这次是真正的迷宫：有岔路，还有死胡同！每次运行都不一样。
# A real maze this time: branches AND dead ends! Different every run.
# 写一个函数 solve()：走到星星，并且 return 一共走了几格。
# Write a function solve(): reach the star, and return how many cells you moved.
# 🔬 过关前，检查员还会用 4 个秘密迷宫再考你的 solve()！
# 🔬 Before you pass, the inspector tests your solve() on 4 more secret mazes!
# 指令 / commands: forward(60)  left(90)  right(90)  wall_ahead()  wall_left()  wall_right()  at_goal()

def solve():
    steps = 0
    while not at_goal():
        if not wall_ahead():
            forward(60)
        else:
            left(90)
    return steps

print("steps:", solve())
