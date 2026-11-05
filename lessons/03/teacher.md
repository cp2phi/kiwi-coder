---
title: 第 3 课 · 教案
title_en: Lesson 3 · Teacher plan
lesson: "03"
tab: teacher
---

# 👩‍🏫 第 3 课教案：重复的魔法（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子能自己说出「for 循环就是让电脑替我重复」，能写出正确的 `for i in range(n):` + 缩进，并发现「次数 × 角度 = 360」的规律。第一次把 AI 当老师用（请它解释，不要它写）。

**今天的铁律：** 每个画板都**先猜再运行**。老师不碰键盘；孩子猜错了，不要纠正，让他运行看结果。

**知识点：** for、range()、缩进。复习：变量（热身）、turtle。**不要**提前讲 if / while。列表只说「第 5 课学，先当魔法」。

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-3">
  <li>自己把 <a href="../learn/">学一学</a> 的 8 个画板全部跑一遍，特别是「缩进实验」：删掉空格看报错框显示的是不是「缩进」提示。</li>
  <li>玩一遍 <a href="{{ '/games/robot/' | relative_url }}">💎 宝石机器人</a> 前 3 关，知道哪一关开始必须用循环。</li>
  <li>看一眼孩子第 2 课的作业和笔记本，热身时提一句他上周做的东西。</li>
  <li>准备一张纸：写「次数 × 角度 = ___」，等孩子自己填出 360。</li>
  <li>确认 AI 工具（Codex / ChatGPT）能登录，用家长账号。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>打开热身画板。「上周的盒子还记得吗？改一个 size，几条边变了？」<br>让他数 forward 写了几次——「烦不烦？今天就治这个烦。」</td><td>能不能说出「变量 = 盒子」</td></tr>
<tr><td><b>5–15</b></td><td>✨ 新魔法</td><td>讲俯卧撑的比喻。看「以前 / 现在」对比。<b>先做猜一猜</b>再运行例 1。<br>改一改：6/60、8/45、3/120。拿出那张纸：「次数 × 角度 = ？」等他自己说 360。</td><td>他能不能自己发现 360？发现了就大声夸「你自己找到规律了」</td></tr>
<tr><td><b>15–25</b></td><td>🧪 例 2、例 3</td><td>例 2 多边形机：填 5、8、36、100。「100 条边像什么？」<br>例 3 螺旋：先做猜一猜（i=50 走几步）。改 59 → 90 → 91，感受 1 度的差别。</td><td>他是否理解「i 每次在变」。可以让他口头数：第 0 次走 0，第 1 次走 2……</td></tr>
<tr><td><b>25–33</b></td><td>🔮 例 4 + 文字</td><td>万花筒：先做猜一猜（48 次）。用手比划：「里面画完一个正方形，外面才转一下。」<br>倒计时例子 1 分钟带过。</td><td>嵌套循环不要求完全懂，能改数字玩出花样就够</td></tr>
<tr><td><b>33–38</b></td><td>🐞 缩进实验</td><td>让他<b>故意删空格</b>，运行，<b>自己读</b>红框。「电脑说哪一行？说了什么？」修好。</td><td>第一反应是慌还是读？引导他读</td></tr>
<tr><td><b>38–45</b></td><td>🤖 AI 解释</td><td>复制模板，挑一行他不懂的（通常是 <code>i % 6</code>）问 AI。读完让他<b>改代码验证</b>：把 6 改成 3 看颜色是不是 3 种轮流。</td><td>他会不会自己检验 AI 的话？这是今天的「渔」</td></tr>
<tr><td><b>45–52</b></td><td>💎 游戏</td><td>宝石机器人前 2–3 关。第 3 关指令太多，引导他：「能不能用 for？」</td><td>是否主动想到循环</td></tr>
<tr><td><b>52–57</b></td><td>🏆 挑战</td><td>花朵：填 12 和 30（或 36 和 10）。存到作品墙。</td><td>他记不记得「× = 360」</td></tr>
<tr><td><b>57–60</b></td><td>📓 收尾</td><td>让他给家人讲 <code>range(4)</code> 是什么。写笔记本 3 行。看作业页，说清楚 🥉 必做。</td><td>能否用自己的话说「重复」</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>例 1 + 360 规律</b> &gt; <b>例 3 螺旋</b> &gt; <b>缩进实验</b> &gt; AI 解释 &gt; 例 4 万花筒 &gt; 游戏 &gt; 挑战。<br>
万花筒和游戏可以留给作业周。宁可少，别赶。
</div>

---

## 🗣️ 好用的话术

- 「先别运行——**你猜会怎样？**」
- 「次数乘角度等于……？」（停住，等他说）
- 「电脑说**哪一行**？它抱怨了什么？」
- 「AI 说的对不对？**改一下试试就知道。**」
- 「你刚才**自己发现了** 360 的规律，这就是程序员干的事。」

## 🧱 常见卡点和应对

| 卡点 | 现象 | 怎么办 |
|---|---|---|
| 忘了冒号 | `for i in range(4)` 报 SyntaxError | 「for 这一行最后要有什么？」指指知识卡片 |
| 没缩进 / 缩进不齐 | IndentationError | 让他读报错框；用 Tab 键缩进（画板里 Tab = 4 空格） |
| `range(4)` 以为是 1–4 | 问「i 第一次是几」答 1 | 跑倒计时例子的 `print(i)`，亲眼看到 0 |
| 中文括号 | 报错框会提示「中文符号」 | 切输入法 |
| 螺旋转太快看不清 | 想看过程 | 把 `t.speed(0)` 改成 `t.speed(6)` |
| 嵌套循环看不懂 | 例 4 | 不强求。让他只改外面的数字，保证 × = 360 |

## ✅ 参考答案

<details class="hint"><summary>例 2 多边形机</summary><pre>sides = 8      # 任何 3 以上的整数都对</pre></details>
<details class="hint"><summary>挑战：花朵</summary><pre>for i in range(12):
    t.circle(70)
    t.left(30)      # 12 × 30 = 360；或 range(36) + left(10)</pre>
星星加分：<pre>import random  # （第 4 课才学 random，孩子用固定坐标也行）
for i in range(30):
    t.penup()
    t.goto(random.randint(-280, 280), random.randint(-280, 280))
    t.pendown()
    t.dot(5, "white")</pre></details>
<details class="hint"><summary>作业 🥉 倒计时</summary><pre>for i in range(3, 0, -1):
    print(i)
print("开工！")</pre></details>
<details class="hint"><summary>作业 🥈 螺旋</summary><pre>t.penup()
t.goto(-200, 0)
t.pendown()
colors = ["red", "gold"]
for i in range(80):
    t.color(colors[i % 2])
    t.pensize(i / 10)
    t.forward(i * 2)
    t.left(91)</pre></details>
<details class="hint"><summary>作业 🥇 万花筒（一种可能）</summary><pre>for i in range(18):
    t.color(colors[i % 2])
    for j in range(3):
        t.forward(90)
        t.left(120)
    t.left(20)      # 18 × 20 = 360</pre></details>

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 他自己说出 360 规律了吗？用了多久？ | |
| 第一次看到 IndentationError 的反应？ | |
| 问 AI 的那一行是什么？他检验了吗？ | |
| 宝石机器人玩到第几关？主动用循环了吗？ | |
| 下周要补的 | |
