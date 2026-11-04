# 🎲 搞笑故事生成器 / Silly story maker
# 三个列表，每次随机各抽一个，拼成一句话
# Three lists; pick one from each at random and join them into a sentence
import random

who = ["一只奇异鸟", "我的老师", "一个机器人", "超级海龟"]
where = ["在学校食堂", "在海滩上", "在 Minecraft 里", "在天空塔顶上"]
did = ["吃掉了 100 个饺子", "跳了一支机器人舞", "打败了一条龙", "发明了会飞的鞋"]

a = random.choice(who)
b = random.choice(where)
c = random.choice(did)
print(f"{a}{b}{c}！")
