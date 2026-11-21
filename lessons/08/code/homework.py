# 🎮 第 8 课作业：我的对战游戏 Lesson 8 homework: My Battle Game
# 作者 By：（写你的昵称 your nickname）
# AI 帮我排错的一次 A time AI helped me debug：（写下你问了什么、它给了什么提示 / what you asked and the hint it gave）
# 🥇 实验记录 Experiment notes：简单模式胜率 ___%，困难模式胜率 ___%（easy-mode win rate, hard-mode win rate）
# test-input: ROCK | banana | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布
import random

choices = ["石头", "剪刀", "布"]

# ===== 🥉 必做 Part 1（3 个 TODO）/ Must do (3 TODOs) =====

# 交回 play 能赢的拳 / return the play that `play` beats
def beats_what(play):
    if play == "石头":
        return "剪刀"
    elif play == "剪刀":
        return "布"
    else:
        return "石头"

def judge(me, computer):
    if me == computer:
        return "平"
    # ✍️ TODO 1：用 beats_what 判断「赢」（只要 2 行！）/ use beats_what to spot a win (just 2 lines!)
    return "输"

# 把英文的拳变成中文；任何大小写、前后空格都要认得；认不出的原样交回
# Turn English plays into Chinese; any capitals or spaces must work; return anything else unchanged
def to_chinese(word):
    word = word.strip().lower()
    # ✍️ TODO 2：rock → 石头，scissors → 剪刀，paper → 布
    return word

def ask_player():
    while True:
        me = to_chinese(input("你出什么？石头 / 剪刀 / 布（英文也行 / English OK）： "))
        if me in choices:
            return me
        print("只能出 石头 / 剪刀 / 布 / rock / scissors / paper 哦！")

# 🧪 测试：全部是 True 才能开始玩！ Tests: all True before you play!
print("测试 judge:", judge("布", "石头") == "赢", judge("石头", "布") == "输", judge("剪刀", "剪刀") == "平")
print("测试 to_chinese:", to_chinese("  ROCK ") == "石头", to_chinese("Paper") == "布", to_chinese("香蕉") == "香蕉")

# target 有默认值 3：play_game() 就是 3 分制 / target defaults to 3: play_game() means first to 3
def play_game(target=3):
    my_score = 0
    computer_score = 0
    ties = 0
    rounds = 0
    while my_score < target and computer_score < target and rounds < 15:
        computer = random.choice(choices)
        me = ask_player()
        rounds += 1
        result = judge(me, computer)
        print("你:", me, " 电脑:", computer, " →", result)
        # ✍️ TODO 3：根据 result 加分（平局加给 ties）/ add points (ties go to ties)

        print("比分  你", my_score, ":", computer_score, "电脑")
    return my_score, computer_score, ties        # 一次交回三个数 / hand back three numbers at once

# ===== 主程序 Main program =====
mine, theirs, ties = play_game()
if mine > theirs:
    print("🏆 你赢了这一局！ You won the game!")
elif mine < theirs:
    print("🤖 电脑赢了这一局！ The computer won the game!")
else:
    print("🤝 平手（安全带停下了）/ A draw (the seatbelt stopped it)")


# ===== 🥈 加分 Part 2：N 局几胜 + 再来一局 + 总统计 / Bonus: best of N + play again + overall stats =====
# 1) 先问「几局几胜？3 / 5 / 7」——不是 3、5、7 就一直问（像 ask_player 那样）
#    Ask "best of 3 / 5 / 7?" — keep asking until it's 3, 5 or 7 (like ask_player)
# 2) 用 play_game(target) 玩；玩完问「再来一局？(y / n)」
#    Play with play_game(target); afterwards ask "play again? (y / n)"
# 3) 最后打印：赢了几局、输了几局、所有轮里平了几次、你的总胜率 %
#    At the end print: games won, games lost, total ties, and your overall win rate %


# ===== 🥇 挑战 Part 3：会学习的对手 + 小实验 / Challenge: a learning opponent + an experiment =====
# 1) 加「简单 / 困难」模式：简单 = 随机出拳；困难 = 学一学第 5 步那样，数你的拳，出能赢你最爱的拳
#    Add "easy / hard" modes: easy = random; hard = like Learn step 5, count your moves and beat your favourite
# 2) 做实验：两个模式各玩 15 轮以上，把你的胜率写在最上面的「实验记录」里。哪个更难打？为什么？
#    Experiment: play 15+ rounds in each mode and write your win rates in the notes at the top. Which is harder? Why?
# 3) 再想一招让困难模式更聪明（比如记住你「上一轮出了什么」）
#    Think of one more trick to make hard mode smarter (e.g. remember what you played last round)
