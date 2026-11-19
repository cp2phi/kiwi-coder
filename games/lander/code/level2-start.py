# 🛬 第 2 关：点火！/ Level 2: light the engine!
# step(True) = 点火走一拍（减速），step(False) = 不点火走一拍（重力让它变快）
# step(True) = one tick with the engine on (slows down), step(False) = one tick with it off (gravity speeds it up)
# 三枚助推器一枚接一枚飞回来，高度都不一样！每一枚落地速度都要 4 或更小（SAFE）。
# Three boosters come back one after another, each from a different height! Each must touch down at speed 4 or less (SAFE).
# 规则写在 if 里：什么时候点火？/ Put your rule in the if: when should the engine fire?

for i in range(1000):
    if landed():
        break
    step(False)
