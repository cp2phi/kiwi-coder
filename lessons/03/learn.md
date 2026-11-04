---
title: 第 3 课 · 学一学
title_en: Lesson 3 · Learn
lesson: "03"
tab: learn
playground: true
---

# 🌀 <span class="zh">for 循环：让电脑替你重复</span><span class="en">for loops: make the computer repeat</span>

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">第 2 课的变量：<code>size = 100</code> 是一个有名字的盒子。下面的正方形 4 条边都用它。</span><span class="en">Lesson 2 variables: <code>size = 100</code> is a box with a name. All 4 sides of this square use it.</span></p>

<div class="playground" data-src="{{ '/lessons/03/code/warmup.py' | relative_url }}" data-title="🔁 变量正方形" data-title-en="🔁 Variable square" data-save="variable-square" data-rows="8"></div>

<ul class="quests" data-key="l3-warmup">
  <li><span class="zh">把 <code>size</code> 改成 160，运行。只改了 1 个数字，几条边变了？</span><span class="en">Change <code>size</code> to 160 and run. You changed 1 number — how many sides changed?</span></li>
  <li><span class="zh">把 <code>colour</code> 改成 <code>"hotpink"</code>。</span><span class="en">Change <code>colour</code> to <code>"hotpink"</code>.</span></li>
  <li>🤔 <span class="zh">数一数：<code>t.forward</code> 和 <code>t.left</code> 一共写了几次？是不是有点烦？</span><span class="en">Count: how many times is <code>t.forward</code> + <code>t.left</code> written? A bit boring, right?</span></li>
</ul>

---

## ✨ <span class="zh">今天的新魔法：for 循环</span><span class="en">Today's new magic: the for loop</span>
{: #magic}

<p class="zh">体育老师不会说 4 次「做一个俯卧撑」，她会说：「<b>做 4 个俯卧撑！</b>」<br>Python 也一样。与其写 4 次「走、转」，不如告诉电脑：「<b>把这两行重复 4 次</b>」。</p>
<p class="en">A PE teacher doesn't say "do one push-up" four times. She says: "<b>Do 4 push-ups!</b>"<br>Python is the same. Instead of writing "move, turn" 4 times, tell the computer: "<b>repeat these 2 lines 4 times</b>".</p>

<div class="two">
<div><b><span class="zh">😩 以前（8 行）</span><span class="en">😩 Before (8 lines)</span></b>
<pre>t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)</pre></div>
<div><b><span class="zh">😎 现在（3 行）</span><span class="en">😎 Now (3 lines)</span></b>
<pre>for i in range(4):
    t.forward(100)
    t.left(90)</pre>
<p class="muted" style="font-size:.9rem"><span class="zh">读法：「对于 4 次里的每一次 i，做下面这两行。」</span><span class="en">Read it as: "for each of 4 times, do these two lines."</span></p></div>
</div>

<div class="cmds">
  <div class="cmd"><code>for i in range(4):</code><span><span class="zh">重复 4 次。最后的冒号 <code>:</code> 不能少</span><span class="en">Repeat 4 times. The colon <code>:</code> at the end is a must</span></span></div>
  <div class="cmd"><code>    t.forward(100)</code><span><span class="zh">前面 4 个空格 = 「我属于这个循环」</span><span class="en">4 spaces in front = "I belong to this loop"</span></span></div>
  <div class="cmd"><code>range(4)</code><span><span class="zh">数数：0, 1, 2, 3（一共 4 个）</span><span class="en">Counts: 0, 1, 2, 3 (4 numbers)</span></span></div>
  <div class="cmd"><code>i</code><span><span class="zh">计数的变量，每次都变：0 → 1 → 2 → 3</span><span class="en">The counting variable: 0 → 1 → 2 → 3</span></span></div>
</div>

### 🤔 <span class="zh">先猜，再运行</span><span class="en">Guess first, then run</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的代码会画出什么？（先别点运行！）</span><span class="en">What will the code below draw? (Don't click Run yet!)</span></p>
  <div class="opts"><button><span class="zh">4 条分开的线</span><span class="en">4 separate lines</span></button><button><span class="zh">一个正方形</span><span class="en">One square</span></button><button><span class="zh">4 个正方形</span><span class="en">4 squares</span></button></div>
  <div class="why"><span class="zh">一个正方形！循环里的「走 100、左转 90」做了 4 次，和第 1 课手写 8 行一模一样。</span><span class="en">One square! "Move 100, turn left 90" happens 4 times — exactly like the 8 hand-written lines in lesson 1.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/03/code/square-loop.py' | relative_url }}" data-title="🌀 例 1：循环正方形" data-title-en="🌀 Example 1: loop square" data-save="loop-square" data-rows="8"></div>

