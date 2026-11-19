# 第 8 关：城堡的牙齿 / Level 8: castle teeth
# 每颗「牙齿」形状都一样：上 h → 右 50 → 下 h → 右 50，只是高度 h 不一样。
# Every tooth has the same shape: up h → right 50 → down h → right 50 — only the height h changes.
# ⚠️ 高度每次运行都会变！它们在列表 heights 里。/ The heights change every run! They are in the list heights.
print(heights)

def tooth(h):
    # 教海龟走一颗牙齿，走完要脸朝右 / teach the turtle one tooth; it must end facing right
    left(90)
    forward(___)

tooth(heights[0])
# 然后呢？用 for 走完每一颗牙齿 / and then? use for to do every tooth
