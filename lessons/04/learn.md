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

<p><span class="zh">上周的 for 循环：倒计时 + 螺旋。改两个数字热热身。</span><span class="en">Last week's for loops: a countdown + a spiral. Change two numbers to warm up.</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/warmup.py' | relative_url }}" data-title="🔁 热身" data-title-en="🔁 Warm-up" data-save="warmup-4" data-rows="8"></div>

<ul class="quests" data-key="l4-warmup">
  <li><span class="zh">倒计时改成从 5 开始。</span><span class="en">Make the countdown start at 5.</span></li>
  <li><span class="zh">螺旋的 <code>91</code> 改成 <code>120</code>。</span><span class="en">Change the spiral's <code>91</code> to <code>120</code>.</span></li>
  <li>🤔 <span class="zh">不看代码，说出 <code>range(3, 0, -1)</code> 会数出哪几个数。</span><span class="en">Without looking, say which numbers <code>range(3, 0, -1)</code> counts.</span></li>
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
  <li><span class="zh">把 <code>else:</code> 改成两段：<code>elif guess &gt; secret:</code> 打印「太大了」，<code>else:</code> 打印「太小了」。</span><span class="en">Split <code>else:</code> into two: <code>elif guess &gt; secret:</code> prints "too big", <code>else:</code> prints "too small".</span></li>
  <li>🐞 <span class="zh">故意把 <code>==</code> 改成 <code>=</code>，运行，读报错，改回来。</span><span class="en">Change <code>==</code> to <code>=</code> on purpose, run, read the error, change it back.</span></li>
</ul>

---

### 🧪 <span class="zh">例 2：电子骰子（随机数 + elif）</span><span class="en">Example 2: electronic dice (random + elif)</span>

<p><span class="zh">游戏要好玩，电脑得会<b>随机</b>。<code>random.randint(1, 6)</code> 就像掷一个骰子。然后用 <code>if / elif / else</code> 给不同的点数不同的反应。</span><span class="en">For a game to be fun, the computer needs <b>randomness</b>. <code>random.randint(1, 6)</code> is like rolling a die. Then <code>if / elif / else</code> reacts differently to each roll.</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/dice.py' | relative_url }}" data-canvas="no" data-title="🎲 例 2：电子骰子" data-title-en="🎲 Example 2: dice" data-save="dice" data-rows="9"></div>

<ul class="quests" data-key="l4-dice">
  <li><span class="zh">运行 5 次，每次一样吗？</span><span class="en">Run it 5 times. Same every time?</span></li>
  <li><span class="zh">改成 20 面骰子：<code>randint(1, 20)</code>，「大吉」改成 20。</span><span class="en">Make a 20-sided die: <code>randint(1, 20)</code>, and jackpot on 20.</span></li>
  <li><span class="zh">在 <code>elif dice &gt;= 4:</code> <b>下面</b>再加一个 <code>elif dice &gt;= 5:</code> 打印「🤩 很好」。掷很多次，它出现过吗？为什么？把它挪到 <code>&gt;= 4</code> <b>上面</b>再试。（提示：从上往下，第一个成立的才跑）</span><span class="en">Add <code>elif dice &gt;= 5:</code> printing "🤩 great" <b>below</b> <code>elif dice &gt;= 4:</code>. Roll lots of times — does it ever show? Why? Move it <b>above</b> <code>&gt;= 4</code> and try again. (Hint: top to bottom, the first true one wins)</span></li>
</ul>

<p><span class="zh">海龟也能掷硬币！<code>randint(1, 2)</code> 不是 1 就是 2：</span><span class="en">The turtle can flip coins too! <code>randint(1, 2)</code> is 1 or 2:</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/random-colour.py' | relative_url }}" data-title="🎨 例 2b：掷硬币选颜色" data-title-en="🎨 Example 2b: coin-flip colours" data-save="coin-colours" data-rows="9"></div>