### 🔍 <span class="zh">改一改</span><span class="en">Change it</span>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">如果把 <code>range(4)</code> 改成 <code>range(6)</code>，<code>left(90)</code> 改成 <code>left(60)</code>，会画出什么？</span><span class="en">If you change <code>range(4)</code> to <code>range(6)</code> and <code>left(90)</code> to <code>left(60)</code>, what do you get?</span></p>
  <div class="opts"><button><span class="zh">还是正方形</span><span class="en">Still a square</span></button><button><span class="zh">一个三角形</span><span class="en">A triangle</span></button><button><span class="zh">一个六边形</span><span class="en">A hexagon</span></button></div>
  <div class="why"><span class="zh">六边形！6 次 × 60° = 360°，正好转一圈回到起点。</span><span class="en">A hexagon! 6 × 60° = 360°, exactly one full turn back to the start.</span></div>
</div>

<ul class="quests" data-key="l3-modify">
  <li>6️⃣ <span class="zh">改成 <code>range(6)</code> + <code>left(60)</code>，验证你的猜测。</span><span class="en">Change to <code>range(6)</code> + <code>left(60)</code> and check your guess.</span></li>
  <li>8️⃣ <span class="zh">改成 <code>range(8)</code> + <code>left(45)</code>。</span><span class="en">Change to <code>range(8)</code> + <code>left(45)</code>.</span></li>
  <li>3️⃣ <span class="zh">三角形要几次、转几度？</span><span class="en">For a triangle: how many times, how many degrees?</span></li>
  <li>🧠 <span class="zh">发现规律了吗？<b>次数 × 角度 = ？</b>（答案在下面的例 2 里）</span><span class="en">Spot the pattern? <b>times × angle = ?</b> (the answer is in Example 2)</span></li>
</ul>

<div class="box box-tip"><span class="zh">⚠️ 两个最常见的小错误：① <code>for</code> 那一行最后忘了冒号 <code>:</code>　② 循环里的行忘了缩进。报错框会告诉你是哪一种。</span><span class="en">⚠️ The two most common slips: ① forgetting the colon <code>:</code> at the end of the <code>for</code> line　② forgetting to indent the lines inside. The error box tells you which one.</span></div>

---

### 🧪 <span class="zh">例 2：万能多边形机（填空）</span><span class="en">Example 2: the any-polygon machine (fill in)</span>

<p><span class="zh">规律是 <b>次数 × 角度 = 360</b>。所以角度 = 360 ÷ 边数——这个除法让电脑算！把 <code>___</code> 换成边数。</span><span class="en">The pattern is <b>times × angle = 360</b>. So angle = 360 ÷ sides — let the computer do the division! Replace <code>___</code> with the number of sides.</span></p>

<div class="playground" data-src="{{ '/lessons/03/code/polygon.py' | relative_url }}" data-title="🧪 例 2：多边形机" data-title-en="🧪 Example 2: polygon machine" data-save="polygon-machine" data-draft="l3-polygon" data-rows="8"></div>

<ul class="quests" data-key="l3-polygon">
  <li><span class="zh">试 5、8、12。</span><span class="en">Try 5, 8, 12.</span></li>
  <li><span class="zh">试 36 或 100——像什么？（圆其实就是很多很多条边！）</span><span class="en">Try 36 or 100 — what does it look like? (A circle is just lots and lots of sides!)</span></li>
  <li><span class="zh">把 <code>t.forward(80)</code> 改成 <code>t.forward(20)</code>，边数 100，再看看。</span><span class="en">Change <code>t.forward(80)</code> to <code>t.forward(20)</code> with 100 sides and look again.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh"><code>sides = 5</code> 就是五边形。注意 <code>range(sides)</code> 和 <code>360 / sides</code> 用的是同一个盒子，所以只要改一个数字。</span><span class="en"><code>sides = 5</code> gives a pentagon. <code>range(sides)</code> and <code>360 / sides</code> use the same box, so you only change one number.</span></details>

---

### 🧪 <span class="zh">例 3：彩虹螺旋（i 的秘密）</span><span class="en">Example 3: rainbow spiral (the secret of i)</span>

