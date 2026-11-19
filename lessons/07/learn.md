---
title: 第 7 课 · 学一学
title_en: Lesson 7 · Learn
lesson: "07"
tab: learn
playground: true
---

# 📦 <span class="zh">把代码打包：def 招式</span><span class="en">Packing code: tricks with def</span>

<p class="zh">海龟会 <code>forward</code>、<code>left</code>……这些都是<b>别人教给它的招式</b>。今天，<b>你来教它新招式</b>：画房子、画火箭、检查能不能发射。教一次，以后随叫随到。</p>
<p class="en">The turtle knows <code>forward</code>, <code>left</code>… those are <b>tricks someone else taught it</b>. Today <b>you teach it new tricks</b>: draw a house, draw a rocket, check if it's safe to launch. Teach once, call any time.</p>

---

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">上节课的 <code>while</code> 和第 5 课的列表。这次只有<b>一个空</b>，但还<b>少了一整行</b>——你来补。</span><span class="en">Last lesson's <code>while</code> plus lists from Lesson 5. Only <b>one blank</b> this time, but <b>a whole line is missing</b> too — you add it.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/warmup.py' | relative_url }}" data-title="🔁 热身：彩色圆圈" data-title-en="🔁 Warm-up: coloured circles" data-save="warmup-7" data-rows="10"></div>