<ul class="quests" data-key="l4-coin">
  <li><span class="zh">改成 3 种颜色：<code>randint(1, 3)</code>，加一个 <code>elif coin == 2:</code>。</span><span class="en">Make it 3 colours: <code>randint(1, 3)</code> plus an <code>elif coin == 2:</code>.</span></li>
  <li><span class="zh">把 <code>t.left(10)</code> 改成 <code>t.left(random.randint(5, 30))</code>——每条线转的角度也随机！</span><span class="en">Change <code>t.left(10)</code> to <code>t.left(random.randint(5, 30))</code> — random angles too!</span></li>
</ul>

---

### 🧪 <span class="zh">例 3：完整的猜数字游戏（填空）</span><span class="en">Example 3: the whole guessing game (fill in)</span>
{: #guess}

<p><span class="zh">把例 1 和例 2 合起来：电脑<b>随机</b>出题，你有 <b>5 次</b>机会（for 循环！），每次 if 判断大了还是小了。猜对了就 <code>break</code>——跳出循环，不用再猜。填好 3 个 <code>___</code>。</span><span class="en">Example 1 + Example 2 together: the computer picks a <b>random</b> number, you get <b>5 tries</b> (a for loop!), and each guess gets an if check. A correct guess hits <code>break</code> — leave the loop, no more guessing. Fill in the 3 <code>___</code>.</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">如果没有 <code>break</code>，猜对以后会怎样？</span><span class="en">Without <code>break</code>, what happens after a correct guess?</span></p>
  <div class="opts"><button><span class="zh">程序报错</span><span class="en">An error</span></button><button><span class="zh">还会继续问你，直到 5 次用完</span><span class="en">It keeps asking until all 5 tries are used</span></button><button><span class="zh">什么都不变</span><span class="en">Nothing changes</span></button></div>
  <div class="why"><span class="zh">for 循环不知道你猜对了，它只管数 5 次。<code>break</code> 就是对循环喊「停！」。</span><span class="en">The for loop doesn't know you won — it just counts to 5. <code>break</code> shouts "stop!" at the loop.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/04/code/guess.py' | relative_url }}" data-canvas="no" data-title="🎯 例 3：猜数字游戏" data-title-en="🎯 Example 3: guessing game" data-save="guess-game" data-draft="l4-guess" data-rows="14"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">第一个空：数字范围是 1 到 10，所以 <code>randint(1, ?)</code>。</span><span class="en">First blank: the range is 1 to 10, so <code>randint(1, ?)</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2</span><span class="en">💡 Hint 2</span></summary><span class="zh">第二个空：猜的数字要和哪个盒子比？看看第一行创建了什么盒子。</span><span class="en">Second blank: which box should the guess be compared with? Look at the box made on the first line.</span></details>

<ul class="quests" data-key="l4-guess">
  <li><span class="zh">填完 3 个空，玩一局。</span><span class="en">Fill the 3 blanks and play a round.</span></li>
  <li><span class="zh">让老师玩一局，你来看代码里现在跑到哪一行。</span><span class="en">Let your teacher play while you follow which line is running.</span></li>
  <li><span class="zh">改成 1 到 100，机会改成 7 次。还够猜吗？（聪明的猜法：每次猜中间！）</span><span class="en">Change to 1–100 with 7 tries. Still enough? (Smart strategy: always guess the middle!)</span></li>
</ul>

---

### 🧪 <span class="zh">例 4：海龟随机散步（if 遇上 for）</span><span class="en">Example 4: random walk (if meets for)</span>

<p><span class="zh">每走一步掷一次硬币决定往哪转；<code>i % 2 == 0</code> 判断是不是偶数步来换颜色。每次运行都不一样！</span><span class="en">Every step flips a coin to decide which way to turn; <code>i % 2 == 0</code> checks for even steps to swap colours. Different every run!</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/random-walk.py' | relative_url }}" data-title="🐾 例 4：随机散步" data-title-en="🐾 Example 4: random walk" data-save="random-walk" data-draft="l4-walk"></div>

