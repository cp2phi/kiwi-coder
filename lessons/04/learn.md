---
title: 第 4 课 · 学一学
title_en: Lesson 4 · Learn
lesson: "04"
tab: learn
playground: true
---

# 🎲 <span class="zh">if / else：让程序自己做决定</span><span class="en">if / else: programs that decide</span>

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">上周的 for 循环 + 第 2 课的 f-string。<b>先猜再运行</b>：<code>range(10, 0, -3)</code> 会数出哪几个数？</span><span class="en">Last week's for loop + lesson 2's f-strings. <b>Guess before you run</b>: which numbers does <code>range(10, 0, -3)</code> count?</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/warmup.py' | relative_url }}" data-title="🔁 热身" data-title-en="🔁 Warm-up" data-save="warmup-4" data-rows="8"></div>

<ul class="quests" data-key="l4-warmup">
  <li>🤔 <span class="zh">先在纸上写出 <code>range(10, 0, -3)</code> 的数，再运行对答案。</span><span class="en">Write down the numbers of <code>range(10, 0, -3)</code> on paper first, then run to check.</span></li>
  <li>✍️ <span class="zh"><b>自己写 2 行</b>：一个新的 for 循环，打印「第 1 级 / Stage 1」到「第 3 级 / Stage 3」。（提示：<code>i</code> 从 0 开始，所以要用 <code>i + 1</code>）</span><span class="en"><b>Write 2 lines yourself</b>: a new for loop that prints "Stage 1" to "Stage 3". (Hint: <code>i</code> starts at 0, so use <code>i + 1</code>)</span></li>
  <li><span class="zh">螺旋的 <code>91</code> 改成 <code>120</code>。</span><span class="en">Change the spiral's <code>91</code> to <code>120</code>.</span></li>
</ul>

---

