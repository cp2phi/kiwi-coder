# 🐞 虫虫医院 病号 7：隐藏代码（每次随机给分数）/ Bug Hospital patient 7: hidden setup (random scores every run)
import random

scores = [90, random.randint(91, 100), random.randint(70, 89), random.randint(50, 69), random.randint(0, 49), random.randint(0, 100)]
random.shuffle(scores)
_scores = scores[:]
