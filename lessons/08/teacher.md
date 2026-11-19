---
title: 第 8 课 · 教案
title_en: Lesson 8 · Teacher plan
lesson: "08"
tab: teacher
---

# 👩‍🏫 第 8 课教案：迷你项目——石头剪刀布（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子**第一次大部分自己写**，把变量、input、if、random、while、列表、函数拼成一个能玩的游戏；学会「一次一小步，每步都运行」和「**先写测试，再写代码**」；学会用排错模板问 AI。进阶：N 局几胜 + 胜率统计、问到合格为止的输入循环、把规则装进函数、用列表计数做一个「会学习的电脑」。

**今天的铁律：老师手放背后。** 不碰键盘、不碰鼠标、不说答案。只问问题：「你猜？」「哪个测试是 ❌？」「报错说第几行？」「这一步你想让它做什么？」「小词典里有吗？」孩子要答案时，把他引向四步法。今天**允许慢**：第 4 步做完就已经是一个完整的游戏了。

<div class="box box-tip"><span class="box-title">📈 这一课比原版难了大约 30–40%</span>
① 热身和第 1 步只剩一个「整行」的空；② 第 2 步改成<b>问到合格为止</b>的 <code>ask_player()</code>（while True + return），代替原来的 continue；③ 第 3 步<b>没有填空</b>，孩子对着 6 个测试自己写 judge（测试先行），进阶改写成 <code>beats_what()</code> 规则招式；④ 第 4 步改成「N 局几胜」，加分 / 宣布赢家 / 胜率三块全自己写；⑤ 新增第 5 步「会学习的电脑」（用列表计数、找最大值）；⑥ 两个病号都是<b>不报错</b>的逻辑 bug；⑦ 4 道追踪型猜一猜。作业 🥉 要写 to_chinese（strip/lower 真用上），🥇 是一个对比实验。<br>
<b>如果孩子吃力</b>：见下面「怎么砍」——第 5 步、beats_what 进阶、胜率可以先砍。
</div>

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-8">
  <li>自己把每一步跑一遍：第 3 步先跑出 3 个 ❌ 再写到全 ✅；第 4 步自己写三个 TODO；第 5 步一直出石头，看电脑第 4 轮开始出布。</li>
  <li>先做一遍 4 道猜一猜（answer.lower()、问几次、judge 追踪、五局三胜第几轮停、favourite 追踪），想好怎么讲「一样大不算大于」。</li>
  <li>准备好「排错模板」怎么用：画板红框里的「📋 复制问 AI 要提示的话」按钮——课上让孩子自己点。</li>
  <li>第 7 课作业反馈写在 <a href="{{ '/feedback/' | relative_url }}">老师的话</a>，开课先聊 2 分钟。</li>
  <li>想好一句开场：「今天你是主厨，我只是递调料的。」</li>
</ul>

---

