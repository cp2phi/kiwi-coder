---
title: 第 10 课 · 作业
title_en: Lesson 10 · Homework
lesson: "10"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 10 课作业：任务计划书 + 第一次试飞</span><span class="en">Lesson 10 homework: the mission plan + a first test flight</span>

<p><span class="zh">这周的作业主要是<b>想清楚</b>：计划书 + 跑起来的骨架 + 第一个功能。下周就靠它了！</span><span class="en">This week is mostly about <b>thinking it through</b>: the plan + a running skeleton + the first feature. Next week depends on it!</span> <span class="pill">⏱ <span class="zh">大约 30–40 分钟</span><span class="en">about 30–40 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week10-plan.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：计划书填完，存为 week10-plan</span><span class="en">Must do: finish the plan, save as week10-plan</span></h3>
    <p><span class="zh">用<a href="../learn/#plan">学一学</a>里的表格拼到 ⭐⭐⭐⭐⭐（名字、做什么、选的任务、必做 3 个、加分 2 个、小步骤至少 5 步、<b>至少 1 个要测的 assert</b>），复制到下面的画板，<b>运行没有报错</b>，存到作品墙。</span><span class="en">Use the form in <a href="../learn/#plan">Learn</a> to reach ⭐⭐⭐⭐⭐ (name, what, mission, 3 must-haves, 2 nice-to-haves, ≥5 small steps, <b>at least 1 assert you'll test</b>), paste it below, <b>run it with no errors</b>, save to the Gallery.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：骨架跑起来 + 做好必做功能 1</span><span class="en">Bonus: skeleton runs + must-have 1 done</span></h3>
    <p><span class="zh">把你选的骨架贴到第二个画板，完成<b>必做功能 1</b>：🚀 燃料会用完（仪表盘显示）/ ☄️ <code>keep_inside</code> + 它的 3 个测试 / 🛰️ <code>all_systems_go</code> + 它的 2 个测试。存为 <code>week10-skeleton</code>。下周第 11 课的作业画板会<b>自动接着这里写</b>（同一台电脑）。</span><span class="en">Paste your chosen skeleton into the second playground and finish <b>must-have 1</b>: 🚀 fuel runs out (shown on the dashboard) / ☄️ <code>keep_inside</code> + its 3 tests / 🛰️ <code>all_systems_go</code> + its 2 tests. Save as <code>week10-skeleton</code>. Next week the Lesson 11 homework playground <b>picks up right where you left off</b> (on the same computer).</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：自己写 2 个 assert，其中 1 个是边界测试</span><span class="en">Challenge: write 2 asserts of your own, 1 of them an edge test</span></h3>
    <p><span class="zh">在骨架<b>已经有的</b> <code>def test():</code> 里加 2 个你自己想的 <code>assert</code>，其中一个测「刚好在线上」的数字（比如 <code>use_fuel(1) == 0</code>、<code>keep_inside(270) == 270</code>）。然后<b>故意改坏</b>函数里的一个数字或 <code>&lt;=</code>，看你的测试能不能抓到它，再改回来。</span><span class="en">Inside the skeleton's <b>existing</b> <code>def test():</code>, add 2 <code>asserts</code> you thought of yourself, one testing a number "exactly on the line" (like <code>use_fuel(1) == 0</code> or <code>keep_inside(270) == 270</code>). Then <b>break</b> a number or a <code>&lt;=</code> in the function on purpose, see whether your test catches it, and change it back.</span></p>
  </div></div>
</div>

## 🧪 <span class="zh">作业画板 1：计划书</span><span class="en">Homework playground 1: the plan</span>

<div class="playground" data-src="{{ '/lessons/10/code/plan-template.py' | relative_url }}" data-title="📄 我的任务计划书" data-title-en="📄 My mission plan" data-canvas="no" data-save="week10-plan" data-draft="l10-plan" data-rows="14"></div>

## 🧪 <span class="zh">作业画板 2：我的项目（🥈 🥇）</span><span class="en">Homework playground 2: my project (🥈 🥇)</span>

<p class="muted"><span class="zh">先在<a href="../learn/#choose">学一学</a>里，在你选的骨架（🚀 A / ☄️ B / 🛰️ C）上点 <b>📋 复制</b>，再贴到这里（把下面几行全部换掉）。写的代码会自动记在这台电脑上，第 11 课的作业画板会接着用它。</span><span class="en">In <a href="../learn/#choose">Learn</a>, click <b>📋 Copy</b> on your chosen skeleton (🚀 A / ☄️ B / 🛰️ C), then paste it here (replacing the lines below). Your code is saved on this computer automatically, and the Lesson 11 homework playground carries on from it.</span></p>

<div class="hw-status" data-file="week10-skeleton.py"></div>

<div class="playground" data-title="🛠️ 我的项目（骨架）" data-title-en="🛠️ My project (skeleton)" data-save="week10-skeleton" data-draft="project" data-rows="14"><textarea># 🛠️ 我的项目 My project
# 把你选的骨架 🚀 A / ☄️ B / 🛰️ C 贴到这里（先删掉这几行）
# Paste your chosen skeleton 🚀 A / ☄️ B / 🛰️ C here (delete these lines first)
</textarea></div>

<details class="hint"><summary><span class="zh">💡 提示 1：小步骤怎么拆？</span><span class="en">💡 Hint 1: how to split steps</span></summary><span class="zh">每一步都要能<b>运行看到变化</b>。「做出着陆游戏」不是一步；「仪表盘显示燃料」「按 ↑ 燃料少 1」「燃料是 0 时按 ↑ 没反应」才是。</span><span class="en">Every step must be something you can <b>run and see</b>. "Make the landing game" isn't a step; "the dashboard shows fuel", "↑ uses 1 fuel", "with 0 fuel ↑ does nothing" are.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：TODO 在哪？「删掉 #」是什么意思？</span><span class="en">💡 Hint 2: where are the TODOs? What does "remove the #" mean?</span></summary><span class="zh">在画板里按 Ctrl+F（Mac 是 ⌘F）搜 <code>TODO</code>。<code>test()</code> 里有几行 assert 前面有 <code>#</code>，它们现在是「睡着的测试」。删掉 <code>#</code>（注意保留前面的 4 个空格），测试就醒了——函数还没写好时它会<b>变红</b>，这是正常的！写好函数，它就变绿。</span><span class="en">Press Ctrl+F (⌘F on Mac) in the playground and search <code>TODO</code>. Some asserts in <code>test()</code> start with <code>#</code> — they're "sleeping tests". Remove the <code>#</code> (keep the 4 spaces in front) and the test wakes up — it goes <b>red</b> while the function isn't written yet, and that's normal! Write the function and it turns green.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：assert 写什么？</span><span class="en">💡 Hint 3: what to assert</span></summary><span class="zh">写「必须一直是真的」的事，一个普通的 + 一个太大或太小的 + 一个刚好在边上的：<code>assert use_fuel(1) == 0</code>、<code>assert keep_inside(-271) == -270</code>、<code>assert all_systems_go({"燃料": "GO"}) == True</code>。</span><span class="en">Things that must always be true — a normal one + a too-big or too-small one + one exactly on the edge: <code>assert use_fuel(1) == 0</code>, <code>assert keep_inside(-271) == -270</code>, <code>assert all_systems_go({"fuel": "GO"}) == True</code>.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">画板 1 点 <b>📤 存到作品墙</b>，文件名 <code>week10-plan</code>，GitHub 上点 <b>Commit changes</b>。</span><span class="en">On playground 1 click <b>📤 Save to Gallery</b>, name it <code>week10-plan</code>, click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">做了 🥈 的话，画板 2 也存一次，文件名 <code>week10-skeleton</code>。</span><span class="en">If you did 🥈, save playground 2 as <code>week10-skeleton</code>.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 的第 10 课写「我选的任务是」和「拆成的小步骤」。</span><span class="en">In your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>, Lesson 10, write "my mission is" and "small steps".</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：制作周！</b>整节课你自己写、自己测、自己修，还会学 4 招排错和「游戏心跳」。老师<b>只回答问题，不给代码</b>。带上你的计划书和四步法。</span><span class="en">🔮 <b>Next week: build week!</b> A whole lesson of writing, testing and fixing by yourself, plus 4 debugging tricks and the "game heartbeat". The teacher <b>answers questions but gives no code</b>. Bring your plan and the 4 steps.</span></div>
