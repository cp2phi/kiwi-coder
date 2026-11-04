---
title: 第 7 课 · 今日任务
title_en: Lesson 7 · Today
lesson: "07"
tab: home
---

# 📦 <span class="zh">第 7 课：把代码打包</span><span class="en">Lesson 7: Packing code into functions</span>

<p class="muted"><span class="zh">今天的目标：学会给一段代码<b>起名字</b>，以后一喊名字它就跑。写一次，用一百次！</span><span class="en">Today's goal: learn to <b>give a piece of code a name</b>, then run it just by calling the name. Write once, use a hundred times!</span></p>

<div class="grid">
  <div class="card"><div class="big-emoji">🥋</div><b><span class="zh">教海龟新招式</span><span class="en">Teach the turtle a trick</span></b><br><span class="muted"><span class="zh">def 一下，正方形随叫随到</span><span class="en">def it, and squares appear on demand</span></span></div>
  <div class="card"><div class="big-emoji">🏘️</div><b><span class="zh">一条街</span><span class="en">A whole street</span></b><br><span class="muted"><span class="zh">5 座房子只写 1 次</span><span class="en">5 houses, written once</span></span></div>
  <div class="card"><div class="big-emoji">🔁</div><b><span class="zh">return 交回结果</span><span class="en">return hands back a result</span></b><br><span class="muted"><span class="zh">招式也能「回答问题」</span><span class="en">tricks can answer questions too</span></span></div>
  <div class="card"><div class="big-emoji">🏙️</div><b><span class="zh">我的小镇</span><span class="en">My town</span></b><br><span class="muted"><span class="zh">挂上作品墙</span><span class="en">onto the gallery</span></span></div>
</div>

## 🎯 <span class="zh">今日任务清单</span><span class="en">Today's checklist</span>

<p><span class="zh">点一下就能打勾 ✅。全部完成有徽章！</span><span class="en">Click to tick ✅. Finish them all for a badge!</span></p>

<div class="progress" data-for="l7"><span></span></div>
<p class="muted" style="text-align:right;margin:.2em 0"><span class="progress-label" data-for="l7"></span></p>

<ul class="quests" data-key="l7">
  <li><div><b>🔁 <span class="zh">热身：while + 列表</span><span class="en">Warm-up: while + lists</span></b> <span class="pill">5 min</span><br><span class="zh">填好空，让海龟画 5 个彩色的圆。</span><span class="en">Fill in the blanks so the turtle draws 5 coloured circles.</span> <a href="learn/#warmup"><span class="zh">去热身 →</span><span class="en">Warm up →</span></a></div></li>
  <li><div><b>✨ <span class="zh">新魔法：def 招式</span><span class="en">New magic: def</span></b> <span class="pill">12 min</span><br><span class="zh">先猜会画几个正方形，再运行；然后给招式加「参数」。</span><span class="en">Guess how many squares, then run; then add "parameters" to the trick.</span> <a href="learn/#magic"><span class="zh">学一学 →</span><span class="en">Learn →</span></a></div></li>
  <li><div><b>🏘️ <span class="zh">一条街 + return</span><span class="en">A street + return</span></b> <span class="pill">12 min</span><br><span class="zh">把第 1 课的房子打包成 house()，再学会让招式「交回」答案。</span><span class="en">Pack the Lesson 1 house into house(), then make tricks that hand back answers.</span> <a href="learn/#street"><span class="zh">去画街 →</span><span class="en">Draw the street →</span></a></div></li>
  <li><div><b>🏙️ <span class="zh">小镇 + 挑战</span><span class="en">Town + challenge</span></b> <span class="pill">12 min</span><br><span class="zh">填好小镇的空，再做你自己的小镇，存到作品墙。</span><span class="en">Fill in the town, then build your own and save it to the gallery.</span> <a href="learn/#town"><span class="zh">去建镇 →</span><span class="en">Build the town →</span></a></div></li>
  <li><div><b>🎮 <span class="zh">玩游戏：宝石机器人</span><span class="en">Play: Gem Robot</span></b> <span class="pill">8 min</span><br><span class="zh">第 5–6 关不写函数可过不了！</span><span class="en">Levels 5–6 can't be beaten without a function!</span> <a href="{{ '/games/robot/' | relative_url }}"><span class="zh">去玩 →</span><span class="en">Play →</span></a></div></li>
  <li><div><b>🏠 <span class="zh">看作业 + 写 3 行笔记</span><span class="en">Homework + 3 lines in the notebook</span></b> <span class="pill">5 min</span><br><span class="zh">看看 <a href="homework/">海龟城市规划师</a>，然后在 <a href="{{ '/notebook/' | relative_url }}">笔记本</a> 写：学会了 / 卡在哪 / 怎么解决。</span><span class="en">Check <a href="homework/">Turtle City Planner</a>, then write in your <a href="{{ '/notebook/' | relative_url }}">notebook</a>: learned / stuck / fixed.</span></div></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🤝 今天的约定：一起做</span><span class="en">🤝 Today's deal: we build together</span></span>
<span class="zh">从这一课开始，<b>你写大部分</b>，老师只给提示。看到 <code>___</code> 就是你的地盘。想不出来？先翻 <a href="{{ '/cheatsheet/' | relative_url }}">📖 小词典</a>，再问 AI 要<b>提示</b>。</span>
<span class="en">From now on <b>you write most of it</b> and the teacher only gives hints. Every <code>___</code> is your territory. Stuck? Check the <a href="{{ '/cheatsheet/' | relative_url }}">📖 cheat sheet</a> first, then ask AI for a <b>hint</b>.</span>
</div>

<div class="box box-good"><span class="box-title"><span class="zh">💡 为什么要打包？</span><span class="en">💡 Why pack code up?</span></span>
<span class="zh">还记得第 1 课的房子吗？想画 5 座就要复制粘贴 5 遍，改一个数字要改 5 处。今天学完，<b>改一处，全部都变</b>。这就是程序员的「懒」——聪明的懒！</span>
<span class="en">Remember the Lesson 1 house? Drawing 5 of them meant copy-pasting 5 times, and changing one number meant 5 edits. After today, <b>change it once and everything changes</b>. That's programmer laziness — the clever kind!</span>
</div>

---

<p class="muted" style="font-size:.9rem">👩‍🏫 <span class="zh">给老师 / 家长：</span><span class="en">For teachers / parents (Chinese only): </span><a href="teacher/"><span class="zh">第 7 课教案</span><span class="en">Lesson 7 plan</span></a></p>
