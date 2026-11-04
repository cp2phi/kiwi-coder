---
title: 第 7 课 · 学一学
title_en: Lesson 7 · Learn
lesson: "07"
tab: learn
playground: true
---

# 📦 <span class="zh">把代码打包：def 招式</span><span class="en">Packing code: tricks with def</span>

<p class="zh">海龟会 <code>forward</code>、<code>left</code>……这些都是<b>别人教给它的招式</b>。今天，<b>你来教它新招式</b>：比如「画正方形」「画房子」。教一次，以后随叫随到。</p>
<p class="en">The turtle knows <code>forward</code>, <code>left</code>… those are <b>tricks someone else taught it</b>. Today <b>you teach it new tricks</b>: "draw a square", "draw a house". Teach once, call any time.</p>

---

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">上节课的 <code>while</code> 和第 5 课的列表。把 <code>___</code> 填好，让海龟画 5 个彩色的圆，画完<b>自己停下</b>。</span><span class="en">Last lesson's <code>while</code> plus lists from Lesson 5. Fill in <code>___</code> so the turtle draws 5 coloured circles and <b>stops by itself</b>.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/warmup.py' | relative_url }}" data-title="🔁 热身：5 个圆" data-title-en="🔁 Warm-up: 5 circles" data-save="warmup-7" data-rows="8"></div>

<ul class="quests" data-key="l7-warmup">
  <li><span class="zh">填好两个空，运行。打印出「画了 5 个圆」了吗？</span><span class="en">Fill both blanks and run. Does it print "5 circles drawn"?</span></li>
  <li>🐞 <span class="zh">故意把 <code>count = count + 1</code> 删掉再运行——按「■ 停下」救它。为什么停不下来？</span><span class="en">Delete <code>count = count + 1</code> on purpose and run — press "■ Stop" to rescue it. Why doesn't it stop?</span></li>
</ul>

---