<p><span class="zh">还记得第 1 课作品墙上那个彩虹螺旋吗？现在你能看懂了！秘密是：<b><code>i</code> 每次都在变大</b>——0、1、2、3……所以 <code>t.forward(i * 2)</code> 每次走得比上次远一点。</span><span class="en">Remember the rainbow spiral from lesson 1's gallery? Now you can read it! The secret: <b><code>i</code> grows every time</b> — 0, 1, 2, 3… so <code>t.forward(i * 2)</code> goes a little further each time.</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh"><code>for i in range(100): t.forward(i * 2)</code>——第 50 次循环时，海龟走几步？</span><span class="en"><code>for i in range(100): t.forward(i * 2)</code> — on the 50th time round, how far does the turtle go?</span></p>
  <div class="opts"><button>50</button><button>100</button><button>200</button></div>
  <div class="why"><span class="zh">i = 50 时，i × 2 = 100 步。第 0 次走 0 步，最后一次（i = 99）走 198 步，越来越长就成了螺旋。</span><span class="en">When i = 50, i × 2 = 100 steps. The first time (i = 0) it goes 0, the last time (i = 99) it goes 198. Longer and longer = a spiral.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/03/code/spiral.py' | relative_url }}" data-title="🌈 例 3：彩虹螺旋" data-title-en="🌈 Example 3: rainbow spiral" data-save="rainbow-spiral" data-draft="l3-spiral"></div>

<ul class="quests" data-key="l3-spiral">
  <li><span class="zh">把 <code>59</code> 改成 <code>90</code>，再改成 <code>91</code>。差 1 度，差别大吗？</span><span class="en">Change <code>59</code> to <code>90</code>, then <code>91</code>. Just 1 degree — big difference?</span></li>
  <li><span class="zh">试试 <code>120</code>、<code>121</code>、<code>144</code>。</span><span class="en">Try <code>120</code>, <code>121</code>, <code>144</code>.</span></li>
  <li><span class="zh">把 <code>i * 2</code> 改成 <code>i * 3</code>，或者 <code>range(100)</code> 改成 <code>range(200)</code>。</span><span class="en">Change <code>i * 2</code> to <code>i * 3</code>, or <code>range(100)</code> to <code>range(200)</code>.</span></li>
  <li>🎨 <span class="zh">换掉列表里的颜色（用引号包起来）。</span><span class="en">Swap the colours in the list (keep the quotes).</span></li>
</ul>

<div class="swatches" data-colors="red orange gold limegreen deepskyblue purple hotpink white cyan"></div>

<div class="box box-think"><span class="zh">🔮 <code>colors = [...]</code> 这种用方括号装一串东西的，叫<b>列表</b>，第 5 课正式学。今天先当魔法用：<code>colors[i % 6]</code> 会把 6 种颜色轮流拿出来。</span><span class="en">🔮 <code>colors = [...]</code>, a bunch of things in square brackets, is a <b>list</b> — lesson 5. For now treat it as magic: <code>colors[i % 6]</code> hands out the 6 colours in turn.</span></div>

---

### 🧪 <span class="zh">例 4：万花筒（循环里面还有循环！）</span><span class="en">Example 4: kaleidoscope (a loop inside a loop!)</span>

<p><span class="zh">里面的循环画<b>一个正方形</b>，外面的循环说：「画一个，转 30 度，再画一个……做 12 次。」12 × 30 = 360，正好转一圈！</span><span class="en">The inner loop draws <b>one square</b>. The outer loop says: "draw one, turn 30, draw one… 12 times." 12 × 30 = 360, one full turn!</span></p>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">外面 <code>range(12)</code>，里面 <code>range(4)</code>，<code>t.forward</code> 一共跑了几次？</span><span class="en">Outer <code>range(12)</code>, inner <code>range(4)</code>: how many times does <code>t.forward</code> run in total?</span></p>
  <div class="opts"><button>12</button><button>16</button><button>48</button></div>
  <div class="why"><span class="zh">48 次！每一次外循环，里面都要完整跑 4 次：12 × 4 = 48。</span><span class="en">48! Every outer loop runs the whole inner loop 4 times: 12 × 4 = 48.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/03/code/kaleidoscope.py' | relative_url }}" data-title="🔮 例 4：万花筒" data-title-en="🔮 Example 4: kaleidoscope" data-save="kaleidoscope" data-draft="l3-kaleido"></div>

