---
title: 第 8 课 · 教案
title_en: Lesson 8 · Teacher plan
lesson: "08"
tab: teacher
---

# 👩‍🏫 第 8 课教案：迷你项目——石头剪刀布（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子**第一次大部分自己写**，把变量、input、if、random、while、列表、函数拼成一个能玩的游戏；学会「一次一小步，每步都运行」；学会用排错模板问 AI。

**今天的铁律：老师手放背后。** 不碰键盘、不碰鼠标、不说答案。只问问题：「你猜？」「报错说第几行？」「这一步你想让它做什么？」「小词典里有吗？」孩子要答案时，把他引向四步法。今天**允许慢**：第 5、6 步做不到完全没关系，第 4 步做完就已经是一个游戏了。

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-8">
  <li>自己把 6 步全部跑一遍，特别是第 4 步的输入检查（输入香蕉、空、带空格）和两个病号。</li>
  <li>准备好「排错模板」怎么用：画板红框里的「📋 复制问 AI 要提示的话」按钮——课上让孩子自己点。</li>
  <li>第 7 课作业反馈写在 <a href="{{ '/feedback/' | relative_url }}">老师的话</a>，开课先聊 2 分钟。</li>
  <li>想好一句开场：「今天你是主厨，我只是递调料的。」</li>
  <li>把 <a href="{{ '/games/bugs/' | relative_url }}">🐞 虫虫医院</a> 打开备用，第 1 关自己过一遍。</li>
</ul>

---

## ⏱️ 60 分钟时间表（35 分钟在搭）

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>💌 反馈 + 热身</td><td>聊上周作业。热身画板：两个空（random.choice、range(times)）。<br>开场白：「今天没有新魔法，零件你都有了。我们要做的是<b>拼</b>。」看流程图，讲「一次一小步，每步都能跑」。</td><td>热身能 2 分钟内做完吗？（如果不行，说明函数 / 列表要在搭的时候多提示）</td></tr>
<tr><td><b>5–23</b></td><td>🪜 第 1–3 步</td><td><b>第 1 步</b>（3 分钟）：猜一猜 → 填 choice → 跑 5 次。<br><b>第 2 步</b>（7 分钟）：先跑 lower-demo，<b>先猜每行输出</b>。然后 step2：输入「  石头 」，再删掉 strip 对比。输入香蕉看拒绝。<br><b>第 3 步</b>（8 分钟）：对着规则表填 4 个空。强调「前三行 print 是在<b>测试</b> judge」。改 and→or 看哪个测试坏——这是今天最重要的「测试」体验。</td><td>第 3 步他是自己对规则表写，还是等你念？and / or 分得清吗？</td></tr>
<tr><td><b>23–38</b></td><td>🪜 第 4–5 步</td><td><b>第 4 步</b>（9 分钟）：先做 while 的猜一猜。填两个空，玩一整局。问 continue 是什么（让他输入香蕉验证 rounds 没加）。改 5 分制——如果他改了 3 处，引出 target 变量。<br><b>第 5 步</b>（6 分钟）：跑起来看金星。sad_face 让他<b>自己尝试</b>，不会就看提示 1，不求完美。</td><td>他会不会在改完一处后<b>主动运行</b>？（这是「每步都跑」的习惯）输了 / 赢了时表情——游戏感出来了吗？</td></tr>
<tr><td><b>38–46</b></td><td>🧪 测试 + 虫虫医院</td><td>「现在你是捣蛋鬼」：按清单 5 项逐个试。<br>病号 1（逻辑错，不报错）：对着规则表找。病号 2（报错）：让他读红框，自己说出 = 和 == 的区别。</td><td>病号 1 他是读代码找到的，还是乱改碰到的？</td></tr>
<tr><td><b>46–52</b></td><td>🤖 排错伙伴</td><td>如果今天有真实 bug（通常有），用画板红框的按钮生成排错话术，贴给 AI，<b>只要提示</b>。没有 bug 就把病号 1 改坏再问。对比页面上的好问题 / 坏问题。</td><td>AI 给了答案他会直接贴，还是自己改？</td></tr>
<tr><td><b>52–57</b></td><td>🦎 第 6 步（选做）/ 🎮 游戏</td><td>时间够就看 beats 列表（「一行代替十行」）；不够就玩虫虫医院 1–2 关。</td><td></td></tr>
<tr><td><b>57–60</b></td><td>📓 收尾</td><td>第 4 步或第 5 步的版本存到作品墙（rps-step4）。笔记本 3 行 + 「AI 帮我排错的一次」。看作业页：🥉 是把 TODO 补完 + 捣蛋测试。</td><td>能说出「我今天自己写了 ___」吗？</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>第 1–4 步</b> &gt; 测试清单 &gt; 病号 2 &gt; 排错模板 &gt; 第 5 步 &gt; 病号 1 &gt; 第 6 步 &gt; 游戏。<br>
第 4 步做完就是一个完整的游戏，<b>宁可停在这里把它玩透</b>，也不要赶第 5 步。第 6 步完全可以留给作业 🥇。
</div>