## ✨ <span class="zh">今天的新魔法：def = 给代码起名字</span><span class="en">Today's new magic: def = name a piece of code</span>
{: #magic}

<div class="box box-think"><span class="zh">🥋 想象你在教海龟一个<b>招式</b>。<code>def square():</code> 是在说「听好，这个招式叫 square，内容是下面这几行」。<b>教的时候它不动</b>——直到你喊 <code>square()</code>，它才表演一次。</span><span class="en">🥋 Imagine teaching the turtle a <b>trick</b>. <code>def square():</code> says "listen, this trick is called square, and here's what it does". <b>Teaching doesn't move it</b> — only when you call <code>square()</code> does it perform.</span></div>

<div class="cmds">
  <div class="cmd"><code>def square():</code><span><span class="zh">教一个叫 square 的招式（最后有冒号！）</span><span class="en">Teach a trick called square (colon at the end!)</span></span></div>
  <div class="cmd"><code>    t.forward(80)</code><span><span class="zh">招式的内容要往右缩 4 格</span><span class="en">The trick's body is indented 4 spaces</span></span></div>
  <div class="cmd"><code>square()</code><span><span class="zh">喊名字 = 表演一次（调用）</span><span class="en">Call the name = perform once</span></span></div>
  <div class="cmd"><code>def square(size):</code><span><span class="zh">括号里是参数：喊的时候递东西进去</span><span class="en">Inside the brackets: a parameter you hand in</span></span></div>
</div>

### 🤔 <span class="zh">先猜，再运行</span><span class="en">Guess first, then run</span>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">下面的代码里，<code>def square()</code> 写了 1 次，<code>square()</code> 喊了 3 次。会画出几个正方形？</span><span class="en">Below, <code>def square()</code> appears once and <code>square()</code> is called 3 times. How many squares get drawn?</span></p>
  <div class="opts"><button>1</button><button>4</button><button>3</button><button><span class="zh">0 个，会报错</span><span class="en">0, it errors</span></button></div>
  <div class="why"><span class="zh">3 个！<code>def</code> 只是「教」，不画。每喊一次 <code>square()</code> 画一个。中间用 penup / goto 换了地方，所以三个在不同位置。</span><span class="en">3! <code>def</code> only teaches, it doesn't draw. Every <code>square()</code> call draws one. penup / goto moves between them, so they're in different spots.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/07/code/square-fn.py' | relative_url }}" data-title="🥋 例 1：新招式 square()" data-title-en="🥋 Example 1: the square() trick" data-save="square-trick" data-rows="12"></div>

### 🔍 <span class="zh">改一改</span><span class="en">Change it</span>

<ul class="quests" data-key="l7-ex1">
  <li><span class="zh">把最后三次 <code>square()</code> 删掉，换成一个 <code>for i in range(5):</code> 循环，每次喊 <code>square()</code> 然后 <code>t.left(72)</code>。会变成什么图案？</span><span class="en">Delete the last three <code>square()</code> calls and replace them with <code>for i in range(5):</code> that calls <code>square()</code> then <code>t.left(72)</code>. What pattern appears?</span></li>
  <li><span class="zh">把 <code>def</code> 里的 <code>80</code> 改成 <code>120</code>——<b>只改一处</b>，所有正方形都变大了吗？这就是打包的好处！</span><span class="en">Change <code>80</code> to <code>120</code> inside <code>def</code> — <b>one edit</b>, did every square grow? That's the point of packing!</span></li>
  <li>🐞 <span class="zh">把 <code>def square():</code> 最后的冒号删掉，看报错说什么，再修好。</span><span class="en">Delete the colon after <code>def square():</code>, read the error, then fix it.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 第 1 个任务的提示</span><span class="en">💡 Hint for task 1</span></summary><span class="zh">最后几行变成：<br><code>for i in range(5):</code><br><code>    square()</code><br><code>    t.left(72)</code><br>72 × 5 = 360，转一整圈，像一朵花！</span><span class="en">The last lines become:<br><code>for i in range(5):</code><br><code>    square()</code><br><code>    t.left(72)</code><br>72 × 5 = 360, a full turn — like a flower!</span></details>

### 🧪 <span class="zh">例 2：带参数的招式——你说多大、什么颜色</span><span class="en">Example 2: a trick with parameters — you pick size and colour</span>

<p><span class="zh">喊 <code>square(60, "red")</code> 时，<b>60 会跑进 size，"red" 会跑进 colour</b>。括号里的名字叫<b>参数</b>，就像点餐时告诉厨师「要大份、辣的」。</span><span class="en">When you call <code>square(60, "red")</code>, <b>60 goes into size and "red" goes into colour</b>. Those names in the brackets are <b>parameters</b> — like telling the chef "large, spicy" when you order.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/square-params.py' | relative_url }}" data-title="🎨 例 2：square(size, colour)" data-title-en="🎨 Example 2: square(size, colour)" data-save="square-params" data-rows="12"></div>

<ul class="quests" data-key="l7-ex2">
  <li><span class="zh">把 <code>square(60, c)</code> 改成 <code>square(30 + i * 10, c)</code>——哦不对，循环里没有 <code>i</code>！先想想怎么改循环，让正方形一个比一个大。</span><span class="en">Try <code>square(30 + i * 10, c)</code> — wait, there's no <code>i</code> in this loop! Think about how to change the loop so each square is bigger than the last.</span></li>
  <li><span class="zh">在 <code>colours</code> 列表里再加 2 个颜色。要改循环吗？</span><span class="en">Add 2 more colours to the <code>colours</code> list. Do you need to change the loop?</span></li>
  <li>🐞 <span class="zh">喊 <code>square(60)</code>（少给一个）会怎样？读读报错里的 <code>missing</code>。</span><span class="en">What happens with <code>square(60)</code> (one missing)? Read the word <code>missing</code> in the error.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 一个比一个大的提示</span><span class="en">💡 Hint: growing squares</span></summary><span class="zh">用 <code>for i in range(6):</code> 然后 <code>square(30 + i * 10, colours[i])</code>。<code>colours[i]</code> 是第 i 个颜色（第 5 课学的！）。</span><span class="en">Use <code>for i in range(6):</code> then <code>square(30 + i * 10, colours[i])</code>. <code>colours[i]</code> is the i-th colour (from Lesson 5!).</span></details>

---

## 🏘️ <span class="zh">例 3：一条街——第 1 课的房子，打包！</span><span class="en">Example 3: a street — the Lesson 1 house, packed!</span>
{: #street}

<p><span class="zh">还记得第 1 课的作业「海龟建筑师」吗？正方形 + 三角形屋顶。那时候画 1 座要 12 行。现在把它打包成 <code>house(x, y, size)</code>，<b>画 5 座只要 2 行</b>。</span><span class="en">Remember Lesson 1's "Turtle Builder"? Square + triangle roof, 12 lines for one house. Now pack it into <code>house(x, y, size)</code> and <b>draw 5 houses in 2 lines</b>.</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh"><code>house(-250 + i * 120, -100, 80)</code>，当 i = 2 时，房子的 x 是多少？</span><span class="en">In <code>house(-250 + i * 120, -100, 80)</code>, what is x when i = 2?</span></p>
  <div class="opts"><button>-130</button><button>-10</button><button>110</button></div>
  <div class="why"><span class="zh">-250 + 2 × 120 = -250 + 240 = -10。i 每大 1，房子就往右挪 120。</span><span class="en">-250 + 2 × 120 = -250 + 240 = -10. Every time i grows by 1, the house shifts right by 120.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/07/code/street.py' | relative_url }}" data-title="🏘️ 例 3：一条街" data-title-en="🏘️ Example 3: a street" data-save="my-street" data-rows="14"></div>

<ul class="quests" data-key="l7-ex3">
  <li><span class="zh">把 <code>range(5)</code> 改成 <code>range(8)</code>，把 120 改成 70，size 改成 50——一条挤挤的小街！</span><span class="en">Change <code>range(5)</code> to <code>range(8)</code>, 120 to 70 and size to 50 — a cosy little street!</span></li>
  <li><span class="zh">给 <code>house</code> 加第 4 个参数 <code>colour</code>，在身体那里用 <code>t.color(colour)</code>。然后喊的时候递一个颜色进去。</span><span class="en">Add a 4th parameter <code>colour</code> to <code>house</code> and use <code>t.color(colour)</code> for the body. Then hand a colour in when you call it.</span></li>
  <li><span class="zh">再画<b>第二排</b>：复制那个 for 循环，把 -100 改成 60。</span><span class="en">Draw a <b>second row</b>: copy the for loop and change -100 to 60.</span></li>
</ul>

### 🔁 <span class="zh">例 4：return——招式做完，把结果「交回来」</span><span class="en">Example 4: return — the trick hands a result back</span>

<p><span class="zh">有的招式不画画，而是<b>算出一个答案</b>。<code>return</code> 就是「把答案交回去」。交回来的东西可以 <code>print</code>，可以存进变量，可以放进 <code>if</code>。</span><span class="en">Some tricks don't draw — they <b>work out an answer</b>. <code>return</code> means "hand the answer back". You can <code>print</code> it, store it in a variable, or use it in an <code>if</code>.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/return-demo.py' | relative_url }}" data-canvas="no" data-title="🔁 例 4：return" data-title-en="🔁 Example 4: return" data-save="return-demo" data-rows="12"></div>

