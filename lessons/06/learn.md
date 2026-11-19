---
title: 第 6 课 · 学一学
title_en: Lesson 6 · Learn
lesson: "06"
tab: learn
playground: true
---

# 🧠 <span class="zh">第 6 课：while 循环 + 会思考的机器</span><span class="en">Lesson 6: while loops + thinking machines</span>

<p class="zh"><code>for</code> 是「重复 5 次」。但如果不知道要几次呢？「<b>没猜对就一直猜</b>」「<b>没去遍所有行星就一直飞</b>」——这就是今天的 <code>while</code>。学完它，我们就能写一个会「思考」的程序。</p>
<p class="en"><code>for</code> means "repeat 5 times". But what if you don't know how many? "<b>Keep guessing until it's right</b>", "<b>keep flying until you've visited every planet</b>" — that's today's <code>while</code>. Then we'll use it to write a program that "thinks".</p>

---

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">上节课的列表 + <code>in</code> + <code>append</code>：飞船随机飞，去过的行星记在 <code>visited</code> 里。</span><span class="en">Last lesson's lists + <code>in</code> + <code>append</code>: the ship flies at random and remembers planets in <code>visited</code>.</span></p>

<div class="playground" data-src="{{ '/lessons/06/code/warmup.py' | relative_url }}" data-canvas="no" data-title="🔁 行星之旅" data-title-en="🔁 Planet tour" data-save="planet-tour" data-draft="l6-warmup" data-rows="12"></div>

<ul class="quests" data-key="l6-warmup">
  <li>🤔 <span class="zh">先猜：<code>range(3)</code> 的时候，<code>len(visited)</code> 最多是几？可能是 4 吗？</span><span class="en">Guess: with <code>range(3)</code>, what's the most <code>len(visited)</code> can be? Could it be 4?</span></li>
  <li>✍️ <span class="zh">太阳系一共 8 颗行星。把另外 4 颗加进 <code>planets</code>：<code>"Jupiter", "Saturn", "Uranus", "Neptune"</code>。</span><span class="en">Our Solar System has 8 planets. Add the other 4 to <code>planets</code>: <code>"Jupiter", "Saturn", "Uranus", "Neptune"</code>.</span></li>
  <li>🤔 <span class="zh">改成 <code>range(10)</code>，运行几次。10 次一定能去遍 8 颗吗？要循环几次才<b>保证</b>去遍？——说不准！for 循环搞不定这种问题。</span><span class="en">Change to <code>range(10)</code> and run a few times. Are 10 flights always enough for all 8? How many loops would <b>guarantee</b> it? — Nobody knows! A for loop can't handle this.</span></li>
</ul>

---

