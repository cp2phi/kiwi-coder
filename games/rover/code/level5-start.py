# 🛰️ 第 5 关：地毯式勘探 / Level 5: survey sweep
# 勘探区大小随机。像割草机一样一排一排扫：往右扫一排 → 左转上去一格左转 → 往左扫一排 → 右转上去一格右转 → ……
# The survey area has a random size. Sweep row by row like a lawnmower: sweep right → left, up one, left → sweep left → right, up one, right → ...

def sweep_row():
    # 扫一整排：收脚下的样本，一直开到前面挡住 / sweep one row: collect what's underfoot, drive until blocked
    if sample_here():
        collect()
    # TODO: while ... :

def u_turn(side):
    # side 是 "left" 或 "right"。上面还有一排 → 掉头上去，return True；没有了 → return False
    # side is "left" or "right". Another row above → turn up into it and return True; no more rows → return False
    if side == "left":
        turn_left()
    else:
        turn_right()
    # TODO: 前面挡住了吗？/ blocked ahead?
    move()
    if side == "left":
        turn_left()
    else:
        turn_right()
    return True

sweep_row()
u_turn("left")
sweep_row()
