# ✊ 第 3 步进阶：把规则装进一个招式 Step 3 stretch: put the rules in one trick
# 不再写三个 elif，而是问：「我出的拳能赢什么？」 No more three elifs — just ask "what does my play beat?"

# 交回 play 能赢的那个拳 / return the play that `play` beats
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
    if beats_what(me) == computer:      # 我能赢的，正好是电脑出的？ is what I beat exactly what the computer played?
        return "赢"
    return "输"

print(judge("布", "石头"), judge("石头", "布"), judge("剪刀", "剪刀"))

# ✍️ 写 winner_against(play)：交回「能赢 play 的拳」。第 5 步要用！
# ✍️ Write winner_against(play): return the play that BEATS play. Step 5 needs it!
