# 第 8 关：扫地机器人 / Level 8: robot vacuum
# ⚠️ 田地的大小和宝石每次都不一样！/ The field size and gems change every run!
# 计划：扫一行 → 掉头到上一行 → 扫一行 → 掉头（换另一边）→ …… 一直到上面没有路
# Plan: sweep a row → U-turn onto the next row → sweep → U-turn (the other way) → … until there's no row above

def sweep_row():
    # 扫完这一行，走到墙边为止 / sweep this row up to the wall
    if gem_here():
        pick()
    while front_is_clear():
        move()
        if gem_here():
            pick()

def next_row(side):
    # side 是 "left" 或 "right"：往那一边掉头，到上面一行
    # 成功就 return True；上面没路了就 return False
    # side is "left" or "right": U-turn that way onto the row above
    # return True if it worked; return False if there is no row above
    return False    # ✏️ 你来写 / your turn

side = "left"
sweep_row()
while next_row(side):
    sweep_row()
    # ✏️ 下一次要往另一边掉头 / next time, U-turn the other way
