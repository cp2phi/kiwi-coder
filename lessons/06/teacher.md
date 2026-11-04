---
title: 第 6 课 · 教案
title_en: Lesson 6 · Teacher plan
lesson: "06"
tab: teacher
---

# 👩‍🏫 第 6 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 两件事。① 语法：会用 `while`、计数器 `+= 1`、`and / or / not`，并且**亲手经历一次死循环并自己停下来**。② 概念：能用自己的话说出「写规则的程序」和「从例子学的 AI」有什么不同，以及「例子不好 AI 就学歪」。这是整个课程里最重要的 AI 概念课。

**今天的铁律：** 让他写死循环，不要拦。点红色 ■ 的那一刻比任何讲解都管用。概念部分**多问少讲**：「为什么它把狗猜成猫？」「企鹅怎么办？」「写得完吗？」

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-6">
  <li>自己把 <a href="../learn/">学一学</a> 跑一遍，特别试一下删掉 <code>n = n - 1</code> 后点 ■ 停下是否正常。</li>
  <li>准备 10 张动物卡（手写纸条就行）：猫、狗、tui、kiwi、鲨鱼、金鱼、马、企鹅、蝙蝠、海龟。企鹅和蝙蝠是「陷阱卡」。</li>
  <li><b>Teachable Machine</b>：提前用 <a href="https://teachablemachine.withgoogle.com/train/image" target="_blank" rel="noopener">图片项目</a> 自己做一遍「好模型」和「坏模型」（坏模型：一类只拍 3 张且都在角落）。确认摄像头权限、网速。如果没有摄像头，用「Upload」上传手机照片也可以。</li>
  <li>想好一个和孩子兴趣相关的 AI 偏见例子（比如：只用白天照片训练的「认路」AI，晚上就不行了）。</li>
  <li>打开 <a href="{{ '/games/reader/' | relative_url }}">🔮 读心术</a>，看看第 1 关。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>列表 + random.choice。让他加 foods 列表，不给提示。顺便问「names[0] 是什么？」</td><td>上节课的「从 0 开始」还在吗</td></tr>
<tr><td><b>5–17</b></td><td>🚀 while</td><td>公交车比喻 1 分钟。猜一猜「最后打印的是几」→ 运行倒计时。<br><b>关键 3 分钟：</b>让他删掉 <code>n = n - 1</code>，运行，看刷屏，<b>自己</b>点 ■。然后问：「什么时候 n &gt; 0 会变成 False？」<br>例 2 while True + break：改 10 → 3。<br>例 3 猜数字 2.0：玩一局，改成 1～100，问「最聪明怎么猜」（二分法，不用说术语）。</td><td>死循环时的第一反应是慌还是找按钮？能不能说出「条件永远是 True」</td></tr>
<tr><td><b>17–25</b></td><td>🔐 and / or / not</td><td>先做两个猜一猜（真值表），再运行秘密基地的门，试 4 种输入。让他把 and 改成 or，自己解释为什么密码错也能进。</td><td>and 和 or 会不会混</td></tr>
<tr><td><b>25–32</b></td><td>✂️ 不插电</td><td>动物卡游戏。他当「AI」，写 3 条规则分「鸟 / 不是鸟」，你出卡他按规则答。<b>然后出企鹅和蝙蝠。</b>规则错了→改规则→再出一张（鸵鸟？）。<br>💬「写得完吗？世界上有多少种动物？」</td><td>他有没有自己说出「规则永远写不完」</td></tr>
<tr><td><b>32–42</b></td><td>🕵️ 规则版 AI</td><td>运行动物猜猜猜，填空（蝙蝠 → "yes"）。想一只狗→被猜成猫→「为什么？」→加第 4 个问题「会汪汪叫吗」+ 一条规则。<br>提示 if/elif 顺序：具体的规则放前面。</td><td>能不能自己想到要加新问题，而不只是加 elif</td></tr>
<tr><td><b>42–52</b></td><td>📸 Teachable Machine</td><td>① 好模型：拳头 / 手掌各 20+ 张，训练，测试。② 坏模型：拳头只拍 3 张且全在左上角。测试：拳头放中间→它可能说「手掌」。<br>💬「它学到的规律可能是什么？」（左上角 = 拳头）「这叫数据偏见。如果认人脸的 AI 只见过一种人呢？」</td><td>他能不能说出「例子少 / 例子偏 → 学歪」。这句话要写进笔记本</td></tr>
<tr><td><b>52–56</b></td><td>🌀 海龟 while（可选）</td><td>时间够就跑 spiral.py，改 250 → 100。不够就跳过，作业里有。</td><td></td></tr>
<tr><td><b>56–60</b></td><td>📓 收尾</td><td>作业页：🥉 只要加 elif。笔记本 3 行 + 「规则 vs 数据」1 行。读心术第 1 关留作家庭任务。</td><td>用自己的话复述「规则 vs 学习」</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>while + 死循环体验</b> &gt; <b>动物猜猜猜 + 不插电</b> &gt; <b>Teachable Machine 坏模型</b> &gt; and/or/not（作业里会复习）&gt; 海龟 while &gt; 猜数字 2.0。<br>Teachable Machine 网络不好时：只做「坏模型」部分，用上传照片；或者口头讨论「如果只给它 3 张图会怎样」。</div>