<ul class="quests" data-key="l7-warmup">
  <li><span class="zh">填好空，<b>不要</b>直接写 5——用 <code>len(colours)</code>。再往列表里加一个颜色：while 那行不用改，也多画了一个圆吗？</span><span class="en">Fill the blank, but <b>don't</b> just write 5 — use <code>len(colours)</code>. Then add a colour to the list: did it draw one more circle without touching the while line?</span></li>
  <li>🐞 <span class="zh">补上少掉的那一行。补之前先想：不补的话会怎样？（真跑起来停不下就按「■ 停下」。）</span><span class="en">Add the missing line. First think: what happens without it? (If it really won't stop, press "■ Stop".)</span></li>
</ul>

---

## ✨ <span class="zh">今天的新魔法：def = 给代码起名字</span><span class="en">Today's new magic: def = name a piece of code</span>
{: #magic}

<div class="box box-think"><span class="zh">🥋 想象你在教海龟一个<b>招式</b>。<code>def square():</code> 是在说「听好，这个招式叫 square，内容是下面这几行」。<b>教的时候它不动</b>——直到你喊 <code>square()</code>，它才表演一次。</span><span class="en">🥋 Imagine teaching the turtle a <b>trick</b>. <code>def square():</code> says "listen, this trick is called square, and here's what it does". <b>Teaching doesn't move it</b> — only when you call <code>square()</code> does it perform.</span></div>

<div class="cmds">
  <div class="cmd"><code>def square():</code><span><span class="zh">教一个叫 square 的招式（最后有冒号！）</span><span class="en">Teach a trick called square (colon at the end!)</span></span></div>
  <div class="cmd"><code>    t.forward(80)</code><span><span class="zh">招式的内容要往右缩 4 格</span><span class="en">The trick's body is indented 4 spaces</span></span></div>
  <div class="cmd"><code>square()</code><span><span class="zh">喊名字 = 表演一次（调用）</span><span class="en">Call the name = perform once</span></span></div>
  <div class="cmd"><code>def square(size, colour):</code><span><span class="zh">括号里是参数：喊的时候递东西进去</span><span class="en">Inside the brackets: parameters you hand in</span></span></div>
  <div class="cmd"><code>return n * 2</code><span><span class="zh">把结果交回去（例 4）</span><span class="en">Hand a result back (Example 4)</span></span></div>
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
  <li><span class="zh">把最后三次 <code>square()</code> 删掉，换成一个 <code>for</code> 循环：喊 5 次 <code>square()</code>，每次之后转一下，<b>正好转一整圈</b>。转几度？自己算。</span><span class="en">Delete the last three <code>square()</code> calls and use a <code>for</code> loop instead: call <code>square()</code> 5 times, turning after each, so it makes <b>exactly one full turn</b>. How many degrees? Work it out.</span></li>
  <li><span class="zh">把 <code>def</code> 里的 <code>80</code> 改成 <code>120</code>——<b>只改一处</b>，所有正方形都变大了吗？这就是打包的好处！</span><span class="en">Change <code>80</code> to <code>120</code> inside <code>def</code> — <b>one edit</b>, did every square grow? That's the point of packing!</span></li>
  <li>🐞 <span class="zh">把 <code>def square():</code> 最后的冒号删掉，看报错说什么，再修好。</span><span class="en">Delete the colon after <code>def square():</code>, read the error, then fix it.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 第 1 个任务的提示</span><span class="en">💡 Hint for task 1</span></summary><span class="zh">一整圈是 360 度，分 5 次转：360 ÷ 5 = ？循环里两行：<code>square()</code> 和 <code>t.left(?)</code>。</span><span class="en">A full turn is 360 degrees, split into 5 turns: 360 ÷ 5 = ? Two lines in the loop: <code>square()</code> and <code>t.left(?)</code>.</span></details>

### 🧪 <span class="zh">例 2：带参数的招式——你说多大、什么颜色</span><span class="en">Example 2: a trick with parameters — you pick size and colour</span>

<p><span class="zh">喊 <code>square(60, "red")</code> 时，<b>60 会跑进 size，"red" 会跑进 colour</b>。括号里的名字叫<b>参数</b>，就像点餐时告诉厨师「要大份、辣的」。</span><span class="en">When you call <code>square(60, "red")</code>, <b>60 goes into size and "red" goes into colour</b>. Those names in the brackets are <b>parameters</b> — like telling the chef "large, spicy" when you order.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/square-params.py' | relative_url }}" data-title="🎨 例 2：square(size, colour)" data-title-en="🎨 Example 2: square(size, colour)" data-save="square-params" data-rows="12"></div>

<ul class="quests" data-key="l7-ex2">
  <li><span class="zh">🎯 <b>目标：</b>让 6 个正方形<b>一个比一个大</b>（30、40、50……）。现在的循环里没有数字可以用——你得自己改循环。</span><span class="en">🎯 <b>Goal:</b> make the 6 squares <b>each bigger than the last</b> (30, 40, 50…). The current loop has no number to use — you'll have to change the loop yourself.</span></li>
  <li><span class="zh">在 <code>colours</code> 列表里再加 2 个颜色。你的新循环还能自动画 8 个吗？不能的话，改到能为止。</span><span class="en">Add 2 more colours to the list. Does your new loop draw 8 by itself? If not, fix it until it does.</span></li>
  <li>🐞 <span class="zh">喊 <code>square(60)</code>（少给一个）会怎样？读读报错里的 <code>missing</code>。</span><span class="en">What happens with <code>square(60)</code> (one missing)? Read the word <code>missing</code> in the error.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">要一个会变大的数，就要 <code>for i in range(...)</code>。颜色可以用 <code>colours[i]</code> 拿（第 5 课）。</span><span class="en">For a number that grows you need <code>for i in range(...)</code>. Get the colour with <code>colours[i]</code> (Lesson 5).</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2</span><span class="en">💡 Hint 2</span></summary><span class="zh"><code>for i in range(len(colours)):</code> 然后 <code>square(30 + i * 10, colours[i])</code>。用 <code>len</code>，加颜色就不用改循环。</span><span class="en"><code>for i in range(len(colours)):</code> then <code>square(30 + i * 10, colours[i])</code>. With <code>len</code>, adding colours needs no loop change.</span></details>

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
  <li><span class="zh">给 <code>house</code> 加第 4 个参数 <code>colour</code>，用它给房子身体上色。记住：参数要<b>两头都加</b>——def 那头和喊的那头。</span><span class="en">Add a 4th parameter <code>colour</code> to <code>house</code> and use it for the body. Remember: parameters go on <b>both ends</b> — the def and the call.</span></li>
  <li><span class="zh">✍️ <b>自己写一个招式</b> <code>row(y, n)</code>：在高度 y 画 n 座房子。然后只用两行 <code>row(-150, 5)</code>、<code>row(20, 3)</code> 画出两排。这就是<b>招式里喊招式</b>！</span><span class="en">✍️ <b>Write your own trick</b> <code>row(y, n)</code>: draws n houses at height y. Then draw two rows with just <code>row(-150, 5)</code> and <code>row(20, 3)</code>. That's <b>a trick calling a trick</b>!</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 row 的提示</span><span class="en">💡 Hint for row</span></summary><span class="zh">把最下面那个 for 循环「搬进」<code>def row(y, n):</code> 里面（记得缩进），把 <code>range(5)</code> 换成 <code>range(n)</code>，把 <code>-100</code> 换成 <code>y</code>。</span><span class="en">Move the for loop at the bottom <b>inside</b> <code>def row(y, n):</code> (indent it), change <code>range(5)</code> to <code>range(n)</code> and <code>-100</code> to <code>y</code>.</span></details>

### 🔁 <span class="zh">例 4：return——招式做完，把结果「交回来」</span><span class="en">Example 4: return — the trick hands a result back</span>

<p><span class="zh">有的招式不画画，而是<b>算出一个答案</b>。<code>return</code> 就是「把答案交回去」，而且招式<b>马上结束</b>。交回来的东西可以 <code>print</code>，可以存进变量，可以放进 <code>if</code>，还可以<b>再递给另一个招式</b>。</span><span class="en">Some tricks don't draw — they <b>work out an answer</b>. <code>return</code> means "hand the answer back" and the trick <b>ends right there</b>. You can <code>print</code> the result, store it, use it in an <code>if</code>, or <b>hand it to another trick</b>.</span></p>

<div class="quiz" data-answer="1">
  <p class="q"><span class="zh">先读代码里的 <code>bigger(a, b)</code>。最后一行 <code>print(bigger(7, 12), bigger(double(7), 12))</code> 打印什么？</span><span class="en">Read <code>bigger(a, b)</code> in the code first. What does the last line <code>print(bigger(7, 12), bigger(double(7), 12))</code> print?</span></p>
  <div class="opts"><button>12 14</button><button>12 12</button><button>7 14</button><button>12 24</button></div>
  <div class="why"><span class="zh">第一个：7 不比 12 大，所以交回 b = 12。第二个：先算里面 <code>double(7)</code> = 14，再算 <code>bigger(14, 12)</code>，14 &gt; 12，交回 14。<b>先里面，再外面</b>。</span><span class="en">First: 7 isn't bigger than 12, so it returns b = 12. Second: inside first, <code>double(7)</code> = 14, then <code>bigger(14, 12)</code>; 14 &gt; 12, so 14. <b>Inside first, then outside</b>.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/07/code/return-demo.py' | relative_url }}" data-canvas="no" data-title="🔁 例 4：return" data-title-en="🔁 Example 4: return" data-save="return-demo" data-rows="14"></div>

