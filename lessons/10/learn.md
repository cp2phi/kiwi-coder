---
title: 第 10 课 · 学一学
title_en: Lesson 10 · Learn
lesson: "10"
tab: learn
playground: true
---

# 📖 <span class="zh">第 10 课：像程序员一样做项目</span><span class="en">Lesson 10: Work on a project like a programmer</span>

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>

<p><span class="zh">第 9 课的<b>字典</b> + 第 7 课的<b>函数</b>：一个「查一下」函数。</span><span class="en"><b>Dicts</b> (Lesson 9) + <b>functions</b> (Lesson 7): a "look it up" function.</span></p>

<div class="playground" data-title="🔁 热身：查一下" data-title-en="🔁 Warm-up: look it up" data-canvas="no" data-save="lookup" data-rows="9"><textarea># 🔁 热身 Warm-up
animals = {"kiwi": "几维鸟", "kea": "啄羊鹦鹉", "tūī": "簇舌吸蜜鸟"}

def lookup(name):
    return animals.get(name, "❓ 不认识")

print(lookup("kiwi"))
print(lookup("kea"))
print(lookup("dragon"))
</textarea></div>

<ul class="quests" data-key="l10-warm">
  <li><span class="zh">加一个新动物，再查一次。</span><span class="en">Add a new animal and look it up.</span></li>
  <li><span class="zh">让 <code>lookup</code> 查到的时候多说一句「🐦 找到了：」。</span><span class="en">Make <code>lookup</code> say "🐦 Found: " when it finds one.</span></li>
</ul>

---