## ⏱️ 60 分钟时间表（大约 40 分钟在搭）

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>💌 反馈 + 热身</td><td>聊上周作业。热身：那一行 <code>basket.append(random.choice(fruits))</code> 让他自己拼出来。count_fruit 时间不够就留作业。<br>开场白：「今天没有新魔法，零件你都有了。我们要做的是<b>拼</b>，而且大部分你自己写。」看流程图。</td><td>能自己拼出 append + choice 吗？（不能的话，今天的函数部分要多给提示）</td></tr>
<tr><td><b>5–22</b></td><td>🪜 第 1–3 步</td><td><b>第 1 步</b>（2 分钟）：<code>return random.choice(choices)</code>。<br><b>第 2 步</b>（6 分钟）：先做 answer.lower() 的猜一猜，再跑 lower-demo。再做「问几次」的猜一猜，跑 step2 验证。强调「<b>return 会跳出循环</b>」。<br><b>第 3 步</b>（9 分钟）：先运行，看 3 个 ❌——「测试就是说明书」。让他对着规则表写到 6 个 ✅。改 and→or 看哪个测试变红。<b>beats_what 进阶</b>：做追踪题即可，winner_against 时间够再写（第 5 步里已经写好了一份）。</td><td>他是自己对规则表写，还是等你念？会不会每写一种「赢」就运行一次看测试？</td></tr>
<tr><td><b>22–34</b></td><td>🪜 第 4 步</td><td>先做「第几轮停」的猜一猜——让他<b>一轮一轮数出来</b>。然后 TODO 1 加分，玩一局五局三胜；TODO 2 宣布赢家；TODO 3 统计 + 胜率（int 去小数）。问「输入 4 会怎样？」——留给作业 🥈。</td><td>加分时会写 if / elif / else 三支吗？胜率算式里分子用对了吗？</td></tr>
<tr><td><b>34–42</b></td><td>🧪 测试 + 虫虫医院</td><td>「现在你是捣蛋鬼」：按清单逐个试，特别是「几局几胜」输入 abc（ValueError，读报错）。<br>病号 1：对着规则表找。病号 2：让他回想第 2 步的猜一猜——<b>「做出了新的，没存回去」</b>。</td><td>不报错的 bug 他是读代码找到的，还是乱改碰到的？</td></tr>
<tr><td><b>42–50</b></td><td>🧠 第 5 步（进阶）</td><td>先讲一句：「这就是第 6 课说的<b>从数据学习</b>——它的数据就是你出的拳。」做 favourite 追踪题（[2, 3, 3]）。运行，一直出石头，看它第 4 轮开始出布。挑战：「现在你知道它的秘密了，打败它！」</td><td>他能说出电脑「学」到的是什么吗？能想到反制策略吗？</td></tr>
<tr><td><b>50–56</b></td><td>🤖 排错伙伴</td><td>如果今天有真实 bug（通常有），用画板红框的按钮生成排错话术，贴给 AI，<b>只要提示</b>。没有 bug 就把病号 1 改坏再问。对比页面上的好问题 / 坏问题。</td><td>AI 给了答案他会直接贴，还是自己改？</td></tr>
<tr><td><b>56–60</b></td><td>📓 收尾</td><td>第 4 步的版本存到作品墙（rps-step4）。笔记本 3 行 + 「AI 帮我排错的一次」。看作业页：🥉 是 judge + to_chinese + 加分，两行测试全 True。第 6 步加料、虫虫医院游戏回家选做。</td><td>能说出「我今天自己写了 ___」吗？</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够 / 太难时怎么砍</span>
优先级：<b>第 1–3 步（judge 测试全 ✅）</b> &gt; <b>第 4 步 TODO 1–2</b> &gt; 测试清单 &gt; 病号 2 &gt; 胜率（TODO 3）&gt; 排错模板 &gt; 病号 1 &gt; 第 5 步 &gt; beats_what 进阶 &gt; 第 6 步。<br>
<b>孩子吃力时：</b>① 第 3 步允许看提示 1 后照抄一种「赢」再写另外两种；② beats_what 进阶只做追踪题、不写 winner_against；③ 第 5 步改成「老师演示 + 孩子玩」，只做猜一猜和「打败它」；④ 胜率留到作业 🥈。<b>宁可停在第 4 步把它玩透</b>，也不要赶第 5 步。<br>
<b>孩子很快时：</b>第 2 步加「数你试了几次」；第 5 步让他给 favourite 加「一样多时随机选一个」；第 6 步想想「6 种拳能不能公平」。
</div>

---

## 🗣️ 好用的话术（手放背后专用）

- 「这一步你想让它做什么？用中文说一遍。」（先说再写）
- 「跑一下？哪个测试还是 ❌？」（每改一处就问）
- 「报错说第几行？那一行你自己读一遍。」
- 「<code>.lower()</code> 做出来的新字，你存到哪里了？」
- 「一轮一轮数给我听：现在比分多少？」（追踪题和第 4 步）
- 「电脑现在『学到』了什么？」（第 5 步）
- 「小词典 / 笔记本里有没有？」
- 「你刚才自己找到了那个 bug！」（夸过程）
- 绝不说：「应该写 ___」。实在要帮，就说「看看第 3 步你是怎么写的」。