<ul class="quests" data-key="l3-kaleido">
  <li><span class="zh">改成 <code>range(36)</code> 和 <code>t.left(10)</code>（36 × 10 还是 360）。</span><span class="en">Change to <code>range(36)</code> and <code>t.left(10)</code> (36 × 10 is still 360).</span></li>
  <li><span class="zh">把里面的正方形换成三角形（3 次、120 度）。</span><span class="en">Swap the inner square for a triangle (3 times, 120 degrees).</span></li>
  <li><span class="zh">在外循环里加一行 <code>t.color(colors[i % 6])</code>——要先把例 3 的 <code>colors</code> 列表复制过来哦。</span><span class="en">Add <code>t.color(colors[i % 6])</code> in the outer loop — copy the <code>colors</code> list from Example 3 first.</span></li>
</ul>

---

### 📣 <span class="zh">文字也能重复</span><span class="en">Words can repeat too</span>

<p><span class="zh">循环不只给海龟用。<code>range(5, 0, -1)</code> 是倒着数：5、4、3、2、1。</span><span class="en">Loops aren't just for turtles. <code>range(5, 0, -1)</code> counts down: 5, 4, 3, 2, 1.</span></p>

<div class="playground" data-src="{{ '/lessons/03/code/countdown.py' | relative_url }}" data-canvas="no" data-title="🚀 倒计时" data-title-en="🚀 Countdown" data-save="countdown" data-rows="8"></div>

<ul class="quests" data-key="l3-countdown">
  <li><span class="zh">把「我爱 Python」改成重复 10 次。</span><span class="en">Make "I love Python" repeat 10 times.</span></li>
  <li><span class="zh">改成从 10 倒数。</span><span class="en">Count down from 10.</span></li>
  <li><span class="zh">加一行 <code>for i in range(0, 20, 2): print(i)</code>——猜猜会打印什么？</span><span class="en">Add <code>for i in range(0, 20, 2): print(i)</code> — guess what it prints first.</span></li>
</ul>

### 🐞 <span class="zh">缩进实验：故意弄坏它</span><span class="en">Indentation experiment: break it on purpose</span>

<p><span class="zh">把第 9 行前面的 4 个空格删掉，运行，<b>读一读红框</b>，再修好。这是今天最重要的报错！</span><span class="en">Delete the 4 spaces at the start of line 9, run it, <b>read the red box</b>, then fix it. This is today's most important error!</span></p>

<div class="playground" data-src="{{ '/lessons/03/code/indent.py' | relative_url }}" data-title="🐞 缩进实验" data-title-en="🐞 Indentation experiment" data-save="indent-test" data-rows="8"></div>

<div class="box box-good"><span class="zh">💡 <b>报错不是失败。</b>电脑在告诉你：「第 9 行，缩进不对」。修好它，你就学会了读报错——这比写对代码还重要。</span><span class="en">💡 <b>An error is not a failure.</b> The computer is telling you: "line 9, indentation wrong". Fix it and you've learned to read errors — even more important than writing correct code.</span></div>

---