<ul class="quests" data-key="l7-ex4">
  <li><span class="zh">运行前先在纸上写下 5 行输出，再运行对答案。全对吗？</span><span class="en">Before running, write the 5 output lines on paper, then run and check. All right?</span></li>
  <li><span class="zh">✍️ 照着说明<b>自己写</b>：<code>is_even(n)</code> 交回 True / False（双数是 True）。测试：<code>print(is_even(4), is_even(7))</code> 应该是 <code>True False</code>。</span><span class="en">✍️ <b>Write it yourself</b> from the spec: <code>is_even(n)</code> returns True / False (True for even numbers). Test: <code>print(is_even(4), is_even(7))</code> should give <code>True False</code>.</span></li>
  <li><span class="zh">✍️ 再写 <code>smallest(a, b, c)</code>：交回三个数里最小的。测试 <code>smallest(5, 2, 9)</code>、<code>smallest(3, 3, 8)</code>、<code>smallest(7, 6, 1)</code>。</span><span class="en">✍️ Then write <code>smallest(a, b, c)</code>: returns the smallest of three numbers. Test <code>smallest(5, 2, 9)</code>, <code>smallest(3, 3, 8)</code>, <code>smallest(7, 6, 1)</code>.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 is_even 提示</span><span class="en">💡 is_even hint</span></summary><span class="zh">第 4 课的 <code>%</code>：双数除以 2 余 0。<code>n % 2 == 0</code> 本身就是 True 或 False——直接 return 它，不用写 if！</span><span class="en">Lesson 4's <code>%</code>: even numbers leave remainder 0 when divided by 2. <code>n % 2 == 0</code> is already True or False — just return it, no if needed!</span></details>
