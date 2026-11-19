---
title: 第 8 课 · 今日任务
title_en: Lesson 8 · Today
lesson: "08"
tab: home
---

# ✊ <span class="zh">第 8 课：迷你项目——石头剪刀布</span><span class="en">Lesson 8: Mini project — Rock Paper Scissors</span>

<p class="muted"><span class="zh">今天的目标：<b>第一次大部分自己写</b>，做出一个能和电脑对战、N 局几胜、会算胜率的游戏，再做一个<b>会学习的电脑对手</b>。老师只给提示，AI 当排错伙伴。</span><span class="en">Today's goal: <b>write most of it yourself</b> for the first time — a best-of-N game against the computer with win-rate stats, plus a <b>computer opponent that learns</b>. The teacher only hints; AI is your debugging buddy.</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">🧪</div><b><span class="zh">测试先行</span><span class="en">Tests first</span></b><br><span class="muted"><span class="zh">6 个 ❌ 变成 6 个 ✅</span><span class="en">turn 6 ❌ into 6 ✅</span></span></div>
  <div class="card"><div class="big-emoji">🧹</div><b><span class="zh">整理输入</span><span class="en">Tidy the input</span></b><br><span class="muted"><span class="zh">.strip() .lower()，问到合格为止</span><span class="en">.strip() .lower(), ask until valid</span></span></div>
  <div class="card"><div class="big-emoji">🔢</div><b><span class="zh">五局三胜 + 胜率</span><span class="en">Best of 5 + win rate</span></b><br><span class="muted"><span class="zh">while + 计数器</span><span class="en">while + counters</span></span></div>
  <div class="card"><div class="big-emoji">🧠</div><b><span class="zh">会学习的电脑</span><span class="en">A learning computer</span></b><br><span class="muted"><span class="zh">它在偷偷记你的习惯！</span><span class="en">it's secretly learning your habits!</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<div class="progress" data-for="l8"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l8"></span></p>

<ul class="quests" data-key="l8">
  <li><div><b>🔁 <span class="zh">热身：交回一个列表</span><span class="en">Warm-up: return a list</span></b> <span class="pill">5 min</span><br><a href="learn/#warmup"><span class="zh">去热身 →</span><span class="en">Warm up →</span></a></div></li>
  <li><div><b>🪜 <span class="zh">第 1–3 步：出拳、整理输入、judge() + 测试</span><span class="en">Steps 1–3: play, tidy input, judge() + tests</span></b> <span class="pill">17 min</span><br><span class="zh">电脑出拳 → 问到合格为止 → 自己写 judge，让 6 个测试全变 ✅。</span><span class="en">Computer plays → ask until valid → write judge yourself until all 6 tests are ✅.</span> <a href="learn/#step1"><span class="zh">开始搭 →</span><span class="en">Start building →</span></a></div></li>
  <li><div><b>🪜 <span class="zh">第 4 步：N 局几胜 + 统计</span><span class="en">Step 4: best of N + stats</span></b> <span class="pill">12 min</span><br><span class="zh">自己写加分、宣布赢家、胜率。</span><span class="en">Write the scoring, the winner and the win rate yourself.</span> <a href="learn/#step4"><span class="zh">继续 →</span><span class="en">Continue →</span></a></div></li>
  <li><div><b>🧪 <span class="zh">测试 + 虫虫医院</span><span class="en">Test + bug hospital</span></b> <span class="pill">8 min</span><br><span class="zh">当捣蛋鬼，再治好两个「不报错」的病号。</span><span class="en">Be a troublemaker, then cure two patients that don't crash.</span> <a href="learn/#test"><span class="zh">去测试 →</span><span class="en">Test →</span></a></div></li>
  <li><div><b>🧠 <span class="zh">第 5 步（进阶）：会学习的电脑</span><span class="en">Step 5 (stretch): a learning computer</span></b> <span class="pill">8 min</span><br><span class="zh">看懂它怎么学你，然后打败它！</span><span class="en">Work out how it learns you, then beat it!</span> <a href="learn/#step5"><span class="zh">去挑战 →</span><span class="en">Take it on →</span></a></div></li>
  <li><div><b>🏠 <span class="zh">看作业 + 写 3 行笔记</span><span class="en">Homework + 3 lines in the notebook</span></b> <span class="pill">5 min</span><br><span class="zh">看看 <a href="homework/">我的对战游戏</a>，然后在 <a href="{{ '/notebook/' | relative_url }}">笔记本</a> 写 3 行，特别记下<b>AI 帮你排错的一次</b>。</span><span class="en">Check <a href="homework/">My Battle Game</a>, then write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">notebook</a>, especially <b>a time AI helped you debug</b>.</span></div></li>
  <li><div><b>🎮 <span class="zh">回家玩：虫虫医院</span><span class="en">At home: Bug Hospital</span></b> <span class="pill"><span class="zh">选做</span><span class="en">optional</span></span><br><a href="{{ '/games/bugs/' | relative_url }}"><span class="zh">去玩 →</span><span class="en">Play →</span></a></div></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🤝 今天的约定：你写，老师只给提示</span><span class="en">🤝 Today's deal: you write, the teacher only hints</span></span>
<span class="zh">老师今天<b>手放背后</b>。卡住了按四步法：① 读报错 → ② 翻 <a href="{{ '/notebook/' | relative_url }}">笔记本</a> / <a href="{{ '/cheatsheet/' | relative_url }}">小词典</a> → ③ 用「排错模板」问 AI 要<b>提示</b>（不要答案）→ ④ 问老师。</span>
<span class="en">The teacher's <b>hands stay behind their back</b> today. Stuck? The 4 steps: ① read the error → ② check your <a href="{{ '/notebook/' | relative_url }}">notebook</a> / <a href="{{ '/cheatsheet/' | relative_url }}">cheat sheet</a> → ③ ask AI for a <b>hint</b> (not the answer) with the debugging template → ④ ask the teacher.</span>
</div>

<div class="box box-good"><span class="box-title"><span class="zh">💡 项目的秘诀：一次只做一小步</span><span class="en">💡 The project secret: one small step at a time</span></span>
<span class="zh">真正的程序员不会一口气写完整个游戏。他们先让电脑出拳（第 1 步），<b>运行，能跑</b>，再加下一步；每写一个招式，先用<b>测试</b>检查它。每一步都能跑、都测过，bug 就藏不住。</span>
<span class="en">Real programmers never write a whole game in one go. First the computer plays (step 1), <b>run it, it works</b>, then the next step; every new trick gets checked with <b>tests</b> first. When every step runs and is tested, bugs can't hide.</span>
</div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 8 课教案</span><span class="en">Lesson 8 plan</span></a></p>
