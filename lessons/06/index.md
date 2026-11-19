---
title: 第 6 课 · 今日任务
title_en: Lesson 6 · Today
lesson: "06"
tab: home
---

# 🧠 <span class="zh">第 6 课：会思考的机器——AI 是怎么学习的？</span><span class="en">Lesson 6: Thinking machines — how does AI learn?</span>

<p class="muted"><span class="zh">今天的目标：学会 <code>while</code>（一直重复，直到……），然后<b>自己写一个「规则版 AI」</b>，再和真正会学习的 AI 比一比：它们到底哪里不一样？</span><span class="en">Today's goal: learn <code>while</code> (keep repeating until…), then <b>write a "rule-based AI" yourself</b> and compare it with an AI that really learns. What's the difference?</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">🔁</div><b><span class="zh">while 循环</span><span class="en">while loops</span></b><br><span class="muted"><span class="zh">没到站就继续坐</span><span class="en">Stay on until your stop</span></span></div>
  <div class="card"><div class="big-emoji">✅</div><b>True / False</b><br><span class="muted"><span class="zh">and、or、not</span><span class="en">and, or, not</span></span></div>
  <div class="card"><div class="big-emoji">🕵️</div><b><span class="zh">动物猜猜猜</span><span class="en">Animal guesser</span></b><br><span class="muted"><span class="zh">我写规则的 AI</span><span class="en">An AI with my rules</span></span></div>
  <div class="card"><div class="big-emoji">📸</div><b>Teachable Machine</b><br><span class="muted"><span class="zh">从例子学的 AI</span><span class="en">An AI that learns from examples</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<p><span class="zh">点一下就能打勾 ✅。全部完成有徽章！</span><span class="en">Click to tick ✅. Finish them all for a badge!</span></p>

<div class="progress" data-for="l6"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l6"></span></p>

<ul class="quests" data-key="l6">
  <li><b>🔁 <span class="zh">热身：行星之旅</span><span class="en">Warm-up: planet tour</span></b> <span class="pill">5 min</span><br><span class="zh">上节课的列表 + in + append。for 循环能保证去遍 8 颗行星吗？</span><span class="en">Last lesson's lists + in + append. Can a for loop guarantee visiting all 8 planets?</span> <a href="learn/#warmup"><span class="zh">去热身 →</span><span class="en">Warm up →</span></a></li>
  <li><b>🚀 <span class="zh">新魔法：while</span><span class="en">New magic: while</span></b> <span class="pill">12 min</span><br><span class="zh">倒计时（先在纸上跟着 n 走）、停不下来的程序、太空日志（while True + break）。</span><span class="en">Countdown (trace n on paper first), a program that can't stop, a space log (while True + break).</span> <a href="learn/#magic"><span class="zh">学一学 →</span><span class="en">Learn →</span></a></li>
  <li><b>🔐 <span class="zh">and / or / not：秘密基地 + 猜数字 2.0</span><span class="en">and / or / not: secret base + guess 2.0</span></b> <span class="pill">13 min</span><br><span class="zh">用两个条件管一个 while，结束后自己写「谁赢了」；再用旗子变量等一个 🚩 发射窗口。</span><span class="en">Two conditions running one while, then write "who won" yourself; then wait for a 🚩 launch window with a flag variable.</span> <a href="learn/#bool"><span class="zh">去开门 →</span><span class="en">Open the door →</span></a></li>
  <li><b>🕵️ <span class="zh">写一个规则版 AI：动物猜猜猜</span><span class="en">Write a rule-based AI: animal guesser</span></b> <span class="pill">12 min</span><br><span class="zh">先不插电，再写代码——蝙蝠的规则你来写。</span><span class="en">Unplugged first, then code — you write the bat rule.</span> <a href="learn/#rules"><span class="zh">去写规则 →</span><span class="en">Write the rules →</span></a></li>
  <li><b>📸 <span class="zh">训练一个会学习的 AI</span><span class="en">Train an AI that learns</span></b> <span class="pill">10 min</span><br><span class="zh">Teachable Machine：先用好例子，再用坏例子，看它怎么学坏。</span><span class="en">Teachable Machine: good examples first, then bad ones — watch it learn badly.</span> <a href="learn/#tm"><span class="zh">去训练 →</span><span class="en">Train it →</span></a></li>
  <li><b>🔮 <span class="zh">玩游戏：读心术</span><span class="en">Play: Mind Reader</span></b> <span class="pill">🏠 <span class="zh">回家玩</span><span class="en">at home</span></span><br><span class="zh">猜猜代码会打印什么，过 1 关。</span><span class="en">Predict what the code prints. Beat 1 level.</span> <a href="{{ '/games/reader/' | relative_url }}"><span class="zh">去游戏 →</span><span class="en">Play →</span></a></li>
  <li><b>🏠 <span class="zh">看作业 + 写 3 行笔记</span><span class="en">Homework + 3 lines of notes</span></b> <span class="pill">5 min</span><br><span class="zh">作业是「动物侦探」。笔记本里多写一行：「写规则」和「从数据学」有什么不同。</span><span class="en">Homework is "Animal Detective". Add one extra line to your notebook: rules vs learning from data.</span> <a href="homework/"><span class="zh">看作业 →</span><span class="en">Homework →</span></a></li>
</ul>

<div class="box box-warn"><span class="box-title"><span class="zh">🛑 今天一定会遇到的事：程序停不下来</span><span class="en">🛑 It will happen today: a program that won't stop</span></span>
<span class="zh"><code>while</code> 写错了，程序就会<b>永远转圈</b>。不用慌：点画板上红色的 <b>■ 停下</b>，然后想一想「什么时候条件才会变成 False？」</span>
<span class="en">Get a <code>while</code> wrong and the program <b>spins forever</b>. No panic: click the red <b>■ Stop</b> on the playground, then ask "when does the condition become False?"</span>
</div>

<div class="box box-rule"><span class="box-title"><span class="zh">🤝 今天的大问题</span><span class="en">🤝 Today's big question</span></span>
<span class="zh">我们写的动物猜猜猜，<b>只知道我们告诉它的规则</b>。真正的 AI 是<b>从很多例子里自己找规律</b>。例子不好，它就学不好——这是 AI 最重要的秘密。</span>
<span class="en">Our animal guesser <b>only knows the rules we gave it</b>. Real AI <b>finds patterns in lots of examples by itself</b>. Bad examples, bad learning — that's AI's most important secret.</span>
</div>

<div class="box box-think"><span class="box-title"><span class="zh">🚀 做得快？挑战在等你</span><span class="en">🚀 Finished early? A challenge awaits</span></span>
<span class="zh"><a href="learn/#challenge">🏆 太空知识闯关</a>：3 条命，while + and + 两个计数器——题目准备好了，游戏你来设计。</span>
<span class="en"><a href="learn/#challenge">🏆 Space quiz</a>: 3 lives, while + and + two counters — the questions are ready; you design the game.</span>
</div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 6 课教案</span><span class="en">Lesson 6 plan</span></a></p>
