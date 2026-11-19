# 🔁 热身：函数 + 列表 + .strip().lower()  Warm-up: a function + a list + .strip().lower()
# 这是上节课石头剪刀布里，一个玩家出过的拳（打字很乱！）
# These are the moves one player typed in last lesson's game (messy typing!)

moves = ["Rock", " paper", "ROCK", "scissors ", "rock", "Paper", "rock"]

# 交回 target 在 moves 里出现了几次 / return how many times target appears in moves
def count_move(moves, target):
    count = 0
    for m in moves:
        if ___ == target:      # 👈 先把 m 整理干净再比 / tidy m up before comparing
            count += 1
    return count

print("rock:", count_move(moves, "rock"))           # 应该是 4 / should be 4
print("paper:", count_move(moves, "paper"))         # 应该是 2 / should be 2
print("scissors:", count_move(moves, "scissors"))   # 应该是 1 / should be 1