<details class="hint"><summary><span class="zh">💡 smallest 提示</span><span class="en">💡 smallest hint</span></summary><span class="zh">方法 1：<code>if a &lt;= b and a &lt;= c: return a</code>，再判断 b，剩下的就是 c。方法 2（更酷）：<b>用两次</b>一个「两个里挑小的」招式。</span><span class="en">Way 1: <code>if a &lt;= b and a &lt;= c: return a</code>, then check b, and what's left is c. Way 2 (cooler): use a "smaller of two" trick <b>twice</b>.</span></details>

<div class="box box-tip"><span class="box-title"><span class="zh">🔍 小秘密：函数里的变量只住在函数里</span><span class="en">🔍 Secret: variables inside a function live only inside</span></span>
<span class="zh">参数和在函数里新建的变量，是函数的「私人物品」。<b>就算名字一样</b>，里面的 fuel 和外面的 fuel 也是两个不同的盒子。</span><span class="en">Parameters and variables made inside a function are its "private things". <b>Even with the same name</b>, the fuel inside and the fuel outside are two different boxes.</span></div>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">先读下面画板里的代码（别运行！）。最后三行打印的 fuel、x、y 是多少？</span><span class="en">Read the code in the playground below (don't run it!). What are fuel, x and y in the last three lines?</span></p>
  <div class="opts"><button>6, 7, 15</button><button>3, 7, 15</button><button>3, 7, 7</button><button>3, 6, 12</button></div>
  <div class="why"><span class="zh"><code>boost(3)</code>：里面的 fuel 变成 6，交回 6 + 1 = 7，所以 x = 7。<code>boost(7)</code>：7 × 2 + 1 = 15。外面的 fuel 一直是 <b>3</b>——函数改的是它自己的 fuel。</span><span class="en"><code>boost(3)</code>: the inside fuel becomes 6, it returns 6 + 1 = 7, so x = 7. <code>boost(7)</code>: 7 × 2 + 1 = 15. The outside fuel stays <b>3</b> — the function only changed its own fuel.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/07/code/scope.py' | relative_url }}" data-canvas="no" data-title="🔍 函数里的 fuel 和外面的 fuel" data-title-en="🔍 fuel inside vs fuel outside" data-save="scope-demo" data-rows="10"></div>

---

