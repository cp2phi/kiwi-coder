---
title: 第 5 课 · 今日任务
title_en: Lesson 5 · Today
lesson: "05"
tab: home
---

# 🎰 <span class="zh">第 5 课：随机生成器</span><span class="en">Lesson 5: Random generators</span>

<p class="muted"><span class="zh">今天的目标：学会用<b>列表</b>管理一堆东西，然后让电脑<b>随机</b>从里面抽——做一台会讲笑话故事的机器！</span><span class="en">Today's goal: learn to keep a bunch of things in a <b>list</b>, then let the computer pick from it at <b>random</b> — and build a machine that tells silly stories!</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">📦</div><b><span class="zh">列表</span><span class="en">Lists</span></b><br><span class="muted"><span class="zh">一排带编号的抽屉</span><span class="en">A row of numbered drawers</span></span></div>
  <div class="card"><div class="big-emoji">🎲</div><b><span class="zh">搞笑故事生成器</span><span class="en">Silly story maker</span></b><br><span class="muted"><span class="zh">每次运行都不一样</span><span class="en">Different every run</span></span></div>
  <div class="card"><div class="big-emoji">🇳🇿</div><b><span class="zh">毛利语小测验</span><span class="en">Te reo Māori quiz</span></b><br><span class="muted"><span class="zh">会记分的</span><span class="en">It keeps score</span></span></div>
  <div class="card"><div class="big-emoji">🌈</div><b><span class="zh">彩虹六边形</span><span class="en">Rainbow hexagon</span></b><br><span class="muted"><span class="zh">海龟按列表换颜色</span><span class="en">Colours from a list</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<p><span class="zh">点一下就能打勾 ✅。全部完成有徽章！</span><span class="en">Click to tick ✅. Finish them all for a badge!</span></p>

<div class="progress" data-for="l5"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l5"></span></p>

<ul class="quests" data-key="l5">
  <li><b>🔁 <span class="zh">热身：掷骰子</span><span class="en">Warm-up: roll the dice</span></b> <span class="pill">5 min</span><br><span class="zh">用上节课的 if / elif 和 random，再加一个 for 循环。</span><span class="en">Last lesson's if / elif and random, plus a for loop.</span> <a href="learn/#warmup"><span class="zh">去热身 →</span><span class="en">Warm up →</span></a></li>
  <li><b>📦 <span class="zh">新魔法：列表</span><span class="en">New magic: lists</span></b> <span class="pill">10 min</span><br><span class="zh">抽屉编号从 0 开始！先猜再运行。</span><span class="en">Drawer numbers start at 0! Guess first, then run.</span> <a href="learn/#magic"><span class="zh">学一学 →</span><span class="en">Learn →</span></a></li>
  <li><b>🎲 <span class="zh">做一台搞笑故事生成器</span><span class="en">Build a silly story maker</span></b> <span class="pill">10 min</span><br><span class="zh">加上你自己的角色和地点。</span><span class="en">Add your own characters and places.</span> <a href="learn/#story"><span class="zh">去做 →</span><span class="en">Make it →</span></a></li>
  <li><b>🇳🇿 <span class="zh">毛利语单词小测验</span><span class="en">Te reo Māori word quiz</span></b> <span class="pill">10 min</span><br><span class="zh">填空让它记分，再问 AI 要 5 个新单词（要检验！）。</span><span class="en">Fill in the blank so it keeps score, then ask AI for 5 new words (and check them!).</span> <a href="learn/#quiz"><span class="zh">去测验 →</span><span class="en">Quiz →</span></a></li>
  <li><b>🎨 <span class="zh">玩游戏：图案复刻</span><span class="en">Play: Copy the Pattern</span></b> <span class="pill">🏠 <span class="zh">回家玩</span><span class="en">at home</span></span><br><span class="zh">复刻目标图案，至少过 2 关；第 5 关要用到今天的颜色列表！</span><span class="en">Copy the target drawings — beat at least 2 levels. Level 5 uses today's colour lists!</span> <a href="{{ '/games/copy/' | relative_url }}"><span class="zh">去游戏 →</span><span class="en">Play →</span></a></li>
  <li><b>🏠 <span class="zh">看作业 + 写 3 行笔记</span><span class="en">Homework + 3 lines of notes</span></b> <span class="pill">5 min</span><br><span class="zh">作业是「故事机 3000」。然后在 <a href="{{ '/notebook/' | relative_url }}">工程师笔记本</a> 写 3 行。</span><span class="en">Homework is "Story Machine 3000". Then write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">Engineer's Notebook</a>.</span> <a href="homework/"><span class="zh">看作业 →</span><span class="en">Homework →</span></a></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🤝 今天的约定：AI 说的要检验</span><span class="en">🤝 Today's deal: check what AI says</span></span>
<span class="zh">今天我们会请 AI 教几个毛利语单词。AI 有时候会<b>很自信地说错</b>——所以它给的每个词，都要找老师或字典核对一遍。</span>
<span class="en">Today we'll ask AI for some te reo Māori words. AI sometimes <b>sounds confident but is wrong</b> — so every word it gives us gets checked with the teacher or a dictionary.</span>
</div>

<div class="box box-good"><span class="box-title"><span class="zh">💡 从 0 开始数</span><span class="en">💡 Counting from 0</span></span>
<span class="zh">程序员数抽屉是从 <b>0</b> 开始的：第一个是 <code>[0]</code>，第二个是 <code>[1]</code>。今天大概会搞错一次——没关系，报错会告诉你。</span>
<span class="en">Programmers count drawers from <b>0</b>: the first is <code>[0]</code>, the second is <code>[1]</code>. You'll probably get it wrong once today — that's fine, the error will tell you.</span>
</div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 5 课教案</span><span class="en">Lesson 5 plan</span></a></p>