## ✨ <span class="zh">今天的新魔法 1：while——没到站就继续坐</span><span class="en">New magic 1: while — stay on until your stop</span>
{: #magic}

<p><span class="zh">坐公交车的时候，你不会数「坐 7 站就下车」，你会想「<b>还没到我的站？那就继续坐</b>」。<code>while 条件:</code> 就是这个意思：条件还是 <code>True</code>，就再跑一遍；变成 <code>False</code> 了，就下车。</span><span class="en">On a bus you don't count "get off after 7 stops" — you think "<b>not my stop yet? stay on</b>". <code>while condition:</code> means exactly that: while it's still <code>True</code>, run again; once it's <code>False</code>, get off.</span></p>

<div class="cmds">
  <div class="cmd"><code>while n > 0:</code><span><span class="zh">n 还大于 0，就再跑一遍</span><span class="en">While n is still above 0, run again</span></span></div>
  <div class="cmd"><code>n = n - 1</code><span><span class="zh">让条件有一天变成 False（很重要！）</span><span class="en">Make the condition become False one day (important!)</span></span></div>
  <div class="cmd"><code>count += 1</code><span><span class="zh">和 count = count + 1 一样（<code>-= 1</code> 是减一）</span><span class="en">Same as count = count + 1 (<code>-= 1</code> takes one away)</span></span></div>
  <div class="cmd"><code>while True:</code><span><span class="zh">永远重复……</span><span class="en">Repeat forever…</span></span></div>
  <div class="cmd"><code>break</code><span><span class="zh">……除非用它跳出来</span><span class="en">…unless this jumps out</span></span></div>
</div>

### 🤔 <span class="zh">先猜，再运行</span><span class="en">Guess first, then run</span>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">这段代码一共打印几个数？最后一个是几？（在纸上一圈一圈地跟着 n 走）<pre style="margin:.4em 0">n = 10
while n > 0:
    print(n)
    n = n - 3</pre></span><span class="en">How many numbers does this print, and what's the last one? (Follow n round by round on paper)<pre style="margin:.4em 0">n = 10
while n > 0:
    print(n)
    n = n - 3</pre></span></p>
  <div class="opts"><button><span class="zh">3 个，最后是 4</span><span class="en">3, the last is 4</span></button><button><span class="zh">4 个，最后是 0</span><span class="en">4, the last is 0</span></button><button><span class="zh">4 个，最后是 1</span><span class="en">4, the last is 1</span></button><button><span class="zh">永远停不下来</span><span class="en">It never stops</span></button></div>
  <div class="why"><span class="zh">10 → 7 → 4 → 1 都大于 0，打印 4 个。1 − 3 = −2，<code>-2 &gt; 0</code> 是 False，下车！0 从来没出现过。</span><span class="en">10 → 7 → 4 → 1 are all above 0: 4 numbers printed. 1 − 3 = −2, and <code>-2 &gt; 0</code> is False — off the bus! 0 never appears.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/06/code/countdown.py' | relative_url }}" data-canvas="no" data-title="🚀 倒计时" data-title-en="🚀 Countdown" data-save="countdown" data-rows="8"></div>

### 🔍 <span class="zh">改一改</span><span class="en">Change it</span>

<ul class="quests" data-key="l6-countdown">
  <li><span class="zh">改成 <code>n = n - 3</code>，验证上面的猜一猜。</span><span class="en">Change it to <code>n = n - 3</code> and check the quiz above.</span></li>
  <li>🐞 <span class="zh">把 <code>n = n - 1</code> 那一行<b>删掉</b>，运行。发生什么了？点红色 <b>■ 停下</b>，再把它加回来。</span><span class="en"><b>Delete</b> the <code>n = n - 1</code> line and run it. What happens? Click the red <b>■ Stop</b>, then put it back.</span></li>
  <li>✍️ <span class="zh"><b>自己写</b>一个新的 while：从 1 数到 10（往上数）。开始是几？条件是什么？每次加还是减？</span><span class="en"><b>Write</b> a new while that counts up from 1 to 10. What's the start? The condition? Add or subtract?</span></li>
  <li>✍️ <span class="zh">回到热身：把 <code>for i in range(10):</code> 换成 <code>while len(visited) &lt; 8:</code>，再加一个 <code>flights</code> 计数器——这次一定能去遍 8 颗！一共飞了几次？</span><span class="en">Back to the warm-up: swap <code>for i in range(10):</code> for <code>while len(visited) &lt; 8:</code> and add a <code>flights</code> counter — now it always visits all 8! How many flights did it take?</span></li>
</ul>

<div class="box box-warn"><span class="box-title"><span class="zh">🛑 停不下来的程序</span><span class="en">🛑 The program that never stops</span></span>
<span class="zh">删掉 <code>n = n - 1</code> 以后，n 永远是 10，<code>10 &gt; 0</code> 永远是 True——程序就<b>永远转圈</b>（程序员叫它「死循环」）。每个程序员都写过死循环，不丢人。记住两件事：① 红色 ■ 能救你；② 问自己「<b>什么时候条件会变成 False？</b>」</span>
<span class="en">Without <code>n = n - 1</code>, n stays 10 forever and <code>10 &gt; 0</code> is always True — the program <b>spins forever</b> (programmers call it an "infinite loop"). Every programmer has written one. Remember: ① the red ■ saves you; ② ask yourself "<b>when does the condition become False?</b>"</span>
</div>

### 🧪 <span class="zh">例 2：while True + break——太空日志</span><span class="en">Example 2: while True + break — space log</span>

<p><span class="zh">有时候我们<b>故意</b>写 <code>while True:</code>（永远重复），然后在里面用 <code>if … break</code> 决定什么时候跳出来。比如：不知道你要写几条日志，就一直收，直到你打 <code>end</code>。这个 <code>end</code> 就像一个「停车暗号」。</span><span class="en">Sometimes we write <code>while True:</code> (repeat forever) <b>on purpose</b> and use <code>if … break</code> inside to decide when to jump out. Like this: we don't know how many log entries you'll write, so keep collecting until you type <code>end</code>. That <code>end</code> is a "stop code word".</span></p>

<div class="playground" data-src="{{ '/lessons/06/code/forever.py' | relative_url }}" data-canvas="no" data-title="♾️ 太空日志" data-title-en="♾️ Space log" data-save="space-log" data-draft="l6-log" data-rows="13"></div>

<ul class="quests" data-key="l6-forever">
  <li><span class="zh">写 3 条日志再 <code>end</code>。如果第一下就打 <code>end</code>，会打印什么？</span><span class="en">Write 3 entries, then <code>end</code>. What if you type <code>end</code> straight away?</span></li>
  <li>🐞 <span class="zh">把 <code>break</code> 那一行删掉，运行，打几次 end——停得下来吗？■ 停下，再改回来。</span><span class="en">Delete the <code>break</code> line, run it and type end a few times — does it stop? ■ Stop, then put it back.</span></li>
  <li>✍️ <span class="zh">日志本只有 5 页：再加一个 if，<code>len(log) == 5</code> 的时候打印「📕 本子写满了」并 break。这个 if 放在 <code>append</code> 的前面还是后面？</span><span class="en">The logbook only has 5 pages: add another if — when <code>len(log) == 5</code>, print "📕 logbook full" and break. Does this if go before or after the <code>append</code>?</span></li>
</ul>

---

## ✨ <span class="zh">新魔法 2：True / False 和 and / or / not</span><span class="en">New magic 2: True / False and and / or / not</span>
{: #bool}

<p><span class="zh">每个条件（<code>n &gt; 0</code>、<code>guess == secret</code>）的答案只有两种：<b><code>True</code></b> 或 <b><code>False</code></b>。想把两个条件合起来？用这三个词：</span><span class="en">Every condition (<code>n &gt; 0</code>, <code>guess == secret</code>) has only two answers: <b><code>True</code></b> or <b><code>False</code></b>. Want to combine two conditions? Three words:</span></p>

<div class="table-wrap">
<table>
<tr><th></th><th><span class="zh">意思</span><span class="en">Means</span></th><th><span class="zh">例子</span><span class="en">Example</span></th></tr>
<tr><td><code>and</code></td><td><span class="zh"><b>两个都</b>要 True</span><span class="en"><b>Both</b> must be True</span></td><td><code>password == "kiwi" and age &gt;= 10</code></td></tr>
<tr><td><code>or</code></td><td><span class="zh"><b>只要一个</b> True 就行</span><span class="en"><b>Just one</b> needs to be True</span></td><td><code>age &lt; 6 or age &gt; 99</code></td></tr>
<tr><td><code>not</code></td><td><span class="zh">把 True 变 False，False 变 True</span><span class="en">Flips True and False</span></td><td><code>not age &gt;= 10</code></td></tr>
</table>
</div>


<div class="quiz" data-answer="1">
  <p class="q"><span class="zh"><code>age = 11</code>。<code>age &gt; 10 and age &lt; 20</code> 是？</span><span class="en"><code>age = 11</code>. What is <code>age &gt; 10 and age &lt; 20</code>?</span></p>
  <div class="opts"><button>True</button><button>False</button></div>
  <div class="why"><span class="zh">11 &gt; 10 是 True，11 &lt; 20 也是 True，两个都 True → True。</span><span class="en">11 &gt; 10 is True, 11 &lt; 20 is True, both True → True.</span></div>
</div>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh"><code>wind = 25</code>，<code>rain = True</code>。<code>wind &lt; 30 and not rain</code> 是？</span><span class="en"><code>wind = 25</code>, <code>rain = True</code>. What is <code>wind &lt; 30 and not rain</code>?</span></p>
  <div class="opts"><button>True</button><button>False</button></div>
  <div class="why"><span class="zh">一块一块算：<code>wind &lt; 30</code> → True；<code>not rain</code> → not True → False。True and False → <b>False</b>。（这就是后面火箭能不能发射的规则！）</span><span class="en">Piece by piece: <code>wind &lt; 30</code> → True; <code>not rain</code> → not True → False. True and False → <b>False</b>. (That's the rocket launch rule coming up!)</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/06/code/password.py' | relative_url }}" data-canvas="no" data-title="🔐 秘密基地的门" data-title-en="🔐 Secret base door" data-save="secret-door" data-draft="l6-door" data-rows="12"></div>

<ul class="quests" data-key="l6-door">
  <li><span class="zh">试 4 种情况：密码对+年龄够、密码对+年龄小、密码错、年龄 200。</span><span class="en">Try 4 cases: right password + old enough, right password + too young, wrong password, age 200.</span></li>
  <li><span class="zh">把第一个 <code>and</code> 改成 <code>or</code>。现在密码错也能进了？为什么？</span><span class="en">Change the first <code>and</code> to <code>or</code>. Now a wrong password gets in? Why?</span></li>
  <li>✍️ <span class="zh">在 <code>else</code> 前面再加一个 <code>elif</code>：密码<b>不对</b>（<code>!=</code>）<b>而且</b>年龄小于 6 → 打印「👶 小朋友，去找爸爸妈妈」。</span><span class="en">Add another <code>elif</code> before <code>else</code>: password is <b>wrong</b> (<code>!=</code>) <b>and</b> age is under 6 → print "👶 Little one, go find your parents".</span></li>
</ul>

---

### 🧪 <span class="zh">例 3：猜数字 2.0——两个条件一起管</span><span class="en">Example 3: guess the number 2.0 — two conditions in charge</span>
{: #guess}

<p><span class="zh">第 4 课用 for + break。现在只用一行 while 就说清楚：<code>while guess != secret and tries &lt; 6:</code>——「<b>还没猜对，而且还有机会</b>」就继续。循环停下来以后，谁赢了？那几行<b>你来写</b>。</span><span class="en">Lesson 4 used for + break. Now one while line says it all: <code>while guess != secret and tries &lt; 6:</code> — keep going "<b>while not right yet AND tries left</b>". After the loop stops, who won? <b>You</b> write those lines.</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">秘密数字是 20，你依次输入 10、30、25、20。循环停下来的时候，<code>tries</code> 是几？</span><span class="en">The secret is 20 and you type 10, 30, 25, 20. When the loop stops, what is <code>tries</code>?</span></p>
  <div class="opts"><button>3</button><button>4</button><button>6</button></div>
  <div class="why"><span class="zh">每猜一次 tries 加 1：10 → 1，30 → 2，25 → 3，20 → 4。这时 <code>guess != secret</code> 变成 False，<code>and</code> 整个就是 False，停！</span><span class="en">tries goes up once per guess: 10 → 1, 30 → 2, 25 → 3, 20 → 4. Now <code>guess != secret</code> is False, so the whole <code>and</code> is False — stop!</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/06/code/guess.py' | relative_url }}" data-canvas="no" data-title="🎲 猜数字 2.0" data-title-en="🎲 Guess 2.0" data-save="guess-2" data-draft="l6-guess" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 提示：怎么知道是哪个原因停的？</span><span class="en">💡 Hint: how do you know why it stopped?</span></summary><span class="zh">循环外面（不缩进）再问一次：<code>if guess == secret:</code> → 赢了；<code>else:</code> → 机会用完了。</span><span class="en">Outside the loop (no indent) ask again: <code>if guess == secret:</code> → won; <code>else:</code> → out of tries.</span></details>

<ul class="quests" data-key="l6-guess">
  <li><span class="zh">写好最后的 if / else，玩一局赢的、一局输的（故意乱猜）。</span><span class="en">Write the final if / else, then play one round to win and one to lose (guess badly on purpose).</span></li>
  <li>🐞 <span class="zh">把 <code>and</code> 改成 <code>or</code>，玩到第 7 次。还在问？为什么？（用真值表想一想）</span><span class="en">Change <code>and</code> to <code>or</code> and play past try 6. Still asking? Why? (Think with the truth table)</span></li>
  <li><span class="zh">在最后加一句：如果 <code>tries &lt;= 3</code> <b>而且</b>猜对了，打印「🏆 太神了」。</span><span class="en">At the end add: if <code>tries &lt;= 3</code> <b>and</b> you got it, print "🏆 Genius".</span></li>
</ul>

---

## 🚩 <span class="zh">加餐：旗子变量——等到天气好才发射</span><span class="en">Extra: a flag variable — wait for good weather to launch</span>
{: #flag}

<p><span class="zh">真正的火箭发射也会因为天气推迟。下面的程序用一个<b>旗子变量</b> <code>launched</code>：一开始是 <code>False</code>（旗子放下）；条件都满足时把它变成 <code>True</code>（举旗），<code>while not launched</code> 下一次检查就停了。还有一个秘密：<code>rain = random.randint(1, 4) == 1</code>——比较的结果 True / False 也能放进盒子！（发射规则是我们为游戏编的。）</span><span class="en">Real rocket launches get delayed by weather too. The program below uses a <b>flag variable</b> <code>launched</code>: it starts <code>False</code> (flag down); when every condition is met it becomes <code>True</code> (flag up), and <code>while not launched</code> stops at its next check. Another secret: <code>rain = random.randint(1, 4) == 1</code> — a comparison's True / False can be stored in a box! (The launch rules are made up for our game.)</span></p>

<div class="playground" data-src="{{ '/lessons/06/code/launch.py' | relative_url }}" data-canvas="no" data-title="🚩 等待发射窗口" data-title-en="🚩 Waiting for a launch window" data-save="launch-window" data-draft="l6-launch" data-rows="18"></div>

<ul class="quests" data-key="l6-launch">
  <li><span class="zh">运行 5 次。最快几天？最慢几天？为什么每次不一样？</span><span class="en">Run it 5 times. Fastest? Slowest? Why is it different each time?</span></li>
  <li>✍️ <span class="zh">加一个 <code>scrubs</code> 计数器：每次 NO GO 加 1，最后说「推迟了 ? 次」。</span><span class="en">Add a <code>scrubs</code> counter: +1 on every NO GO, then say "delayed ? times" at the end.</span></li>
  <li>✍️ <span class="zh">加一条规则：温度 <code>temp = random.randint(-5, 30)</code>，低于 0 度也不能发射。（要改哪一行的条件？）</span><span class="en">Add a rule: temperature <code>temp = random.randint(-5, 30)</code> — below 0 means no launch either. (Which condition changes?)</span></li>
  <li>🌟 <span class="zh">任务最多等 10 天：把条件改成 <code>while not launched and day &lt; 10:</code>，循环后用 <code>if launched:</code> 说「发射成功」还是「任务取消」。</span><span class="en">The mission waits 10 days at most: change it to <code>while not launched and day &lt; 10:</code>, then after the loop use <code>if launched:</code> to say "launched" or "mission cancelled".</span></li>
</ul>

---

## 🕵️ <span class="zh">会思考的机器：先不插电</span><span class="en">Thinking machines: unplugged first</span>
{: #rules}

<div class="box box-think"><span class="box-title"><span class="zh">✂️ 不插电活动（5 分钟，和老师一起）</span><span class="en">✂️ Unplugged (5 min, with your teacher)</span></span>
<span class="zh">桌上有 10 张动物卡：猫、狗、tūī、kiwi、鲨鱼、金鱼、马、企鹅、蝙蝠、海龟。<br>① 你是「AI」，<b>写 3 条规则</b>把它们分成「鸟 / 不是鸟」，比如「会飞 → 鸟」。<br>② 老师拿一张卡，你<b>只能按规则</b>回答。<br>③ 现在试试<b>企鹅</b>（鸟，但不会飞）和<b>蝙蝠</b>（会飞，但不是鸟）。规则出错了吗？改规则！<br>👉 这就是今天要写的程序：<b>只知道我们写进去的规则</b>。</span>
<span class="en">10 animal cards on the table: cat, dog, tūī, kiwi, shark, goldfish, horse, penguin, bat, turtle.<br>① You are the "AI". <b>Write 3 rules</b> to sort them into "bird / not bird", e.g. "can fly → bird".<br>② The teacher holds up a card; you may <b>only answer by the rules</b>.<br>③ Now try the <b>penguin</b> (a bird that can't fly) and the <b>bat</b> (flies but isn't a bird). Did the rules fail? Fix them!<br>👉 That's the program we write next: it <b>only knows the rules we put in</b>.</span>
</div>

### 🧪 <span class="zh">例 4：动物猜猜猜（规则版 AI）</span><span class="en">Example 4: animal guesser (rule-based AI)</span>

<p><span class="zh">程序问 3 个 yes / no 问题，然后用 <code>if / elif</code> + <code>and</code> 按规则猜。外面套一个 <code>while again == "yes":</code>，想玩几次玩几次。蝙蝠的规则还没有——<b>你来写</b>（2 行，写在 ✍️ 那里）。</span><span class="en">The program asks 3 yes / no questions, then guesses by rules with <code>if / elif</code> + <code>and</code>. It's wrapped in <code>while again == "yes":</code> so you can play as often as you like. The bat rule is missing — <b>you write it</b> (2 lines, at the ✍️).</span></p>

<p class="muted"><span class="zh">⌨️ 回答只打 <b>yes</b> 或 <b>no</b>（英文、小写）。打「有」「是」或者 Yes，程序都听不懂——第 8 课会教怎么让它听懂大写。</span><span class="en">⌨️ Answer only <b>yes</b> or <b>no</b> (English, lowercase). "Yes" with a capital won't be understood — Lesson 8 shows how to fix that.</span></p>

<div class="playground" data-src="{{ '/lessons/06/code/animal.py' | relative_url }}" data-canvas="no" data-title="🕵️ 动物猜猜猜" data-title-en="🕵️ Animal guesser" data-save="animal-guesser" data-draft="l6-animal" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 蝙蝠规则提示</span><span class="en">💡 Bat rule hint</span></summary><span class="zh">蝙蝠有毛、会飞。照着猫那条写：<code>elif fur == "yes" and fly == ...:</code>，下一行打印 🦇。注意 <code>elif</code> 要和上面的 <code>elif</code> 对齐。</span><span class="en">A bat has fur and can fly. Copy the cat rule's shape: <code>elif fur == "yes" and fly == ...:</code>, then print 🦇 on the next line. Line <code>elif</code> up with the one above.</span></details>

<ul class="quests" data-key="l6-animal">
  <li><span class="zh">想一只<b>狗</b>，回答问题。它猜对了吗？为什么猜成猫？（规则里猫和狗一样！）</span><span class="en">Think of a <b>dog</b> and answer. Did it guess right? Why did it say cat? (In the rules, cat and dog look the same!)</span></li>
  <li>✍️ <span class="zh">加第 4 个问题 <code>bark = input("它会汪汪叫吗？")</code>，再加一条规则认出狗。这条规则要放在猫的<b>前面</b>还是后面？</span><span class="en">Add a 4th question <code>bark = input("Does it bark?")</code> and a rule that recognises a dog. Does it go <b>before</b> or after the cat rule?</span></li>
  <li><span class="zh">想一只<b>企鹅</b>。程序怎么说？它需要什么新问题、什么新规则？</span><span class="en">Think of a <b>penguin</b>. What does the program say? What new question and rule does it need?</span></li>
</ul>

<div class="box box-rule"><span class="box-title"><span class="zh">🤔 发现了吗？</span><span class="en">🤔 Did you notice?</span></span>
<span class="zh">每多一种动物，就要<b>我们</b>多写一条规则。世界上有几百万种动物……写不完！那真正的 AI 是怎么认出照片里的猫的？——<b>它不靠人写规则，它看几百万张例子，自己找规律。</b>下面我们就训练一个。</span>
<span class="en">Every new animal needs <b>us</b> to write another rule. There are millions of animals… we'd never finish! So how does real AI recognise a cat in a photo? — <b>Nobody writes the rules. It looks at millions of examples and finds the patterns itself.</b> Let's train one.</span>
</div>

---

## 📸 <span class="zh">训练一个真正会学习的 AI</span><span class="en">Train an AI that really learns</span>
{: #tm}

<p><span class="zh">打开 <a href="https://teachablemachine.withgoogle.com/train/image" target="_blank" rel="noopener">Teachable Machine</a>（需要摄像头，和老师一起）。这次我们<b>不写任何规则</b>，只给它<b>例子</b>。<br>📷 没有摄像头或者摄像头被禁用？点 <b>Upload</b> 上传照片也可以。🔒 拍手、玩具、文具，<b>不拍脸</b>；不要点「保存到 Google Drive」。</span><span class="en">Open <a href="https://teachablemachine.withgoogle.com/train/image" target="_blank" rel="noopener">Teachable Machine</a> (needs a camera; do it with your teacher). This time we write <b>no rules at all</b> — we only give it <b>examples</b>.<br>📷 No camera, or it's blocked? Click <b>Upload</b> and use photos instead. 🔒 Photograph hands, toys or pencils — <b>not faces</b> — and don't save to Google Drive.</span></p>

<ol class="steps">
  <li><strong><span class="zh">好好教它</span><span class="en">Teach it well</span></strong><br><span class="zh">两个类别：「✊ 拳头」和「✋ 手掌」。每个用摄像头拍 <b>20 张以上</b>，角度、远近都换一换。点 <b>Train Model</b>，然后测试：它认得出来吗？</span><span class="en">Two classes: "✊ fist" and "✋ open hand". Take <b>20+ photos</b> of each with the webcam, changing angle and distance. Click <b>Train Model</b> and test it. Does it get it right?</span></li>
  <li><strong><span class="zh">故意教坏它</span><span class="en">Teach it badly on purpose</span></strong><br><span class="zh">新建一个项目。这次「拳头」只拍 <b>3 张</b>，而且全部在画面的<b>左上角</b>；「手掌」拍 20 张在中间。再训练、再测试：把拳头放在中间，它说什么？</span><span class="en">Start a new project. This time take only <b>3 photos</b> of "fist", all in the <b>top-left corner</b>; take 20 of "hand" in the middle. Train and test again: hold a fist in the middle — what does it say?</span></li>
  <li><strong><span class="zh">想一想</span><span class="en">Think</span></strong><br><span class="zh">第二个模型为什么学坏了？它学到的「规律」可能是「左上角 = 拳头」！<b>例子少、例子偏，AI 就学歪。</b>这叫<b>数据偏见</b>。如果一个认人脸的 AI 只用一种人的照片训练，会怎样？</span><span class="en">Why did the second model learn badly? Its "pattern" might be "top-left corner = fist"! <b>Few or lopsided examples make a lopsided AI.</b> That's called <b>data bias</b>. What if a face-recognising AI was trained on photos of only one kind of person?</span></li>
</ol>

<div class="two">
  <div class="card"><b>🕵️ <span class="zh">规则版（我们写的）</span><span class="en">Rules (we wrote them)</span></b><ul><li><span class="zh">人写规则</span><span class="en">People write the rules</span></li><li><span class="zh">每种新东西都要加规则</span><span class="en">Every new thing needs a new rule</span></li><li><span class="zh">可以看懂它为什么这么猜</span><span class="en">You can see why it guessed</span></li></ul></div>
  <div class="card"><b>📸 <span class="zh">学习版（Teachable Machine）</span><span class="en">Learning (Teachable Machine)</span></b><ul><li><span class="zh">给例子，它自己找规律</span><span class="en">Give examples, it finds patterns</span></li><li><span class="zh">例子越多越好、越全越好</span><span class="en">More and more varied examples = better</span></li><li><span class="zh">很难知道它到底学了什么</span><span class="en">Hard to know what it really learned</span></li></ul></div>
</div>

---

## 🧪 <span class="zh">例 5（选做）：海龟一直画到边上</span><span class="en">Example 5 (optional): the turtle draws until the edge</span>
{: #spiral}

<p><span class="zh"><code>while</code> 不只会数数。<code>t.distance(0, 0)</code> 是海龟离中间多远——「离中间还不到 250，就继续画」。</span><span class="en"><code>while</code> isn't just for counting. <code>t.distance(0, 0)</code> is how far the turtle is from the middle — "while less than 250 away, keep drawing".</span></p>

<div class="playground" data-src="{{ '/lessons/06/code/spiral.py' | relative_url }}" data-title="🌀 画到边上" data-title-en="🌀 Until the edge" data-save="edge-spiral" data-draft="l6-spiral"></div>

<ul class="quests" data-key="l6-spiral">
  <li><span class="zh">把 250 改成 100，再改成 290。</span><span class="en">Change 250 to 100, then 290.</span></li>
  <li><span class="zh">把 <code>t.left(30)</code> 改成 <code>t.left(91)</code>。</span><span class="en">Change <code>t.left(30)</code> to <code>t.left(91)</code>.</span></li>
  <li><span class="zh">用上节课的颜色列表，让每一步换颜色（提示：加一个 <code>i</code> 计数器，<code>colours[i % 6]</code>）。</span><span class="en">Use last lesson's colour list to change colour each step (hint: add an <code>i</code> counter and <code>colours[i % 6]</code>).</span></li>
</ul>

---

## 🏆 <span class="zh">挑战：太空知识闯关（3 条命）</span><span class="en">Challenge: space quiz with 3 lives</span>
{: #challenge}

<p><span class="zh">把今天学的全用上：<code>while</code> + <code>and</code> + 两个计数器 + 第 5 课的配对列表。题目和答案已经准备好了，<b>游戏你来设计</b>。做好了让家人玩，存到作品墙！</span><span class="en">Use everything from today: <code>while</code> + <code>and</code> + two counters + lesson 5's paired lists. The questions and answers are ready — <b>you design the game</b>. Let your family play, then save it to the Gallery!</span></p>

<div class="playground" data-src="{{ '/lessons/06/code/challenge.py' | relative_url }}" data-canvas="no" data-title="🏆 太空知识闯关" data-title-en="🏆 Space quiz" data-save="space-quiz" data-draft="l6-challenge" data-rows="20"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：while 那一行</span><span class="en">💡 Hint 1: the while line</span></summary><span class="zh"><code>while lives &gt; 0 and score &lt; 5:</code>——两个条件都要 True 才继续。</span><span class="en"><code>while lives &gt; 0 and score &lt; 5:</code> — keep going only while both are True.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：不重复</span><span class="en">💡 Hint 2: no repeats</span></summary><span class="zh">问之前先 <code>q = questions.pop(i)</code> 和 <code>a = answers.pop(i)</code>。但题目会被问完！所以 while 还要加一个条件：<code>len(questions) &gt; 0</code>。</span><span class="en">Before asking, <code>q = questions.pop(i)</code> and <code>a = answers.pop(i)</code>. But the questions can run out! So the while needs another condition: <code>len(questions) &gt; 0</code>.</span></details>

---

## 🤖 <span class="zh">和 AI 一起：问问它自己</span><span class="en">With AI: ask it about itself</span>

<div class="chat">
  <div class="bubble me"><span class="zh">你是「人写的规则」做出来的，还是「从很多例子学」出来的？用小学生能懂的话解释，不超过 5 句。</span><span class="en">Were you made from "rules people wrote" or by "learning from lots of examples"? Explain for a Year 6 student in 5 sentences or fewer.</span></div>
  <div class="bubble ai"><span class="zh">（看看它怎么说！）</span><span class="en">(See what it says!)</span></div>
</div>

<ul class="quests" data-key="l6-ai">
  <li><span class="zh">问完以后想：它的回答和今天学的一样吗？有没有哪句你<b>没法检验</b>？</span><span class="en">After asking, think: does its answer match today's lesson? Is there a sentence you <b>can't check</b>?</span></li>
  <li><span class="zh">再问：「你会不会因为例子不好而学歪？举一个例子。」</span><span class="en">Ask: "Can you learn wrongly because of bad examples? Give one example."</span></li>
</ul>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>while</b><code>while n > 0:
    print(n)
    n -= 1</code><span><span class="zh">条件是 True 就一直重复；里面要有东西让它变 False</span><span class="en">Repeats while True; something inside must make it False</span></span></div>
  <div class="k"><b>while True + break</b><code>while True:
    x = input("?")
    if x == "end":
        break</code><span><span class="zh">永远重复，直到「停车暗号」</span><span class="en">Forever, until the stop code word</span></span></div>
  <div class="k"><b><span class="zh">计数器</span><span class="en">Counter</span></b><code>tries = 0
tries += 1</code><span><span class="zh">+= 1 就是加一</span><span class="en">+= 1 adds one</span></span></div>
  <div class="k"><b>and / or / not</b><code>a and b   # 两个都 / both
a or b    # 一个就行 / either
not a     # 反过来 / flip</code><span><span class="zh">答案只有 True 或 False</span><span class="en">Always True or False</span></span></div>
  <div class="k"><b><span class="zh">两个条件管 while</span><span class="en">Two conditions in a while</span></b><code>while guess != secret and tries < 6:</code><span><span class="zh">停下来以后，用 if 查是哪个原因</span><span class="en">After it stops, use if to see why</span></span></div>
  <div class="k"><b><span class="zh">旗子变量</span><span class="en">Flag variable</span></b><code>launched = False
while not launched:
    ...
    launched = True</code><span><span class="zh">放下旗子开始，举起旗子结束</span><span class="en">Start with the flag down, raise it to finish</span></span></div>
  <div class="k"><b><span class="zh">规则 vs 学习</span><span class="en">Rules vs learning</span></b><code>if fur == "yes" and ...:   # 规则 / rule</code><span><span class="zh">我们写规则 ≠ AI 从例子学。例子不好，AI 学歪。</span><span class="en">Rules we write ≠ AI learning from examples. Bad examples, bad AI.</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l06">📖 小词典 · 第 6 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l06">📖 cheat sheet · Lesson 6</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/06/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
