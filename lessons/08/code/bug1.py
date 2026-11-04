# 🐞 病号 1：这个 judge 有 1 个 bug——有一种情况判错了。修好它！
# Patient 1: this judge has 1 bug — one case is judged wrong. Fix it!
def judge(me, computer):
    if me == computer:
        return "平"
    elif me == "石头" and computer == "剪刀":
        return "赢"
    elif me == "剪刀" and computer == "布":
        return "赢"
    elif me == "布" and computer == "剪刀":
        return "赢"
    else:
        return "输"

print(judge("石头", "剪刀"))
print(judge("剪刀", "布"))
print(judge("布", "石头"))
print(judge("布", "剪刀"))
print(judge("石头", "石头"))