## 🚀 <span class="zh">例 5（进阶）：发射控制中心</span><span class="en">Example 5 (stretch): launch control</span>
{: #launch}

<p><span class="zh">真正的程序员最爱这样用函数：<b>每个小问题一个招式</b>，再用一个大招式把它们拼起来。这个例子里藏着 3 个新本领：</span><span class="en">Real programmers love using functions like this: <b>one small trick per small question</b>, then one big trick that combines them. Three new skills are hiding in this example:</span></p>

<ol class="code-walk">
  <li><code>return fuel &gt;= 90</code><span><span class="zh">交回 True / False，可以直接放进 <code>if</code></span><span class="en">returns True / False, goes straight into an <code>if</code></span></span></li>
  <li><code>def countdown(start=10):</code><span><span class="zh"><b>默认值</b>：喊 <code>countdown()</code> 不递东西，start 就是 10</span><span class="en"><b>default value</b>: call <code>countdown()</code> with nothing and start is 10</span></span></li>
  <li><code>return numbers</code><span><span class="zh">交回<b>一整个列表</b>，外面可以用 <code>for</code> 一个一个拿</span><span class="en">hands back <b>a whole list</b>; outside, a <code>for</code> can take the items one by one</span></span></li>
</ol>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh"><code>print(len(countdown()))</code>——括号里什么都没递，会怎样？</span><span class="en"><code>print(len(countdown()))</code> — nothing is handed in. What happens?</span></p>
  <div class="opts"><button><span class="zh">打印 0</span><span class="en">Prints 0</span></button><button><span class="zh">打印 10</span><span class="en">Prints 10</span></button><button><span class="zh">报错：少了一个参数</span><span class="en">Error: missing an argument</span></button></div>
  <div class="why"><span class="zh">start 有默认值 10，所以 <code>countdown()</code> 交回 [10, 9, …, 1]，一共 10 个数。如果 def 里写的是 <code>countdown(start)</code>（没有 =10），才会报 missing。</span><span class="en">start defaults to 10, so <code>countdown()</code> returns [10, 9, …, 1] — 10 numbers. Only if the def said <code>countdown(start)</code> (no =10) would it say missing.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/07/code/launch.py' | relative_url }}" data-canvas="no" data-title="🚀 例 5：发射控制中心" data-title-en="🚀 Example 5: launch control" data-save="launch-control" data-draft="l7-launch" data-rows="16"></div>

<ul class="quests" data-key="l7-launch">
  <li><span class="zh">把 <code>wind = 8</code> 改成能让发射<b>推迟</b>的数。再改 fuel，让它因为<b>另一个原因</b>推迟。</span><span class="en">Change <code>wind = 8</code> so the launch is <b>scrubbed</b>. Then change fuel so it's scrubbed for <b>a different reason</b>.</span></li>
  <li><span class="zh">✍️ 写 <code>crew_ok(crew)</code>：宇航员人数在 1 到 4 之间（包括 1 和 4）才交回 True。再把它加进 <code>go_for_launch</code>（要加第 3 个参数）。</span><span class="en">✍️ Write <code>crew_ok(crew)</code>: True only if the crew is from 1 to 4 (1 and 4 included). Then add it into <code>go_for_launch</code> (it needs a 3rd parameter).</span></li>
  <li><span class="zh">✍️ 给 <code>countdown</code> 再加一个默认参数 <code>step=1</code>，让 <code>countdown(10, 2)</code> 交回 <code>[10, 8, 6, 4, 2]</code>，而 <code>countdown(3)</code> 还是 <code>[3, 2, 1]</code>。</span><span class="en">✍️ Give <code>countdown</code> another default parameter <code>step=1</code> so <code>countdown(10, 2)</code> returns <code>[10, 8, 6, 4, 2]</code> while <code>countdown(3)</code> is still <code>[3, 2, 1]</code>.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 crew_ok 提示</span><span class="en">💡 crew_ok hint</span></summary><span class="zh"><code>return crew &gt;= 1 and crew &lt;= 4</code>。然后 <code>def go_for_launch(fuel, wind, crew):</code> 里多一个 <code>and crew_ok(crew)</code>——别忘了下面喊它的地方也要多递一个数！</span><span class="en"><code>return crew &gt;= 1 and crew &lt;= 4</code>. Then <code>def go_for_launch(fuel, wind, crew):</code> gets an extra <code>and crew_ok(crew)</code> — and don't forget to hand in one more number where it's called!</span></details>
<details class="hint"><summary><span class="zh">💡 step 提示</span><span class="en">💡 step hint</span></summary><span class="zh"><code>def countdown(start=10, step=1):</code>，循环里把 <code>n -= 1</code> 改成 <code>n -= step</code>。</span><span class="en"><code>def countdown(start=10, step=1):</code>, and in the loop change <code>n -= 1</code> to <code>n -= step</code>.</span></details>

---

## 🏙️ <span class="zh">例 6：火箭小镇——街道招式你自己写</span><span class="en">Example 6: rocket town — you write the street trick</span>
{: #town}

<p><span class="zh"><code>house</code>、<code>tree</code>、<code>rocket</code> 都写好了（看看 <code>rocket</code> 的 <code>size=120</code> 默认值！）。这次<b>没有填空</b>：照着代码里的说明，自己写 <code>street(n, y)</code>，再把最下面的两行喊出来。</span><span class="en"><code>house</code>, <code>tree</code> and <code>rocket</code> are ready (look at <code>rocket</code>'s default <code>size=120</code>!). This time there are <b>no blanks</b>: follow the instructions in the code, write <code>street(n, y)</code> yourself, then switch on the two calls at the bottom.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/town.py' | relative_url }}" data-title="🏙️ 例 6：火箭小镇" data-title-en="🏙️ Example 6: rocket town" data-save="my-town" data-draft="l7-town" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">骨架：<code>def street(n, y):</code> → 里面一个 <code>for i in range(n):</code> → 里面喊一次 <code>house(...)</code>。x 怎么随 i 变？看例 3。</span><span class="en">Skeleton: <code>def street(n, y):</code> → inside, <code>for i in range(n):</code> → inside that, one <code>house(...)</code> call. How does x change with i? See Example 3.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：i % len(colours) 是什么？</span><span class="en">💡 Hint 2: what is i % len(colours)?</span></summary><span class="zh">只有 4 个颜色，第 5 座房子（i = 4）怎么办？<code>4 % 4 = 0</code>，又从第一个颜色开始——颜色<b>轮流</b>用，永远不会超出列表。</span><span class="en">There are only 4 colours, so what about house 5 (i = 4)? <code>4 % 4 = 0</code>, back to the first colour — colours are used <b>in turn</b> and never run off the end of the list.</span></details>

### 🏆 <span class="zh">挑战：我的太空小镇</span><span class="en">Challenge: my space town</span>

<p><span class="zh">这次有 5 条规则（写在画板最上面）：<b>≥ 4 个自己写的招式</b>、≥ 1 个<b>默认值</b>、≥ 1 个会 <b>return</b> 而且结果真的被用上、≥ 1 个<b>招式里喊招式</b>、用 <code>for</code> 喊招式。发射台、星星、卫星、月亮……满意了就 <b>📤 存到作品墙</b>！</span><span class="en">5 rules this time (at the top of the playground): <b>≥ 4 tricks you wrote</b>, ≥ 1 <b>default value</b>, ≥ 1 trick that <b>returns</b> something that really gets used, ≥ 1 <b>trick calling a trick</b>, and tricks called from a <code>for</code>. Launch pad, stars, satellites, a moon… Happy with it? <b>📤 Save to Gallery</b>!</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/challenge.py' | relative_url }}" data-title="🏆 挑战：我的太空小镇" data-title-en="🏆 Challenge: my space town" data-save="my-town-challenge" data-draft="l7-challenge" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 星空怎么画？</span><span class="en">💡 How to draw a starry sky?</span></summary><span class="zh"><code>def stars(n, colour="white"):</code> → <code>for</code> 循环 n 次 → <code>t.penup()</code>、<code>t.goto(random.randint(-300, 300), random.randint(0, 280))</code>、<code>t.dot(4, colour)</code>。一个招式就同时用上了默认值和 for！</span><span class="en"><code>def stars(n, colour="white"):</code> → loop n times → <code>t.penup()</code>, <code>t.goto(random.randint(-300, 300), random.randint(0, 280))</code>, <code>t.dot(4, colour)</code>. One trick that uses a default value and a for!</span></details>
<details class="hint"><summary><span class="zh">💡 「招式里喊招式」想不出来？</span><span class="en">💡 Can't think of "a trick calling a trick"?</span></summary><span class="zh">写一个 <code>launch_pad(x, y)</code>：先画一个灰色的长方形平台，然后在平台上<b>喊 rocket</b>。或者 <code>town()</code> 一个招式喊所有其他招式。</span><span class="en">Write <code>launch_pad(x, y)</code>: draw a grey rectangle platform, then <b>call rocket</b> on top of it. Or a <code>town()</code> trick that calls all the others.</span></details>

---

## 🤖 <span class="zh">和 AI 一起：让 AI 帮你打包</span><span class="en">With AI: let AI pack your code</span>

<p><span class="zh">AI 很擅长「把重复的代码改成函数」。但规则不变：<b>AI 给的每一行，你都要看懂，而且要运行了才算数</b>。</span><span class="en">AI is great at "turn this repeated code into a function". The rule stays: <b>understand every line AI gives you, and it only counts once it runs</b>.</span></p>

<div class="chat">
  <div class="bubble me"><span class="zh">😃 我是小学生，正在学 Python turtle。下面的代码画了 3 次一样的三角形（贴代码）。请把它改成一个有参数的函数，其中一个参数要有<b>默认值</b>，然后<b>一行一行解释</b>你改了什么。只用 turtle。</span><span class="en">😃 I'm a kid learning Python turtle. This code draws the same triangle 3 times (paste code). Please turn it into a function with parameters, one of them with a <b>default value</b>, and <b>explain line by line</b> what you changed. Only use turtle.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">好的！<code>def triangle(x, y, size=60):</code> …（然后它解释每一行）</span><span class="en">Sure! <code>def triangle(x, y, size=60):</code> … (then it explains each line)</span></div>
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
  <div class="k"><b><span class="zh">参数</span><span class="en">parameters</span></b><code>def house(x, y, size):
    ...
house(-100, 0, 80)</code><span><span class="zh">喊的时候按顺序递进去。</span><span class="en">Handed in, in order, when you call.</span></span></div>
  <div class="k"><b>return <span class="zh">交回结果</span><span class="en">hand back</span></b><code>def double(n):
    return n * 2
x = double(double(5))   # 20</code><span><span class="zh">可以存、print、放进 if、再递给别的招式。</span><span class="en">Store it, print it, use it in an if, or hand it on.</span></span></div>
  <div class="k"><b><span class="zh">交回 True / False</span><span class="en">return True / False</span></b><code>def fuel_ok(fuel):
    return fuel >= 90
if fuel_ok(95):
    print("go!")</code><span><span class="zh">问题招式直接放进 if。</span><span class="en">A question-trick goes straight into an if.</span></span></div>
  <div class="k"><b><span class="zh">默认值</span><span class="en">default values</span></b><code>def countdown(start=10):
    ...
countdown()     # start = 10
countdown(3)    # start = 3</code><span><span class="zh">不递东西就用默认值。</span><span class="en">Nothing handed in → the default is used.</span></span></div>
  <div class="k"><b><span class="zh">招式里喊招式</span><span class="en">tricks calling tricks</span></b><code>def street(n, y):
    for i in range(n):
        house(i * 120, y, 80)</code><span><span class="zh">大问题 = 几个小招式拼起来。</span><span class="en">Big problem = small tricks combined.</span></span></div>
  <div class="k"><b><span class="zh">交回列表</span><span class="en">return a list</span></b><code>def evens(n):
    result = []
    for i in range(n):
        result.append(i * 2)
    return result</code><span><span class="zh">一次交回很多东西。</span><span class="en">Hand back lots of things at once.</span></span></div>
  <div class="k"><b><span class="zh">里面的变量</span><span class="en">local variables</span></b><code>def boost(fuel):
    fuel = fuel * 2   # 只改里面的 / inside only
    return fuel + 1</code><span><span class="zh">函数里的变量外面看不到，也改不到外面。</span><span class="en">Inside variables can't be seen — or change anything — outside.</span></span></div>
</div>

<p><span class="zh">全部指令在 <a href="{{ '/cheatsheet/' | relative_url }}#l07">📖 小词典 · 第 7 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l07">📖 cheat sheet · Lesson 7</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/07/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
