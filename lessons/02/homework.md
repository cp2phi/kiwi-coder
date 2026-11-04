---
title: 第 2 课 · 作业
title_en: Lesson 2 · Homework
lesson: "02"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 2 课作业：聊天机器人 2000</span><span class="en">Lesson 2 homework: Chatbot 2000</span>

<p><span class="zh">做一个<b>属于你的聊天机器人</b>，它会问问题、会回应，还会算数、会画画！</span><span class="en">Build <b>your own chatbot</b> that asks questions, replies, does maths and even draws!</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week02-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：至少 3 个问题</span><span class="en">Must do: at least 3 questions</span></h3>
    <p><span class="zh">画板里已经有 2 个问题了。再加<b>至少 1 个</b>，每个问题的回应都要用 <code>f"…{盒子}…"</code>。最后一句话要<b>同时用到两个盒子</b>。</span><span class="en">The playground already has 2 questions. Add <b>at least 1 more</b>; every reply must use <code>f"…{box}…"</code>. The last line must use <b>two boxes at once</b>.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：会算数 + 会画画</span><span class="en">Bonus: maths + drawing</span></h3>
    <p><span class="zh">① 用 <code>int()</code> 问一个数字，算点东西（明年几岁？再过几年 18 岁？多少个月？）。② 程序最后问「你想要多大的正方形」，海龟画出那么大的正方形（起始代码里有一半了，试试再问颜色！）。</span><span class="en">① Use <code>int()</code> to ask for a number and calculate something (age next year? years until 18? months alive?). ② At the end, ask "how big a square?" and the turtle draws it that size (half is already there — try asking for the colour too!).</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战（选做）：问 AI 学一招</span><span class="en">Challenge (optional): learn a trick from AI</span></h3>
    <p><span class="zh">问 AI：「Python 里怎么把一个名字变成大写字母？只要提示。」把学到的用进去（比如 <code>name.upper()</code>），在代码里写一行注释：AI 教了我什么。</span><span class="en">Ask AI: "How do I make a name UPPERCASE in Python? Hint only." Use what you learn (like <code>name.upper()</code>) and add a comment: what AI taught me.</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>box = input("问题？ ")</code><span><span class="zh">问一个问题，答案放进盒子</span><span class="en">Ask, store the answer</span></span></div>
  <div class="cmd"><code>print(f"回应 {box}")</code><span><span class="zh">用盒子里的东西回应</span><span class="en">Reply using the box</span></span></div>
  <div class="cmd"><code>n = int(input("数字？ "))</code><span><span class="zh">要算数的，先变成数字</span><span class="en">Turn it into a number first</span></span></div>
  <div class="cmd"><code>t.forward(size)</code><span><span class="zh">海龟走「盒子里的数」那么远</span><span class="en">Walk as far as the number in the box</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。先猜会打印什么，再运行！</span><span class="en">Your code is saved on this computer automatically. Guess what it prints before you run it!</span></p>

<div class="playground" data-src="{{ '/lessons/02/code/homework.py' | relative_url }}" data-title="🤖 聊天机器人 2000" data-title-en="🤖 Chatbot 2000" data-save="week02-homework" data-draft="l2-homework"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：加问题</span><span class="en">💡 Hint 1: adding a question</span></summary><span class="zh">复制 <code>food = input(…)</code> 和它下面的 <code>print(f"…")</code> 这两行，粘贴到 TODO 下面，把 <code>food</code> 改成新名字（比如 <code>game</code>），改问题和回应。</span><span class="en">Copy the two lines <code>food = input(…)</code> and the <code>print(f"…")</code> under it, paste them under the TODO, rename <code>food</code> (e.g. <code>game</code>) and change the words.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：算数</span><span class="en">💡 Hint 2: maths</span></summary><span class="zh"><code>age = int(input("你几岁？ "))</code> 然后 <code>print(f"再过 {18 - age} 年你就 18 岁了！")</code></span><span class="en"><code>age = int(input("How old? "))</code> then <code>print(f"{18 - age} years until you're 18!")</code></span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：海龟的颜色也问一问</span><span class="en">💡 Hint 3: ask for the turtle's colour too</span></summary><span class="zh"><code>colour = input("什么颜色？（英文） ")</code> 然后 <code>t.color(colour)</code>。注意：<code>t.color(colour)</code> 里<b>不要</b>加引号，因为 colour 是盒子。</span><span class="en"><code>colour = input("Which colour? (English) ")</code> then <code>t.color(colour)</code>. Note: <b>no</b> quotes in <code>t.color(colour)</code>, because colour is a box.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">运行一遍，<b>自己回答所有问题</b>，确认没有红色报错。</span><span class="en">Run it once, <b>answer every question yourself</b>, and check there's no red error.</span></li>
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week02-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b>, name it <code>week02-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 第 2 课下面写 3 行。</span><span class="en">Write 3 lines under Lesson 2 in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>正方形要写 4 遍 <code>forward</code>。下周我们学一个魔法，<b>1 行</b>就能让海龟重复 100 次——彩虹螺旋就是这么画出来的！</span><span class="en">🔮 <b>Next week:</b> a square takes 4 <code>forward</code> lines. Next week's magic makes the turtle repeat 100 times in <b>1 line</b> — that's how the rainbow spiral is drawn!</span></div>
