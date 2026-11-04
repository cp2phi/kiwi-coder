---
title: 第 11 课 · 今日任务
title_en: Lesson 11 · Today
lesson: "11"
tab: home
---

# 🛠️ <span class="zh">第 11 课：项目制作</span><span class="en">Lesson 11: Building the project</span>

<p class="muted"><span class="zh">今天的目标：把第 10 课的计划变成<b>能跑的程序</b>。你写、你测、你排错；老师只回答问题，<b>不给代码</b>。</span><span class="en">Today's goal: turn last week's plan into a <b>working program</b>. You write it, test it and fix it; the teacher only answers questions and <b>gives no code</b>.</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">🧰</div><b><span class="zh">排错工具箱</span><span class="en">A debugging toolbox</span></b><br><span class="muted"><span class="zh">4 招，一辈子都用得上</span><span class="en">4 tricks you'll use forever</span></span></div>
  <div class="card"><div class="big-emoji">⌨️</div><b><span class="zh">键盘 / 定时器 / 点击</span><span class="en">Keys / timers / clicks</span></b><br><span class="muted"><span class="zh">让程序「活」起来</span><span class="en">Make programs come alive</span></span></div>
  <div class="card"><div class="big-emoji">🏗️</div><b><span class="zh">我的项目 v1</span><span class="en">My project v1</span></b><br><span class="muted"><span class="zh">能跑的版本</span><span class="en">A version that runs</span></span></div>
  <div class="card"><div class="big-emoji">🧪</div><b><span class="zh">自己的测试</span><span class="en">My own tests</span></b><br><span class="muted"><span class="zh">让电脑帮你检查</span><span class="en">Let the computer check</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<p><span class="zh">点一下就能打勾 ✅。全部完成有惊喜！</span><span class="en">Click to tick ✅. Finish them all for a surprise!</span></p>

<div class="progress" data-for="l11"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l11"></span></p>

<ul class="quests" data-key="l11">
  <li><b>🔁 <span class="zh">热身：治好 3 个 bug</span><span class="en">Warm-up: cure 3 bugs</span></b> <span class="pill">5 min</span><br><a href="learn/#warmup"><span class="zh">去热身 →</span><span class="en">Warm up →</span></a></li>
  <li><b>🧰 <span class="zh">学 4 招排错</span><span class="en">Learn 4 debugging tricks</span></b> <span class="pill">10 min</span><br><a href="learn/#toolbox"><span class="zh">print 侦探、读报错、小黄鸭、二分法 →</span><span class="en">print detective, read the error, rubber duck, halving →</span></a></li>
  <li><b>⌨️ <span class="zh">游戏专用魔法</span><span class="en">Game magic</span></b> <span class="pill">8 min</span><br><a href="learn/#events"><span class="zh">方向键、定时器、点击 →</span><span class="en">arrow keys, timers, clicks →</span></a></li>
  <li><b>🏗️ <span class="zh">做项目：功能 1 → 测 → 功能 2 → 测</span><span class="en">Build: feature 1 → test → feature 2 → test</span></b> <span class="pill">30 min</span><br><a href="learn/#build"><span class="zh">开工清单 →</span><span class="en">Build checklist →</span></a></li>
  <li><b>📤 <span class="zh">存档到作品墙</span><span class="en">Save to the gallery</span></b> <span class="pill">2 min</span><br><span class="zh">文件名 <code>week11-project</code>。没做完也要存！</span><span class="en">Name it <code>week11-project</code>. Save even if it's not finished!</span></li>
  <li><b>📓 <span class="zh">笔记本 3 行 + 看作业</span><span class="en">3 notebook lines + homework</span></b> <span class="pill">5 min</span><br><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">工程师笔记本</a> 写：做到了 / 最难的 bug / 怎么解决的。看看 <a href="homework/">作业</a>。</span><span class="en">Write in your <a href="{{ '/notebook/' | relative_url }}">notebook</a>: got done / hardest bug / how I fixed it. Check the <a href="homework/">homework</a>.</span></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🤝 今天的约定：顾问模式</span><span class="en">🤝 Today's deal: consultant mode</span></span>
<span class="zh">老师<b>不碰键盘，不给代码</b>。卡住了就走四步法：① 读报错 → ② 翻笔记本 → ③ 问 AI 要<b>提示</b> → ④ 问老师。问老师的时候，老师也只会反问你：「报错说了什么？」「你觉得是哪一行？」「怎么验证？」</span>
<span class="en">The teacher <b>doesn't touch the keyboard and gives no code</b>. Stuck? Use the 4 steps: ① read the error → ② check your notebook → ③ ask AI for a <b>hint</b> → ④ ask the teacher. Even then the teacher only asks back: "What does the error say?" "Which line do you think?" "How can you check?"</span>
</div>

<div class="box box-good"><span class="box-title"><span class="zh">💾 每 15 分钟存一次</span><span class="en">💾 Save every 15 minutes</span></span>
<span class="zh">真正的程序员一天存档几十次。点 <b>📤 存到作品墙</b>，名字用 <code>week11-project</code>；提示「已存在」就加 <code>-v2</code>、<code>-v3</code>。坏了也能回去看上一版！</span>
<span class="en">Real programmers save dozens of times a day. Click <b>📤 Save to Gallery</b>, name it <code>week11-project</code>; if it says "already exists" add <code>-v2</code>, <code>-v3</code>. If something breaks you can go back!</span>
</div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 11 课教案</span><span class="en">Lesson 11 plan</span></a></p>
