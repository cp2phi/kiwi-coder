# 🧮 游戏里记分：函数里改外面的变量要用 global / Keeping score: use global to change an outside variable
score = 0

def add_point():
    global score          # 告诉电脑：我要改外面那个 score / "I mean the score outside"
    score = score + 1
    print("得分：", score)

add_point()
add_point()
add_point()
print("最后得分：", score)