<ul class="quests" data-key="l4-walk">
  <li><span class="zh">把 <code>range(80)</code> 改成 <code>range(300)</code>。</span><span class="en">Change <code>range(80)</code> to <code>range(300)</code>.</span></li>
  <li><span class="zh">把转弯改成 <code>randint(1, 3)</code>：1 左转、2 右转、3 直走（用 <code>elif</code>）。</span><span class="en">Make turning <code>randint(1, 3)</code>: 1 left, 2 right, 3 straight (use <code>elif</code>).</span></li>
  <li>🌟 <span class="zh">加一个 if：<code>if i == 40:</code> 就 <code>t.pensize(8)</code>——散步到一半笔突然变粗。</span><span class="en">Add <code>if i == 40:</code> then <code>t.pensize(8)</code> — the pen gets thick halfway through the walk.</span></li>
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

### 🐞 <span class="zh">找 bug 游戏：治好 3 个病号</span><span class="en">Bug hunt: cure 3 patients</span>

<p><span class="zh">下面 3 个程序都「生病」了。先运行，<b>读红框</b>（第 1 步！），再修好。修好了会有 🏆。</span><span class="en">These 3 programs are "sick". Run each one, <b>read the red box</b> (step 1!), then fix it. A fixed patient earns a 🏆.</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/bug1.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 1" data-title-en="🐞 Patient 1" data-save="bug-1" data-draft="l4-bug1" data-expect="嗨\n嗨\n嗨" data-rows="5" data-badge="lesson4-bug1"></div>
<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh"><code>for</code> 那一行的最后少了什么符号？</span><span class="en">What symbol is missing at the end of the <code>for</code> line?</span></details>

<div class="playground" data-src="{{ '/lessons/04/code/bug2.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 2" data-title-en="🐞 Patient 2" data-save="bug-2" data-draft="l4-bug2" data-expect="正确" data-rows="5" data-badge="lesson4-bug2"></div>
<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">「等于吗？」要几个等号？</span><span class="en">How many equals signs does "is it equal?" need?</span></details>

<div class="playground" data-src="{{ '/lessons/04/code/bug3.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 3" data-title-en="🐞 Patient 3" data-save="bug-3" data-draft="l4-bug3" data-expect="大\n结束" data-rows="6" data-badge="lesson4-bug3"></div>
<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">「属于」if 的那一行要怎么样？「结束」属不属于 if？</span><span class="en">What must the line that "belongs" to the if look like? Does "结束" belong to the if?</span></details>

<p style="text-align:center;margin-top:1.4em"><a class="pg-btn run" style="text-decoration:none;font-size:1.05rem" href="{{ '/games/bugs/' | relative_url }}"><span class="zh">想当更厉害的医生？去 🐞 虫虫医院 →</span><span class="en">Want to be a better doctor? Go to 🐞 Bug Hospital →</span></a></p>

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
    ...</code><span><span class="zh">很多条路，从上往下第一个成立的</span><span class="en">Many roads; the first true one from the top</span></span></div>
  <div class="k"><b>== vs =</b><code>x = 5      # 放进盒子
x == 5     # 等于吗？</code><span><span class="zh">一个是动作，两个是问题</span><span class="en">One is an action, two is a question</span></span></div>
  <div class="k"><b>&lt; &gt; &lt;= &gt;= !=</b><code>if guess > secret:
    print("太大了")</code><span><span class="zh">比大小</span><span class="en">Comparing</span></span></div>
  <div class="k"><b>random.randint(a, b)</b><code>import random
dice = random.randint(1, 6)</code><span><span class="zh">a 到 b 里随机挑一个</span><span class="en">A random number from a to b</span></span></div>
  <div class="k"><b>break</b><code>for i in range(5):
    if guess == secret:
        break</code><span><span class="zh">对循环喊「停！」</span><span class="en">Shout "stop!" at the loop</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l04">📖 小词典 · 第 4 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l04">📖 cheat sheet · Lesson 4</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/04/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