## 🐞 常见卡点和应对

| 卡点 | 表现 | 怎么办 |
|---|---|---|
| 中文引号 / 括号 | SyntaxError，画板会指出中文符号 | 让他切换输入法重打那个符号 |
| and 写成 or | 测试里出现 ❌ | 「布和石头，电脑出石头……or 的意思是什么？」 |
| strip / lower 没存回去 | 带空格 / 大写还是不认 | 回到第 2 步那道猜一猜 |
| return 后面还想写代码 | 那几行永远不跑 | 「return 之后招式就结束了」 |
| ties 没加 / 加错变量 | 平局数一直是 0 / 比分反了 | 让他 print 出 result 看看到底是哪个字 |
| 胜率算成 0 或很怪 | 分子分母写反、忘了 × 100 | 「赢了 2 轮，一共 5 轮，胜率应该是多少？用这两个数代进去算一遍」 |
| 「几局几胜」输入 abc | ValueError | 这是好 bug：让他读报错，留给作业 🥈 修 |
| 循环停不下来 | 一直问 | 按「■ 停下」，看 while 的条件和安全带 |
| 想一口气写完 | 跳过运行 | 「先跑一下，再加下一步」 |

---

## ✅ 参考答案

<details class="hint"><summary>热身 + 第 1 步</summary><pre>basket.append(random.choice(fruits))

def count_fruit(basket, name):
    count = 0
    for f in basket:
        if f == name:
            count += 1
    return count

# 第 1 步
def computer_play():
    return random.choice(choices)</pre></details>

<details class="hint"><summary>第 2 步：两道猜一猜 + 数次数</summary>answer.lower() 那题：打印 <b>YES</b>（没存回去）。问几次那题：<b>问 2 次，me = 布</b>。<pre>def ask_player():
    tries = 0
    while True:
        me = input("你出什么？ ").strip()
        tries += 1
        if me in choices:
            print("你试了", tries, "次")
            return me
        print("只能出 石头 / 剪刀 / 布 哦！")</pre></details>

<details class="hint"><summary>第 3 步 judge + beats_what 进阶</summary><pre>def judge(me, computer):
    if me == computer:
        return "平"
    elif me == "石头" and computer == "剪刀":
        return "赢"
    elif me == "剪刀" and computer == "布":
        return "赢"
    elif me == "布" and computer == "石头":
        return "赢"
    return "输"

# 进阶：step3-rules.py 打印「赢 输 平」；追踪题答案：剪刀；输
def winner_against(play):
    if play == "石头":
        return "布"
    elif play == "剪刀":
        return "石头"
    else:
        return "剪刀"</pre></details>

<details class="hint"><summary>第 4 步三个 TODO</summary>猜一猜：<b>第 6 轮后，3:1，ties = 2</b>。<pre>    # TODO 1（循环里）
    if result == "赢":
        my_score += 1
    elif result == "输":
        computer_score += 1
    else:
        ties += 1

# TODO 2
if my_score &gt; computer_score:
    print("🏆 你赢了！")
elif my_score &lt; computer_score:
    print("🤖 电脑赢了！")
else:
    print("🤝 平手！")

# TODO 3
print("一共", rounds, "轮，平了", ties, "次")
print("你的胜率:", int(my_score / rounds * 100), "%")</pre>输入 4：<code>int(4 / 2) + 1</code> = 3，「四局三胜」不合理（可能 2:2 后还要继续），所以作业只接受 3、5、7。</details>

<details class="hint"><summary>第 5 步</summary>猜一猜：<b>剪刀；电脑出石头</b>（3 &gt; 3 不成立，best 停在 1）。一直出石头 → 第 4 轮起电脑一直出布。打败它：当它出布时你出剪刀；几轮后你的「最爱」变成剪刀，它就改出石头……<pre>print("你的胜率:", int(my_wins / 10 * 100), "%")</pre></details>

