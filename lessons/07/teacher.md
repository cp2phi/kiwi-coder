---
title: 第 7 课 · 教案
title_en: Lesson 7 · Teacher plan
lesson: "07"
tab: teacher
---

# 👩‍🏫 第 7 课教案：把代码打包（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子能自己写出一个带参数的函数并在循环里调用它；能说出「def 是教，调用是表演」「参数是递进去的东西」「return 是交回来」。

**今天的铁律：** 这是第二阶段「一起做」的第 3 课。看到 `___` 老师**不碰键盘**；孩子卡住先问「小词典里有没有？」再给提示。今天的核心感受是「**改一处，全部都变**」——每次他改 def 里的数字时，请大声指出来。

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-7">
  <li>自己把 <a href="../learn/">学一学</a> 从头跑一遍，特别是例 5 小镇的 3 个空和例 4 的输出。</li>
  <li>打开 <a href="{{ '/games/robot/' | relative_url }}">💎 宝石机器人</a>，确认第 4 关以后确实需要函数（给孩子一个「非学不可」的理由）。</li>
  <li>检查第 6 课作业是否已交（<a href="{{ '/gallery/' | relative_url }}">作品墙</a>），在 <a href="{{ '/feedback/' | relative_url }}">老师的话</a> 写好反馈——开课先花 2 分钟聊反馈。</li>
  <li>准备一句「生活中的函数」比喻：点餐（「大份、辣」是参数）、遥控器按钮（按一下表演一次）、食谱（写一次做很多次）。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>💌 反馈 + 热身</td><td>聊上周作业反馈（夸过程）。做热身画板：填 while 的两个空。问：「少了 count + 1 会怎样？」让他自己按停。</td><td>还记得 while 的停下条件吗？列表下标会用吗？</td></tr>
<tr><td><b>5–17</b></td><td>✨ def 招式</td><td>先讲比喻（遥控器 / 教海龟新招）。<b>先做猜一猜</b>：画几个正方形？运行例 1。关键一问：「def 那几行运行的时候海龟动了吗？」<br>改一改：for 循环喊 5 次 + left(72) 变花；<b>只改 def 里的 80</b>，看全部变大——大声说「改一处，全变」。<br>例 2 参数：用点餐比喻。让他自己加 2 个颜色。</td><td>他能分清「教」和「喊」吗？会不会忘记冒号 / 缩进？（这是今天最常见的报错）</td></tr>
<tr><td><b>17–29</b></td><td>🏘️ 街 + return</td><td>例 3：「这就是你第 1 课画的房子！」先做 x 的猜一猜，再运行。让他加 colour 参数（提示：参数要「两头都加」——def 里加，喊的时候也加）。<br>例 4 return：<b>先在纸上写 7 行输出</b>再运行。说「return 就像把答案交回来，不 print 你是看不见的」。<br>scope 小画板：先猜，再运行，讲「函数里的 n 是它自己的」。不用深究。</td><td>return 和 print 分得清吗？（常见误解：以为 return 会显示）</td></tr>
<tr><td><b>29–41</b></td><td>🏙️ 小镇 + 挑战</td><td>例 5 填 3 个空，强调 <code>street(n)</code> 里喊 <code>house</code>：招式里喊招式。然后挑战：他自己的小镇，≥3 个函数。<b>老师手放背后</b>，只问「这个东西能不能变成一个招式？」</td><td>他会主动把重复代码变函数吗？参数命名有意义吗？</td></tr>
<tr><td><b>41–49</b></td><td>🎮 宝石机器人</td><td>玩 2–3 关。后面的关需要函数——这是学函数的「真实理由」。</td><td>卡关时他先想函数还是先复制粘贴？</td></tr>
<tr><td><b>49–55</b></td><td>🤖 和 AI 一起</td><td>把挑战里重复最多的几行贴给 AI，用页面上的问法。贴回来运行——跑得起来吗？找一行看不懂的追问。</td><td>他会检验 AI 的代码还是直接信？</td></tr>
<tr><td><b>55–60</b></td><td>📓 收尾</td><td>作品存到作品墙。笔记本 3 行。看作业页：🥉 必做是加屋顶 + 4 座房子。预告下周迷你项目。</td><td>能用自己的话说出 def / 参数 / return 吗？</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>例 1 + 改一改</b> &gt; <b>例 2 参数</b> &gt; <b>例 3 街</b> &gt; 例 4 return &gt; 例 5 小镇 &gt; 挑战 &gt; 游戏 &gt; AI。<br>
return 可以留到第 8 课 judge() 时再讲——那时候有真实需求。scope 小画板可以完全跳过。
</div>

---

## 🗣️ 好用的话术

- 「这几行是在<b>教</b>还是在<b>喊</b>？」（每次看到 def 和调用都问）
- 「你改了一个数字，几个正方形变了？为什么？」
- 「这个东西你画了几遍？能不能变成一个招式？」
- 「return 交回来的东西去哪了？你看得见吗？」
- 「参数要两头加：def 那头加了，喊的那头加了吗？」

## 🐞 常见卡点和应对

| 卡点 | 表现 | 怎么办 |
|---|---|---|
| 忘记冒号 | `SyntaxError` 在 def 那行 | 让他读报错，画板会提示「最后要有冒号」 |
| 缩进不一致 | `IndentationError` | 问「哪几行属于这个招式？」让他用 4 个空格对齐 |
| 教了没喊 | 运行什么都没画 | 「你教了它，喊了吗？」 |
| 参数数量不对 | `TypeError: ... missing` | 「def 要几个？你给了几个？」 |
| 以为 return 会显示 | 「怎么没东西？」 | 加 print 包住：`print(double(5))` |
| 在函数外用函数里的变量 | `NameError` | 回到 scope 小画板那句话 |

---

## ✅ 参考答案

<details class="hint"><summary>热身 warmup.py</summary><pre>while count &lt; 5:
    ...
    count = count + 1</pre></details>

<details class="hint"><summary>例 5 小镇 town.py</summary><pre>street(4)
tree(280, -150)
sun(200, 180, 40)</pre></details>

<details class="hint"><summary>作业 🥉 屋顶 + 🥈 树 / 太阳 / 黑夜 + 🥇 随机颜色</summary><pre>def house(x, y, size, colour):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup(); t.goto(x, y + size); t.pendown()
    t.fillcolor("firebrick")
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def tree(x, y):
    t.penup(); t.goto(x, y); t.pendown()
    t.color("saddlebrown"); t.left(90); t.forward(40); t.right(90)
    t.color("green"); t.begin_fill(); t.circle(25); t.end_fill()
    t.color("black")

def sun(x, y, r):
    t.penup(); t.goto(x, y); t.pendown()
    t.color("gold"); t.begin_fill(); t.circle(r); t.end_fill()
    t.color("black")

def random_colour():
    return random.choice(["tomato", "gold", "lightgreen", "skyblue", "plum"])

is_night = True
if is_night:
    turtle.bgcolor("midnightblue")
    t.penup(); t.goto(200, 180); t.dot(50, "lightyellow")
else:
    turtle.bgcolor("skyblue")
    sun(200, 180, 40)

for i in range(4):
    house(-250 + i * 130, -120, 90, random_colour())
tree(-290, -120)
tree(290, -120)</pre></details>

---

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 能不能自己写出一个带参数的函数？ | |
| 改一改时他最兴奋的是哪一步？ | |
| 今天的报错他第一反应是什么（读 / 问 / 乱改）？ | |
| AI 的代码他检验了吗？ | |
| 作业等级预估（🥉🥈🥇） | |
