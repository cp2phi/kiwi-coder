---
title: 第 2 课 · 今日任务
title_en: Lesson 2 · Today
lesson: "02"
tab: home
---

# 💬 <span class="zh">第 2 课：会聊天的程序</span><span class="en">Lesson 2: A program that chats</span>

<p class="muted"><span class="zh">今天的目标：让程序<b>记住东西</b>（变量），还能<b>听你说话</b>（input）。做一个会问名字、会回应的聊天机器人！</span><span class="en">Today's goal: make a program that <b>remembers things</b> (variables) and <b>listens to you</b> (input). Build a chatbot that asks your name and talks back!</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">📦</div><b><span class="zh">变量</span><span class="en">Variables</span></b><br><span class="muted"><span class="zh">带名字的盒子</span><span class="en">Boxes with names</span></span></div>
  <div class="card"><div class="big-emoji">🤖</div><b><span class="zh">聊天机器人</span><span class="en">A chatbot</span></b><br><span class="muted"><span class="zh">会问问题、会回应</span><span class="en">Asks and answers</span></span></div>
  <div class="card"><div class="big-emoji">🎨</div><b><span class="zh">名字画家</span><span class="en">Name Painter</span></b><br><span class="muted"><span class="zh">海龟写出你的名字</span><span class="en">The turtle writes your name</span></span></div>
  <div class="card"><div class="big-emoji">🔐</div><b><span class="zh">密码破译</span><span class="en">Secret Code</span></b><br><span class="muted"><span class="zh">用变量解开密码</span><span class="en">Crack codes with variables</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<p><span class="zh">点一下就能打勾 ✅。全部完成有惊喜！</span><span class="en">Click to tick ✅. Finish them all for a surprise!</span></p>

<div class="progress" data-for="l2"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l2"></span></p>

<ul class="quests" data-key="l2">
  <li><div><b>🔁 <span class="zh">热身：上周的房子</span><span class="en">Warm-up: last week's house</span></b> <span class="pill">5 min</span><br><span class="zh">给老师看你的作业，说说你是怎么画屋顶的。然后去 <a href="learn/#warmup">学一学</a> 的热身画板。</span><span class="en">Show your homework to your teacher and explain how you drew the roof. Then do the warm-up in <a href="learn/#warmup">Learn</a>.</span></div></li>
  <li><div><b>🔐 <span class="zh">玩游戏：密码破译第 1 关</span><span class="en">Play: Secret Code level 1</span></b> <span class="pill">🏠 <span class="zh">回家玩</span><span class="en">at home</span></span><br><a href="{{ '/games/secret/' | relative_url }}"><span class="zh">去破译密码 →</span><span class="en">Go crack the code →</span></a></div></li>
  <li><div><b>📦 <span class="zh">新魔法 1：变量</span><span class="en">New magic 1: variables</span></b> <span class="pill">10 min</span><br><a href="learn/#variables"><span class="zh">改 1 个数字，整个正方形一起变 →</span><span class="en">Change 1 number, the whole square changes →</span></a></div></li>
  <li><div><b>💬 <span class="zh">新魔法 2：input() 聊天</span><span class="en">New magic 2: chatting with input()</span></b> <span class="pill">12 min</span><br><a href="learn/#input"><span class="zh">让程序问你问题 →</span><span class="en">Make the program ask you questions →</span></a></div></li>
  <li><div><b>🎨 <span class="zh">名字画家 + 挑战</span><span class="en">Name Painter + challenge</span></b> <span class="pill">10 min</span><br><a href="learn/#name-art"><span class="zh">海龟写你的名字 →</span><span class="en">The turtle writes your name →</span></a></div></li>
  <li><div><b>🏠 <span class="zh">看看作业，开个头</span><span class="en">Look at the homework and start it</span></b> <span class="pill">10 min</span><br><a href="homework/"><span class="zh">聊天机器人 2000 →</span><span class="en">Chatbot 2000 →</span></a></div></li>
  <li><div><b>📓 <span class="zh">展示 + 写笔记本</span><span class="en">Show + write in your notebook</span></b> <span class="pill">5 min</span><br><span class="zh">给老师演示你的聊天机器人，然后在 <a href="{{ '/notebook/' | relative_url }}">工程师笔记本</a> 写 3 行。</span><span class="en">Demo your chatbot to your teacher, then write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">Engineer's Notebook</a>.</span></div></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🤝 今天的约定：先猜，再运行</span><span class="en">🤝 Today's deal: guess first, then run</span></span>
<span class="zh">每次点 ▶ 之前，先说出来：「我觉得它会打印……」猜错了更好——那说明你马上要学到新东西了！</span>
<span class="en">Before every ▶, say it out loud: "I think it will print…" Being wrong is even better — it means you're about to learn something new!</span>
</div>

<div class="box box-tip"><span class="zh">📖 指令忘了？去 <a href="{{ '/cheatsheet/' | relative_url }}">Python 小词典</a>。卡住了？用四步法：读报错 → 翻笔记本 → 问 AI 要提示 → 问老师。</span><span class="en">📖 Forgot a command? Check the <a href="{{ '/cheatsheet/' | relative_url }}">cheat sheet</a>. Stuck? Use the 4 steps: read the error → check your notebook → ask AI for a hint → ask your teacher.</span></div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 2 课教案</span><span class="en">Lesson 2 plan</span></a></p>
