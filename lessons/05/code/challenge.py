# 🏆 挑战：太空任务生成器 / Challenge: space mission generator
# test-input: Kiwi
import random

crew = ["Kiwi", "小海龟", "机器人 9 号", "Tama", "Aroha", "Leo"]
places = ["月球 the Moon", "火星 Mars", "国际空间站 the ISS", "木星的卫星 a moon of Jupiter"]

# ✍️ 设计说明 Design brief（先想好步骤，再写代码 / plan the steps first, then code）：
# 1. 随机选 3 个「不重复」的宇航员，放进新列表 team（提示：选一个，就从 crew 里 remove 掉）
#    Pick 3 DIFFERENT astronauts at random into a new list team (hint: once picked, remove them from crew)
# 2. 随机选一个目的地，任务编号是 1 到 999 的随机数 / Pick a random destination and a mission number 1-999
# 3. 打印一张任务卡：编号、目的地，再用 for 把 team 一个一个带编号打印出来
#    Print a mission card: number, destination, then use for to print team members with numbers
# 4. 🌟 问「谁想留在地球？」——如果这个名字在 team 里（in），把他换成 crew 里剩下的另一个人
#    🌟 Ask "who wants to stay on Earth?" — if that name is in team, swap them for someone left in crew