## 🔄 <span class="zh">程序员是怎么做项目的？</span><span class="en">How do programmers build things?</span>
{: #flow}

<p class="zh">不是坐下来从第一行写到最后一行！真正的程序员是转一个<b>循环</b>——每转一圈，项目就好一点：</p>
<p class="en">Not by typing line 1 to the end in one go! Real programmers go round a <b>loop</b> — each lap makes the project a little better:</p>

<div class="flow">
  <div class="f"><span class="e">🗺️</span><b><span class="zh">计划</span><span class="en">Plan</span></b><small><span class="zh">做什么？拆成小步</span><span class="en">what? small steps</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">⌨️</span><b><span class="zh">写</span><span class="en">Code</span></b><small><span class="zh">只写一小步</span><span class="en">one small step</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🧪</span><b><span class="zh">测</span><span class="en">Test</span></b><small><span class="zh">运行、试、assert</span><span class="en">run, try, assert</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🔧</span><b><span class="zh">修</span><span class="en">Fix</span></b><small><span class="zh">读报错、四步法</span><span class="en">read errors, 4 steps</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🚀</span><b><span class="zh">发布</span><span class="en">Ship</span></b><small><span class="zh">存到作品墙 / 上线</span><span class="en">save / go live</span></small></div>
</div>

<div class="box box-tip"><span class="box-title"><span class="zh">👩‍💻 程序员的一天</span><span class="en">👩‍💻 A programmer's day</span></span>
<span class="zh">早上：看计划，挑<b>一个</b>小步骤（比如「让篮子能左右动」）。写 10 行 → 运行 → 坏了 → 读报错 → 修好 → 再运行 → 好了！→ <b>存档（commit）</b>。然后挑下一个小步骤。一天转十几圈。没有人一次写对，<b>修</b>就是工作的一部分。</span>
<span class="en">Morning: read the plan, pick <b>one</b> small step (like "make the basket move left and right"). Write 10 lines → run → broken → read the error → fix → run → works! → <b>save (commit)</b>. Then the next step. A dozen laps a day. Nobody gets it right first time; <b>fixing</b> is part of the job.</span>
</div>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">我们这个网站是怎么「发布」的？</span><span class="en">How does our website "ship"?</span></p>
  <div class="opts"><button><span class="zh">老师每周手动上传</span><span class="en">The teacher uploads it weekly</span></button><button><span class="zh">要买一台服务器</span><span class="en">You have to buy a server</span></button><button><span class="zh">在 GitHub 点 Commit，1 分钟后自动变成网站</span><span class="en">Click Commit on GitHub; a minute later it's live</span></button></div>
  <div class="why"><span class="zh">对！这叫 <b>GitHub Pages</b>。每次 commit（存档）= 一次发布。第 12 课你的项目也会这样上线。</span><span class="en">Right! That's <b>GitHub Pages</b>. Every commit (save) = one release. In Lesson 12 your project goes live the same way.</span></div>
</div>

---

## 👓 <span class="zh">读懂别人的代码</span><span class="en">Reading other people's code</span>
{: #read}

<p class="zh">做项目时你会看到很多<b>别人写的代码</b>（AI 的、骨架的、游戏里的）。读代码有三步：① 从上到下找<b>函数的名字</b>（def）——它们是「目录」；② 找<b>主循环</b>（while）——程序在这里转；③ 找<b>变量</b>——程序记住了什么。</p>
<p class="en">In a project you'll read lots of <b>code written by others</b> (AI, skeletons, games). Three steps: ① scan top to bottom for <b>function names</b> (def) — they're the table of contents; ② find the <b>main loop</b> (while) — where the program spins; ③ find the <b>variables</b> — what it remembers.</p>

<p><span class="zh">练习对象：一个 25 行的<b>待办 app</b>。先别改，先读。</span><span class="en">Practice on a 25-line <b>to-do app</b>. Don't change it yet — read it.</span></p>

<div class="playground" data-src="{{ '/lessons/10/code/todo.py' | relative_url }}" data-title="📝 迷你待办 app" data-title-en="📝 Mini to-do app" data-canvas="no" data-save="todo-app" data-draft="l10-todo" data-rows="18"></div>

<ol class="code-walk">
  <li><code>todo = []</code><span><span class="zh">③ 变量：一个空列表，记住要做的事</span><span class="en">③ variable: an empty list of things to do</span></span></li>
  <li><code>def show():</code><span><span class="zh">① 函数 1：显示全部</span><span class="en">① function 1: show everything</span></span></li>
  <li><code>def add(thing):</code><span><span class="zh">① 函数 2：加一件</span><span class="en">① function 2: add one</span></span></li>
  <li><code>def done(number):</code><span><span class="zh">① 函数 3：做完一件，<code>pop</code> 拿掉</span><span class="en">① function 3: finish one, <code>pop</code> removes it</span></span></li>
  <li><code>while True:</code><span><span class="zh">② 主循环：显示菜单 → 问 → 做</span><span class="en">② main loop: menu → ask → do</span></span></li>
  <li><code>break</code><span><span class="zh">选 4 的时候跳出循环，程序结束</span><span class="en">on 4, leave the loop and end</span></span></li>
</ol>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">选 <b>2</b> 之后输入 <code>1</code>，哪个函数会被调用？</span><span class="en">After choosing <b>2</b> and typing <code>1</code>, which function runs?</span></p>
  <div class="opts"><button>show()</button><button>done(1)</button><button>add("1")</button></div>
  <div class="why"><span class="zh">菜单 2 = 做完一件 → <code>done(int(...))</code>，把输入变成数字 1，再 <code>pop(0)</code> 拿掉第一件。</span><span class="en">Menu 2 = finish one → <code>done(int(...))</code> turns the input into the number 1, then <code>pop(0)</code> removes the first item.</span></div>
</div>

<ul class="quests" data-key="l10-read">
  <li><span class="zh">说出 3 个函数的名字，和每个是干嘛的。</span><span class="en">Name the 3 functions and what each does.</span></li>
  <li><span class="zh">哪一行让程序停下来？（提示：找 <code>break</code>）</span><span class="en">Which line stops the program? (hint: find <code>break</code>)</span></li>
  <li><span class="zh">运行：加两件事 → 看全部 → 做完第 1 件 → 看全部 → 退出。</span><span class="en">Run it: add two → show → finish #1 → show → quit.</span></li>
  <li><span class="zh">改一个地方：让「加好了」后面自动显示全部（提示：在 <code>add</code> 里调用 <code>show()</code>）。</span><span class="en">Change one thing: show the list automatically after adding (hint: call <code>show()</code> inside <code>add</code>).</span></li>
  <li>🐞 <span class="zh">「做完第 9 件」会怎样？运行试试，读报错。这就是下一节要讲的——<b>测试</b>。</span><span class="en">What if you "finish #9"? Try it and read the error. That's what the next part is about — <b>testing</b>.</span></li>
</ul>

---

## 🧪 <span class="zh">测试：让电脑帮你检查</span><span class="en">Testing: let the computer check</span>
{: #test}

<p class="zh">每次改完代码都要自己玩一遍太累了。<b><code>assert</code></b> 的意思是「我断言这件事是真的」——它后面的条件必须是 True，否则程序<b>立刻停下来报错</b>。写几个 assert，一点运行就能知道有没有改坏。</p>
<p class="en">Playing the whole thing after every change gets tiring. <b><code>assert</code></b> means "I claim this is true" — the condition after it must be True, or the program <b>stops with an error</b>. Write a few asserts and one click tells you if anything broke.</p>

<div class="cmds">
  <div class="cmd"><code>assert add(2, 3) == 5</code><span><span class="zh">add(2, 3) 必须等于 5</span><span class="en">add(2, 3) must equal 5</span></span></div>
  <div class="cmd"><code>assert x > 0, "x 要大于 0"</code><span><span class="zh">逗号后面是失败时的提示</span><span class="en">after the comma: the message if it fails</span></span></div>
  <div class="cmd"><code>def test(): …</code><span><span class="zh">把测试放进一个函数，程序开头调用</span><span class="en">put tests in a function, call it at the start</span></span></div>
</div>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的代码里有一个 bug 和一个「写错的测试」。运行后，第一个报错会在哪一行附近？</span><span class="en">The code below has one bug and one "wrongly written test". When you run it, where is the first error?</span></p>
  <div class="opts"><button><span class="zh">第 1 个 assert</span><span class="en">The 1st assert</span></button><button><span class="zh">最后那个 double(5) == 11</span><span class="en">The last one, double(5) == 11</span></button><button><span class="zh">不会报错</span><span class="en">No error</span></button></div>
  <div class="why"><span class="zh"><code>double</code> 的 <code>n + n</code> 其实是对的（两倍！），所以前面全过。最后那个测试本身写错了：5 的两倍是 10 不是 11。<b>测试也会有 bug</b>——报错时两边都要看。</span><span class="en"><code>n + n</code> in <code>double</code> is actually right (it doubles!), so the earlier tests pass. The last test itself is wrong: double 5 is 10, not 11. <b>Tests can have bugs too</b> — check both sides when one fails.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/10/code/tests.py' | relative_url }}" data-title="🧪 我的第一个测试" data-title-en="🧪 My first tests" data-canvas="no" data-save="my-tests" data-draft="l10-tests" data-rows="16"></div>

<ul class="quests" data-key="l10-test">
  <li><span class="zh">运行，读红框：AssertionError 说了什么？</span><span class="en">Run it and read the red box: what does AssertionError say?</span></li>
  <li><span class="zh">修好那个写错的测试，让「✅ 所有测试都通过了」出现。</span><span class="en">Fix the wrong test so "✅ All tests passed" shows up.</span></li>
  <li><span class="zh">现在把 <code>double</code> 改成 <code>n * 3</code>（故意改坏）。哪个测试先抓到它？</span><span class="en">Now break <code>double</code> on purpose (<code>n * 3</code>). Which test catches it first?</span></li>
  <li><span class="zh">给 <code>add</code> 再写一个你自己的测试。</span><span class="en">Write one more test of your own for <code>add</code>.</span></li>
</ul>

<div class="box box-tip"><span class="box-title"><span class="zh">📋 测试清单（手动的也算测试！）</span><span class="en">📋 Test checklist (manual tests count too!)</span></span>
<span class="zh">每次做完一步，问自己：① 正常用，对吗？ ② 输入<b>错的东西</b>（字母、空的、太大的数）会怎样？ ③ 连玩 3 遍还正常吗？ ④ 有没有一个 assert 能帮我自动检查？</span>
<span class="en">After every step ask: ① Does it work normally? ② What if I type <b>something wrong</b> (letters, nothing, a huge number)? ③ Still fine after 3 rounds? ④ Could an assert check this for me?</span>
</div>

---

## 🗺️ <span class="zh">选你的项目</span><span class="en">Choose your project</span>
{: #plan}

<p class="zh">第 11 课你会<b>自己做</b>，第 12 课<b>发布上线</b>。三种类型，选<b>一种</b>。每种都有一个<b>能跑的骨架</b>——先运行看看它长什么样！</p>
<p class="en">In Lesson 11 you <b>build it yourself</b>; in Lesson 12 you <b>ship it</b>. Three types — choose <b>one</b>. Each has a <b>running skeleton</b>: run it first to see what it looks like!</p>

### A · 🎮 <span class="zh">游戏：接星星</span><span class="en">Game: Catch the Stars</span>

<div class="two">
<div>
<p><span class="zh"><b>必做</b>：① 篮子能 ← → 移动 ② 星星越来越快 ③ 10 分显示「你赢了」<br><b>加分</b>：漏接减命；第二种掉落物（炸弹 💣 碰到扣分）<br><b>用到</b>：函数（7）、if（4）、random（4）、键盘事件（11）</span><span class="en"><b>Must</b>: ① basket moves with ← → ② star speeds up ③ "You win" at 10 points<br><b>Bonus</b>: lose a life on a miss; a second falling thing (bomb 💣 = lose points)<br><b>Uses</b>: functions (7), if (4), random (4), keyboard events (11)</span></p>
<p class="muted"><span class="zh">像这个：<a href="{{ '/games/catch/' | relative_url }}">🍎 接水果</a>。先点画布再按键盘！</span><span class="en">Like this: <a href="{{ '/games/catch/' | relative_url }}">🍎 Fruit Catcher</a>. Click the canvas, then use the keys!</span></p>
</div>
<div>
<div class="playground" data-src="{{ '/lessons/10/code/skeleton-game.py' | relative_url }}" data-title="🎮 骨架 A：接星星" data-title-en="🎮 Skeleton A: Catch the Stars" data-save="week11-project" data-draft="l10-skel-game" data-rows="10"></div>
</div>
</div>

### B · 📱 <span class="zh">app：有菜单的文字程序</span><span class="en">App: a text program with a menu</span>

<div class="two">
<div>
<p><span class="zh">问答机 / 翻译机 / 待办 / 算命机 / 计算器……都行。<br><b>必做</b>：① 菜单循环 ② 至少 3 个功能（每个一个函数）③ 输入错的东西不会崩溃<br><b>加分</b>：记分或记录；随机惊喜<br><b>用到</b>：while（6）、函数（7）、字典（9）、input（2）</span><span class="en">Quiz / translator / to-do / fortune teller / calculator… anything.<br><b>Must</b>: ① a menu loop ② at least 3 features (one function each) ③ wrong input doesn't crash it<br><b>Bonus</b>: score or history; a random surprise<br><b>Uses</b>: while (6), functions (7), dicts (9), input (2)</span></p>
</div>
<div>
<div class="playground" data-src="{{ '/lessons/10/code/skeleton-app.py' | relative_url }}" data-title="📱 骨架 B：问答 app" data-title-en="📱 Skeleton B: Quiz app" data-canvas="no" data-save="week11-project" data-draft="l10-skel-app" data-rows="10"></div>
</div>
</div>

### C · 🎨 <span class="zh">互动画画：点一下就画</span><span class="en">Interactive art: click to draw</span>

<div class="two">
<div>
<p><span class="zh"><b>必做</b>：① 点哪里画哪里 ② 每次换形状或颜色 ③ 一个键清空画布<br><b>加分</b>：按数字键换花瓣数；按住拖动画线<br><b>用到</b>：函数（7）、for（3）、列表 + random（5）、鼠标事件（11）</span><span class="en"><b>Must</b>: ① draw where you click ② a different shape or colour each time ③ one key clears the canvas<br><b>Bonus</b>: number keys change the petal count; drag to draw lines<br><b>Uses</b>: functions (7), for (3), lists + random (5), mouse events (11)</span></p>
</div>
<div>
<div class="playground" data-src="{{ '/lessons/10/code/skeleton-art.py' | relative_url }}" data-title="🎨 骨架 C：点一下就画" data-title-en="🎨 Skeleton C: Click to draw" data-save="week11-project" data-draft="l10-skel-art" data-rows="10"></div>
</div>
</div>

<div class="box box-think"><span class="zh">🧠 <b>选不出来？</b>问自己：哪个做完了我最想给朋友看？选那个。三个都想做？先做一个，做完再说——「小一点，但做完」。</span><span class="en">🧠 <b>Can't decide?</b> Ask: which finished one would I most want to show a friend? Pick that. Want all three? Finish one first — "small, but finished".</span></div>

### 📄 <span class="zh">一页项目计划书</span><span class="en">The one-page plan</span>

<p><span class="zh">填下面的表格，它会帮你拼成计划书。拼好后<b>复制</b>，贴到下面的画板里（计划书也是一个 Python 文件——全是注释！），存到作品墙就交了作业。</span><span class="en">Fill in the form and it builds your plan. Then <b>copy</b> it, paste it into the playground below (the plan is a Python file too — all comments!) and save it to the Gallery to hand it in.</span></p>

<style>
.plan-form label { display: block; font-weight: 700; margin: 10px 0 4px; }
.plan-form input, .plan-form textarea { width: 100%; font: inherit; font-size: 1rem; padding: 8px 12px; border-radius: 10px; border: 2px solid var(--line); background: var(--bg); color: var(--text); }
.plan-form .chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
.plan-form .chip { font: inherit; font-size: .85rem; border: 2px solid var(--line); background: var(--bg); border-radius: 999px; padding: 1px 10px; cursor: pointer; color: var(--text); }
.plan-form .result { margin-top: 14px; background: var(--code-bg); border: 2px dashed var(--brand); border-radius: 14px; padding: 12px 14px; white-space: pre-wrap; font-size: .9rem; font-family: "JetBrains Mono", monospace; }
.plan-form .score { font-weight: 700; margin-top: 8px; }
</style>
<div class="card plan-form" id="plan-form">
  <label>🏷️ <span class="zh">项目名字</span><span class="en">Project name</span></label>
  <input name="p-name" data-ph-zh="比如：星星猎人" data-ph-en="e.g. Star Hunter" placeholder="比如：星星猎人">
  <label>🎯 <span class="zh">它是做什么的（一句话）</span><span class="en">What it does (one sentence)</span></label>
  <input name="p-what" data-ph-zh="比如：用篮子接住掉下来的星星，接到 10 个就赢" data-ph-en="e.g. catch falling stars with a basket; 10 to win" placeholder="比如：用篮子接住掉下来的星星，接到 10 个就赢">
  <label>🗂️ <span class="zh">类型</span><span class="en">Type</span></label>
  <input name="p-type" placeholder="🎮 / 📱 / 🎨">
  <div class="chips" data-for="p-type"><button class="chip"><span class="zh">🎮 游戏</span><span class="en">🎮 game</span></button><button class="chip"><span class="zh">📱 app</span><span class="en">📱 app</span></button><button class="chip"><span class="zh">🎨 互动画画</span><span class="en">🎨 interactive art</span></button></div>
  <label>🕹️ <span class="zh">玩家怎么用（2–3 句）</span><span class="en">How the player uses it (2–3 lines)</span></label>
  <textarea name="p-how" rows="3" data-ph-zh="1. 点一下画布  2. 按左右键移动  3. ……" data-ph-en="1. click the canvas  2. use arrow keys  3. …" placeholder="1. 点一下画布  2. 按左右键移动  3. ……"></textarea>
  <label>✅ <span class="zh">必做的 3 个功能（每行一个）</span><span class="en">3 must-have features (one per line)</span></label>
  <textarea name="p-must" rows="3" placeholder="1.&#10;2.&#10;3."></textarea>
  <label>⭐ <span class="zh">加分的 2 个功能</span><span class="en">2 nice-to-have features</span></label>
  <textarea name="p-bonus" rows="2" placeholder="1.&#10;2."></textarea>
  <label>🪜 <span class="zh">拆成的小步骤（至少 5 步，每步 10 分钟能做完）</span><span class="en">Small steps (≥5, each doable in 10 minutes)</span></label>
  <textarea name="p-steps" rows="5" placeholder="1. 先让骨架跑起来&#10;2.&#10;3.&#10;4.&#10;5."></textarea>
  <label>📖 <span class="zh">我需要的知识点（课数）</span><span class="en">Knowledge I need (lesson numbers)</span></label>
  <input name="p-know" data-ph-zh="比如：while（6）、函数（7）、字典（9）" data-ph-en="e.g. while (6), functions (7), dicts (9)" placeholder="比如：while（6）、函数（7）、字典（9）">
  <label>🤖 <span class="zh">我会问 AI 什么（只要提示）</span><span class="en">What I'll ask AI (hints only)</span></label>
  <input name="p-ai" data-ph-zh="比如：按左键让海龟往左，提示我用哪个指令" data-ph-en="e.g. a hint for which command moves the turtle on a key press" placeholder="比如：按左键让海龟往左，提示我用哪个指令">
  <div class="result" id="plan-out"></div>
  <div class="score" id="plan-score"></div>
  <p><button class="pg-btn run" id="plan-copy"><span class="zh">📋 复制计划书</span><span class="en">📋 Copy the plan</span></button></p>
</div>

<script>
(function () {
  var form = document.getElementById('plan-form');
  var out = document.getElementById('plan-out'), score = document.getElementById('plan-score');
  var v = function (n) { var e = form.querySelector('[name="' + n + '"]'); return e ? e.value.trim() : ''; };
  var lines = function (s) { return s.split('\n').map(function (l) { return l.trim(); }).filter(Boolean); };
  function build() {
    var E = window.KC && KC.lang() === 'en';
    var filled = 0;
    var L = ['# 🗺️ ' + (E ? 'My project plan' : '我的项目计划书') + (v('p-name') ? '：' + v('p-name') : ''), '#'];
    var sec = function (title, body) { L.push('# ===== ' + title + ' ====='); if (body) { body.forEach(function (b) { L.push('#   ' + b); }); filled++; } else L.push('#   ...'); L.push('#'); };
    sec(E ? '1. Project name' : '1. 项目名字', v('p-name') ? [v('p-name')] : null);
    sec(E ? '2. What it does' : '2. 它是做什么的', v('p-what') ? [v('p-what')] : null);
    sec(E ? '3. Type' : '3. 类型', v('p-type') ? [v('p-type')] : null);
    sec(E ? '4. How the player uses it' : '4. 玩家怎么用', lines(v('p-how')).length ? lines(v('p-how')) : null);
    sec(E ? '5. Must-have features (3)' : '5. 必做的 3 个功能', lines(v('p-must')).length ? lines(v('p-must')).map(function (l) { return '[ ] ' + l; }) : null);
    sec(E ? '6. Nice-to-have (2)' : '6. 加分的 2 个功能', lines(v('p-bonus')).length ? lines(v('p-bonus')).map(function (l) { return '[ ] ' + l; }) : null);
    sec(E ? '7. Small steps' : '7. 拆成的小步骤', lines(v('p-steps')).length ? lines(v('p-steps')) : null);
    sec(E ? '8. Knowledge I need' : '8. 我需要的知识点', v('p-know') ? [v('p-know')] : null);
    sec(E ? '9. What I will ask AI (hints only)' : '9. 我会问 AI 什么（只要提示）', v('p-ai') ? [v('p-ai')] : null);
    L.push('print("🗺️ ' + (E ? 'This is my project plan. The code comes in Lesson 11!' : '这是我的项目计划书，代码在第 11 课写！') + '")');
    out.textContent = L.join('\n');
    var steps = lines(v('p-steps')).length, must = lines(v('p-must')).length;
    var msg;
    if (filled < 3) msg = E ? 'Start with the name and what it does ✏️' : '先填名字和「它是做什么的」✏️';
    else if (must < 3) msg = E ? '⭐ Good start! Write 3 must-have features' : '⭐ 不错的开始！必做功能要写满 3 个';
    else if (steps < 5) msg = E ? '⭐⭐ Nice! Split it into at least 5 small steps' : '⭐⭐ 很好！小步骤至少 5 步';
    else if (filled < 9) msg = E ? '⭐⭐⭐ Almost — fill in the last sections' : '⭐⭐⭐ 快好了，把最后几栏填上';
    else msg = E ? '⭐⭐⭐⭐ A real project plan! Copy it and save it' : '⭐⭐⭐⭐ 一份真正的项目计划书！复制它，存起来';
    score.textContent = msg;
  }
  form.addEventListener('input', build);
  form.querySelectorAll('.chips .chip').forEach(function (c) { c.type = 'button'; c.addEventListener('click', function () {
    var E = window.KC && KC.lang() === 'en'; var s = c.querySelector(E ? '.en' : '.zh');
    form.querySelector('[name="p-type"]').value = (s || c).textContent; build();
  }); });
  document.addEventListener('kc-lang', build);
  document.getElementById('plan-copy').addEventListener('click', function () {
    var t = out.textContent, b = this, old = b.innerHTML;
    var ok = function () { b.innerHTML = '<span class="zh">✅ 复制好了，贴到下面的画板里</span><span class="en">✅ Copied — paste it into the playground below</span>'; setTimeout(function () { b.innerHTML = old; }, 2500); };
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(ok, function () { window.prompt('Copy:', t); }); else window.prompt('Copy:', t);
  });
  build();
})();
</script>

<div class="playground" data-src="{{ '/lessons/10/code/plan-template.py' | relative_url }}" data-title="📄 我的项目计划书" data-title-en="📄 My project plan" data-canvas="no" data-save="week10-plan" data-draft="l10-plan" data-rows="14"></div>

<ul class="quests" data-key="l10-plan">
  <li><span class="zh">计划书拼到 ⭐⭐⭐⭐，复制，贴进画板（把模板里的空替换掉），运行一下确认没有报错。</span><span class="en">Get the plan to ⭐⭐⭐⭐, copy it, paste it into the playground (replacing the template), run it to check for errors.</span></li>
  <li><span class="zh">把你选的骨架（A / B / C）运行一次，找到里面的 3 个 <code>TODO</code>。</span><span class="en">Run your chosen skeleton (A / B / C) and find its 3 <code>TODO</code>s.</span></li>
  <li><span class="zh">给老师讲一遍你的计划（讲出来 = 真的想清楚了）。</span><span class="en">Explain your plan to your teacher (saying it out loud = really thought it through).</span></li>
</ul>

---

## 🤖 <span class="zh">和 AI 一起：头脑风暴，但计划我来写</span><span class="en">Together with AI: brainstorm, but I write the plan</span>

<p><span class="zh">AI 很会出点子。可以这样问：</span><span class="en">AI is great at ideas. Ask like this:</span></p>

<pre class="zh" style="white-space:pre-wrap">我是小学 6 年级的学生，会用 Python 的 turtle、if、for、while、列表、函数和字典。
给我 5 个适合我做的小游戏（或小 app）点子，每个只用一句话，
每个都要能在 1 小时内做出最简单的版本。不要写代码。</pre>
<pre class="en" style="white-space:pre-wrap">I'm a Year 6 student who knows Python turtle, if, for, while, lists, functions and dicts.
Give me 5 ideas for a small game (or app) I could make, one sentence each,
and each must have a simplest version doable in 1 hour. No code.</pre>
<button class="pg-btn copy-prev">📋 <span class="zh">复制</span><span class="en">Copy</span></button>

<div class="chat">
  <div class="bubble me"><span class="zh">（坏问法）帮我做一个游戏。</span><span class="en">(bad) Make me a game.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">给你 200 行代码……</span><span class="en">Here are 200 lines of code…</span></div>
  <div class="bubble me"><span class="zh">（好问法）我计划做「接星星」，必做功能是篮子左右移动。我卡在「按键让篮子动」这一步，<b>给我一个提示</b>用哪个 turtle 指令，不要写完整代码。</span><span class="en">(good) I'm planning "Catch the Stars"; must-have: basket moves left/right. I'm stuck on "key press moves the basket". <b>Give me a hint</b> about which turtle command, no full code.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">看看 <code>screen.onkey(函数, "Left")</code>，然后别忘了 <code>screen.listen()</code>。</span><span class="en">Look at <code>screen.onkey(function, "Left")</code>, and don't forget <code>screen.listen()</code>.</span></div>
</div>

<div class="box box-rule"><span class="zh">📜 <b>规矩：</b>点子可以问 AI；<b>选哪个、拆步骤、必做功能——由你写</b>。计划是你的，所以你才看得懂自己的项目。</span><span class="en">📜 <b>Rule:</b> ideas can come from AI; <b>which one, the steps, the must-haves — you write them</b>. The plan is yours, so you understand your own project.</span></div>

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b><span class="zh">五步循环</span><span class="en">The 5-step loop</span></b><code>🗺️ 计划 → ⌨️ 写 → 🧪 测 → 🔧 修 → 🚀 发布</code><span><span class="zh">每圈只做一小步；commit = 发布</span><span class="en">one small step per lap; commit = ship</span></span></div>
  <div class="k"><b><span class="zh">读代码三步</span><span class="en">Read code in 3 steps</span></b><code>① def 函数名  ② while 主循环  ③ 变量</code><span><span class="zh">先看目录，再看它在哪转，再看它记住了什么</span><span class="en">contents, where it spins, what it remembers</span></span></div>
  <div class="k"><b><span class="zh">assert 测试</span><span class="en">assert tests</span></b><code>assert add(2, 3) == 5, "2+3 应该是 5"</code><span><span class="zh">不是 True 就立刻报错</span><span class="en">errors at once if not True</span></span></div>
  <div class="k"><b><span class="zh">测试函数</span><span class="en">A test function</span></b><code>def test():
    assert ...
test()</code><span><span class="zh">放在程序开头，一运行就检查</span><span class="en">at the top, checked on every run</span></span></div>
  <div class="k"><b><span class="zh">TODO 注释</span><span class="en">TODO comments</span></b><code># TODO: 加上计分</code><span><span class="zh">标记还没做的小步骤</span><span class="en">mark steps not done yet</span></span></div>
  <div class="k"><b><span class="zh">计划书</span><span class="en">The plan</span></b><code>名字 / 做什么 / 必做 3 / 加分 2 / 小步骤 ≥5</code><span><span class="zh">小一点，但做完</span><span class="en">small, but finished</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l10">📖 小词典 · 第 10 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l10">📖 cheat sheet · Lesson 10</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/10/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
