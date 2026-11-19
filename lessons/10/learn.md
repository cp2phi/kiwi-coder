---
title: 第 10 课 · 学一学
title_en: Lesson 10 · Learn
lesson: "10"
tab: learn
playground: true
---

# 📖 <span class="zh">第 10 课：像工程师一样做项目</span><span class="en">Lesson 10: Build a project like an engineer</span>

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">第 9 课的<b>字典</b> + 第 7 课的<b>函数</b> + 第 8 课的<b>字符串方法</b>：一个「火箭资料库」。先猜：最后一行会打印什么？</span><span class="en"><b>Dicts</b> (Lesson 9) + <b>functions</b> (Lesson 7) + <b>string methods</b> (Lesson 8): a "rocket database". Predict first: what will the last line print?</span></p>

<div class="playground" data-title="🔁 热身：火箭资料库" data-title-en="🔁 Warm-up: rocket database" data-canvas="no" data-save="rocket-database" data-draft="l10-warmup" data-rows="12"><textarea># 🔁 热身 Warm-up：火箭资料库 / rocket database
rockets = {
    "falcon 9": "一级助推器能飞回来降落，再用一次 / its first stage flies back, lands and flies again",
    "starship": "两级：Super Heavy 助推器 + Starship 飞船 / two stages: Super Heavy booster + Starship ship",
    "saturn v": "把宇航员送去月球的火箭 / the rocket that took astronauts to the Moon",
}

def info(name):
    return rockets.get(name, "❓ 资料库里没有 / not in the database")

print(info("falcon 9"))
print(info("starship"))
print(info("Saturn V"))
</textarea></div>

<ul class="quests" data-key="l10-warm">
  <li><span class="zh">为什么 <code>info("Saturn V")</code> 查不到？改 <code>info</code> 函数（只改一行！），让 <code>"Saturn V"</code> 和 <code>"  STARSHIP "</code> 都能查到。提示：第 8 课的 <code>.lower()</code> 和 <code>.strip()</code>。</span><span class="en">Why does <code>info("Saturn V")</code> find nothing? Change <code>info</code> (just one line!) so <code>"Saturn V"</code> and <code>"  STARSHIP "</code> both work. Hint: Lesson 8's <code>.lower()</code> and <code>.strip()</code>.</span></li>
  <li><span class="zh">加一枚你知道的火箭（键用小写），再查一次。</span><span class="en">Add a rocket you know (lower-case key) and look it up.</span></li>
</ul>

---

