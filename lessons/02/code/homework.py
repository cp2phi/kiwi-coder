# 🤖 第 2 课作业：聊天机器人 2000  Lesson 2 homework: Chatbot 2000
# 作者 By：（写你的昵称 your nickname）
# AI 帮忙的地方 How AI helped：（如果问了 AI，写下它给的提示 / write any hint AI gave you）
# test-input: 小海龟 | 披萨 | 150

# ===== 🥉 第 1 部分：至少 3 个问题 + 回应  Part 1: at least 3 questions + replies =====
print("你好！我是你的聊天机器人 🤖")

name = input("你叫什么名字？ ")
print(f"你好，{name}！")

food = input("你最喜欢吃什么？ ")
print(f"{food}？我也想吃！")

# TODO: 再加一个问题，并用 f"..." 回应  Add one more question and reply with f"..."


# ===== 🥈 第 2 部分：用 int() 算点东西  Part 2: calculate something with int() =====
# TODO: 问年龄（或别的数字），算一算，比如明年几岁、多少个月  Ask for a number and calculate with it


# ===== 🥈 第 3 部分：海龟画一个大小由你决定的图形  Part 3: a turtle shape sized by your input =====
import turtle

size = int(input("你想要多大的正方形？（输入一个数字） "))
t = turtle.Turtle()
t.color("purple")
t.pensize(4)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)

# ===== 🥇 第 4 部分（选做）：问 AI 学一招  Part 4 (optional): learn a trick from AI =====
# TODO: 比如 name.upper() 能把名字变大写。AI 教了我什么：