## ✨ <span class="zh">今天的新魔法：if</span><span class="en">Today's new magic: if</span>
{: #magic}

<p class="zh">早上出门前你会想：「<b>如果</b>下雨，<b>就</b>带伞；<b>不然</b>就不带。」程序也能这样想！到现在为止，我们的程序每次都做一模一样的事。从今天起，它会<b>看情况决定</b>。</p>
<p class="en">Before leaving in the morning you think: "<b>If</b> it's raining, <b>then</b> take an umbrella; <b>otherwise</b> don't." Programs can think like that too! Until now our programs did the same thing every time. From today they <b>decide depending on the situation</b>.</p>

<div class="cmds">
  <div class="cmd"><code>if guess == secret:</code><span><span class="zh">如果……（最后有冒号，下面要缩进）</span><span class="en">If… (colon at the end, indent below)</span></span></div>
  <div class="cmd"><code>else:</code><span><span class="zh">不然……</span><span class="en">Otherwise…</span></span></div>
  <div class="cmd"><code>elif guess > secret:</code><span><span class="zh">不然如果……（可以有好几个）</span><span class="en">Otherwise if… (you can have several)</span></span></div>
  <div class="cmd"><code>==</code><span><span class="zh">「等于吗？」要<b>两个</b>等号！</span><span class="en">"Is it equal?" needs <b>two</b> equals signs!</span></span></div>
</div>

<div class="box box-warn"><span class="zh">⚠️ 今天最大的陷阱：<code>x = 5</code> 是「把 5 放进盒子 x」；<code>x == 5</code> 是「x 等于 5 吗？」。一个等号是动作，两个等号是问题。</span><span class="en">⚠️ Today's biggest trap: <code>x = 5</code> means "put 5 in box x"; <code>x == 5</code> means "is x equal to 5?". One = is an action, two == is a question.</span></div>

### 🤔 <span class="zh">先猜，再运行</span><span class="en">Guess first, then run</span>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">下面的代码，秘密数字是 7。如果你输入 7，<code>print</code> 会打印出几行字？（不算你输入的那一行）</span><span class="en">In the code below the secret is 7. If you type 7, how many lines does <code>print</code> show? (not counting the line you typed)</span></p>
  <div class="opts"><button><span class="zh">1 行：🎉 猜对了</span><span class="en">1 line: 🎉</span></button><button><span class="zh">3 行：🎉、❌、游戏结束</span><span class="en">3 lines: 🎉, ❌, game over</span></button><button><span class="zh">2 行：🎉 和 游戏结束</span><span class="en">2 lines: 🎉 and game over</span></button></div>
  <div class="why"><span class="zh">2 行！<code>if</code> 和 <code>else</code> 只会跑<b>其中一个</b>；最后那行 <code>print("游戏结束")</code> 没有缩进，不属于 if，所以总是会跑。</span><span class="en">2 lines! Only <b>one</b> of <code>if</code> / <code>else</code> runs; the last <code>print("游戏结束")</code> isn't indented, so it's not part of the if and always runs.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/04/code/if-first.py' | relative_url }}" data-canvas="no" data-title="🎲 例 1：第一个决定" data-title-en="🎲 Example 1: first decision" data-save="first-if" data-rows="9"></div>

<p class="muted"><span class="zh">（运行后，在黑色框下面的输入框里打数字，按回车。）</span><span class="en">(After Run, type a number in the box under the black area and press Enter.)</span></p>

### 🔍 <span class="zh">改一改</span><span class="en">Change it</span>

<ul class="quests" data-key="l4-modify">
  <li><span class="zh">输入 3，再输入 7，看看哪一行出现、哪一行没出现。</span><span class="en">Type 3, then 7. Which line shows up, which doesn't?</span></li>
  <li>✍️ <span class="zh">把 <code>else:</code> 拆成两段：<code>elif guess &gt; secret:</code> 打印「太大了」，<code>else:</code> 打印「太小了」。<b>自己打</b>，不复制。</span><span class="en">Split <code>else:</code> into two: <code>elif guess &gt; secret:</code> prints "too big", <code>else:</code> prints "too small". <b>Type it yourself</b>, no copying.</span></li>
  <li>✍️ <span class="zh">在最上面加一个<b>单独的</b> if：如果 <code>guess &gt; 10</code>，打印「⚠️ 超出范围」。输入 50 试试——会打印几行？</span><span class="en">Add a <b>separate</b> if near the top: if <code>guess &gt; 10</code>, print "⚠️ out of range". Try 50 — how many lines print?</span></li>
  <li>🐞 <span class="zh">故意把 <code>==</code> 改成 <code>=</code>，运行，读报错，改回来。</span><span class="en">Change <code>==</code> to <code>=</code> on purpose, run, read the error, change it back.</span></li>
</ul>

---

### 🧪 <span class="zh">例 2：电子骰子（随机数 + elif）</span><span class="en">Example 2: electronic dice (random + elif)</span>

<p><span class="zh">游戏要好玩，电脑得会<b>随机</b>。<code>random.randint(1, 6)</code> 就像掷一个骰子。然后用 <code>if / elif / else</code> 给不同的点数不同的反应。</span><span class="en">For a game to be fun, the computer needs <b>randomness</b>. <code>random.randint(1, 6)</code> is like rolling a die. Then <code>if / elif / else</code> reacts differently to each roll.</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/dice.py' | relative_url }}" data-canvas="no" data-title="🎲 例 2：电子骰子" data-title-en="🎲 Example 2: dice" data-save="dice" data-rows="9"></div>

<ul class="quests" data-key="l4-dice">
  <li><span class="zh">运行 5 次，每次一样吗？</span><span class="en">Run it 5 times. Same every time?</span></li>
  <li><span class="zh">在 <code>elif dice &gt;= 4:</code> <b>下面</b>再加一个 <code>elif dice &gt;= 5:</code> 打印「🤩 很好」。掷很多次，它出现过吗？为什么？把它挪到 <code>&gt;= 4</code> <b>上面</b>再试。</span><span class="en">Add <code>elif dice &gt;= 5:</code> printing "🤩 great" <b>below</b> <code>elif dice &gt;= 4:</code>. Roll lots of times — does it ever show? Why? Move it <b>above</b> <code>&gt;= 4</code> and try again.</span></li>
  <li>✍️ <span class="zh">用第 3 课的 for 把它包起来，一次掷 10 个骰子。（哪几行要缩进？）</span><span class="en">Wrap it in a lesson-3 for loop to roll 10 dice at once. (Which lines need indenting?)</span></li>
</ul>

<div class="box box-tip"><span class="zh">🧭 <b>elif 的规矩：</b>从上往下检查，<b>第一个成立的才跑</b>，后面的就不看了。所以「更严格」的条件要放在上面。</span><span class="en">🧭 <b>The elif rule:</b> checked top to bottom, <b>only the first true one runs</b>, the rest are skipped. So the "stricter" condition goes on top.</span></div>

---

### 🧪 <span class="zh">加餐：% 余数——每 3 个一次</span><span class="en">Extra: % remainder — once every 3</span>
{: #mod}

<p><span class="zh">第 3 课的彩虹螺旋里见过 <code>%</code>。它是「<b>除完以后剩几</b>」：<code>7 % 3</code> 是 1，<code>9 % 3</code> 是 0。<b>余数是 0 = 刚好整除</b>，所以 <code>i % 3 == 0</code> 就是「i 是 3 的倍数吗？」，<code>i % 2 == 0</code> 就是「i 是双数吗？」。</span><span class="en">You met <code>%</code> in lesson 3's rainbow spiral. It means "<b>what's left after dividing</b>": <code>7 % 3</code> is 1, <code>9 % 3</code> is 0. <b>Remainder 0 = divides exactly</b>, so <code>i % 3 == 0</code> asks "is i a multiple of 3?" and <code>i % 2 == 0</code> asks "is i even?".</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的「太空报数」跑到 <code>i = 10</code> 的时候，会打印什么？</span><span class="en">In the "Space Fizz" below, what is printed when <code>i = 10</code>?</span></p>
  <div class="opts"><button>10</button><button>10 ⭐</button><button>10 🚀</button></div>
  <div class="why"><span class="zh">10 % 15 是 10（不是 0），10 % 3 是 1（不是 0），10 % 5 是 0 ✅ → 打印 <code>10 ⭐</code>。</span><span class="en">10 % 15 is 10 (not 0), 10 % 3 is 1 (not 0), 10 % 5 is 0 ✅ → prints <code>10 ⭐</code>.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/04/code/space-fizz.py' | relative_url }}" data-canvas="no" data-title="🚀 太空报数" data-title-en="🚀 Space Fizz" data-save="space-fizz" data-draft="l4-fizz" data-rows="12"></div>

<ul class="quests" data-key="l4-fizz">
  <li>🐞 <span class="zh">把 <code>if i % 15 == 0:</code> 那两行挪到<b>最下面</b>（<code>else</code> 前面，改成 <code>elif</code>；原来的第一个 <code>elif</code> 要变成 <code>if</code>）。15 现在打印什么？为什么？再挪回来。</span><span class="en">Move the <code>if i % 15 == 0:</code> pair to the <b>bottom</b> (just before <code>else</code>, as an <code>elif</code>; the old first <code>elif</code> becomes <code>if</code>). What does 15 print now? Why? Move it back.</span></li>
  <li>✍️ <span class="zh"><b>自己写 4 行</b>：一个新循环，1 到 10，双数打印「🌍 双数」，单数打印「🌙 单数」。</span><span class="en"><b>Write 4 lines yourself</b>: a new loop from 1 to 10 printing "🌍 even" for even numbers and "🌙 odd" for odd ones.</span></li>
  <li>🌟 <span class="zh"><b>if 里面套 if</b>：不用 <code>% 15</code>，改成在 <code>i % 3 == 0</code> 里面<b>再问</b>一次 <code>if i % 5 == 0:</code>。结果一样吗？</span><span class="en"><b>An if inside an if</b>: drop <code>% 15</code>, and inside <code>i % 3 == 0</code> ask <b>again</b> with <code>if i % 5 == 0:</code>. Same result?</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 if 套 if 提示</span><span class="en">💡 Nested if hint</span></summary><span class="zh">里面的 if 要再缩进 4 格（一共 8 格）：<pre>    if i % 3 == 0:
        if i % 5 == 0:
            print(f"{i} 🚀⭐")
        else:
            print(f"{i} 🚀")
    elif i % 5 == 0:
        ...</pre></span><span class="en">The inner if is indented 4 more spaces (8 in total):<pre>    if i % 3 == 0:
        if i % 5 == 0:
            print(f"{i} 🚀⭐")
        else:
            print(f"{i} 🚀")
    elif i % 5 == 0:
        ...</pre></span></details>

---

### 🧪 <span class="zh">例 3：完整的猜数字游戏——判断的部分你来写</span><span class="en">Example 3: the whole guessing game — you write the deciding part</span>
{: #guess}

<p><span class="zh">把例 1 和例 2 合起来：电脑<b>随机</b>出题（1–20），你有 <b>5 次</b>机会（for 循环！）。这次判断「猜对 / 太大 / 太小」的 7 行，<b>你自己写</b>。猜对了就 <code>break</code>——跳出循环，不用再猜。</span><span class="en">Example 1 + Example 2 together: the computer picks a <b>random</b> number (1–20), you get <b>5 tries</b> (a for loop!). This time <b>you write</b> the 7 lines that decide "right / too big / too small". A correct guess hits <code>break</code> — leave the loop, no more guessing.</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">秘密数字是 7，你<b>依次</b>准备输入 3、9、7、2。写好的程序（有 break）一共会问你几次？</span><span class="en">The secret is 7 and you plan to type 3, 9, 7, 2 <b>in that order</b>. How many times will the finished program (with break) ask you?</span></p>
  <div class="opts"><button>2</button><button>3</button><button>4</button><button>5</button></div>
  <div class="why"><span class="zh">第 1 次 3 → 太小；第 2 次 9 → 太大；第 3 次 7 → 🎉 然后 <code>break</code>！循环马上停，2 根本没机会输入。没有 break 的话，它会一直问到 5 次。</span><span class="en">Try 1: 3 → too small; try 2: 9 → too big; try 3: 7 → 🎉 then <code>break</code>! The loop stops at once, so 2 is never typed. Without break it would keep asking until 5 tries.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/04/code/guess.py' | relative_url }}" data-canvas="no" data-title="🎯 例 3：猜数字游戏" data-title-en="🎯 Example 3: guessing game" data-save="guess-game" data-draft="l4-guess" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：长什么样</span><span class="en">💡 Hint 1: the shape</span></summary><span class="zh">一个 <code>if</code>、一个 <code>elif</code>、一个 <code>else</code>，每个下面一行 <code>print</code>；<code>break</code> 放在 <b>if 里面</b>、print 的下一行。它们都要和 <code>guess = …</code> 对齐（缩进 4 格），下面的行再缩进 4 格。</span><span class="en">One <code>if</code>, one <code>elif</code>, one <code>else</code>, each with a <code>print</code> under it; <code>break</code> goes <b>inside the if</b>, after its print. They line up with <code>guess = …</code> (4 spaces), and the lines under them get 4 more.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：前两行</span><span class="en">💡 Hint 2: the first two lines</span></summary><pre>    if guess == secret:
        print("🎉 猜对了！You got it!")</pre><span class="zh">剩下的照着这个样子写。</span><span class="en">Write the rest in the same pattern.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：差点忘了 break</span><span class="en">💡 Hint 3: don't forget break</span></summary><span class="zh">猜对了还一直问？<code>break</code> 是不是忘了，或者缩进不在 if 里面？</span><span class="en">Still asking after a correct guess? Did you forget <code>break</code>, or is it not indented inside the if?</span></details>

<ul class="quests" data-key="l4-guess">
  <li><span class="zh">写好 7 行，玩一局。再让老师玩一局，你来指：代码现在跑到哪一行？</span><span class="en">Write the 7 lines and play. Then let your teacher play while you point: which line is running now?</span></li>
  <li>✍️ <span class="zh">猜错的时候加一句「还剩 ? 次」。（提示：<code>tries</code> 是 0、1、2、3、4，剩下的是 <code>4 - tries</code>）</span><span class="en">On a wrong guess, add "? tries left". (Hint: <code>tries</code> goes 0–4, so what's left is <code>4 - tries</code>)</span></li>
  <li>🌟 <span class="zh"><b>if 套 if</b>：太大的时候，如果 <code>guess - secret &lt;= 2</code>，再加一句「🔥 但是很接近！」。太小的时候呢？（<code>secret - guess</code>）</span><span class="en"><b>if inside if</b>: when too big, if <code>guess - secret &lt;= 2</code>, also say "🔥 but very close!". And when too small? (<code>secret - guess</code>)</span></li>
  <li><span class="zh">改成 1 到 100，7 次机会。还够猜吗？（聪明的猜法：每次猜中间！）</span><span class="en">Change to 1–100 with 7 tries. Still enough? (Smart strategy: always guess the middle!)</span></li>
</ul>

---

### 🧪 <span class="zh">例 4：卫星随机散步（if 遇上 for 和 %）</span><span class="en">Example 4: satellite random walk (if meets for and %)</span>

<p><span class="zh">每走一步掷一次硬币决定往哪转；<code>i % 2</code> 换颜色；<code>i % 10 == 0</code> 每 10 步留下一颗星。每次运行都不一样！</span><span class="en">Every step flips a coin to decide which way to turn; <code>i % 2</code> swaps colours; <code>i % 10 == 0</code> leaves a star every 10 steps. Different every run!</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/random-walk.py' | relative_url }}" data-title="🛰️ 例 4：卫星散步" data-title-en="🛰️ Example 4: satellite walk" data-save="random-walk" data-draft="l4-walk"></div>

<ul class="quests" data-key="l4-walk">
  <li><span class="zh">把 <code>range(80)</code> 改成 <code>range(300)</code>，星星改成每 25 步一颗。</span><span class="en">Change <code>range(80)</code> to <code>range(300)</code> and drop a star every 25 steps.</span></li>
  <li>✍️ <span class="zh">把转弯改成 <code>randint(1, 3)</code>：1 左转、2 右转、3 直走（用 <code>elif</code>）。</span><span class="en">Make turning <code>randint(1, 3)</code>: 1 left, 2 right, 3 straight (use <code>elif</code>).</span></li>
  <li>🌟 <span class="zh">if 套 if：到了放星星的步数，<b>再</b>掷一次硬币：1 → 白色大星，2 → 红色小星。</span><span class="en">if inside if: on a star step, flip <b>another</b> coin: 1 → big white star, 2 → small red star.</span></li>
</ul>

---

## 🛟 <span class="zh">卡住了怎么办？四步法</span><span class="en">Stuck? The 4 steps</span>
{: #stuck}

<p><span class="zh">从今天起，每次卡住都走这 4 步。<b>前 3 步自己来</b>，第 4 步才问老师——这样你会越来越厉害。</span><span class="en">From today, every time you're stuck, take these 4 steps. <b>Do the first 3 yourself</b>; the teacher is step 4 — that's how you get stronger.</span></p>

<div class="flow">
  <div class="f"><span class="e">1️⃣</span><b><span class="zh">读报错</span><span class="en">Read the error</span></b><small><span class="zh">哪一行？说了什么？</span><span class="en">Which line? What does it say?</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">2️⃣</span><b><span class="zh">翻笔记本</span><span class="en">Check your notebook</span></b><small><span class="zh">以前遇到过吗？</span><span class="en">Seen it before?</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">3️⃣</span><b><span class="zh">问 AI 要提示</span><span class="en">Ask AI for a hint</span></b><small><span class="zh">报错框里有「复制」按钮</span><span class="en">The error box has a copy button</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">4️⃣</span><b><span class="zh">问老师</span><span class="en">Ask your teacher</span></b><small><span class="zh">前三步都试过了</span><span class="en">After trying all three</span></small></div>
</div>

<p class="muted"><span class="zh">完整的守则和问 AI 的模板在 <a href="{{ '/ai-rules/' | relative_url }}">🤖 AI 伙伴守则</a>。</span><span class="en">The full rules and AI templates are in <a href="{{ '/ai-rules/' | relative_url }}">🤖 AI Buddy Rules</a>.</span></p>

### 🐞 <span class="zh">找 bug 游戏：治好 4 个病号</span><span class="en">Bug hunt: cure 4 patients</span>

<p><span class="zh">下面 4 个程序都「生病」了。先运行，<b>读红框</b>（第 1 步！），再修好。修好了会有 🏆。<b>病号 4 最狡猾</b>：它没有红框，只是答案不对。</span><span class="en">These 4 programs are "sick". Run each one, <b>read the red box</b> (step 1!), then fix it. A fixed patient earns a 🏆. <b>Patient 4 is the sneakiest</b>: no red box, just a wrong answer.</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/bug1.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 1" data-title-en="🐞 Patient 1" data-save="bug-1" data-draft="l4-bug1" data-expect="嗨\n嗨\n嗨" data-rows="5" data-badge="lesson4-bug1"></div>
<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh"><code>for</code> 那一行的最后少了什么符号？</span><span class="en">What symbol is missing at the end of the <code>for</code> line?</span></details>

<div class="playground" data-src="{{ '/lessons/04/code/bug2.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 2" data-title-en="🐞 Patient 2" data-save="bug-2" data-draft="l4-bug2" data-expect="正确" data-rows="5" data-badge="lesson4-bug2"></div>
<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">「等于吗？」要几个等号？</span><span class="en">How many equals signs does "is it equal?" need?</span></details>

<div class="playground" data-src="{{ '/lessons/04/code/bug3.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 3" data-title-en="🐞 Patient 3" data-save="bug-3" data-draft="l4-bug3" data-expect="大\n结束" data-rows="6" data-badge="lesson4-bug3"></div>
<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">「属于」if 的那一行要怎么样？「结束」属不属于 if？</span><span class="en">What must the line that "belongs" to the if look like? Does "结束" belong to the if?</span></details>

<div class="playground" data-src="{{ '/lessons/04/code/bug4.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 4（没有红框）" data-title-en="🐞 Patient 4 (no red box)" data-save="bug-4" data-draft="l4-bug4" data-expect="🏆 优秀" data-rows="9" data-badge="lesson4-bug4"></div>
<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">95 &gt;= 60 是不是已经成立了？成立了以后，下面的 elif 还会看吗？哪个条件应该先检查？</span><span class="en">Is 95 &gt;= 60 already true? Once it's true, does Python even look at the elif below? Which condition should be checked first?</span></details>

<p style="text-align:center;margin-top:1.4em"><a class="pg-btn run" style="text-decoration:none;font-size:1.05rem" href="{{ '/games/bugs/' | relative_url }}"><span class="zh">想当更厉害的医生？去 🐞 虫虫医院 →</span><span class="en">Want to be a better doctor? Go to 🐞 Bug Hospital →</span></a></p>

---

### 🏆 <span class="zh">挑战：火箭发射控制中心</span><span class="en">Challenge: rocket launch control</span>
{: #challenge}

<p><span class="zh">真正的火箭发射前，控制中心会检查很多东西，天气不好也会推迟。这次<b>没有起始代码</b>，只有两行 <code>input</code> 和一份「设计说明」——你要自己想清楚 <b>if 套在哪里、for 放在哪里</b>。做好了就 <b>📤 存到作品墙</b>！</span><span class="en">Before a real rocket launch, mission control checks lots of things, and bad weather can delay it. This time there's <b>no starter code</b>, just two <code>input</code> lines and a "design brief" — you decide <b>where the ifs nest and where the for goes</b>. When it works, <b>📤 Save to Gallery</b>!</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/challenge.py' | relative_url }}" data-title="🏆 发射控制中心" data-title-en="🏆 Launch control" data-save="launch-control" data-draft="l4-challenge" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：先画一棵「决定树」</span><span class="en">💡 Hint 1: draw a decision tree first</span></summary><span class="zh">在纸上画：燃料够吗？→ 不够：NO GO。→ 够：风大吗？→ 大：NO GO；不大：GO + 倒数。第二个问题在第一个问题的<b>「够」那条路里面</b>，所以它的 if 要缩进在 else 里面。</span><span class="en">On paper: enough fuel? → no: NO GO. → yes: too windy? → yes: NO GO; no: GO + countdown. The second question lives <b>inside the "yes" branch</b> of the first, so its if is indented inside the else.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：倒数放哪里？</span><span class="en">💡 Hint 2: where does the countdown go?</span></summary><span class="zh"><code>for s in range(10, 0, -1):</code> 要放在「✅ GO!」那一行的<b>下面、同样的缩进</b>。循环里面再用 <code>if s % 2 == 0:</code> 判断双数秒。</span><span class="en"><code>for s in range(10, 0, -1):</code> goes <b>right under "✅ GO!" with the same indent</b>. Inside the loop, use <code>if s % 2 == 0:</code> for even seconds.</span></details>

---

## 🤖 <span class="zh">和 AI 一起：让它当排错伙伴</span><span class="en">With AI: a debugging buddy</span>
{: #ai}

<p><span class="zh">报错的时候，红框里有一个 <b>📋 复制「问 AI 要提示」的话</b> 按钮。它会把报错和你的代码一起打包好，你只要补上「我想让它______」。</span><span class="en">When there's an error, the red box has a <b>📋 Copy a "hint please" message</b> button. It packs the error and your code together; you just fill in "I want it to ______".</span></p>

<pre class="zh" style="white-space:pre-wrap">我在做猜数字游戏，我想让它在猜对的时候停下来，
但是它猜对了还一直问。
请给我一个提示，告诉我去看哪里，不要直接给我改好的代码。</pre>
<pre class="en" style="white-space:pre-wrap">I'm making a guessing game. I want it to stop when the guess is right,
but it keeps asking after a correct guess.
Please give me a hint about where to look. Don't give me the fixed code.</pre>
<button class="pg-btn copy-prev">📋 <span class="zh">复制这段话</span><span class="en">Copy this</span></button>

<div class="chat">
  <div class="bubble me"><span class="zh">😕 <b>不好的问法：</b>「代码坏了，帮我修。」（AI 不知道你想做什么，也不知道报了什么错）</span><span class="en">😕 <b>Not so good:</b> "My code is broken, fix it." (AI doesn't know what you want or what the error says)</span></div>
  <div class="bubble me"><span class="zh">😃 <b>好的问法：</b>「我想让它______，但是它______（贴报错）。请给我一个提示。」</span><span class="en">😃 <b>Good:</b> "I want it to ______, but it ______ (paste error). Give me a hint please."</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">提示：看看「猜对了」那段 if 里面——for 循环会一直数到 5 次。有没有一个词可以让循环提前停下来？你在课上学过……</span><span class="en">Hint: look inside the "you got it" part of the if — the for loop keeps counting to 5. Is there a word that makes a loop stop early? You learned it in class…</span></div>
</div>

<ul class="quests" data-key="l4-ai">
  <li><span class="zh">在任何一个病号上点「📋 复制」，看看它帮你写了什么。</span><span class="en">Click "📋 Copy" on any patient and see what it writes for you.</span></li>
  <li>🔍 <span class="zh">病号 4 没有红框，AI 按钮不会出现。<b>自己</b>写一段问法：「我想让它______，但它______」。</span><span class="en">Patient 4 has no red box, so no AI button. Write the question <b>yourself</b>: "I want it to ______, but it ______".</span></li>
  <li>🔍 <span class="zh">AI 给了提示以后，<b>自己改</b>，再运行检验。</span><span class="en">After AI's hint, <b>fix it yourself</b> and run to check.</span></li>
</ul>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>if / else</b><code>if guess == secret:
    print("对")
else:
    print("错")</code><span><span class="zh">两条路只走一条</span><span class="en">Two roads, only one is taken</span></span></div>
  <div class="k"><b>elif</b><code>if d == 6:
    ...
elif d >= 4:
    ...
else:
    ...</code><span><span class="zh">很多条路，从上往下第一个成立的；严格的放上面</span><span class="en">Many roads; the first true one from the top — strict ones first</span></span></div>
  <div class="k"><b>== vs =</b><code>x = 5      # 放进盒子
x == 5     # 等于吗？</code><span><span class="zh">一个是动作，两个是问题</span><span class="en">One is an action, two is a question</span></span></div>
  <div class="k"><b>&lt; &gt; &lt;= &gt;= !=</b><code>if guess > secret:
    print("太大了")</code><span><span class="zh">比大小</span><span class="en">Comparing</span></span></div>
  <div class="k"><b>random.randint(a, b)</b><code>import random
dice = random.randint(1, 6)</code><span><span class="zh">a 到 b 里随机挑一个</span><span class="en">A random number from a to b</span></span></div>
  <div class="k"><b>break</b><code>for i in range(5):
    if guess == secret:
        break</code><span><span class="zh">对循环喊「停！」</span><span class="en">Shout "stop!" at the loop</span></span></div>
  <div class="k"><b>% </b><code>i % 2 == 0   # 双数？
i % 3 == 0   # 3 的倍数？</code><span><span class="zh">余数是 0 = 刚好整除</span><span class="en">Remainder 0 = divides exactly</span></span></div>
  <div class="k"><b><span class="zh">if 套 if</span><span class="en">if inside if</span></b><code>if fuel >= 90:
    if wind > 40:
        print("NO GO")</code><span><span class="zh">先过第一关，才问第二个问题；多缩进 4 格</span><span class="en">Pass the first check before asking the second; 4 more spaces</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l04">📖 小词典 · 第 4 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l04">📖 cheat sheet · Lesson 4</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/04/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
