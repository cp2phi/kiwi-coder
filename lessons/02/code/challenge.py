# 🏆 挑战：三个问题的聊天机器人  Challenge: a 3-question chatbot
# test-input: 小海龟 | 游泳 | 3
# 把下面的问题换成你自己的，然后加第 3 个问题！ Replace the questions with your own, then add a 3rd one!

print("嗨！我想了解你的爱好 🎈")

hobby = input("你最喜欢做什么？ ")
print(f"{hobby}！听起来很好玩。")

when = input(f"你一般什么时候{hobby}？ ")
print(f"原来是{when}，难怪你这么厉害。")

# 👇 在这里加第 3 个问题（提示：复制上面两行，改一改）
# 👇 Add a 3rd question here (hint: copy the two lines above and change them)


# 最后用一句话总结（用 f 和 {}）  Finish with one summary line (use f and {})
print(f"总结：你喜欢{hobby}，一般{when}去做。")
