---
title: 第 8 课 · 今日任务
title_en: Lesson 8 · Today
lesson: "08"
tab: home
---

# ✊ <span class="zh">第 8 课：迷你项目——石头剪刀布</span><span class="en">Lesson 8: Mini project — Rock Paper Scissors</span>

<p class="muted"><span class="zh">今天的目标：<b>第一次大部分自己写</b>，做出一个能和电脑对战、会记分的游戏。老师只给提示，AI 当排错伙伴。</span><span class="en">Today's goal: <b>write most of it yourself</b> for the first time — a game you can play against the computer, with scores. The teacher only hints; AI is your debugging buddy.</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">🪜</div><b><span class="zh">6 步搭起来</span><span class="en">Build it in 6 steps</span></b><br><span class="muted"><span class="zh">每一步都能运行</span><span class="en">every step runs</span></span></div>
  <div class="card"><div class="big-emoji">🧹</div><b><span class="zh">整理输入</span><span class="en">Tidy the input</span></b><br><span class="muted"><span class="zh">.strip() .lower()</span><span class="en">.strip() .lower()</span></span></div>
  <div class="card"><div class="big-emoji">🧪</div><b><span class="zh">测试你的游戏</span><span class="en">Test your game</span></b><br><span class="muted"><span class="zh">故意乱打，看它会不会坏</span><span class="en">type nonsense, see if it breaks</span></span></div>
  <div class="card"><div class="big-emoji">🏆</div><b><span class="zh">能玩的游戏</span><span class="en">A playable game</span></b><br><span class="muted"><span class="zh">带回家和家人对战</span><span class="en">take it home, beat your family</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<div class="progress" data-for="l8"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l8"></span></p>

<ul class="quests" data-key="l8">
  <li><div><b>🔁 <span class="zh">热身：函数 + 列表 + random</span><span class="en">Warm-up: functions + lists + random</span></b> <span class="pill">5 min</span><br><a href="learn/#warmup"><span class="zh">去热身 →</span><span class="en">Warm up →</span></a></div></li>
  <li><div><b>🪜 <span class="zh">第 1–3 步：出拳、整理输入、judge()</span><span class="en">Steps 1–3: play, tidy input, judge()</span></b> <span class="pill">18 min</span><br><span class="zh">电脑出拳 → 你出拳 → 写判断输赢的招式。</span><span class="en">Computer plays → you play → write the trick that decides the winner.</span> <a href="learn/#step1"><span class="zh">开始搭 →</span><span class="en">Start building →</span></a></div></li>
  <li><div><b>🪜 <span class="zh">第 4–5 步：记分 + 海龟庆祝</span><span class="en">Steps 4–5: scores + turtle celebration</span></b> <span class="pill">15 min</span><br><span class="zh">while 循环玩到 3 分，赢了画星星。</span><span class="en">while loop until 3 points, stars when you win.</span> <a href="learn/#step4"><span class="zh">继续 →</span><span class="en">Continue →</span></a></div></li>
  <li><div><b>🧪 <span class="zh">测试 + 虫虫医院</span><span class="en">Test + bug hospital</span></b> <span class="pill">8 min</span><br><span class="zh">故意乱打，再治好两个病号。</span><span class="en">Type nonsense on purpose, then cure two patients.</span> <a href="learn/#test"><span class="zh">去测试 →</span><span class="en">Test →</span></a></div></li>
  <li><div><b>🎮 <span class="zh">玩游戏：虫虫医院</span><span class="en">Play: Bug Hospital</span></b> <span class="pill">6 min</span><br><a href="{{ '/games/bugs/' | relative_url }}"><span class="zh">去玩 →</span><span class="en">Play →</span></a></div></li>
  <li><div><b>🏠 <span class="zh">看作业 + 写 3 行笔记</span><span class="en">Homework + 3 lines in the notebook</span></b> <span class="pill">5 min</span><br><span class="zh">看看 <a href="homework/">我的对战游戏</a>，然后在 <a href="{{ '/notebook/' | relative_url }}">笔记本</a> 写 3 行，特别记下<b>AI 帮你排错的一次</b>。</span><span class="en">Check <a href="homework/">My Battle Game</a>, then write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">notebook</a>, especially <b>a time AI helped you debug</b>.</span></div></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🤝 今天的约定：你写，老师只给提示</span><span class="en">🤝 Today's deal: you write, the teacher only hints</span></span>
<span class="zh">老师今天<b>手放背后</b>。卡住了按四步法：① 读报错 → ② 翻 <a href="{{ '/notebook/' | relative_url }}">笔记本</a> / <a href="{{ '/cheatsheet/' | relative_url }}">小词典</a> → ③ 用「排错模板」问 AI 要<b>提示</b>（不要答案）→ ④ 问老师。</span>
<span class="en">The teacher's <b>hands stay behind their back</b> today. Stuck? The 4 steps: ① read the error → ② check your <a href="{{ '/notebook/' | relative_url }}">notebook</a> / <a href="{{ '/cheatsheet/' | relative_url }}">cheat sheet</a> → ③ ask AI for a <b>hint</b> (not the answer) with the debugging template → ④ ask the teacher.</span>
</div>

<div class="box box-good"><span class="box-title"><span class="zh">💡 项目的秘诀：一次只做一小步</span><span class="en">💡 The project secret: one small step at a time</span></span>
<span class="zh">真正的程序员不会一口气写完整个游戏。他们先让电脑出拳（第 1 步），<b>运行，能跑</b>，再加下一步。每一步都能跑，bug 就藏不住。</span>
<span class="en">Real programmers never write a whole game in one go. First the computer plays (step 1), <b>run it, it works</b>, then the next step. When every step runs, bugs can't hide.</span>
</div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 8 课教案</span><span class="en">Lesson 8 plan</span></a></p>