<ul class="quests" data-key="l7-ex4">
  <li><span class="zh">运行前先在纸上写下 7 行输出，再运行对答案。全对吗？</span><span class="en">Before running, write the 7 output lines on paper, then run and check. All right?</span></li>
  <li><span class="zh">加一个招式 <code>def triple(n):</code> 交回 3 倍，然后 <code>print(triple(double(2)))</code>。先猜结果！</span><span class="en">Add <code>def triple(n):</code> that returns 3 times n, then <code>print(triple(double(2)))</code>. Guess first!</span></li>
  <li><span class="zh">把 <code>greet</code> 改成用毛利语和中文都打招呼：<code>return f"Kia ora, {name}! 你好！"</code></span><span class="en">Make <code>greet</code> say hello in te reo and Chinese: <code>return f"Kia ora, {name}! 你好！"</code></span></li>
</ul>

<div class="box box-tip"><span class="box-title"><span class="zh">🔍 小秘密：函数里的变量只住在函数里</span><span class="en">🔍 Secret: variables inside a function live only inside</span></span>
<span class="zh">参数和在函数里新建的变量，是函数的「私人物品」，外面看不到。先猜猜下面最后两行打印什么，再运行。</span><span class="en">Parameters and variables made inside a function are its "private things" — the outside can't see them. Guess what the last two lines print, then run.</span></div>