<details class="hint"><summary>第 6 步 / sad_face</summary>6 种拳没法完全公平：每种拳要面对另外 5 种，5 不能平分成「赢一半、输一半」。（5 种、7 种可以：每种赢 2 输 2 / 赢 3 输 3。）<pre>def sad_face(x, y):
    t.penup(); t.goto(x, y); t.setheading(0); t.pendown()
    t.color("gray")
    t.circle(25)
    t.penup(); t.goto(x - 10, y + 32); t.dot(6)
    t.goto(x + 10, y + 32); t.dot(6)
    t.goto(x + 12, y + 12); t.setheading(120); t.pendown()
    t.circle(14, 120)          # 从右往左画一座小山 ∩ = 撇嘴
    t.setheading(0)
# 在「输」的分支里：
sad_face(-200 + computer_score * 100, -100)</pre></details>

<details class="hint"><summary>病号 1 / 病号 2</summary>病号 1：第三个 elif 应为 <code>me == "布" and computer == "石头"</code>。<br>病号 2：<code>text = text.strip()</code>、<code>text = text.lower()</code>（或者一行 <code>return text.strip().lower()</code>）。</details>

<details class="hint"><summary>作业 🥉🥈🥇 参考</summary><pre># 🥉 TODO 1
    if beats_what(me) == computer:
        return "赢"

# 🥉 TODO 2
def to_chinese(word):
    word = word.strip().lower()
    if word == "rock":
        return "石头"
    elif word == "scissors":
        return "剪刀"
    elif word == "paper":
        return "布"
    return word

# 🥉 TODO 3（play_game 循环里）
        if result == "赢":
            my_score += 1
        elif result == "输":
            computer_score += 1
        else:
            ties += 1

# 🥈（替换「主程序」）
def ask_best_of():
    while True:
        n = input("几局几胜？3 / 5 / 7： ").strip()
        if n == "3" or n == "5" or n == "7":
            return int(n)
        print("只能是 3、5 或 7！")

games_won = 0
games_lost = 0
total_ties = 0
rounds_won = 0
total_rounds = 0
again = "y"
while again == "y":
    best_of = ask_best_of()
    mine, theirs, ties = play_game(int(best_of / 2) + 1)
    if mine &gt; theirs:
        games_won += 1
    elif mine &lt; theirs:
        games_lost += 1
    total_ties += ties
    rounds_won += mine
    total_rounds += mine + theirs + ties
    again = input("再来一局？(y / n) ").strip().lower()
print("赢了", games_won, "局，输了", games_lost, "局，平了", total_ties, "轮")
print("总胜率", int(rounds_won / total_rounds * 100), "%")

# 🥇
counts = [0, 0, 0]
# winner_against 和 favourite 照学一学第 5 步
def computer_move(mode, rounds):
    if mode == "hard" and rounds &gt;= 3:
        return winner_against(favourite())
    return random.choice(choices)

mode = input("easy 还是 hard？ ").strip().lower()
wins = 0
for rounds in range(15):
    computer = computer_move(mode, rounds)
    me = ask_player()
    for i in range(len(choices)):
        if choices[i] == me:
            counts[i] += 1
    if judge(me, computer) == "赢":
        wins += 1
print(mode, "模式胜率", int(wins / 15 * 100), "%")</pre>
🥇 的评价重点：实验记录里真的写了两个胜率，并能说出「为什么困难模式更难 / 为什么我能打败它」（比如「我知道它会出布，所以我出剪刀」）。「记住上一轮」的点子：存一个 <code>last = me</code>，困难模式出 <code>winner_against(last)</code>。</details>

---

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 做到了第几步？ | |
| 哪一步是完全自己写出来的？测试全 ✅ 了吗？ | |
| 追踪题（问几次 / 第几轮停 / favourite）猜对了几道？ | |
| 遇到 bug 的第一反应：读报错 / 看测试 / 问老师 / 乱改 / 问 AI？ | |
| 第 5 步：能说出电脑「学」到了什么吗？打败它了吗？ | |
| 难度感受：太难 / 刚好 / 还能更难？ | |
| 作业等级预估（🥉🥈🥇） | |
