# 第 7 关：绕房间一圈 / Level 7: around the room
# ⚠️ 房间大小和宝石位置每次运行都会变！宝石都在靠墙的那一圈格子上。
# ⚠️ The room size and the gems change every run! All the gems are on the cells along the walls.
# 新指令 / new commands:
#   front_is_clear()  前面一格能走吗？/ can I move forward?
#   gem_here()        脚下有宝石吗？/ is there a gem under me?

while front_is_clear():
    move()
    pick()     # 🤔 每一格都捡？/ pick on every cell?
