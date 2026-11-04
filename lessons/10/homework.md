---
title: 第 10 课 · 作业
title_en: Lesson 10 · Homework
lesson: "10"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 10 课作业：我的项目计划书</span><span class="en">Lesson 10 homework: My project plan</span>

<p><span class="zh">这周的作业不是写很多代码，而是<b>想清楚</b>：计划书 + 跑起来的骨架。下周就靠它了！</span><span class="en">This week isn't about lots of code — it's about <b>thinking it through</b>: the plan + a running skeleton. Next week depends on it!</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week10-plan.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：计划书填完，存为 week10-plan</span><span class="en">Must do: finish the plan, save as week10-plan</span></h3>
    <p><span class="zh">用<a href="../learn/#plan">学一学</a>里的表格拼到 ⭐⭐⭐⭐（名字、做什么、必做 3 个、加分 2 个、小步骤至少 5 步），复制到下面的画板，<b>运行没有报错</b>，存到作品墙。</span><span class="en">Use the form in <a href="../learn/#plan">Learn</a> to reach ⭐⭐⭐⭐ (name, what, 3 must-haves, 2 bonuses, ≥5 small steps), paste it below, <b>run it with no errors</b>, save to the Gallery.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：骨架跑起来 + 加 1 个功能</span><span class="en">Bonus: skeleton runs + 1 feature added</span></h3>
    <p><span class="zh">把你选的骨架（A 游戏 / B app / C 画画）贴到第二个画板，完成骨架里一个<b>必做功能的 TODO</b>，或者你计划书里的<b>步骤 1</b>。存为 <code>week10-skeleton</code>。下周第 11 课的作业画板会<b>自动接着这里写</b>（同一台电脑）。</span><span class="en">Paste your chosen skeleton (A game / B app / C art) into the second playground and finish one <b>must-have TODO</b> or <b>step 1</b> of your plan. Save as <code>week10-skeleton</code>. Next week the Lesson 11 homework playground <b>picks up right where you left off</b> (on the same computer).</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：给你的项目写 2 个 assert</span><span class="en">Challenge: write 2 asserts for your project</span></h3>
    <p><span class="zh">在骨架的 <code>def test():</code> 里，为<b>你自己写的</b>函数或设置加 2 个 <code>assert</code>。故意改坏一个数字，看测试能不能抓到。</span><span class="en">Inside the skeleton's <code>def test():</code>, add 2 <code>asserts</code> for a function or setting <b>you wrote</b>. Break a number on purpose and see if a test catches it.</span></p>
  </div></div>
</div>

## 🧪 <span class="zh">作业画板 1：计划书</span><span class="en">Homework playground 1: the plan</span>

<div class="playground" data-src="{{ '/lessons/10/code/plan-template.py' | relative_url }}" data-title="📄 我的项目计划书" data-title-en="📄 My project plan" data-canvas="no" data-save="week10-plan" data-draft="l10-plan" data-rows="14"></div>

## 🧪 <span class="zh">作业画板 2：骨架（🥈 🥇）</span><span class="en">Homework playground 2: the skeleton (🥈 🥇)</span>

<p class="muted"><span class="zh">先在<a href="../learn/#plan">学一学</a>里点你选的骨架的 <b>📋 复制</b>，再贴到这里。写的代码会自动记在这台电脑上，第 11 课的作业画板会接着用它。</span><span class="en">Click <b>📋 Copy</b> on your chosen skeleton in <a href="../learn/#plan">Learn</a>, then paste it here. Your code is saved on this computer automatically, and the Lesson 11 homework playground carries on from it.</span></p>

<div class="hw-status" data-file="week10-skeleton.py"></div>

<div class="playground" data-title="🛠️ 我的项目（骨架）" data-title-en="🛠️ My project (skeleton)" data-save="week10-skeleton" data-draft="project" data-rows="14"><textarea># 🛠️ 我的项目 My project
# 把骨架 A / B / C 贴到这里（先删掉这几行）
# Paste skeleton A / B / C here (delete these lines first)
</textarea></div>

<details class="hint"><summary><span class="zh">💡 提示 1：小步骤怎么拆？</span><span class="en">💡 Hint 1: how to split steps</span></summary><span class="zh">每一步都要能<b>运行看到变化</b>。「做出游戏」不是一步；「星星能掉下来」「篮子能动」「碰到加 1 分」才是。</span><span class="en">Every step must be something you can <b>run and see</b>. "Make the game" isn't a step; "the star falls", "the basket moves", "touching adds 1 point" are.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：骨架里的 TODO 在哪？</span><span class="en">💡 Hint 2: where are the TODOs?</span></summary><span class="zh">在画板里按 Ctrl+F（Mac 是 ⌘F）搜 <code>TODO</code>。每个 TODO 旁边都写了提示用哪个指令。</span><span class="en">Press Ctrl+F (⌘F on Mac) in the playground and search <code>TODO</code>. Each one has a hint about which command to use.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：assert 写什么？</span><span class="en">💡 Hint 3: what to assert</span></summary><span class="zh">写「必须一直是真的」的事：<code>assert SPEED > 0</code>、<code>assert len(quiz) >= 3</code>、<code>assert lookup("kiwi") != "❓ 不认识"</code>。</span><span class="en">Things that must always be true: <code>assert SPEED > 0</code>, <code>assert len(quiz) >= 3</code>, <code>assert lookup("kiwi") != "❓ unknown"</code>.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">画板 1 点 <b>📤 存到作品墙</b>，文件名 <code>week10-plan</code>，GitHub 上点 <b>Commit changes</b>。</span><span class="en">On playground 1 click <b>📤 Save to Gallery</b>, name it <code>week10-plan</code>, click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">做了 🥈 的话，画板 2 也存一次，文件名 <code>week10-skeleton</code>。</span><span class="en">If you did 🥈, save playground 2 as <code>week10-skeleton</code>.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 的第 10 课写「我的项目是」和「拆成的小步骤」。</span><span class="en">In your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>, Lesson 10, write "my project is" and "small steps".</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：制作周！</b>整节课你自己写、自己测、自己修。老师<b>只回答问题，不给代码</b>。带上你的计划书，还有四步法。</span><span class="en">🔮 <b>Next week: build week!</b> A whole lesson of writing, testing and fixing by yourself. The teacher <b>answers questions but gives no code</b>. Bring your plan and the 4 steps.</span></div>
