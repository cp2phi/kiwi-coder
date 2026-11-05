# 🎮 第 8 课作业：我的对战游戏 Lesson 8 homework: My Battle Game
# 作者 By：（写你的昵称 your nickname）
# AI 帮我排错的一次 A time AI helped me debug：（写下你问了什么、它给了什么提示 / what you asked and the hint it gave）
# test-input: 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | 剪刀 | 布 | 石头 | n
import random

choices = ["石头", "剪刀", "布"]

# ===== 🥉 必做 Part 1：3 分制石头剪刀布，带记分和输入检查 =====
# ===== 🥉 Must do: first-to-3 Rock Paper Scissors with scores and input checking =====
def judge(me, computer):
    if me == computer:
        return "平"
    # TODO：补上三种「赢」的情况（看学一学第 3 步）/ add the three "win" cases (see Learn step 3)

    else:
        return "输"

def play_game():
    my_score = 0
    computer_score = 0
    rounds = 0
    while my_score < 3 and computer_score < 3 and rounds < 15:
        computer = random.choice(choices)
        me = input("你出什么？石头 / 剪刀 / 布： ").strip()
        if me not in choices:
            print("只能出 石头 / 剪刀 / 布 哦！")
            continue
        rounds = rounds + 1
        result = judge(me, computer)
        print("你:", me, " 电脑:", computer, " →", result)
        # TODO：根据 result 给 my_score 或 computer_score 加分 / add points based on result

        print("比分  你", my_score, ":", computer_score, "电脑")
    return my_score, computer_score        # 交回两个数 / hand back both numbers

# ===== 🥈 加分 Part 2：「再来一局？」+ 统计 =====
# ===== 🥈 Bonus: "play again?" + statistics =====
games_won = 0
games_lost = 0
again = "y"
while again == "y":
    mine, theirs = play_game()
    if mine > theirs:
        print("🏆 你赢了这一局！")
        games_won = games_won + 1
    else:
        print("🤖 电脑赢了这一局！")
        games_lost = games_lost + 1
    again = input("再来一局？(y / n) Play again? ").strip().lower()

print(f"你赢了 {games_won} 局，电脑赢了 {games_lost} 局 / You won {games_won}, computer won {games_lost}")

# ===== 🥇 挑战 Part 3：发明你自己的玩法 =====
# ===== 🥇 Challenge: invent your own variant =====
# 点子 Ideas：加蜥蜴和史波克（第 6 步）/ 猜拳加数字：出拳后各喊一个 1–5 的数，和是双数你赢 /
#              让海龟把比分画成柱状图 / 给电脑一个「作弊」模式，30% 的时候它知道你出什么
