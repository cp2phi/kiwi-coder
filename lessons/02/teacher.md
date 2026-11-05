---
title: 第 2 课 · 教案
title_en: Lesson 2 · Teacher plan
lesson: "02"
tab: teacher
---

# 👩‍🏫 第 2 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子能说出「变量是带名字的盒子」，能用 `input()` 做一个会问、会答的小程序，知道 `int()` 是把文字变数字。

**今天的铁律：** 每次运行前都问「**你猜它会打印什么？**」。老师不碰键盘；孩子打字慢没关系，所有例子都是「改」不是「从零写」。

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-2">
  <li>看一眼孩子交的第 1 课作业（作品墙 → week01-homework），准备一句具体的夸奖（夸过程：「你自己想出了屋顶要先转回朝右！」）。在 <a href="../../../feedback/">老师的话</a> 写两行。</li>
  <li>自己把 <a href="../learn/">学一学</a> 从头跑一遍，特别是 input() 的画板：输入框出现在黑色输出区下面，要按回车。</li>
  <li>打开 <a href="../../../games/secret/">密码破译</a> 第 1 关，确认自己会过。</li>
  <li>把「<code>"5" + 1</code>」那个故意的错误自己先看一遍报错长什么样。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>让孩子<b>给你讲</b>上周的房子是怎么画的。做热身画板的两个小任务（变红、变三角形）。<br>💬「想把正方形变大要改几个数字？4 个！要是 100 条边呢？」——制造「需要变量」的感觉。</td><td>他记得 360 ÷ 边数吗？会不会主动去查小词典？</td></tr>
<tr><td><b>5–10</b></td><td>🔐 游戏</td><td>密码破译第 1 关。这一关只用 print 和变量，先玩再学，让他带着「这是什么」的好奇进入新课。过不了就先放着，课后再回来。</td><td>他看到 <code>name = …</code> 的第一反应是什么？</td></tr>
<tr><td><b>10–22</b></td><td>📦 变量</td><td>例 1：<b>先做猜一猜</b>再运行。重点三件事：① f 是什么 ② 删掉 f 会怎样 ③ 拼错名字的 NameError。<br>例 2（最重要的「啊哈」时刻）：让他改 <code>size</code>，说出「只改了一个地方」。<br>例 3：填空 turn = ?，不要提示，让他试。</td><td>他能不能用自己的话说「盒子」？改 size 时眼睛有没有亮？</td></tr>
<tr><td><b>22–35</b></td><td>💬 input</td><td>例 4 聊天机器人：先猜最后一行打印什么，再运行、自己打字回答。改一改：加第 3 个问题（他自己复制粘贴）。<br>例 5 int()：先猜输入 12 会打印什么。<br>故意的错误 <code>"5" + 1</code>：<b>让他读红框</b>，再让他修。</td><td>复制粘贴改问题时，会不会忘记改盒子名字（两个问题都叫 animal）？</td></tr>
<tr><td><b>35–45</b></td><td>🎨 综合 + 挑战</td><td>例 6 名字画家：运行，改 size、改字号。<br>挑战：爱好聊天机器人，自己写第 3 个问题。做出来就 📤 存到作品墙。</td><td>他能不能独立完成「复制两行 → 改字」？</td></tr>
<tr><td><b>45–52</b></td><td>🏠 作业开头</td><td>打开作业页，一起读三个等级。<b>在课上把 🥉 的第 3 个问题加上</b>，这样回家时已经有了开头，不会面对空白。</td><td>—</td></tr>
<tr><td><b>52–57</b></td><td>📓 笔记</td><td>写 3 行。引导：「今天最有用的一个词是什么？」（期待：变量 / f / input / int）</td><td>—</td></tr>
<tr><td><b>57–60</b></td><td>🎤 展示</td><td>让他给家人演示聊天机器人，家人来回答问题。</td><td>讲得出「盒子」就算真学会了。</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>例 1 + 例 2（变量）</b> &gt; <b>例 4（input 聊天）</b> &gt; 例 5 int() &gt; 名字画家 &gt; 挑战 &gt; 游戏。<br>int() 来不及就放到作业里讲，先把「盒子」和「问问题」学扎实。
</div>

---

## 🗣️ 好用的话术

- 「**先别点运行，你猜会打印什么？**」（每次都问，猜错了更好）
- 「这个 <code>name</code> 是哪个盒子？盒子里现在是什么？」（用手比划一个盒子）
- 「电脑不认识 <code>nmae</code>——它说得对吗？为什么？」
- 「<code>"12"</code> 和 <code>12</code> 有什么不一样？」（有引号是文字，像写在纸条上的「12」，不能拿来算）
- 「你想让机器人问什么？你决定，你是队长。」

## 🧱 常见卡点

| 卡点 | 怎么办 |
|---|---|
| 中文引号 “ ” 或中文括号 | 画板会提示；让他把输入法切到英文重打 |
| 忘记写 f，打印出 `{name}` | 不要直接说。问：「它为什么把大括号原样打出来了？和上面那行有什么不同？」 |
| 复制粘贴后两个问题用同一个盒子名 | 让他运行看结果：后面的答案把前面的盖掉了——顺便学到「盒子里只能放一样东西」 |
| `int()` 时输入了文字（比如「十二」） | 读 ValueError 的解释；告诉他现在程序只认数字，以后会学怎么处理 |
| 在 `t.color(colour)` 里给盒子加了引号 | 问：「加了引号，电脑会去找盒子，还是把它当成颜色名字 colour？」 |
| 先用后定义（NameError） | 让他看报错第几行，再看那个盒子是在哪一行「做」的 |

## ✅ 参考答案

<details class="hint"><summary>例 3：side 和 turn</summary>
<pre>turn = 120   # 三角形。144 是五角星，90 是正方形</pre>
</details>

<details class="hint"><summary>故意的错误：文字 + 数字</summary>
<pre>age = "5"
print(int(age) + 1)
# 或者 age = 5（去掉引号）</pre>
</details>

<details class="hint"><summary>作业 🥉 + 🥈 一种写法</summary>
<pre>print("你好！我是你的聊天机器人 🤖")
name = input("你叫什么名字？ ")
print(f"你好，{name}！")
food = input("你最喜欢吃什么？ ")
print(f"{food}？我也想吃！")
game = input("你最喜欢什么游戏？ ")
print(f"{name} 喜欢边吃{food}边玩{game}，好惬意！")

age = int(input("你几岁了？ "))
print(f"再过 {18 - age} 年你就 18 岁啦！")

import turtle
size = int(input("你想要多大的正方形？ "))
colour = input("什么颜色？ ")
t = turtle.Turtle()
t.color(colour)
t.pensize(4)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)</pre>
</details>

<details class="hint"><summary>作业 🥇 AI 可能教的招</summary>
<code>name.upper()</code>（大写）、<code>name.lower()</code>（小写）、<code>len(name)</code>（几个字）、<code>name * 3</code>（重复三遍）。都可以直接在画板里试。
</details>

## 📝 观察记录

| 观察 | 记录 |
|---|---|
| 能用自己的话解释「变量」吗 | |
| 改 size 的「啊哈」时刻出现了吗 | |
| 复制粘贴改问题是否独立完成 | |
| 遇到报错的第一反应（读 / 问 / 放弃） | |
| 最兴奋的环节 | |
