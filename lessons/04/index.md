---
title: 第 4 课 · 今日任务
title_en: Lesson 4 · Today
lesson: "04"
tab: home
---

# 🎲 <span class="zh">第 4 课：猜数字游戏</span><span class="en">Lesson 4: Guess the number</span>

<p class="muted"><span class="zh">今天的目标：让程序<b>自己做决定</b>，做出第一个能玩的游戏；学会<b>卡住了怎么办</b>。</span><span class="en">Today's goal: make programs that <b>decide for themselves</b>, build your first playable game, and learn <b>what to do when stuck</b>.</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">🔀</div><b><span class="zh">if / else</span><span class="en">if / else</span></b><br><span class="muted"><span class="zh">今天的新魔法</span><span class="en">Today's new magic</span></span></div>
  <div class="card"><div class="big-emoji">🎲</div><b><span class="zh">随机数</span><span class="en">Random numbers</span></b><br><span class="muted"><span class="zh">电脑出题</span><span class="en">The computer picks</span></span></div>
  <div class="card"><div class="big-emoji">🎯</div><b><span class="zh">猜数字游戏</span><span class="en">Guessing game</span></b><br><span class="muted"><span class="zh">带回家给家人玩</span><span class="en">Take home for the family</span></span></div>
  <div class="card"><div class="big-emoji">🛟</div><b><span class="zh">四步法</span><span class="en">The 4 steps</span></b><br><span class="muted"><span class="zh">卡住了怎么办</span><span class="en">What to do when stuck</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<div class="progress" data-for="l4"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l4"></span></p>

<ul class="quests" data-key="l4">
  <li><div><b>🔁 <span class="zh">热身：倒计时 + 螺旋</span><span class="en">Warm-up: countdown + spiral</span></b> <span class="pill">5 min</span><br><a href="learn/#warmup"><span class="zh">上周的 for 循环还记得吗？→</span><span class="en">Remember last week's for loop? →</span></a></div></li>
  <li><div><b>🔀 <span class="zh">学一学：if 让程序做决定</span><span class="en">Learn: if makes decisions</span></b> <span class="pill">18 min</span><br><a href="learn/#magic"><span class="zh">if → 骰子 → % 太空报数 → 猜数字 →</span><span class="en">if → dice → % Space Fizz → guessing game →</span></a></div></li>
  <li><div><b>🛟 <span class="zh">学会四步法 + 找 bug 游戏</span><span class="en">The 4 steps + bug hunt</span></b> <span class="pill">10 min</span><br><a href="learn/#stuck"><span class="zh">治好 4 个病号程序（有一个没有红框！）→</span><span class="en">Cure 4 sick programs (one has no red box!) →</span></a></div></li>
  <li><div><b>🐞 <span class="zh">玩游戏：虫虫医院</span><span class="en">Play: Bug Hospital</span></b> <span class="pill">🏠 <span class="zh">回家玩</span><span class="en">at home</span></span><br><a href="{{ '/games/bugs/' | relative_url }}"><span class="zh">读报错、找 bug、过关 →</span><span class="en">Read errors, find bugs, win →</span></a></div></li>
  <li><div><b>🎯 <span class="zh">自己写猜数字的判断部分，给老师玩</span><span class="en">Write the guessing game's deciding part yourself, let your teacher play</span></b> <span class="pill">12 min</span><br><a href="learn/#guess"><span class="zh">去例 3 →</span><span class="en">Go to Example 3 →</span></a></div></li>
  <li><div><b>📓 <span class="zh">展示 + 写 3 行笔记</span><span class="en">Show + write 3 lines</span></b> <span class="pill">5 min</span><br><span class="zh">给老师讲讲 <code>==</code> 和 <code>=</code> 有什么不同，在 <a href="{{ '/notebook/' | relative_url }}">笔记本</a> 写 3 行 + 今天找到的 bug。看看 <a href="homework/">作业</a>。</span><span class="en">Tell your teacher the difference between <code>==</code> and <code>=</code>, write 3 lines + today's bugs in your <a href="{{ '/notebook/' | relative_url }}">notebook</a>. Check the <a href="homework/">homework</a>.</span></div></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🛟 从今天起：卡住了怎么办</span><span class="en">🛟 From today: when you're stuck</span></span>
<span class="zh">① <b>读报错</b>（哪一行？说了什么？）→ ② <b>翻笔记本</b> → ③ <b>问 AI 要提示</b>（不要答案）→ ④ <b>问老师</b>。以后每节课都用。</span>
<span class="en">① <b>Read the error</b> (which line? what does it say?) → ② <b>Check your notebook</b> → ③ <b>Ask AI for a hint</b> (not the answer) → ④ <b>Ask your teacher</b>. We use this every lesson from now on.</span>
</div>

<div class="box box-good"><span class="box-title"><span class="zh">💡 找 bug 是游戏，不是惩罚</span><span class="en">💡 Bug hunting is a game, not a punishment</span></span>
<span class="zh">真正的程序员一半时间都在找 bug。今天我们故意做了 4 个「生病」的程序，看你能不能当医生。</span>
<span class="en">Real programmers spend half their time hunting bugs. Today there are 4 "sick" programs on purpose — can you be the doctor?</span>
</div>

<div class="box box-think"><span class="box-title"><span class="zh">🚀 做得快？挑战在等你</span><span class="en">🚀 Finished early? A challenge awaits</span></span>
<span class="zh"><a href="learn/#challenge">🏆 火箭发射控制中心</a>：没有起始代码，只有设计说明——if 套 if + for 倒数，你来设计。</span>
<span class="en"><a href="learn/#challenge">🏆 Rocket launch control</a>: no starter code, just a design brief — nested ifs + a for countdown, designed by you.</span>
</div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 4 课教案</span><span class="en">Lesson 4 plan</span></a></p>