---

## 🗣️ 好用的话术

- 「别慌，红色按钮在哪？」（死循环时只说这一句）
- 「**什么时候**条件会变成 False？」（每个 while 都问）
- 「and 是『而且』，or 是『或者』——你要的是哪个？」
- 「它为什么把狗猜成猫？是它笨，还是**我们**没告诉它？」
- 「这个模型学到的规律可能是什么？我们怎么知道？」（引出：很难知道 AI 学了什么）
- 夸过程：「你自己发现要加新问题，而不是只加规则——这就是在设计程序。」

## 🧱 常见卡点

| 卡点 | 怎么办 |
|---|---|
| 死循环刷屏，不知道怎么办 | 指一下红色 ■。然后让他自己说出少了哪一行 |
| `while` 后面忘记冒号 / 缩进 | 和 for 一样——「for 是怎么写的？」 |
| `tries += 1` 看不懂 | 让他把它改写成 `tries = tries + 1`，两种都认得就行 |
| `and` / `or` 混用 | 回到真值表猜一猜；用「而且 / 或者」翻译一遍 |
| 回答 `Yes`（大写）程序不认 | 这是真实的 bug！先让他发现，告诉他下节课（第 8 课）会学 `.lower()` 解决 |
| 填空写了 `yes` 没引号 | 报错「不认识 yes」→ 引号 |
| Teachable Machine 坏模型居然没学坏 | 也行：说「这次运气好；例子只有 3 张，换个光线再试」，或者让拳头的 3 张图都带一个明显的背景物 |

---

## ✅ 参考答案

<details class="hint"><summary>倒计时：从 1 数到 10</summary><pre>n = 1
while n <= 10:
    print(n)
    n = n + 1</pre></details>
<details class="hint"><summary>动物猜猜猜：加「会汪汪叫」认出狗</summary><pre>bark = input("它会汪汪叫吗？Does it bark? (yes/no) ")

if water == "yes":
    print("🦈 是鲨鱼 shark？")
elif fur == "yes" and bark == "yes":
    print("🐶 是狗 dog？")
elif fur == "yes" and fly == "no":
    print("🐱 是猫 cat？")
elif fur == "yes" and fly == "yes":
    print("🦇 是蝙蝠 bat？")
...</pre>（狗的规则要放在猫前面）</details>
<details class="hint"><summary>作业 🥈：两个计数器</summary><pre>questions_asked = 0
rounds = 0
while again == "yes":
    rounds += 1
    ...
    questions_asked += 4      # 问了 4 个问题
print(f"玩了 {rounds} 局，问了 {questions_asked} 个问题")</pre></details>
<details class="hint"><summary>海龟 while 换颜色</summary><pre>colours = ["red", "orange", "gold", "green", "blue", "purple"]
i = 0
step = 5
while t.distance(0, 0) < 250:
    t.color(colours[i % 6])
    t.forward(step)
    t.left(30)
    step = step + 2
    i += 1</pre></details>

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 死循环时他做了什么？几秒钟找到 ■？ | |
| 他能说出「什么时候条件变 False」吗？ | |
| 不插电：企鹅 / 蝙蝠出来时他怎么改规则？ | |
| 他用自己的话怎么说「规则 vs 从数据学」？（原话记下来，第 12 课回顾用） | |
| Teachable Machine 坏模型学到了什么「规律」？他猜的是？ | |
| 下节课要复习什么？ | |
