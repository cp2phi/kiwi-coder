# test-input: 1 | 惠灵顿 | 4 | turtle | 2 | 3
# 📱 项目骨架：问答 app  Project skeleton: Quiz app
# 作者 By：（昵称 nickname）
# 一个有菜单的文字 app：你可以把它改成翻译机、待办、算命机、计算器……
# A text app with a menu: turn it into a translator, to-do list, fortune teller, calculator…
import random

# ----- 数据 data（改成你的！/ make it yours!）-----
quiz = {
    "新西兰的首都是？": "惠灵顿",
    "一个正方形有几条边？": "4",
    "Python 的海龟工具箱叫什么？": "turtle",
}
score = {"对": 0, "错": 0}

# ----- 功能 features：每个功能一个函数 / one function per feature -----
def ask(question):                           # 问一题，返回对不对 / ask one question, return True/False
    answer = input(question + " ").strip()
    return answer == quiz[question]

def play():                                  # 功能 1：玩一轮 / feature 1: play a round
    for q in quiz:
        if ask(q):
            print("✅ 对了！")
            score["对"] += 1
        else:
            print(f"❌ 答案是 {quiz[q]}")
            score["错"] += 1

def show_score():                            # 功能 2：看比分 / feature 2: show the score
    print(f"📊 对 {score['对']} 题，错 {score['错']} 题")

# TODO: 功能 3：加一道题。提示：先问题目 q = input("问题？")，再问答案 quiz[q] = input("答案？")
#       feature 3: add a question. Hint: first the question q = input("Question? "), then quiz[q] = input("Answer? ")

def test():                                  # 🧪 小测试 / tiny tests
    assert len(quiz) >= 3, "至少要有 3 道题"
    assert "新西兰的首都是？" in quiz
    assert quiz["新西兰的首都是？"] == "惠灵顿"

# ----- 主循环 main loop -----
test()
while True:
    print("\n1 玩  2 看比分  3 退出")
    choice = input("选： ")
    if choice == "1":
        play()
    elif choice == "2":
        show_score()
    elif choice == "3":
        print("👋 再见！")
        break
    else:
        print("🤔 请输入 1、2 或 3")