<div class="playground" data-src="{{ '/lessons/07/code/scope.py' | relative_url }}" data-canvas="no" data-title="🔍 函数里的 n 和外面的 n" data-title-en="🔍 n inside vs n outside" data-save="scope-demo" data-rows="8"></div>

---

## 🏙️ <span class="zh">例 5：小镇——三个招式合在一起</span><span class="en">Example 5: a town — three tricks together</span>
{: #town}

<p><span class="zh">house、tree、sun 三个招式都写好了，还有一个 <code>street(n)</code> 招式——<b>招式里面可以喊别的招式</b>！把 3 个 <code>___</code> 填好。</span><span class="en">house, tree and sun are ready, plus a <code>street(n)</code> trick — <b>tricks can call other tricks</b>! Fill in the 3 blanks.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/town.py' | relative_url }}" data-title="🏙️ 例 5：小镇" data-title-en="🏙️ Example 5: the town" data-save="my-town" data-draft="l7-town" data-rows="14"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh"><code>street(4)</code> 画 4 座。第二棵树的 x 试试 <code>280</code>。太阳半径试试 <code>40</code>。</span><span class="en"><code>street(4)</code> draws 4. Try <code>280</code> for the second tree's x. Try <code>40</code> for the sun's radius.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：想改房子的颜色？</span><span class="en">💡 Hint 2: want different house colours?</span></summary><span class="zh">在 <code>street</code> 里用一个颜色列表：<code>colours = ["tan", "khaki", "lightpink", "lightblue"]</code>，然后 <code>house(..., colours[i])</code>。</span><span class="en">Inside <code>street</code> use a colour list: <code>colours = ["tan", "khaki", "lightpink", "lightblue"]</code>, then <code>house(..., colours[i])</code>.</span></details>

### 🏆 <span class="zh">挑战：我的小镇</span><span class="en">Challenge: my town</span>

<p><span class="zh">规则：<b>至少 3 个自己写的招式</b>，至少 1 个有参数，用 <code>for</code> 循环喊它们。路灯、云、车、彩虹、围栏、花……都行。满意了就 <b>📤 存到作品墙</b>！</span><span class="en">Rules: <b>at least 3 tricks you wrote</b>, at least 1 with parameters, called from a <code>for</code> loop. Lamp posts, clouds, cars, a rainbow, a fence, flowers… anything. Happy with it? <b>📤 Save to Gallery</b>!</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/challenge.py' | relative_url }}" data-title="🏆 挑战：我的小镇" data-title-en="🏆 Challenge: my town" data-save="my-town-challenge" data-draft="l7-challenge" data-rows="14"></div>

<details class="hint"><summary><span class="zh">💡 路灯怎么画？</span><span class="en">💡 How to draw a lamp post?</span></summary><span class="zh"><code>def lamp(x, y):</code> → 走到 (x, y) → 左转 90 → 粗笔画 forward(60) → 画一个黄色的 <code>dot(16)</code> → 右转 90 回来。</span><span class="en"><code>def lamp(x, y):</code> → goto (x, y) → left 90 → thick forward(60) → a yellow <code>dot(16)</code> → right 90 to face right again.</span></details>

---

## 🤖 <span class="zh">和 AI 一起：让 AI 帮你打包</span><span class="en">With AI: let AI pack your code</span>

<p><span class="zh">AI 很擅长「把重复的代码改成函数」。但规则不变：<b>AI 给的每一行，你都要看懂，而且要运行了才算数</b>。</span><span class="en">AI is great at "turn this repeated code into a function". The rule stays: <b>understand every line AI gives you, and it only counts once it runs</b>.</span></p>

<div class="chat">
  <div class="bubble me"><span class="zh">😃 我是小学生，正在学 Python turtle。下面的代码画了 3 次一样的三角形（贴代码）。请把它改成一个有参数的函数，然后<b>一行一行解释</b>你改了什么。只用 turtle。</span><span class="en">😃 I'm a kid learning Python turtle. This code draws the same triangle 3 times (paste code). Please turn it into a function with parameters and <b>explain line by line</b> what you changed. Only use turtle.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">好的！<code>def triangle(x, y, size):</code> …（然后它解释每一行）</span><span class="en">Sure! <code>def triangle(x, y, size):</code> … (then it explains each line)</span></div>
  <div class="bubble me"><span class="zh">😕 不好的问法：「帮我画一个小镇。」——你什么都没学到，而且不知道代码对不对。</span><span class="en">😕 A bad ask: "Draw me a town." — you learn nothing and can't tell if it's right.</span></div>
</div>

<ul class="quests" data-key="l7-ai">
  <li><span class="zh">把你挑战画板里<b>重复最多的几行</b>贴给 AI，用上面的问法。</span><span class="en">Paste the <b>most repeated lines</b> from your challenge to AI, using the ask above.</span></li>
  <li><span class="zh">把 AI 的函数贴回画板运行。<b>能跑吗？</b>找 1 行看不懂的，再问「这一行是什么意思？」</span><span class="en">Paste AI's function back into the playground. <b>Does it run?</b> Find 1 line you don't get and ask "what does this line mean?"</span></li>
</ul>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>def <span class="zh">教招式</span><span class="en">teach a trick</span></b><code>def square():
    for i in range(4):
        t.forward(80)
        t.left(90)</code><span><span class="zh">只是「教」，不画。冒号 + 缩进。</span><span class="en">Only teaches, doesn't draw. Colon + indent.</span></span></div>
  <div class="k"><b><span class="zh">调用</span><span class="en">call</span></b><code>square()
square()</code><span><span class="zh">喊一次表演一次。</span><span class="en">Each call performs once.</span></span></div>
  <div class="k"><b><span class="zh">参数</span><span class="en">parameters</span></b><code>def house(x, y, size):
    ...
house(-100, 0, 80)</code><span><span class="zh">喊的时候按顺序递进去。</span><span class="en">Handed in, in order, when you call.</span></span></div>
  <div class="k"><b>return <span class="zh">交回结果</span><span class="en">hand back</span></b><code>def double(n):
    return n * 2
x = double(5)   # 10</code><span><span class="zh">结果可以存、可以 print、可以放进 if。</span><span class="en">Store it, print it, or use it in an if.</span></span></div>
  <div class="k"><b><span class="zh">招式里喊招式</span><span class="en">tricks calling tricks</span></b><code>def street(n):
    for i in range(n):
        house(i * 120, 0, 80)</code><span><span class="zh">大问题 = 几个小招式拼起来。</span><span class="en">Big problem = small tricks combined.</span></span></div>
  <div class="k"><b><span class="zh">里面的变量</span><span class="en">local variables</span></b><code>def f(n):
    n = n * 10   # 只改里面的 n
</code><span><span class="zh">函数里的变量外面看不到。</span><span class="en">Variables inside aren't visible outside.</span></span></div>
</div>

<p><span class="zh">全部指令在 <a href="{{ '/cheatsheet/' | relative_url }}#l07">📖 小词典 · 第 7 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l07">📖 cheat sheet · Lesson 7</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/07/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