### 🏆 <span class="zh">挑战：画一朵花</span><span class="en">Challenge: draw a flower</span>
{: #challenge}

<p><span class="zh">一个圆重复很多次，每次转一点点，就变成花瓣！填好 <code>___</code>，画好了就 <b>📤 存到作品墙</b>。想更厉害？再用一个循环在黑夜里画满星星。</span><span class="en">A circle repeated, turning a little each time, becomes petals! Fill in <code>___</code>, then <b>📤 Save to Gallery</b>. Want more? Add another loop that fills a night sky with stars.</span></p>

<div class="playground" data-src="{{ '/lessons/03/code/challenge.py' | relative_url }}" data-title="🏆 挑战：花朵" data-title-en="🏆 Challenge: flower" data-save="my-flower" data-draft="l3-challenge"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">规律还是：次数 × 角度 = 360。想要 12 片花瓣，每次转几度？</span><span class="en">Same pattern: times × angle = 360. For 12 petals, how many degrees each turn?</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2（星星）</span><span class="en">💡 Hint 2 (stars)</span></summary><span class="zh">星星可以用 <code>t.dot(5, "white")</code> 点一个点。跳到不同位置：<code>t.penup()</code> → <code>t.goto(100, 200)</code> → <code>t.pendown()</code>。第 4 课会学 random，让位置随机。</span><span class="en">A star can be <code>t.dot(5, "white")</code>. Jump around with <code>t.penup()</code> → <code>t.goto(100, 200)</code> → <code>t.pendown()</code>. In lesson 4 you'll learn random for random spots.</span></details>

---

## 🤖 <span class="zh">和 AI 一起：请它解释代码</span><span class="en">With AI: ask it to explain code</span>
{: #ai}

<p><span class="zh">今天第一次把 AI 当<b>老师</b>用。不是让它写，而是让它<b>解释</b>。把例 3 的代码复制给 AI，然后这样问：</span><span class="en">Today you use AI as a <b>teacher</b> for the first time. Not to write code, but to <b>explain</b> it. Copy the code from Example 3 to the AI, then ask:</span></p>

<pre class="zh" style="white-space:pre-wrap">我是小学生，正在学 Python 的 for 循环。
请用小学生能听懂的话，解释这段代码的第 ___ 行是什么意思，
再举一个很小的例子。不要改我的代码。</pre>
<pre class="en" style="white-space:pre-wrap">I'm a primary school student learning Python for loops.
Please explain what line ___ of this code means, in simple words,
and give a tiny example. Don't change my code.</pre>
<button class="pg-btn copy-prev">📋 <span class="zh">复制这段话</span><span class="en">Copy this</span></button>

<div class="chat">
  <div class="bubble me"><span class="zh">😕 <b>不好的问法：</b>「帮我写一个螺旋。」（AI 写了，你还是不懂）</span><span class="en">😕 <b>Not so good:</b> "Write me a spiral." (AI writes it, you still don't get it)</span></div>
  <div class="bubble me"><span class="zh">😃 <b>好的问法：</b>「第 14 行 <code>colors[i % 6]</code> 是什么意思？用小学生能听懂的话解释。」</span><span class="en">😃 <b>Good:</b> "What does <code>colors[i % 6]</code> on line 14 mean? Explain it simply."</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh"><code>i % 6</code> 是「i 除以 6 的余数」。i 是 0、1、2、3、4、5 时余数就是自己；i 是 6 时余数又变回 0。所以它会一直在 0～5 之间转圈，刚好用来轮流拿 6 种颜色……</span><span class="en"><code>i % 6</code> is "the remainder of i divided by 6". For i = 0 to 5 it's just i; at i = 6 it goes back to 0. So it cycles 0–5 forever — perfect for taking 6 colours in turn…</span></div>
</div>

<ul class="quests" data-key="l3-ai">
  <li><span class="zh">挑一行你最不明白的，用上面的模板问 AI。</span><span class="en">Pick the line you understand least and ask AI with the template above.</span></li>
  <li>🔍 <span class="zh">检验它：把 AI 说的改一改代码试试，对不对？</span><span class="en">Check it: change the code the way AI described — was it right?</span></li>
  <li><span class="zh">把你学到的那一句写到代码的注释里。</span><span class="en">Write what you learned as a comment in your code.</span></li>
</ul>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>for … in range(n):</b><code>for i in range(4):
    t.forward(100)
    t.left(90)</code><span><span class="zh">重复 n 次。冒号 + 缩进 4 格</span><span class="en">Repeat n times. Colon + 4-space indent</span></span></div>
  <div class="k"><b>i</b><code>for i in range(5):
    print(i)   # 0 1 2 3 4</code><span><span class="zh">计数变量，每次 +1，从 0 开始</span><span class="en">The counter: starts at 0, +1 each time</span></span></div>
  <div class="k"><b>range(a, b, step)</b><code>range(5, 0, -1)
# 5 4 3 2 1</code><span><span class="zh">从 a 到 b 之前，每次跳 step</span><span class="en">From a up to b, jumping by step</span></span></div>
  <div class="k"><b><span class="zh">360 ÷ 边数</span><span class="en">360 ÷ sides</span></b><code>for i in range(sides):
    t.left(360 / sides)</code><span><span class="zh">任何多边形的角度公式</span><span class="en">The angle formula for any polygon</span></span></div>
  <div class="k"><b><span class="zh">循环套循环</span><span class="en">Nested loops</span></b><code>for i in range(12):
    for j in range(4):
        ...
    t.left(30)</code><span><span class="zh">里面跑完一轮，外面才数一次</span><span class="en">Inner finishes fully before outer counts once</span></span></div>
  <div class="k"><b>i * 2 / i % 6</b><code>t.forward(i * 2)
t.color(colors[i % 6])</code><span><span class="zh">用 i 让每次都不一样</span><span class="en">Use i to make each time different</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l03">📖 小词典 · 第 3 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l03">📖 cheat sheet · Lesson 3</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/games/robot/' | relative_url }}"><span class="zh">去玩：💎 宝石机器人 →</span><span class="en">Play: 💎 Gem Robot →</span></a> &nbsp; <a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/03/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