## 🔄 <span class="zh">工程师是怎么做项目的？</span><span class="en">How do engineers build things?</span>
{: #flow}

<p class="zh">不是坐下来从第一行写到最后一行！真正的工程师是转一个<b>循环</b>——每转一圈，项目就好一点：</p>
<p class="en">Not by typing line 1 to the end in one go! Real engineers go round a <b>loop</b> — each lap makes the project a little better:</p>

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

<div class="box box-tip"><span class="box-title"><span class="zh">🚀 SpaceX 也是这样做的：测试 → 失败 → 学习 → 修好</span><span class="en">🚀 SpaceX works this way too: test → fail → learn → fix</span></span>
<span class="zh">SpaceX 是 Elon Musk 在 2002 年创办的火箭公司。他们想让<b>猎鹰 9 号</b>的一级助推器飞回来、自己降落、下次再用。头几次在海上<b>无人船</b>降落的尝试都失败了——有的落得太重，有的倒下炸了。每一次，工程师都看数据、找原因、改设计，再试。2015 年底，第一枚助推器成功落回地面；后来在无人船上也成功了。2024 年 10 月，巨大的 <b>Super Heavy</b> 助推器飞回发射塔，被塔上两只机械臂（大家叫它们「筷子」）接住了。<b>失败不是结束，是数据。</b>你写程序也是一样：每个红字都是一条数据。</span>
<span class="en">SpaceX is the rocket company Elon Musk founded in 2002. They wanted the first-stage booster of <b>Falcon 9</b> to fly back, land by itself and fly again. The first few landing attempts on a <b>drone ship</b> at sea failed — some came down too hard, some tipped over and blew up. Each time the engineers studied the data, found the cause, changed the design and tried again. At the end of 2015 a booster landed back on the ground for the first time; later they landed on the drone ship too. In October 2024 the giant <b>Super Heavy</b> booster flew back to its launch tower and was caught by two mechanical arms (nicknamed "chopsticks"). <b>Failing isn't the end — it's data.</b> Coding is the same: every red error is a piece of data.</span>
</div>

<div class="box box-good"><span class="box-title"><span class="zh">👩‍💻 程序员的一天</span><span class="en">👩‍💻 A programmer's day</span></span>
<span class="zh">早上：看计划，挑<b>一个</b>小步骤（比如「按 ↑ 能减速」）。写 10 行 → 运行 → 坏了 → 读报错 → 修好 → 再运行 → 好了！→ <b>存档（commit）</b>。然后挑下一个小步骤。一天转十几圈。</span>
<span class="en">Morning: read the plan, pick <b>one</b> small step (like "↑ slows the booster down"). Write 10 lines → run → broken → read the error → fix → run → works! → <b>save (commit)</b>. Then the next step. A dozen laps a day.</span>
</div>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">我们这个网站是怎么「发布」的？</span><span class="en">How does our website "ship"?</span></p>
  <div class="opts"><button><span class="zh">老师每周手动上传</span><span class="en">The teacher uploads it weekly</span></button><button><span class="zh">要买一台服务器</span><span class="en">You have to buy a server</span></button><button><span class="zh">在 GitHub 点 Commit，1 分钟后自动变成网站</span><span class="en">Click Commit on GitHub; a minute later it's live</span></button></div>
  <div class="why"><span class="zh">对！这叫 <b>GitHub Pages</b>。每次 commit（存档）= 一次发布。第 12 课你的项目也会这样「发射」上线。</span><span class="en">Right! That's <b>GitHub Pages</b>. Every commit (save) = one release. In Lesson 12 your project "launches" onto the web the same way.</span></div>
</div>

---

## 👓 <span class="zh">读懂别人的代码</span><span class="en">Reading other people's code</span>
{: #read}

<p class="zh">做项目时你会读很多<b>别人写的代码</b>（骨架的、AI 的、游戏里的）。读代码有三步：① 从上到下找<b>函数的名字</b>（def）——它们是「目录」；② 找<b>主循环</b>（while 或 tick）——程序在这里转；③ 找<b>变量</b>——程序记住了什么。</p>
<p class="en">In a project you'll read lots of <b>code written by others</b> (skeletons, AI, games). Three steps: ① scan top to bottom for <b>function names</b> (def) — they're the table of contents; ② find the <b>main loop</b> (while or tick) — where the program spins; ③ find the <b>variables</b> — what it remembers.</p>

<p><span class="zh">练习对象：一个 47 行的<b>火箭货舱清单</b>。先别改，先读。</span><span class="en">Practice on a 47-line <b>rocket cargo manifest</b>. Don't change it yet — read it.</span></p>

<div class="playground" data-src="{{ '/lessons/10/code/cargo.py' | relative_url }}" data-title="🛰️ 火箭货舱清单" data-title-en="🛰️ Rocket cargo manifest" data-canvas="no" data-save="cargo-app" data-draft="l10-cargo" data-rows="18"></div>

<ol class="code-walk">
  <li><code>cargo = []  weights = []  MAX_LOAD</code><span><span class="zh">③ 变量：两个<b>一样长</b>的列表——第 i 件货和它的重量在同一个位置</span><span class="en">③ variables: two lists of the <b>same length</b> — item i and its weight sit at the same position</span></span></li>
  <li><code>def total():</code><span><span class="zh">① 函数 1：把所有重量加起来，<code>return</code> 总重</span><span class="en">① function 1: add up all weights and <code>return</code> the total</span></span></li>
  <li><code>def show():</code><span><span class="zh">① 函数 2：显示清单（里面也用了 <code>total()</code>）</span><span class="en">① function 2: show the manifest (it uses <code>total()</code> too)</span></span></li>
  <li><code>def load(thing, kg):</code><span><span class="zh">① 函数 3：太重就拒绝，不然两个列表都 <code>append</code></span><span class="en">① function 3: refuse if too heavy, otherwise <code>append</code> to both lists</span></span></li>
  <li><code>def unload(number):</code><span><span class="zh">① 函数 4：两个列表都 <code>pop</code> 掉同一个位置</span><span class="en">① function 4: <code>pop</code> the same position from both lists</span></span></li>
  <li><code>while True: … break</code><span><span class="zh">② 主循环：菜单 → 问 → 做；选 4 发射并跳出</span><span class="en">② main loop: menu → ask → do; 4 launches and leaves the loop</span></span></li>
</ol>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">货舱里已经有 350 kg。再装一块 900 kg 的「大石头」，会发生什么？</span><span class="en">The bay already holds 350 kg. You load a 900 kg "big rock". What happens?</span></p>
  <div class="opts"><button><span class="zh">装进去了，总重 1250</span><span class="en">It's loaded, total 1250</span></button><button><span class="zh">打印「太重了」，什么都没装</span><span class="en">It prints "too heavy" and loads nothing</span></button><button><span class="zh">程序报错</span><span class="en">The program crashes</span></button></div>
  <div class="why"><span class="zh"><code>load</code> 先算 <code>total() + kg</code> = 1250，比 <code>MAX_LOAD</code>（1000）大，所以走 <code>if</code> 那条路：只打印，不 <code>append</code>。</span><span class="en"><code>load</code> first works out <code>total() + kg</code> = 1250, which is bigger than <code>MAX_LOAD</code> (1000), so it takes the <code>if</code> path: it prints and doesn't <code>append</code>.</span></div>
</div>

<ul class="quests" data-key="l10-read">
  <li><span class="zh">说出 4 个函数的名字，每个用一句话说它是干嘛的。</span><span class="en">Name the 4 functions and say what each does in one sentence.</span></li>
  <li><span class="zh"><code>total()</code> 被<b>哪两个</b>函数用到了？（在画板里按 Ctrl+F / ⌘F 搜 <code>total()</code>）</span><span class="en"><b>Which two</b> functions use <code>total()</code>? (Press Ctrl+F / ⌘F in the playground and search <code>total()</code>)</span></li>
  <li><span class="zh">运行：装卫星 300 kg → 装食物 50 kg → 看清单 → 卸第 1 件 → 看清单 → 发射。</span><span class="en">Run it: load a satellite 300 kg → food 50 kg → show → unload #1 → show → launch.</span></li>
  <li><span class="zh">改一个地方：每次装好以后自动显示清单（提示：在 <code>load</code> 里调用 <code>show()</code>——放在哪一行？）。</span><span class="en">Change one thing: show the manifest automatically after each load (hint: call <code>show()</code> inside <code>load</code> — on which line?).</span></li>
  <li>🐞 <span class="zh">只装了 2 件，却「卸第 9 件」会怎样？运行试试，读报错。这就是下一节要讲的——<b>测试</b>。</span><span class="en">With only 2 items, "unload #9"? Try it and read the error. That's what the next part is about — <b>testing</b>.</span></li>
</ul>

---

## 🧪 <span class="zh">测试：让电脑帮你检查</span><span class="en">Testing: let the computer check</span>
{: #test}

<p class="zh">每次改完代码都要自己玩一遍太累了。<b><code>assert</code></b> 的意思是「我断言这件事是真的」——它后面的条件必须是 True，否则程序<b>立刻停下来报错</b>。写几个 assert，一点运行就知道有没有改坏。</p>
<p class="en">Playing the whole thing after every change gets tiring. <b><code>assert</code></b> means "I claim this is true" — the condition after it must be True, or the program <b>stops with an error</b>. Write a few asserts and one click tells you if anything broke.</p>

<div class="box box-think"><span class="box-title"><span class="zh">🧩 纯函数：最好测的函数</span><span class="en">🧩 Pure functions: the easiest to test</span></span>
<span class="zh"><b>纯函数</b> = 只吃参数、只吐 <code>return</code>，不碰海龟、不 print、不 input。像计算器上的一个按钮。你没法 assert「画面看起来对」，但能 assert <code>is_safe_landing(1, 10) == True</code>。所以好项目会把<b>规则</b>（安全吗？撞了吗？全部 GO 吗？）写成纯函数，再测它们。三个太空项目都是这样设计的。</span>
<span class="en">A <b>pure function</b> only takes parameters and gives back a <code>return</code> — no turtles, no print, no input. Like one button on a calculator. You can't assert "the picture looks right", but you can assert <code>is_safe_landing(1, 10) == True</code>. So good projects put the <b>rules</b> (safe? crashed? all GO?) into pure functions and test them. All three space projects are built this way.</span>
</div>

<div class="cmds">
  <div class="cmd"><code>assert keep_inside(0) == 0</code><span><span class="zh">keep_inside(0) 必须等于 0</span><span class="en">keep_inside(0) must equal 0</span></span></div>
  <div class="cmd"><code>assert x > 0, "x 要大于 0"</code><span><span class="zh">逗号后面是失败时的提示</span><span class="en">after the comma: the message if it fails</span></span></div>
  <div class="cmd"><code>abs(-30)</code><span><span class="zh">去掉负号 → 30（「离中心多远」常用）</span><span class="en">drops the minus sign → 30 (handy for "how far from the middle")</span></span></div>
  <div class="cmd"><code>def test(): …</code><span><span class="zh">把测试放进一个函数，程序开头调用</span><span class="en">put tests in a function, call it at the start</span></span></div>
</div>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的代码里藏着一个「写错的测试」。运行后，第一个报错会在哪？</span><span class="en">The code below hides one "wrongly written test". When you run it, where is the first error?</span></p>
  <div class="opts"><button><span class="zh">第 1 个 assert</span><span class="en">The 1st assert</span></button><button><span class="zh">最后那个 keep_inside(300) == 300</span><span class="en">The last one, keep_inside(300) == 300</span></button><button><span class="zh">不会报错</span><span class="en">No error</span></button></div>
  <div class="why"><span class="zh">三个函数都没有 bug，前面的测试全过。最后那个测试本身写错了：300 超过 270，应该被拉回 <b>270</b>。<b>测试也会有 bug</b>——报错时，函数和测试两边都要看。</span><span class="en">The three functions have no bug, so the earlier tests pass. The last test itself is wrong: 300 is past 270, so it should be pulled back to <b>270</b>. <b>Tests can have bugs too</b> — when one fails, check both the function and the test.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/10/code/tests.py' | relative_url }}" data-title="🧪 三个任务的测试" data-title-en="🧪 Tests from three missions" data-canvas="no" data-save="space-tests" data-draft="l10-tests" data-rows="16"></div>

<ul class="quests" data-key="l10-test">
  <li><span class="zh">运行，读红框：第几行？AssertionError 后面的话是谁写的？</span><span class="en">Run it and read the red box: which line? Who wrote the words after AssertionError?</span></li>
  <li><span class="zh">决定：是函数错了还是测试错了？修好它，让「✅ 所有测试都通过了」出现。</span><span class="en">Decide: is the function wrong or the test? Fix it so "✅ All tests passed" shows up.</span></li>
  <li><span class="zh">现在故意改坏：把 <code>is_safe_landing</code> 里的 <code>speed &lt;= 2</code> 改成 <code>speed &lt; 2</code>。哪个测试抓到了它？如果没有那个测试，你玩游戏时会发现吗？改回来。</span><span class="en">Now break it on purpose: change <code>speed &lt;= 2</code> to <code>speed &lt; 2</code> in <code>is_safe_landing</code>. Which test catches it? Without that test, would you notice while playing? Change it back.</span></li>
  <li><span class="zh">给 <code>all_systems_go</code> 写一个你自己的测试：3 个系统，<b>最后一个</b>是 NO-GO。</span><span class="en">Write your own test for <code>all_systems_go</code>: 3 systems, the <b>last</b> one is NO-GO.</span></li>
  <li>🏆 <span class="zh">给 <code>keep_inside</code> 写一个「刚好在边上」的测试（270 和 -270）。</span><span class="en">Write an "exactly on the edge" test for <code>keep_inside</code> (270 and -270).</span></li>
</ul>

<div class="box box-tip"><span class="box-title"><span class="zh">🎯 边界测试：bug 最爱躲在边上</span><span class="en">🎯 Edge tests: bugs love to hide at the edges</span></span>
<span class="zh">测「中间」很容易对，测<b>刚好在线上</b>的数字（2、40、270）才抓得到 <code>&lt;</code> 和 <code>&lt;=</code> 搞混的 bug。好测试 = 一个普通的 + 一个太大 / 太小的 + 一个刚好在边上的。手动的也算测试：① 正常玩对吗？② 乱按、乱输入会怎样？③ 连玩 3 遍还正常吗？</span>
<span class="en">The middle is easy to get right; numbers <b>exactly on the line</b> (2, 40, 270) catch the bugs where <code>&lt;</code> and <code>&lt;=</code> got mixed up. Good tests = a normal one + a too-big / too-small one + one exactly on the edge. Manual tests count too: ① does normal play work? ② what if I mash keys or type nonsense? ③ still fine after 3 rounds?</span>
</div>

---

## 🚀 <span class="zh">选你的太空任务</span><span class="en">Choose your space mission</span>
{: #choose}

<p class="zh">第 11 课你会<b>自己做</b>，第 12 课<b>发布上线</b>。三个任务，选<b>一个</b>。每个都有一个<b>能跑的骨架</b>、要你写的纯函数和测试。先每个<b>试飞 2 分钟</b>！（键盘游戏：运行后先点一下画布。）</p>
<p class="en">In Lesson 11 you <b>build it yourself</b>; in Lesson 12 you <b>launch it</b>. Three missions — choose <b>one</b>. Each has a <b>running skeleton</b> plus pure functions and tests for you to write. <b>Test-fly each one for 2 minutes</b> first! (Keyboard games: click the canvas after running.)</p>

<div class="table-wrap">
<table>
<tr><th></th><th>🚀 <span class="zh">助推器回家</span><span class="en">Booster landing</span></th><th>☄️ <span class="zh">陨石大躲避</span><span class="en">Asteroid dodger</span></th><th>🛰️ <span class="zh">任务控制中心</span><span class="en">Mission control</span></th></tr>
<tr><td><span class="zh">玩起来</span><span class="en">Feels like</span></td><td><span class="zh">手要稳，省着用燃料</span><span class="en">steady hands, save fuel</span></td><td><span class="zh">反应快，越来越刺激</span><span class="en">quick reflexes, gets intense</span></td><td><span class="zh">动脑指挥，看动画</span><span class="en">thinking + watching</span></td></tr>
<tr><td><span class="zh">主要练</span><span class="en">Main skills</span></td><td><span class="zh">速度 + 重力、if + and</span><span class="en">velocity + gravity, if + and</span></td><td><span class="zh">列表 + for、碰撞</span><span class="en">lists + for, collisions</span></td><td><span class="zh">字典、input、两个心跳</span><span class="en">dicts, input, two heartbeats</span></td></tr>
<tr><td><span class="zh">要写的纯函数</span><span class="en">Pure functions</span></td><td><code>is_safe_landing</code></td><td><code>keep_inside</code> <code>speed_for</code></td><td><code>all_systems_go</code> <code>stage_for</code></td></tr>
<tr><td><span class="zh">难度</span><span class="en">Difficulty</span></td><td>⭐⭐⭐</td><td><span class="zh">⭐⭐（起步最快）</span><span class="en">⭐⭐ (quickest start)</span></td><td><span class="zh">⭐⭐⭐（代码最长）</span><span class="en">⭐⭐⭐ (most code)</span></td></tr>
</table>
</div>

### 🚀 A · <span class="zh">助推器回家</span><span class="en">Bring the Booster Home</span>

<div class="two">
<div>
<p><span class="zh">助推器从天上掉下来，重力让它越来越快。按 <b>↑</b> 点火减速，<b>← →</b> 侧推对准无人船。燃料有限！落得太快、或者没落在甲板上 = 坠毁。<br><b>小秘密</b>：真正的助推器也是快到海面才点火减速，省燃料。</span><span class="en">The booster falls and gravity makes it faster and faster. Press <b>↑</b> to fire the engine, <b>← →</b> to steer onto the drone ship. Fuel is limited! Too fast, or off the deck = crash.<br><b>Secret</b>: real boosters also wait until close to the sea before the landing burn, to save fuel.</span></p>
<p><span class="zh"><b>必做</b>：① 燃料：点火用 1 份，没油点不了，仪表盘显示燃料 ② ← → 侧推（左右速度 <code>vx</code>）③ 着陆判定：写 <code>is_safe_landing</code> + 测试，成功 / 坠毁不一样<br><b>加分</b>：🔥 点火时出现火焰 · 🌬️ 随机侧风 · 🚢 会动的无人船 · 🌕 月球 / 火星模式（字典存重力）· ⭐ 剩的燃料越多分越高</span><span class="en"><b>Must</b>: ① fuel: each burn uses 1, no fuel = no burn, fuel on the dashboard ② ← → side thrusters (sideways speed <code>vx</code>) ③ landing check: write <code>is_safe_landing</code> + tests; success and crash look different<br><b>Nice</b>: 🔥 a flame when burning · 🌬️ random crosswind · 🚢 a moving drone ship · 🌕 Moon / Mars mode (gravity in a dict) · ⭐ more fuel left = higher score</span></p>
</div>
<div>
<div class="playground" data-src="{{ '/lessons/10/code/skeleton-booster.py' | relative_url }}" data-title="🚀 骨架 A：助推器回家" data-title-en="🚀 Skeleton A: Booster landing" data-save="week10-skeleton" data-draft="l10-skel-booster" data-rows="10"></div>
</div>
</div>

<details class="hint"><summary><span class="zh">📄 例子计划书 A（看完写你自己的版本）</span><span class="en">📄 Example plan A (read it, then write your own)</span></summary>
<p><span class="zh"><b>名字</b>：回家吧，助推器！ <b>一句话</b>：用 ↑ ← → 控制下落的助推器，又慢又准地落在无人船上。<br><b>必做</b>：[ ] 燃料会用完 [ ] 侧推 [ ] 判断成功 / 坠毁<br><b>加分</b>：[ ] 火焰 [ ] 侧风<br><b>小步骤</b>：1. 运行骨架，按 ↑ 看速度变化，读懂 <code>tick()</code> 2. 仪表盘显示燃料 3. 点火扣燃料，没油点不了 4. ← → 侧推 5. 删掉 3 个测试前面的 <code>#</code>，看它们变红 6. 写 <code>is_safe_landing</code>，测试变绿 7. <code>touchdown()</code> 显示成功 / 坠毁 8. 玩 3 遍，存档<br><b>要测的纯函数</b>：<code>is_safe_landing(1, 10) == True</code>、<code>is_safe_landing(5, 10) == False</code>、<code>is_safe_landing(2, 40) == True</code>（边界）</span><span class="en"><b>Name</b>: Come Home, Booster! <b>One sentence</b>: steer a falling booster with ↑ ← → and land it slowly and accurately on the drone ship.<br><b>Must</b>: [ ] fuel runs out [ ] side thrusters [ ] success / crash check<br><b>Nice</b>: [ ] flame [ ] crosswind<br><b>Steps</b>: 1. run the skeleton, press ↑, watch the speed, understand <code>tick()</code> 2. fuel on the dashboard 3. burns use fuel, none left = no burn 4. ← → thrusters 5. remove the <code>#</code> from the 3 tests and watch them go red 6. write <code>is_safe_landing</code>, tests go green 7. <code>touchdown()</code> shows success / crash 8. play 3 times, save<br><b>Pure function tests</b>: <code>is_safe_landing(1, 10) == True</code>, <code>is_safe_landing(5, 10) == False</code>, <code>is_safe_landing(2, 40) == True</code> (edge)</span></p>
</details>

### ☄️ B · <span class="zh">陨石大躲避</span><span class="en">Asteroid Dodger</span>

<div class="two">
<div>
<p><span class="zh">飞船在底下，陨石从上面砸下来。用 <b>← →</b> 躲开，每躲过一颗得 1 分，分数越高陨石越快。撞 3 次就 GAME OVER。它是 <a href="{{ '/games/catch/' | relative_url }}">🍎 接水果</a>「反过来」的版本！</span><span class="en">Your ship sits at the bottom while asteroids rain down. Dodge with <b>← →</b>: 1 point per asteroid dodged, and the higher your score, the faster they fall. 3 hits = GAME OVER. It's <a href="{{ '/games/catch/' | relative_url }}">🍎 Fruit Catcher</a> turned upside down!</span></p>
<p><span class="zh"><b>必做</b>：① 飞船不会飞出画布（写 <code>keep_inside</code> + 测试）② 撞到陨石扣命，命没了 GAME OVER（用 <code>hit</code>）③ 越来越快（写 <code>speed_for</code> + 测试，有上限）<br><b>加分</b>：🔋 收集金色燃料电池 · ❤️ 用 <code>"❤️" * lives</code> 显示命 · 🛡️ 按空格 3 秒护盾 · 🏆 最高分 · 🌠 每颗陨石速度不同</span><span class="en"><b>Must</b>: ① the ship can't leave the screen (write <code>keep_inside</code> + tests) ② hitting a rock costs a life; no lives = GAME OVER (use <code>hit</code>) ③ it speeds up (write <code>speed_for</code> + tests, with a top speed)<br><b>Nice</b>: 🔋 collect gold fuel cells · ❤️ show lives as <code>"❤️" * lives</code> · 🛡️ space bar = 3-second shield · 🏆 high score · 🌠 every rock has its own speed</span></p>
</div>
<div>
<div class="playground" data-src="{{ '/lessons/10/code/skeleton-asteroids.py' | relative_url }}" data-title="☄️ 骨架 B：陨石大躲避" data-title-en="☄️ Skeleton B: Asteroid dodger" data-save="week10-skeleton" data-draft="l10-skel-asteroids" data-rows="10"></div>
</div>
</div>

<details class="hint"><summary><span class="zh">📄 例子计划书 B（看完写你自己的版本）</span><span class="en">📄 Example plan B (read it, then write your own)</span></summary>
<p><span class="zh"><b>名字</b>：陨石带大逃亡 <b>一句话</b>：开着飞船躲陨石，躲得越多越快，撞 3 次结束。<br><b>必做</b>：[ ] 不飞出画布 [ ] 撞了扣命 + GAME OVER [ ] 越来越快<br><b>加分</b>：[ ] 燃料电池 [ ] 心形的命<br><b>小步骤</b>：1. 运行骨架，读懂 <code>rocks</code> 列表和 <code>tick()</code> 里的 <code>for</code> 2. 删掉 <code>keep_inside</code> 测试前面的 <code>#</code> → 红 → 写函数 → 绿 3. ← → 用上 <code>keep_inside</code>（一直按 ← 试试）4. 用 <code>hit</code> 判断撞上：命 -1 5. 命没了 GAME OVER，游戏停 6. <code>speed_for</code> 测试 → 写函数 7. 玩 3 遍，存档<br><b>要测的纯函数</b>：<code>keep_inside(400) == 270</code>、<code>keep_inside(270) == 270</code>（边界）、<code>speed_for(1000) == MAX_SPEED</code></span><span class="en"><b>Name</b>: Asteroid Belt Escape <b>One sentence</b>: fly a ship through falling asteroids; the more you dodge the faster they come; 3 hits and it's over.<br><b>Must</b>: [ ] stays on screen [ ] hits cost lives + GAME OVER [ ] speeds up<br><b>Nice</b>: [ ] fuel cells [ ] heart lives<br><b>Steps</b>: 1. run the skeleton, understand the <code>rocks</code> list and the <code>for</code> in <code>tick()</code> 2. remove the <code>#</code> from the <code>keep_inside</code> tests → red → write it → green 3. ← → use <code>keep_inside</code> (hold ← to check) 4. use <code>hit</code> to detect a crash: lives −1 5. no lives = GAME OVER, game stops 6. <code>speed_for</code> tests → write it 7. play 3 times, save<br><b>Pure function tests</b>: <code>keep_inside(400) == 270</code>, <code>keep_inside(270) == 270</code> (edge), <code>speed_for(1000) == MAX_SPEED</code></span></p>
</details>

### 🛰️ C · <span class="zh">任务控制中心</span><span class="en">Mission Control</span>

<div class="two">
<div>
<p><span class="zh">你是<b>飞行总监</b>。选载荷 → 每个系统报 GO / NO-GO → 全部 GO 才倒数发射 → 一二级分离 → 入轨，绕地球飞 → 打印任务日志。手速不重要，脑子最重要。</span><span class="en">You're the <b>flight director</b>. Pick a payload → every system reports GO / NO-GO → only all-GO gets a countdown → stage separation → orbit around the Earth → print the mission log. Fast fingers don't matter; your brain does.</span></p>
<p><span class="zh"><b>必做</b>：① GO / NO-GO：写 <code>all_systems_go</code> + 测试，有 NO-GO 就推迟发射（scrub）② 倒数 T-10…T-0 写在画布上（ontimer），按两次空格也只发射一次 ③ 一二级分离：写 <code>stage_for</code> + 测试，记日志，一级往下掉<br><b>加分</b>：🔁 推迟后「明天再试」· 🛑 按 A 中止任务 · 🌍 数绕了几圈 · 👩‍🚀 载荷不同、加速度不同（字典）· 🎯 一级飞回来降落（和 🚀 合体！）</span><span class="en"><b>Must</b>: ① GO / NO-GO: write <code>all_systems_go</code> + tests; any NO-GO = scrub ② countdown T-10…T-0 on the canvas (ontimer); pressing space twice still launches once ③ stage separation: write <code>stage_for</code> + tests, log it, stage 1 falls away<br><b>Nice</b>: 🔁 after a scrub, "try tomorrow" · 🛑 press A to abort · 🌍 count the orbits · 👩‍🚀 different payloads, different acceleration (dict) · 🎯 stage 1 flies back and lands (team-up with 🚀!)</span></p>
</div>
<div>
<div class="playground" data-src="{{ '/lessons/10/code/skeleton-mission.py' | relative_url }}" data-title="🛰️ 骨架 C：任务控制中心" data-title-en="🛰️ Skeleton C: Mission control" data-save="week10-skeleton" data-draft="l10-skel-mission" data-rows="10"></div>
</div>
</div>

<details class="hint"><summary><span class="zh">📄 例子计划书 C（看完写你自己的版本）</span><span class="en">📄 Example plan C (read it, then write your own)</span></summary>
<p><span class="zh"><b>名字</b>：猎鹰发射指挥部 <b>一句话</b>：检查每个系统，全部 GO 就倒数发射，看火箭分离、入轨，最后读任务日志。<br><b>必做</b>：[ ] GO / NO-GO 决定发不发射 [ ] 倒数 [ ] 一二级分离<br><b>加分</b>：[ ] 明天再试 [ ] 数圈数<br><b>小步骤</b>：1. 运行骨架（输入 1、2 或 3），读懂 <code>poll()</code> 和 <code>checks</code> 字典 2. <code>all_systems_go</code> 测试 → 写函数 → 绿 3. 主程序：全部 GO 才能按空格发射，不然 SCRUB 4. 写 <code>countdown()</code>：先用 print 倒数，再写到画布上，每 0.5 秒一个数 5. 按两次空格只发射一次 6. <code>stage_for</code> 测试 → 写函数 → 分离时记日志 + 一级往下掉 7. 跑 3 次（有时 SCRUB，正常！），存档<br><b>要测的纯函数</b>：<code>all_systems_go({"燃料": "GO", "天气": "NO-GO"}) == False</code>、<code>stage_for(SEPARATION) == 2</code>（边界）</span><span class="en"><b>Name</b>: Falcon Launch Control <b>One sentence</b>: check every system; if all GO, count down and launch, watch staging and orbit, then read the mission log.<br><b>Must</b>: [ ] GO / NO-GO decides the launch [ ] countdown [ ] stage separation<br><b>Nice</b>: [ ] try tomorrow [ ] count orbits<br><b>Steps</b>: 1. run the skeleton (type 1, 2 or 3), understand <code>poll()</code> and the <code>checks</code> dict 2. <code>all_systems_go</code> tests → write it → green 3. main program: space launches only if all GO, otherwise SCRUB 4. write <code>countdown()</code>: first with print, then on the canvas, one number every 0.5 s 5. pressing space twice launches only once 6. <code>stage_for</code> tests → write it → log the separation + stage 1 falls 7. run 3 times (sometimes it scrubs — that's normal!), save<br><b>Pure function tests</b>: <code>all_systems_go({"fuel": "GO", "weather": "NO-GO"}) == False</code>, <code>stage_for(SEPARATION) == 2</code> (edge)</span></p>
</details>

<div class="box box-think"><span class="zh">🧠 <b>选不出来？</b>问自己三个问题：① 哪个做完了我最想给朋友玩？② 我喜欢<b>手快</b>（☄️）、<b>手稳</b>（🚀）还是<b>动脑指挥</b>（🛰️）？③ 试飞的时候，哪个骨架我最想马上改？三个都想做？先做一个，做完再说——别的写进「下一个项目」。有自己的太空点子（比如「用机械臂接住助推器」）？可以，但要从<b>最像的那个骨架</b>改起，并且先给老师讲清楚 3 个必做功能。</span><span class="en">🧠 <b>Can't decide?</b> Ask three questions: ① which finished one would I most want a friend to play? ② do I like <b>fast hands</b> (☄️), <b>steady hands</b> (🚀) or <b>commanding with my brain</b> (🛰️)? ③ during the test flights, which skeleton did I most want to change right away? Want all three? Finish one first — put the others on your "next project" list. Got your own space idea (like "catch the booster with tower arms")? OK, but start from <b>the most similar skeleton</b> and explain your 3 must-haves to your teacher first.</span></div>

---

## 📄 <span class="zh">写任务计划书</span><span class="en">Write the mission plan</span>
{: #plan}

<p><span class="zh">填下面的表格，它会帮你拼成计划书。<b>可以参考例子计划书，但要用你自己的话写</b>（加分功能尤其要是你自己想要的）。拼好后<b>复制</b>，贴到下面的画板里（计划书也是一个 Python 文件——全是注释！），存到作品墙就交了作业。</span><span class="en">Fill in the form and it builds your plan. <b>You may look at the example plans, but write it in your own words</b> (especially the nice-to-haves — they should be things you really want). Then <b>copy</b> it, paste it into the playground below (the plan is a Python file too — all comments!) and save it to the Gallery to hand it in.</span></p>

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
  <input name="p-name" data-ph-zh="比如：回家吧，助推器！" data-ph-en="e.g. Come Home, Booster!" placeholder="比如：回家吧，助推器！">
  <label>🎯 <span class="zh">它是做什么的（一句话）</span><span class="en">What it does (one sentence)</span></label>
  <input name="p-what" data-ph-zh="比如：用 ↑ ← → 让助推器慢慢落在无人船上" data-ph-en="e.g. use ↑ ← → to land the booster gently on the drone ship" placeholder="比如：用 ↑ ← → 让助推器慢慢落在无人船上">
  <label>🚀 <span class="zh">我选的任务</span><span class="en">My mission</span></label>
  <input name="p-type" data-ph-zh="点下面选一个" data-ph-en="pick one below" placeholder="点下面选一个">
  <div class="chips" data-for="p-type"><button class="chip"><span class="zh">🚀 助推器回家</span><span class="en">🚀 Booster landing</span></button><button class="chip"><span class="zh">☄️ 陨石大躲避</span><span class="en">☄️ Asteroid dodger</span></button><button class="chip"><span class="zh">🛰️ 任务控制中心</span><span class="en">🛰️ Mission control</span></button><button class="chip"><span class="zh">🌌 我自己的太空点子</span><span class="en">🌌 My own space idea</span></button></div>
  <label>🕹️ <span class="zh">玩家怎么玩（2–3 句）</span><span class="en">How the player plays (2–3 lines)</span></label>
  <textarea name="p-how" rows="3" data-ph-zh="1. 点一下画布  2. 按 ↑ 点火  3. ……" data-ph-en="1. click the canvas  2. press ↑ to fire  3. …" placeholder="1. 点一下画布  2. 按 ↑ 点火  3. ……"></textarea>
  <label>✅ <span class="zh">必做的 3 个功能（每行一个）</span><span class="en">3 must-have features (one per line)</span></label>
  <textarea name="p-must" rows="3" placeholder="1.&#10;2.&#10;3."></textarea>
  <label>⭐ <span class="zh">加分的 2 个功能</span><span class="en">2 nice-to-have features</span></label>
  <textarea name="p-bonus" rows="2" placeholder="1.&#10;2."></textarea>
  <label>🪜 <span class="zh">拆成的小步骤（至少 5 步，每步 10 分钟能做完，每步都能运行看到）</span><span class="en">Small steps (≥5, each doable in 10 minutes and visible when run)</span></label>
  <textarea name="p-steps" rows="5" data-ph-zh="1. 运行骨架，读懂 tick()&#10;2.&#10;3.&#10;4.&#10;5." data-ph-en="1. run the skeleton, understand tick()&#10;2.&#10;3.&#10;4.&#10;5." placeholder="1. 运行骨架，读懂 tick()&#10;2.&#10;3.&#10;4.&#10;5."></textarea>
  <label>🧪 <span class="zh">我要测试的纯函数（写 1–3 个 assert）</span><span class="en">Pure functions I'll test (write 1–3 asserts)</span></label>
  <textarea name="p-test" rows="2" data-ph-zh="比如：is_safe_landing(2, 40) == True（边界）" data-ph-en="e.g. is_safe_landing(2, 40) == True (edge)" placeholder="比如：is_safe_landing(2, 40) == True（边界）"></textarea>
  <label>📖 <span class="zh">我需要的知识点（课数）</span><span class="en">Knowledge I need (lesson numbers)</span></label>
  <input name="p-know" data-ph-zh="比如：if + and（4、6）、函数（7）、字典（9）" data-ph-en="e.g. if + and (4, 6), functions (7), dicts (9)" placeholder="比如：if + and（4、6）、函数（7）、字典（9）">
  <label>🤖 <span class="zh">我会问 AI 什么（只要提示）</span><span class="en">What I'll ask AI (hints only)</span></label>
  <input name="p-ai" data-ph-zh="比如：怎么让按 ↑ 键改变速度？给我一个提示" data-ph-en="e.g. a hint for making ↑ change the speed" placeholder="比如：怎么让按 ↑ 键改变速度？给我一个提示">
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
    var L = ['# 🗺️ ' + (E ? 'My mission plan' : '我的任务计划书') + (v('p-name') ? (E ? ': ' : '：') + v('p-name') : ''), '#'];
    var sec = function (title, body) { L.push('# ===== ' + title + ' ====='); if (body) { body.forEach(function (b) { L.push('#   ' + b); }); filled++; } else L.push('#   ...'); L.push('#'); };
    sec(E ? '1. Project name' : '1. 项目名字', v('p-name') ? [v('p-name')] : null);
    sec(E ? '2. What it does' : '2. 它是做什么的', v('p-what') ? [v('p-what')] : null);
    sec(E ? '3. My mission' : '3. 我选的任务', v('p-type') ? [v('p-type')] : null);
    sec(E ? '4. How the player plays' : '4. 玩家怎么玩', lines(v('p-how')).length ? lines(v('p-how')) : null);
    sec(E ? '5. Must-have features (3)' : '5. 必做的 3 个功能', lines(v('p-must')).length ? lines(v('p-must')).map(function (l) { return '[ ] ' + l; }) : null);
    sec(E ? '6. Nice-to-have (2)' : '6. 加分的 2 个功能', lines(v('p-bonus')).length ? lines(v('p-bonus')).map(function (l) { return '[ ] ' + l; }) : null);
    sec(E ? '7. Small steps' : '7. 拆成的小步骤', lines(v('p-steps')).length ? lines(v('p-steps')) : null);
    sec(E ? '8. Pure functions + asserts' : '8. 要测试的纯函数 + assert', lines(v('p-test')).length ? lines(v('p-test')) : null);
    sec(E ? '9. Knowledge I need' : '9. 我需要的知识点', v('p-know') ? [v('p-know')] : null);
    sec(E ? '10. What I will ask AI (hints only)' : '10. 我会问 AI 什么（只要提示）', v('p-ai') ? [v('p-ai')] : null);
    L.push('print("🗺️ ' + (E ? 'This is my mission plan. The code comes in Lesson 11!' : '这是我的任务计划书，代码在第 11 课写！') + '")');
    out.textContent = L.join('\n');
    var steps = lines(v('p-steps')).length, must = lines(v('p-must')).length, tests = lines(v('p-test')).length;
    var msg;
    if (filled < 3) msg = E ? 'Start with the name, what it does and your mission ✏️' : '先填名字、「它是做什么的」和选的任务 ✏️';
    else if (must < 3) msg = E ? '⭐ Good start! Write 3 must-have features' : '⭐ 不错的开始！必做功能要写满 3 个';
    else if (steps < 5) msg = E ? '⭐⭐ Nice! Split it into at least 5 small steps' : '⭐⭐ 很好！小步骤至少 5 步';
    else if (tests < 1) msg = E ? '⭐⭐⭐ Almost — which pure function will you test? Write an assert' : '⭐⭐⭐ 快好了——你要测哪个纯函数？写一个 assert';
    else if (filled < 10) msg = E ? '⭐⭐⭐⭐ Nearly there — fill in the last sections' : '⭐⭐⭐⭐ 差一点点，把最后几栏填上';
    else msg = E ? '⭐⭐⭐⭐⭐ A real mission plan! Copy it and save it' : '⭐⭐⭐⭐⭐ 一份真正的任务计划书！复制它，存起来';
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

<div class="playground" data-src="{{ '/lessons/10/code/plan-template.py' | relative_url }}" data-title="📄 我的任务计划书" data-title-en="📄 My mission plan" data-canvas="no" data-save="week10-plan" data-draft="l10-plan" data-rows="14"></div>

<ul class="quests" data-key="l10-plan">
  <li><span class="zh">计划书拼到 ⭐⭐⭐⭐⭐，复制，贴进画板（把模板替换掉），运行一下确认没有报错。</span><span class="en">Get the plan to ⭐⭐⭐⭐⭐, copy it, paste it into the playground (replacing the template), run it to check for errors.</span></li>
  <li><span class="zh">在你选的骨架里找到所有 <code>TODO</code>（Ctrl+F / ⌘F）。每个 TODO 对应计划书里的哪一步？</span><span class="en">Find every <code>TODO</code> in your chosen skeleton (Ctrl+F / ⌘F). Which plan step does each one match?</span></li>
  <li><span class="zh">给老师讲一遍你的计划，像任务简报一样（讲出来 = 真的想清楚了）。</span><span class="en">Explain your plan to your teacher like a mission briefing (saying it out loud = really thought it through).</span></li>
</ul>

---

## 🤖 <span class="zh">和 AI 一起：头脑风暴，但计划我来写</span><span class="en">Together with AI: brainstorm, but I write the plan</span>

<p><span class="zh">AI 很会出点子。选好任务以后，可以这样问它要<b>加分功能</b>的点子：</span><span class="en">AI is great at ideas. Once you've picked a mission, ask it for <b>nice-to-have</b> ideas like this:</span></p>

<pre class="zh" style="white-space:pre-wrap">我是小学 6 年级的学生，喜欢太空。我在用 Python turtle 做「助推器回家」游戏（按 ↑ 减速，落在无人船上）。
我会用 if、for、while、列表、字典、函数、onkey 和 ontimer。
请给我 5 个「加分功能」的点子，每个只用一句话，每个都要能在 20 分钟内做出最简单的版本。不要写代码。</pre>
<pre class="en" style="white-space:pre-wrap">I'm a Year 6 student who loves space. I'm making a "booster landing" game with Python turtle (press ↑ to slow down, land on a drone ship).
I know if, for, while, lists, dicts, functions, onkey and ontimer.
Give me 5 ideas for nice-to-have features, one sentence each, each with a simplest version I can build in 20 minutes. No code.</pre>
<button class="pg-btn copy-prev">📋 <span class="zh">复制</span><span class="en">Copy</span></button>

<div class="chat">
  <div class="bubble me"><span class="zh">（坏问法）帮我做一个 SpaceX 游戏。</span><span class="en">(bad) Make me a SpaceX game.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">给你 300 行代码……（你看不懂，也改不动）</span><span class="en">Here are 300 lines of code… (you can't read it, so you can't change it)</span></div>
  <div class="bubble me"><span class="zh">（好问法）我在做陨石大躲避，必做功能 1 是飞船不能飞出画布。我写了 <code>keep_inside(x)</code>，但 <code>assert keep_inside(400) == 270</code> 失败了。<b>给我一个提示</b>，不要完整代码。</span><span class="en">(good) I'm making Asteroid Dodger; must-have 1 is "the ship can't leave the screen". I wrote <code>keep_inside(x)</code> but <code>assert keep_inside(400) == 270</code> fails. <b>Give me a hint</b>, no full code.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">看看你的 <code>if</code>：x 比 270 大的时候，你 <code>return</code> 的是什么？用 print 侦探打印一下 <code>keep_inside(400)</code> 试试。</span><span class="en">Look at your <code>if</code>: when x is bigger than 270, what do you <code>return</code>? Try printing <code>keep_inside(400)</code> like a detective.</span></div>
</div>

<div class="box box-rule"><span class="zh">📜 <b>规矩：</b>点子可以问 AI；<b>选哪个任务、拆步骤、必做功能——由你写</b>。计划是你的，所以你才看得懂自己的项目。</span><span class="en">📜 <b>Rule:</b> ideas can come from AI; <b>which mission, the steps, the must-haves — you write them</b>. The plan is yours, so you understand your own project.</span></div>

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b><span class="zh">五步循环</span><span class="en">The 5-step loop</span></b><code>🗺️ 计划 → ⌨️ 写 → 🧪 测 → 🔧 修 → 🚀 发布</code><span><span class="zh">每圈只做一小步；失败 = 数据</span><span class="en">one small step per lap; failing = data</span></span></div>
  <div class="k"><b><span class="zh">读代码三步</span><span class="en">Read code in 3 steps</span></b><code>① def 函数名  ② while / tick 主循环  ③ 变量</code><span><span class="zh">先看目录，再看它在哪转，再看它记住了什么</span><span class="en">contents, where it spins, what it remembers</span></span></div>
  <div class="k"><b><span class="zh">assert 测试</span><span class="en">assert tests</span></b><code>assert keep_inside(400) == 270, "拉回来"</code><span><span class="zh">不是 True 就立刻报错</span><span class="en">errors at once if not True</span></span></div>
  <div class="k"><b><span class="zh">纯函数</span><span class="en">Pure function</span></b><code>def is_safe_landing(speed, drift):
    return speed &lt;= 2 and drift &lt;= 40</code><span><span class="zh">只吃参数、只吐 return，最好测</span><span class="en">parameters in, return out — easiest to test</span></span></div>
  <div class="k"><b><span class="zh">边界测试</span><span class="en">Edge tests</span></b><code>assert is_safe_landing(2, 40) == True</code><span><span class="zh">刚好在线上的数字，抓 &lt; 和 &lt;= 的 bug</span><span class="en">numbers exactly on the line catch &lt; vs &lt;= bugs</span></span></div>
  <div class="k"><b><span class="zh">测试函数 + TODO</span><span class="en">Test function + TODO</span></b><code>def test():
    assert use_fuel(0) == 0
# TODO: 侧推
test()</code><span><span class="zh">一运行就检查；TODO 标记还没做的步骤</span><span class="en">checked on every run; TODO marks unfinished steps</span></span></div>
  <div class="k"><b><span class="zh">任务计划书</span><span class="en">Mission plan</span></b><code>名字 / 做什么 / 必做 3 / 加分 2 / 小步骤 ≥5 / 要测的纯函数</code><span><span class="zh">小一点，但做完</span><span class="en">small, but finished</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l10">📖 小词典 · 第 10 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l10">📖 cheat sheet · Lesson 10</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/10/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
