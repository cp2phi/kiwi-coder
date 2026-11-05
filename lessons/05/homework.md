---
title: 第 5 课 · 作业
title_en: Lesson 5 · Homework
lesson: "05"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 5 课作业：故事机 3000</span><span class="en">Lesson 5 homework: Story Machine 3000</span>

<p><span class="zh">做一台会讲故事、会出题、还会画画的机器——全靠<b>列表</b>！</span><span class="en">Build a machine that tells stories, asks quiz questions and draws — all powered by <b>lists</b>!</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week05-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：故事生成器</span><span class="en">Must do: story maker</span></h3>
    <p><span class="zh">画板里的 3 个列表，每个至少要有 <b>4 样东西</b>（加你自己的！），运行时打印 <b>3 个故事</b>。只要改列表就行。</span><span class="en">Each of the 3 lists in the playground needs at least <b>4 items</b> (add your own!), and it prints <b>3 stories</b>. Just change the lists.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：会记分、会记错题的测验</span><span class="en">Bonus: a quiz that keeps score and remembers mistakes</span></h3>
    <p><span class="zh">第 2 部分已经会记分了。把题目换成<b>你想考的</b>（毛利语、动物、你家人的生日……），答错的词会进 <code>wrong</code> 列表，最后打印出来。至少 5 题。</span><span class="en">Part 2 already keeps score. Change the questions to <b>anything you like</b> (te reo, animals, your family's birthdays…). Wrong answers go into the <code>wrong</code> list and get printed at the end. At least 5 questions.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：随机图形</span><span class="en">Challenge: random shapes</span></h3>
    <p><span class="zh">第 3 部分会从列表里随机选图形、颜色、大小。给 <code>shapes</code> 加一个新图形（五角星？六边形？），再加对应的 <code>elif</code>；然后用 <code>for</code> 循环一次画 5 个，放在不同位置（<code>penup</code> + <code>goto</code>）。</span><span class="en">Part 3 picks a random shape, colour and size from lists. Add a new shape to <code>shapes</code> (a star? a hexagon?) with its own <code>elif</code>; then use a <code>for</code> loop to draw 5 of them in different places (<code>penup</code> + <code>goto</code>).</span></p>
  </div></div>
</div>

<div class="cmds small">
  <div class="cmd"><code>random.choice(列表)</code><span><span class="zh">随机抽一个</span><span class="en">Pick one</span></span></div>
  <div class="cmd"><code>列表.append(x)</code><span><span class="zh">加到最后</span><span class="en">Add to the end</span></span></div>
  <div class="cmd"><code>random.randint(50, 150)</code><span><span class="zh">随机大小</span><span class="en">Random size</span></span></div>
  <div class="cmd"><code>t.penup() / t.goto(x, y) / t.pendown()</code><span><span class="zh">换个地方画</span><span class="en">Draw somewhere else</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。三个部分在同一个文件里，从上往下跑：先打印故事，再出题，最后画画。</span><span class="en">Your code is saved on this computer automatically. All three parts are in one file and run top to bottom: stories, then quiz, then drawing.</span></p>

<div class="playground" data-src="{{ '/lessons/05/code/homework.py' | relative_url }}" data-title="🎰 故事机 3000" data-title-en="🎰 Story Machine 3000" data-save="week05-homework" data-draft="l5-homework" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：列表里的逗号</span><span class="en">💡 Hint 1: commas in lists</span></summary><span class="zh">每样东西之间要有逗号，最后一个后面不用。忘了逗号，电脑会说「看不懂这一行」——而且常常指向<b>下一行</b>。</span><span class="en">Every item needs a comma between it and the next; none after the last one. Miss a comma and the computer says it can't read the line — often pointing at the <b>next</b> line.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：画 5 个图形</span><span class="en">💡 Hint 2: drawing 5 shapes</span></summary><span class="zh">把「从 <code>shape = random.choice(shapes)</code> 到最后」整段放进 <code>for k in range(5):</code> 里（缩进！）。每次开始前 <code>t.penup()</code>、<code>t.goto(random.randint(-200, 200), random.randint(-200, 200))</code>、<code>t.pendown()</code>。</span><span class="en">Put everything from <code>shape = random.choice(shapes)</code> to the end inside <code>for k in range(5):</code> (indent!). Before each one: <code>t.penup()</code>, <code>t.goto(random.randint(-200, 200), random.randint(-200, 200))</code>, <code>t.pendown()</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：五角星</span><span class="en">💡 Hint 3: a star</span></summary><span class="zh">5 条边，每次 <code>t.left(144)</code>。</span><span class="en">5 sides, <code>t.left(144)</code> each time.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week05-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week05-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh this page — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行：学会了什么 / 卡在哪里 / 怎么解决的。</span><span class="en">Write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what I learned / where I got stuck / how I fixed it.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>一种新的重复——<code>while</code>，「没猜对就一直猜」。还有一个大问题：<b>AI 到底是怎么学习的？</b>我们会自己写一个「规则版 AI」，再和真正会学习的 AI 比一比。</span><span class="en">🔮 <b>Next week:</b> a new kind of repeating — <code>while</code>, "keep guessing until you're right". And a big question: <b>how does AI actually learn?</b> We'll write a "rule-based AI" and compare it with one that really learns.</span></div>
