---
title: 第 9 课 · 今日任务
title_en: Lesson 9 · Today
lesson: "09"
tab: home
---

# 🕵️ <span class="zh">第 9 课：做一个聪明的 AI 用户</span><span class="en">Lesson 9: Being a smart AI user</span>

<p class="muted"><span class="zh">今天的目标：学会<b>字典</b>这个新魔法，同时变成一个<b>AI 侦探</b>——AI 说的话，我会检验！从这一课开始，大部分代码<b>你自己写</b>，老师只回答问题。</span><span class="en">Today's goal: learn the <b>dictionary</b> magic and become an <b>AI detective</b> who checks what AI says. From now on <b>you</b> write most of the code; the teacher only answers questions.</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">📖</div><b><span class="zh">一本会说话的词典</span><span class="en">A talking dictionary</span></b><br><span class="muted"><span class="zh">毛利语翻译机</span><span class="en">Te reo translator</span></span></div>
  <div class="card"><div class="big-emoji">🪐</div><b><span class="zh">行星资料库 + 数数</span><span class="en">Planet database + counting</span></b><br><span class="muted"><span class="zh">.items()、数数公式</span><span class="en">.items(), the counting line</span></span></div>
  <div class="card"><div class="big-emoji">🕵️</div><b><span class="zh">AI 侦探证书</span><span class="en">AI detective badge</span></b><br><span class="muted"><span class="zh">抓到 AI 的一个错误</span><span class="en">catch an AI mistake</span></span></div>
  <div class="card"><div class="big-emoji">🔒</div><b><span class="zh">隐私红线</span><span class="en">Privacy red lines</span></b><br><span class="muted"><span class="zh">什么不能告诉 AI</span><span class="en">what never to tell AI</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<p><span class="zh">点一下就能打勾 ✅。全部完成有徽章！</span><span class="en">Click to tick ✅. Finish them all for a badge!</span></p>

<div class="progress" data-for="l9"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l9"></span></p>

<ul class="quests" data-key="l9">
  <li><div><b>🔁 <span class="zh">热身：函数 + 整理输入</span><span class="en">Warm-up: function + tidy input</span></b> <span class="pill">5 min</span><br><a href="learn/#warmup"><span class="zh">数一数乱七八糟的出拳记录 →</span><span class="en">Count a messy list of moves →</span></a></div></li>
  <li><div><b>📖 <span class="zh">新魔法：字典</span><span class="en">New magic: dictionaries</span></b> <span class="pill">15 min</span><br><a href="learn/#dict"><span class="zh">第一个字典、追踪题、会学新词的翻译机 →</span><span class="en">First dict, a trace puzzle, a translator that learns →</span></a></div></li>
  <li><div><b>🪐 <span class="zh">进阶：行星资料库 + 用字典数数</span><span class="en">Stretch: planet database + counting with a dict</span></b> <span class="pill">10 min</span><br><a href="learn/#planets"><span class="zh">抽屉里放列表、.items()、数数公式 →</span><span class="en">Lists in drawers, .items(), the counting line →</span></a></div></li>
  <li><div><b>🕵️ <span class="zh">AI 侦探训练</span><span class="en">AI detective training</span></b> <span class="pill">13 min</span><br><a href="learn/#detective"><span class="zh">AI 会编造（太空题 + 代码题）、怎么核实、隐私红线、提好问题 →</span><span class="en">AI makes things up (space + code rounds), how to check, privacy, good questions →</span></a></div></li>
  <li><div><b>🔍 <span class="zh">侦探行动：找出 AI 的 2 个错</span><span class="en">Detective mission: catch the AI's 2 mistakes</span></b> <span class="pill">10 min</span><br><a href="learn/#mission"><span class="zh">运行、逐条核实、写上来源 →</span><span class="en">Run it, check every answer, note your sources →</span></a></div></li>
  <li><div><b>📓 <span class="zh">作业预览 + 写笔记本</span><span class="en">Homework preview + notebook</span></b> <span class="pill">5 min</span><br><span class="zh">看看<a href="homework/">作业</a>，然后在 <a href="{{ '/notebook/' | relative_url }}">工程师笔记本</a> 写 3 行，再写一行「我抓到 AI 的一个错误」。</span><span class="en">Look at the <a href="homework/">homework</a>, then write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">Engineer's Notebook</a>, plus one line: "an AI mistake I caught".</span></div></li>
  <li><div><b>🎮 <span class="zh">回家玩：密码破译</span><span class="en">At home: Secret Code</span></b> <span class="pill"><span class="zh">选做</span><span class="en">optional</span></span><br><a href="{{ '/games/secret/' | relative_url }}"><span class="zh">去游戏板块 →</span><span class="en">Go to the games →</span></a></div></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🤝 这一课的约定：我是队长，AI 是队员</span><span class="en">🤝 This lesson's deal: I'm the captain, AI is on my team</span></span>
<span class="zh">队员说的话，队长要<b>检查</b>。AI 不是不能用，而是<b>不能不检查就用</b>。今天你会亲手抓到它的错。</span>
<span class="en">The captain <b>checks</b> what the team says. It's fine to use AI — it's not fine to use it <b>without checking</b>. Today you'll catch it making a mistake yourself.</span>
</div>

<div class="box box-good"><span class="box-title"><span class="zh">💡 第三阶段开始了：我做，老师看</span><span class="en">💡 Stage 3 starts: I build, teacher watches</span></span>
<span class="zh">从今天起，老师不再帮你打字。卡住了用四步法：读报错 → 翻笔记本 → 问 AI 要<b>提示</b> → 再问老师。</span>
<span class="en">From today the teacher doesn't type for you. Stuck? Use the 4 steps: read the error → check your notebook → ask AI for a <b>hint</b> → then ask the teacher.</span>
</div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 9 课教案</span><span class="en">Lesson 9 plan</span></a></p>
