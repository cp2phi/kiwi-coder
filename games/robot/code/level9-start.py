# 第 9 关：指令翻译机 / Level 9: the order translator
# 总部用一串字母给机器人发指令（每次都不一样）/ HQ sends the robot a string of letters (different every run):
#   M = move()   L = turn_left()   R = turn_right()   P = pick()
# 可是信号不好：有的字母变成了小写，还夹着空格和横线 - （空格和横线不是指令，跳过它们）
# But the signal is bad: some letters came out lowercase, with spaces and dashes - mixed in (those aren't orders: skip them)
# 写 run(orders)：一个字母一个字母地照着做。🔬 检查员还会用 2 张秘密地图考你的 run()！
# Write run(orders): follow it letter by letter. 🔬 The inspector also tests your run() on 2 secret maps!
print("[" + orders + "]")

def run(orders):
    for c in orders:
        if c == "M":
            move()

run(orders)
