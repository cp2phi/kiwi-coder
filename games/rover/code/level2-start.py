# 🛰️ 第 2 关：绕场一圈采样本 / Level 2: a lap of samples
# 沿着场地的边走一整圈，回到基地 H。紫色的是样本，路上遇到就收。场地大小每次都变！
# Drive one full lap around the edge of the field, back to base H. Purple dots are samples: collect them on the way. The field size changes every run!
# 只在有样本的地方 collect()，不然会浪费力气 / only collect() where there IS a sample, or you waste power

for side in range(4):
    for step in range(10):
        # TODO: 这一格有样本吗？/ is there a sample on this cell?
        if rock_ahead():
            break
        move()
    turn_left()