---

## 🗣️ 好用的话术（手放背后专用）

- 「这一步你想让它做什么？用中文说一遍。」（先说再写）
- 「跑一下？」（每改一处就问，养成习惯）
- 「报错说第几行？那一行你自己读一遍。」
- 「小词典 / 笔记本里有没有？」
- 「你觉得问 AI 的时候要告诉它什么？」（引出三件套）
- 「你刚才自己找到了那个 bug！」（夸过程）
- 绝不说：「应该写 ___」。实在要帮，就说「看看第 3 步你是怎么写的」。

## 🐞 常见卡点和应对

| 卡点 | 表现 | 怎么办 |
|---|---|---|
| 中文引号 / 括号 | SyntaxError，画板会指出中文符号 | 让他切换输入法重打那个符号 |
| and 写成 or | 测试第 3 行变成「赢」 | 「布和石头，电脑出石头……or 的意思是什么？」 |
| 忘了 continue 的意思 | 输入香蕉后 rounds 还是加了 / 没加搞不清 | 让他打印 rounds 验证 |
| 分加错变量 | 比分反了 | 排错模板问 AI 的最佳时机 |
| = 和 == | 病号 2 | 「一个 = 是放进去，两个是问一样吗」 |
| 循环停不下来 | 一直问 | 按「■ 停下」，看 while 的条件和安全带 |
| 想一口气写完 | 跳过运行 | 「先跑一下，再加下一步」 |

---

## ✅ 参考答案

<details class="hint"><summary>第 3 步 judge()</summary><pre>elif me == "剪刀" and computer == "布":
    return "赢"
elif me == "布" and computer == "石头":
    return "赢"</pre></details>

<details class="hint"><summary>第 4 步加分</summary><pre>if result == "赢":
    my_score = my_score + 1
elif result == "输":
    computer_score = computer_score + 1</pre>5 分制只改一处：开头 <code>target = 5</code>，while 里用 <code>my_score &lt; target and computer_score &lt; target</code>。</details>

<details class="hint"><summary>第 5 步 sad_face</summary><pre>def sad_face(x, y):
    t.penup(); t.goto(x, y); t.pendown()
    t.color("gray")
    t.circle(25)
    t.penup(); t.goto(x - 10, y + 32); t.dot(6)
    t.goto(x + 10, y + 32); t.dot(6)
    t.goto(x - 12, y + 10); t.setheading(60); t.pendown()
    t.circle(14, -120)
    t.setheading(0)
# 在「输」的分支里：
sad_face(-200 + computer_score * 100, -100)</pre></details>

<details class="hint"><summary>病号 1 / 病号 2</summary>病号 1：第三个 elif 应为 <code>me == "布" and computer == "石头"</code>。<br>病号 2：<code>if result == "赢":</code>（两个等号）。</details>

<details class="hint"><summary>作业 🥉🥈🥇</summary><pre>def judge(me, computer):
    if me == computer:
        return "平"
    elif me == "石头" and computer == "剪刀":
        return "赢"
    elif me == "剪刀" and computer == "布":
        return "赢"
    elif me == "布" and computer == "石头":
        return "赢"
    else:
        return "输"
# 循环里：
if result == "赢":
    my_score = my_score + 1
elif result == "输":
    computer_score = computer_score + 1
# 🥈 平局统计：play_game 里加 ties = 0，平局时 ties = ties + 1，
#    return my_score, computer_score, ties；外面 mine, theirs, t = play_game()
# 🥇 作弊模式：电脑出拳前
#    if random.random() &lt; 0.3: computer = beats_me(me)  （先写一个交回「能赢 me 的拳」的函数）</pre></details>

---

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 6 步做到了第几步？ | |
| 哪一步是完全自己写出来的？ | |
| 遇到 bug 的第一反应：读报错 / 问老师 / 乱改 / 问 AI？ | |
| 用排错模板问 AI 了吗？拿到提示后是自己改的吗？ | |
| 测试清单做了几项？发现了什么？ | |
| 作业等级预估（🥉🥈🥇） | |
