---
title: 第 11 课 · 学一学
title_en: Lesson 11 · Learn
lesson: "11"
tab: learn
playground: true
---

# 🛠️ <span class="zh">第 11 课：排错工具箱 + 让任务动起来</span><span class="en">Lesson 11: The debugging toolbox + bringing your mission to life</span>

<p class="zh">今天没有新的「大语法」。今天学的是工程师<b>每天都在用</b>的本事：<b>bug 不会自己消失，但有办法把它找出来。</b>然后，用键盘和「游戏心跳」让你的太空任务动起来，并且把它做完。</p>
<p class="en">No big new syntax today. Today is about the skill engineers <b>use every single day</b>: <b>bugs don't vanish on their own, but there are ways to hunt them down.</b> Then we'll use keys and the "game heartbeat" to bring your space mission to life — and finish it.</p>

---

## 🔁 <span class="zh">热身：治好 3 个 bug</span><span class="en">Warm-up: cure 3 bugs</span>
{: #warmup}

<p><span class="zh">这段加燃料的程序生病了，一共 <b>3 个 bug</b>。它想打印两行：「猎鹰 9 号 加了 3 次燃料」和「可以发射！」。先<b>读</b>，再运行，一次治一个。全治好会 🏆！</span><span class="en">This refuelling program is sick with <b>3 bugs</b>. It should print two lines: "猎鹰 9 号 加了 3 次燃料" and "可以发射！". <b>Read</b> first, then run, fix one at a time. Cure them all for a 🏆!</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/warmup-bugs.py' | relative_url }}" data-canvas="no" data-title="🐞 三个 bug" data-title-en="🐞 Three bugs" data-save="three-bugs" data-draft="l11-warmup" data-expect="猎鹰 9 号 加了 3 次燃料\n可以发射！" data-badge="lesson-11-warmup" data-rows="12"></div>

<ul class="quests" data-key="l11-warmup">
  <li>🐞 <span class="zh">Bug 1：运行，读红框。<code>for</code> 那一行少了什么？</span><span class="en">Bug 1: run it, read the red box. What's missing on the <code>for</code> line?</span></li>
  <li>🐞 <span class="zh">Bug 2：又报错了？电脑说它<b>不认识一个名字</b>。和上面的变量名对一对，哪两个字母换了位置？</span><span class="en">Bug 2: another error? The computer <b>doesn't know a name</b>. Compare it with the variable above — which two letters swapped places?</span></li>
  <li>🐞 <span class="zh">Bug 3：「是不是等于」要用<b>两个</b>等号。</span><span class="en">Bug 3: "is it equal to" needs <b>two</b> equals signs.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 全部答案（先自己试！）</span><span class="en">💡 All answers (try first!)</span></summary><span class="zh">① <code>for i in range(3):</code> 最后要有冒号 ② <code>rokcet</code> → <code>rocket</code> ③ <code>if fuel == 3:</code></span><span class="en">① <code>for i in range(3):</code> needs a colon ② <code>rokcet</code> → <code>rocket</code> ③ <code>if fuel == 3:</code></span></details>

<div class="box box-good"><span class="zh">🎯 注意到了吗？电脑<b>一次只报一个错</b>。修好一个，再运行，它才告诉你下一个。这就是排错的节奏：<b>运行 → 读 → 修 → 再运行</b>。</span><span class="en">🎯 Did you notice? The computer <b>reports one error at a time</b>. Fix one, run again, and it tells you the next. That's the rhythm of debugging: <b>run → read → fix → run again</b>.</span></div>

---

## 🧰 <span class="zh">排错工具箱：4 招</span><span class="en">The debugging toolbox: 4 tricks</span>
{: #toolbox}

<div class="flow">
  <div class="f"><span class="e">🔍</span><b><span class="zh">print 侦探</span><span class="en">print detective</span></b><small><span class="zh">没报错但答案不对</span><span class="en">no error, wrong answer</span></small></div>
  <div class="f"><span class="e">📜</span><b><span class="zh">读报错</span><span class="en">Read the traceback</span></b><small><span class="zh">有红字的时候</span><span class="en">when there's red text</span></small></div>
  <div class="f"><span class="e">🦆</span><b><span class="zh">小黄鸭</span><span class="en">Rubber duck</span></b><small><span class="zh">念出来就发现了</span><span class="en">say it out loud</span></small></div>
  <div class="f"><span class="e">✂️</span><b><span class="zh">二分法</span><span class="en">Halving</span></b><small><span class="zh">程序太长不知道从哪看</span><span class="en">too long to know where to look</span></small></div>
</div>

### 🔍 <span class="zh">第 1 招：print 侦探</span><span class="en">Trick 1: the print detective</span>

<p><span class="zh">没有红字，但答案不对——这是最难的 bug。侦探的办法：在怀疑的地方<b>塞一行 <code>print</code></b>，让程序把它心里想的数字「说出来」。</span><span class="en">No red text, but the answer is wrong — the hardest kind of bug. The detective's trick: <b>stick a <code>print</code></b> where you're suspicious, so the program "says out loud" what it's thinking.</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">助推器有 100 份燃料，点火 3 次用掉 30、25、20。下面的程序会打印剩多少？</span><span class="en">The booster has 100 fuel and burns 30, 25 and 20. What will the program below print?</span></p>
  <div class="opts"><button>25</button><button>80</button><button>100</button></div>
  <div class="why"><span class="zh">80！因为 <code>fuel = 100 - burn</code> 每一圈都<b>从 100 重新算</b>，前面用掉的全忘了，最后只剩 100 − 20。</span><span class="en">80! Because <code>fuel = 100 - burn</code> <b>starts again from 100</b> every round, forgetting the earlier burns, so it ends at 100 − 20.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/11/code/detective.py' | relative_url }}" data-canvas="no" data-title="🔍 print 侦探" data-title-en="🔍 print detective" data-save="print-detective" data-draft="l11-detective" data-expect="剩余燃料 25" data-badge="lesson-11-detective" data-rows="10"></div>

<ul class="quests" data-key="l11-detective">
  <li><span class="zh">在 <code>fuel = 100 - burn</code> 的<b>下面</b>加一行 <code>print("现在 fuel 是", fuel)</code>（缩进一样）。运行，看每一圈 fuel 是多少。</span><span class="en">Add <code>print("now fuel is", fuel)</code> <b>under</b> <code>fuel = 100 - burn</code> (same indentation). Run and watch fuel each round.</span></li>
  <li><span class="zh">看出问题了吗？把那一行改对，让它打印「剩余燃料 25」。</span><span class="en">See the problem? Fix that line so it prints "剩余燃料 25".</span></li>
  <li><span class="zh">修好以后，把侦探 print 删掉（或者加 <code>#</code> 变成注释）。</span><span class="en">When it works, delete the detective print (or turn it into a comment with <code>#</code>).</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">「在上次的基础上减」要写 <code>fuel = fuel - burn</code>（第 2 课的变量魔法！）。</span><span class="en">"Subtract from what's left" is <code>fuel = fuel - burn</code> (variable magic from Lesson 2!).</span></details>

<div class="box box-warn"><span class="box-title"><span class="zh">🧊 游戏突然停住，却没有红字？</span><span class="en">🧊 The game suddenly freezes with no red text?</span></span>
<span class="zh">游戏开始以后，<code>tick()</code> 是被定时器叫的。如果 <code>tick()</code> 里出了错，画板有时<b>来不及显示红字</b>，游戏就停住不动了。这时候请出侦探：在 <code>tick()</code> 里每隔几行塞一个 <code>print("到这里了 1")</code>、<code>print("到这里了 2")</code>……看最后打印的是几号，bug 就在它后面。</span>
<span class="en">Once a game is running, <code>tick()</code> is called by the timer. If something goes wrong inside <code>tick()</code>, the playground sometimes <b>can't show the red box</b>, so the game just freezes. Call the detective: put <code>print("got here 1")</code>, <code>print("got here 2")</code>… every few lines in <code>tick()</code>. The last number printed tells you the bug is right after it.</span>
</div>

### 📜 <span class="zh">第 2 招：把报错当地图读</span><span class="en">Trick 2: read the error like a map</span>

<p><span class="zh">红字不是骂你，是一张<b>藏宝图</b>。先运行下面的程序，<b>别改</b>，我们一起读。</span><span class="en">Red text isn't telling you off — it's a <b>treasure map</b>. Run the program below, <b>don't fix it yet</b>, and let's read it together.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/traceback.py' | relative_url }}" data-canvas="no" data-title="📜 读报错" data-title-en="📜 Read the error" data-save="read-error" data-draft="l11-traceback" data-rows="9"></div>

<ol class="code-walk">
  <li><code>🐞 第 9 行出了个小问题</code><span><span class="zh"><b>先看行号</b>。画板已经帮你把那一行标红了。</span><span class="en"><b>Line number first</b>. The playground has already marked that line red.</span></span></li>
  <li><code>IndexError</code><span><span class="zh"><b>错误的种类</b>。Index = 位置。「位置错误」= 你要的位置不存在。</span><span class="en"><b>The kind of error</b>. Index = position. "Position error" = the spot you asked for doesn't exist.</span></span></li>
  <li><code>list index out of range</code><span><span class="zh"><b>电脑的原话</b>：列表的位置超出范围。3 级火箭的位置是 0、1、2，没有 3！</span><span class="en"><b>The computer's words</b>: list position out of range. 3 stages live at 0, 1, 2 — there's no 3!</span></span></li>
  <li><code>stages[3]</code><span><span class="zh"><b>看那一行的代码</b>，找到和错误种类有关的东西。</span><span class="en"><b>Look at that line</b> and find the part that matches the error kind.</span></span></li>
</ol>

<div class="table-wrap">
<table>
<tr><th><span class="zh">错误种类</span><span class="en">Error kind</span></th><th><span class="zh">它在说</span><span class="en">It means</span></th><th><span class="zh">先检查</span><span class="en">Check first</span></th></tr>
<tr><td><code>NameError</code></td><td><span class="zh">不认识这个名字</span><span class="en">Unknown name</span></td><td><span class="zh">拼写、大小写、引号、有没有先创建</span><span class="en">Spelling, capitals, quotes, created yet?</span></td></tr>
<tr><td><code>SyntaxError</code></td><td><span class="zh">看不懂这一行的写法</span><span class="en">Can't read this line</span></td><td><span class="zh">冒号、括号成对、引号成对、上一行</span><span class="en">Colon, matching brackets and quotes, the line above</span></td></tr>
<tr><td><code>IndentationError</code></td><td><span class="zh">前面的空格不对</span><span class="en">Wrong spaces at the start</span></td><td><span class="zh">for / if / def 下面要缩 4 格</span><span class="en">4 spaces under for / if / def</span></td></tr>
<tr><td><code>TypeError</code></td><td><span class="zh">东西的种类搞混了</span><span class="en">Mixed-up kinds</span></td><td><span class="zh">文字和数字混在一起？用 f-string 或 int()</span><span class="en">Text mixed with numbers? Use f-string or int()</span></td></tr>
<tr><td><code>IndexError</code> / <code>KeyError</code></td><td><span class="zh">列表 / 字典里没有这个</span><span class="en">List / dict doesn't have it</span></td><td><span class="zh">第一个是 [0]；键拼对了吗</span><span class="en">First is [0]; key spelled right?</span></td></tr>
<tr><td><code>UnboundLocalError</code></td><td><span class="zh">函数里改了外面的变量</span><span class="en">Changed an outside variable inside a function</span></td><td><span class="zh">函数第一行加 <code>global 名字</code>（下面讲）</span><span class="en">Add <code>global name</code> as the function's first line (see below)</span></td></tr>
</table>
</div>

<ul class="quests" data-key="l11-traceback">
  <li><span class="zh">现在修好它：要么删掉第 9 行，要么往列表里加第 4 级。</span><span class="en">Now fix it: delete line 9, or add a 4th stage to the list.</span></li>
  <li><span class="zh">把这张表抄一行到你的<a href="{{ '/notebook/' | relative_url }}">笔记本</a>「我遇到过的报错」里。</span><span class="en">Copy one row of this table into the "Errors I've met" part of your <a href="{{ '/notebook/' | relative_url }}">notebook</a>.</span></li>
</ul>

#### 🧭 <span class="zh">进阶：标红的那一行，不一定是 bug 住的地方</span><span class="en">Advanced: the red line isn't always where the bug lives</span>

<p><span class="zh">项目里的代码都在<b>函数</b>里。函数出错时，红字标的是「<b>在哪里坏的</b>」，但 bug 常常是<b>别人交给它的东西</b>不对。运行下面的程序（随便输一个数），然后问自己：「这个值是<b>从哪来的</b>？」顺着它往回找。</span><span class="en">Project code lives in <b>functions</b>. When a function fails, the red line shows <b>where it broke</b> — but often the bug is <b>what was handed to it</b>. Run this (type any number), then ask: "where did this value <b>come from</b>?" and follow it backwards.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/traceback2.py' | relative_url }}" data-canvas="no" data-title="🧭 顺着报错往回找" data-title-en="🧭 Follow the error backwards" data-save="follow-error" data-draft="l11-traceback2" data-rows="12"></div>

<ul class="quests" data-key="l11-traceback2">
  <li><span class="zh">红框标的是第几行？它在哪个函数里？</span><span class="en">Which line is marked red? Which function is it in?</span></li>
  <li><span class="zh">TypeError 说 <code>'&lt;=' not supported between 'str' and 'int'</code>：哪个东西是 <code>str</code>（文字）？在函数里加一行 <code>print("speed 是", speed, type(speed))</code> 当侦探。</span><span class="en">TypeError says <code>'&lt;=' not supported between 'str' and 'int'</code>: which thing is a <code>str</code> (text)? Add <code>print("speed is", speed, type(speed))</code> inside the function as a detective.</span></li>
  <li><span class="zh">往回找：<code>speed</code> 是哪一行交进函数的？它又是从哪一行来的？在<b>那里</b>修好（第 2 课的老朋友）。</span><span class="en">Go backwards: which line hands <code>speed</code> to the function? Where did it come from before that? Fix it <b>there</b> (an old friend from Lesson 2).</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh"><code>input()</code> 给的永远是文字。把那一行改成 <code>speed = int(input(…))</code>。函数本身没有错——这就是「报错在 A，bug 在 B」。</span><span class="en"><code>input()</code> always gives text. Change that line to <code>speed = int(input(…))</code>. The function itself was fine — "the error is at A, the bug is at B".</span></details>

### 🦆 <span class="zh">第 3 招：小黄鸭法</span><span class="en">Trick 3: the rubber duck</span>

<p><span class="zh">真的有程序员在桌上放一只橡皮小黄鸭 🦆。卡住的时候，<b>把代码一行一行念给鸭子听</b>，解释它在干嘛。神奇的是：念到一半，你自己就会「啊！」一声发现问题。因为<b>说出来</b>比<b>看</b>更认真。</span><span class="en">Real programmers keep a rubber duck 🦆 on their desk. When stuck, <b>explain the code to the duck line by line</b>. The magic: halfway through you go "oh!" and spot the problem yourself, because <b>saying it</b> is more careful than <b>looking</b>.</span></p>

<p><span class="zh">这个着陆模拟器没有报错，但结果怪怪的。试 3 次：速度 1、5、2。然后念给鸭子听。</span><span class="en">This landing simulator has no error, but the results feel wrong. Try 3 landings: speed 1, 5, 2. Then explain it to the duck.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/duck.py' | relative_url }}" data-canvas="no" data-title="🦆 念给鸭子听" data-title-en="🦆 Tell the duck" data-save="duck-landing" data-draft="l11-duck" data-rows="12"></div>

<ul class="quests" data-key="l11-duck">
  <li><span class="zh">速度 1 的时候，程序说什么？这句话对吗？</span><span class="en">At speed 1, what does it say? Is that right?</span></li>
  <li><span class="zh">念给鸭子（或者老师、家人）：「如果 speed 比 MAX_SPEED <b>大</b>，就说……」念到这里你发现了吗？</span><span class="en">Tell the duck (or the teacher, or family): "If speed is <b>bigger</b> than MAX_SPEED, say…" — did you spot it?</span></li>
  <li><span class="zh">修好它。有两种修法，你能想出两种吗？速度刚好是 2 的时候对不对？（边界测试！）</span><span class="en">Fix it. There are two ways — can you find both? Is speed exactly 2 right? (Edge test!)</span></li>
</ul>

<div class="box box-tip"><span class="box-title"><span class="zh">🤖 没有鸭子？AI 也可以当鸭子</span><span class="en">🤖 No duck? AI can be the duck</span></span>
<span class="zh">复制下面的话发给 AI（注意：是<b>你</b>解释，AI 只负责听和提问）：</span><span class="en">Copy this to the AI (note: <b>you</b> explain, the AI only listens and asks):</span>
<pre class="zh" style="white-space:pre-wrap;margin:.5em 0">我在排错。我会一行一行解释我的代码，请你当小黄鸭：只问我问题，不要告诉我答案。
我的代码：
（粘贴代码）
第 1 行：…</pre>
<pre class="en" style="white-space:pre-wrap;margin:.5em 0">I'm debugging. I'll explain my code line by line. Please be my rubber duck: only ask me questions, don't tell me the answer.
My code:
(paste the code)
Line 1: …</pre>
<button class="pg-btn copy-prev">📋 <span class="zh">复制</span><span class="en">Copy</span></button>
</div>

### ✂️ <span class="zh">第 4 招：二分法</span><span class="en">Trick 4: halving (binary search)</span>

<p><span class="zh">程序很长，画出来不对，不知道从哪看起？<b>把后一半注释掉</b>（每行前面加 <code>#</code>），运行：前一半对吗？对，问题在后一半；不对，问题在前一半。再把那一半分两半……像猜数字一样，几次就找到了。</span><span class="en">Long program, wrong picture, no idea where to look? <b>Comment out the second half</b> (put <code>#</code> in front of each line) and run: is the first half right? If yes, the problem is in the second half; if no, in the first. Halve again… like guess-the-number, a few rounds finds it.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/bisect.py' | relative_url }}" data-title="✂️ 二分法找 bug" data-title-en="✂️ Halving" data-save="bisect-rocket" data-draft="l11-bisect" data-rows="14"></div>

<ul class="quests" data-key="l11-bisect">
  <li><span class="zh">运行一次。箭身、尖头、尾翼、火焰，哪个画错了？</span><span class="en">Run it once. Body, nose cone, fins, flame — which one is wrong?</span></li>
  <li><span class="zh">把「第 3、4 部分」全部加 <code>#</code>，再运行。错误还在吗？在 → 问题在第 1 或第 2 部分。</span><span class="en">Put <code>#</code> on all of "Parts 3 and 4" and run. Still wrong? Yes → the problem is in part 1 or 2.</span></li>
  <li><span class="zh">再把「第 2 部分」也注释掉。现在剩下的都对了？那 bug 就在第 2 部分。盯着那几行找：转弯是不是转反了？修好，再把所有 <code>#</code> 去掉。</span><span class="en">Now comment out "Part 2" too. Is what's left all correct? Then the bug is in part 2. Stare at those lines: are the turns going the wrong way? Fix it, then remove all the <code>#</code>s.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">尖头要从左上角出发，朝右走，然后<b>往上</b>拐。第 2 部分里的两个 <code>t.right(120)</code> 都应该是 <code>t.left(120)</code>。</span><span class="en">The nose cone starts at the top-left corner, goes right, then turns <b>upwards</b>. Both <code>t.right(120)</code> lines in part 2 should be <code>t.left(120)</code>.</span></details>

---

## 🎮 <span class="zh">游戏专用魔法：让任务「活」起来</span><span class="en">Game magic: bringing your mission to life</span>
{: #events}

<p><span class="zh">到现在为止，程序都是「从上跑到下，然后结束」。游戏不一样：程序要<b>等着</b>你按键、要<b>自己一拍一拍地动</b>。这就是「事件」。你的骨架里已经用了它们——现在来真正弄懂。</span><span class="en">Until now, programs "run top to bottom and stop". Games are different: the program must <b>wait</b> for your keys and <b>move by itself, beat by beat</b>. These are "events". Your skeleton already uses them — now let's really understand them.</span></p>

<div class="cmds">
  <div class="cmd"><code>screen = turtle.Screen()</code><span><span class="zh">拿到「屏幕」，事件都挂在它身上</span><span class="en">Get the "screen"; events hang on it</span></span></div>
  <div class="cmd"><code>screen.onkey(函数, "Up")</code><span><span class="zh">按 ↑ 就叫这个函数（注意：写函数名，<b>不加括号</b>）</span><span class="en">Press ↑ to call this function (function name, <b>no brackets</b>)</span></span></div>
  <div class="cmd"><code>screen.listen()</code><span><span class="zh">开始听键盘（忘了这行按键没反应）</span><span class="en">Start listening (forget this and keys do nothing)</span></span></div>
  <div class="cmd"><code>screen.ontimer(函数, 50)</code><span><span class="zh">50 毫秒后叫一次函数——函数里再叫一次，就成了心跳</span><span class="en">Call the function after 50 ms; call it again inside → a heartbeat</span></span></div>
  <div class="cmd"><code>global fuel</code><span><span class="zh">函数里要改外面的变量，先写这一行</span><span class="en">To change an outside variable inside a function, write this first</span></span></div>
</div>

<div class="box box-warn"><span class="box-title"><span class="zh">⚠️ 网页画板的三条规矩</span><span class="en">⚠️ Three rules for the web playground</span></span>
<span class="zh">① 用 <code>onkey</code>，不用 <code>onkeypress</code>（画板会自动帮你换，但电脑上的 Python 两个都行）。② 运行后<b>先点一下画布</b>，键盘才会被听到。③ 主程序跑完以后游戏还在跑，画板会显示「🎮 游戏开始了」；玩完点 <b>■ 结束游戏</b>。</span>
<span class="en">① Use <code>onkey</code>, not <code>onkeypress</code> (the playground swaps it for you; on a computer both work). ② After running, <b>click the canvas first</b> so keys are heard. ③ The game keeps going after the main program ends — the playground shows "🎮 Game on!"; click <b>■ End game</b> when done.</span>
</div>

### ⌨️ <span class="zh">例 1：方向键开飞船</span><span class="en">Example 1: fly a ship with the arrow keys</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的程序里，<code>screen.onkey(go_left, "Left")</code> 为什么写 <code>go_left</code> 而不是 <code>go_left()</code>？</span><span class="en">Why does <code>screen.onkey(go_left, "Left")</code> say <code>go_left</code> and not <code>go_left()</code>?</span></p>
  <div class="opts"><button><span class="zh">写错了，应该加括号</span><span class="en">It's a typo, brackets needed</span></button><button><span class="zh">不加括号 = 把函数「交给」屏幕，按键时再运行</span><span class="en">No brackets = hand the function over; it runs when the key is pressed</span></button><button><span class="zh">加不加都一样</span><span class="en">Makes no difference</span></button></div>
  <div class="why"><span class="zh">加了括号会<b>马上</b>运行一次，然后把结果（什么都没有）交给屏幕。不加括号才是把「函数本身」交给屏幕，等按键的时候用。</span><span class="en">With brackets it runs <b>right now</b> and hands over the result (nothing). Without brackets you hand over the "function itself", to be used when the key is pressed.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/11/code/keys.py' | relative_url }}" data-title="⌨️ 方向键开飞船" data-title-en="⌨️ Arrow-key spaceship" data-save="arrow-ship" data-draft="l11-keys" data-rows="14"></div>

<ul class="quests" data-key="l11-keys">
  <li><span class="zh">运行 → 点画布 → 按方向键。用飞船的尾迹画一个正方形！</span><span class="en">Run → click the canvas → press the arrows. Draw a square with the ship's trail!</span></li>
  <li><span class="zh">把 <code>STEP</code> 改成 5，再改成 60。哪个手感好？</span><span class="en">Change <code>STEP</code> to 5, then 60. Which feels better?</span></li>
  <li><span class="zh">一直按 → 不放。飞船飞出画布了吗？（☄️ 的必做 1 就是修这个！）</span><span class="en">Hold → down. Does the ship fly off the canvas? (☄️'s must-have 1 fixes exactly this!)</span></li>
</ul>

<p class="muted" style="font-size:.9rem"><span class="zh">按键名字：<code>"Left" "Right" "Up" "Down" "space" "a" "b"</code>（字母用小写）。</span><span class="en">Key names: <code>"Left" "Right" "Up" "Down" "space" "a" "b"</code> (letters in lower case).</span></p>

### ☄️ <span class="zh">例 2：掉落的陨石（游戏的心跳）</span><span class="en">Example 2: the falling asteroid (the game's heartbeat)</span>

<p><span class="zh"><code>tick()</code> 做三件事：① 动一下 → ② 检查到底没 → ③ <b>叫自己下一拍再来</b>。几乎所有游戏都是这个心跳。</span><span class="en"><code>tick()</code> does three things: ① move a bit → ② check the bottom → ③ <b>ask to be called again next beat</b>. Almost every game has this heartbeat.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/falling.py' | relative_url }}" data-title="☄️ 掉落的陨石" data-title-en="☄️ Falling asteroid" data-save="falling-rock" data-draft="l11-falling" data-rows="14"></div>

<ul class="quests" data-key="l11-falling">
  <li><span class="zh"><code>SPEED</code> 改成 2，再改成 30。</span><span class="en">Change <code>SPEED</code> to 2, then 30.</span></li>
  <li><span class="zh"><code>BEAT</code> 改成 500。为什么变成一跳一跳的？</span><span class="en">Change <code>BEAT</code> to 500. Why does it jump?</span></li>
  <li><span class="zh">把 ③ 那一行删掉，运行。陨石还会一直掉吗？为什么？（这就是「GAME OVER 时游戏停下」的秘密）</span><span class="en">Delete line ③ and run. Does the asteroid keep falling? Why? (That's the secret of "the game stops at GAME OVER")</span></li>
</ul>

### 🚀 <span class="zh">例 3：会变的速度——重力和点火</span><span class="en">Example 3: changing speed — gravity and thrust</span>

<p><span class="zh">例 2 的陨石速度一直是 8。真的火箭不是这样：重力每一拍都让它<b>更快</b>地往下掉，点火让它<b>慢下来</b>。秘密是多一个变量 <code>vy</code>（速度）：<b>重力改速度，速度改位置</b>。🚀 助推器回家和 🛰️ 任务控制中心都靠它。</span><span class="en">Example 2's asteroid always falls at 8. Real rockets don't: gravity makes them fall <b>faster</b> every beat, and the engine <b>slows</b> them down. The secret is one more variable, <code>vy</code> (velocity): <b>gravity changes the velocity, velocity changes the position</b>. 🚀 Booster landing and 🛰️ Mission control both run on it.</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">火箭正在往下掉（<code>vy = -3</code>）。按一次 ↑（<code>vy = vy + 1</code>），会怎样？</span><span class="en">The rocket is falling (<code>vy = -3</code>). You press ↑ once (<code>vy = vy + 1</code>). What happens?</span></p>
  <div class="opts"><button><span class="zh">马上往上飞</span><span class="en">It flies up at once</span></button><button><span class="zh">还在往下，只是慢了一点（vy = -2）</span><span class="en">Still falling, just a bit slower (vy = -2)</span></button><button><span class="zh">停在半空</span><span class="en">It stops in mid-air</span></button></div>
  <div class="why"><span class="zh">点火改的是<b>速度</b>，不是位置。-3 + 1 = -2，还是负数，所以还在往下，只是慢了。要多按几次，vy 变成正数，它才会往上。</span><span class="en">The engine changes the <b>velocity</b>, not the position. -3 + 1 = -2, still negative, so it's still falling, just slower. Press a few more times until vy is positive and it goes up.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/11/code/thrust.py' | relative_url }}" data-title="🚀 重力 + 点火" data-title-en="🚀 Gravity + thrust" data-save="gravity-thrust" data-draft="l11-thrust" data-rows="14"></div>

<ul class="quests" data-key="l11-thrust">
  <li><span class="zh">运行，什么都不按：看 vy 怎么越变越负。再按 ↑ 试着让火箭<b>悬停</b>（vy 一直在 0 附近）。</span><span class="en">Run it and press nothing: watch vy get more and more negative. Then press ↑ and try to make the rocket <b>hover</b> (vy stays near 0).</span></li>
  <li><span class="zh">把 <code>GRAVITY</code> 改成 0.02——重力小很多，像在月球上（月球的重力大约是地球的六分之一）。悬停变容易了吗？</span><span class="en">Change <code>GRAVITY</code> to 0.02 — much weaker gravity, like on the Moon (the Moon's gravity is about one sixth of Earth's). Is hovering easier?</span></li>
  <li>🏆 <span class="zh">把 <code>GRAVITY</code> 改成 <b>-0.05</b>（负的！）会怎样？这就是 🛰️ 火箭发射时越飞越快的秘密。</span><span class="en">What if <code>GRAVITY</code> is <b>-0.05</b> (negative!)? That's the secret of 🛰️'s rocket speeding up as it climbs.</span></li>
</ul>

### 🧮 <span class="zh">小魔法：函数里改「外面的」变量要用 global</span><span class="en">Little magic: use global to change an outside variable inside a function</span>

<div class="playground" data-src="{{ '/lessons/11/code/global.py' | relative_url }}" data-canvas="no" data-title="🧮 global 燃料" data-title-en="🧮 global fuel" data-save="global-fuel" data-draft="l11-global" data-expect="燃料： 2\n燃料： 1\n燃料： 0\n最后燃料： 0" data-rows="10"></div>

<ul class="quests" data-key="l11-global">
  <li>🐞 <span class="zh">把 <code>global fuel</code> 那一行删掉，运行。读一读报错——这是游戏里最常见的 bug 之一！然后加回来。</span><span class="en">Delete the <code>global fuel</code> line and run. Read the error — one of the most common game bugs! Then put it back.</span></li>
  <li><span class="zh">一个函数要改<b>两个</b>外面的变量怎么办？写成 <code>global vy, fuel</code>（用逗号隔开）。在你的骨架里找一找这样的行。</span><span class="en">What if a function changes <b>two</b> outside variables? Write <code>global vy, fuel</code> (comma between). Find a line like that in your skeleton.</span></li>
</ul>

### 🖱️ <span class="zh">可选：还有一个事件——点击</span><span class="en">Optional: one more event — clicks</span>

<div class="playground" data-src="{{ '/lessons/11/code/click.py' | relative_url }}" data-title="🖱️ 点亮星星" data-title-en="🖱️ Light up stars" data-save="click-stars" data-draft="l11-click" data-rows="10"></div>
<p class="muted"><span class="zh"><code>screen.onclick(函数)</code>：点画布就叫函数，电脑会把 <code>x, y</code> 交给它，所以函数必须写成 <code>def 名字(x, y):</code>。做加分功能可能用得上（比如点一下放一个燃料电池）。</span><span class="en"><code>screen.onclick(function)</code>: clicking the canvas calls the function and hands it <code>x, y</code>, so it must be written <code>def name(x, y):</code>. Handy for nice-to-haves (like clicking to drop a fuel cell).</span></p>

---

## 🏗️ <span class="zh">开工：造出我的任务</span><span class="en">Build time: make my mission</span>
{: #build}

<p><span class="zh">打开你的计划（作品墙上的 <code>week10-plan</code>）和<a href="../homework/">作业页</a>的画板——你第 10 课写的骨架会自动出现在那里。<b>一次只做一小步</b>，做完就运行、测完就存。</span><span class="en">Open your plan (<code>week10-plan</code> on the gallery) and the playground on the <a href="../homework/">homework page</a> — the skeleton from Lesson 10 shows up there automatically. <b>One small step at a time</b>: build it, run it, save it.</span></p>

<div class="box box-think"><span class="box-title"><span class="zh">🔴 → 🟢 先叫醒测试，再写函数</span><span class="en">🔴 → 🟢 Wake the test first, then write the function</span></span>
<span class="zh">骨架里有几行「睡着的测试」（前面有 <code>#</code>）。轮到那个功能时：① 删掉 <code>#</code>（保留前面的 4 个空格）→ ② 运行，看它<b>变红</b>（函数还没写，当然失败！）→ ③ 写函数 → ④ 运行，<b>变绿</b>。真正的工程师也这样做：先写好「怎样才算对」，再动手。</span>
<span class="en">Your skeleton has some "sleeping tests" (starting with <code>#</code>). When you reach that feature: ① remove the <code>#</code> (keep the 4 spaces) → ② run and watch it go <b>red</b> (the function isn't written, so of course it fails!) → ③ write the function → ④ run: <b>green</b>. Real engineers work this way too: first write down "what counts as right", then build it.</span>
</div>

<details class="hint"><summary><b>🚀 <span class="zh">我选了：助推器回家</span><span class="en">I picked: Bring the Booster Home</span></b></summary>
<ol class="steps">
  <li><strong><span class="zh">🦴 运行骨架，读懂 tick()</span><span class="en">🦴 Run the skeleton, understand tick()</span></strong><br><span class="zh">按 ↑ 看速度数字。找到「重力改速度」和「速度改位置」是哪两行。</span><span class="en">Press ↑ and watch the speed. Find the two lines "gravity changes velocity" and "velocity changes position".</span></li>
  <li><strong><span class="zh">⛽ 必做 1a：仪表盘显示燃料</span><span class="en">⛽ Must-have 1a: fuel on the dashboard</span></strong><br><span class="zh">在 <code>show_hud()</code> 的 f-string 里加上 <code>{fuel}</code>。运行能看到 30。</span><span class="en">Add <code>{fuel}</code> to the f-string in <code>show_hud()</code>. Run: you see 30.</span></li>
  <li><strong><span class="zh">⛽ 必做 1b：点火用燃料，没油点不了</span><span class="en">⛽ Must-have 1b: burns use fuel; no fuel, no burn</span></strong><br><span class="zh">在 <code>engine()</code> 里：有油才推，推完用 <code>use_fuel</code> 扣。测：一直按 ↑ 到 0，再按应该没反应。</span><span class="en">In <code>engine()</code>: only push if there's fuel, then spend it with <code>use_fuel</code>. Test: hold ↑ until 0; more presses should do nothing.</span></li>
  <li><strong><span class="zh">↔️ 必做 2：侧推</span><span class="en">↔️ Must-have 2: side thrusters</span></strong><br><span class="zh">照着 <code>engine()</code> 的样子写 <code>go_left()</code> / <code>go_right()</code>，改的是 <code>vx</code>；最下面加两行 <code>onkey</code>。测：能飘过去对准船吗？</span><span class="en">Write <code>go_left()</code> / <code>go_right()</code> like <code>engine()</code>, but changing <code>vx</code>; add two <code>onkey</code> lines at the bottom. Test: can you drift over to the ship?</span></li>
  <li><strong><span class="zh">🔴 必做 3a：叫醒 3 个测试</span><span class="en">🔴 Must-have 3a: wake the 3 tests</span></strong><br><span class="zh">删掉 <code>test()</code> 里 3 行前面的 <code>#</code>，运行 → 红色 AssertionError。正常！</span><span class="en">Remove the <code>#</code> from 3 lines in <code>test()</code>, run → red AssertionError. Normal!</span></li>
  <li><strong><span class="zh">🟢 必做 3b：写 is_safe_landing</span><span class="en">🟢 Must-have 3b: write is_safe_landing</span></strong><br><span class="zh">一行 <code>return … and …</code>。运行 → 测试通过。</span><span class="en">One line: <code>return … and …</code>. Run → tests pass.</span></li>
  <li><strong><span class="zh">🏁 必做 3c：成功还是坠毁</span><span class="en">🏁 Must-have 3c: landed or crashed</span></strong><br><span class="zh">在 <code>touchdown()</code> 里用 <code>if is_safe_landing(speed, drift):</code> 写两种结果（颜色不一样）。测：故意摔一次，再好好落一次。</span><span class="en">In <code>touchdown()</code>, use <code>if is_safe_landing(speed, drift):</code> to show two results (different colours). Test: crash once on purpose, then land properly.</span></li>
  <li><strong><span class="zh">🧪 自己的边界测试 + 存档</span><span class="en">🧪 Your own edge test + save</span></strong><br><span class="zh">比如 <code>assert is_safe_landing(MAX_SPEED, PAD_HALF) == True</code>。玩 3 遍，存 <code>week11-project</code>。</span><span class="en">E.g. <code>assert is_safe_landing(MAX_SPEED, PAD_HALF) == True</code>. Play 3 times, save <code>week11-project</code>.</span></li>
</ol>
</details>

<details class="hint"><summary><b>☄️ <span class="zh">我选了：陨石大躲避</span><span class="en">I picked: Asteroid Dodger</span></b></summary>
<ol class="steps">
  <li><strong><span class="zh">🦴 运行骨架，读懂 rocks 列表</span><span class="en">🦴 Run the skeleton, understand the rocks list</span></strong><br><span class="zh"><code>rocks</code> 里装的是什么？<code>tick()</code> 里的 <code>for rock in rocks:</code> 每一拍做了几次？</span><span class="en">What's inside <code>rocks</code>? How many times does <code>for rock in rocks:</code> run each beat?</span></li>
  <li><strong><span class="zh">🔴🟢 必做 1a：keep_inside</span><span class="en">🔴🟢 Must-have 1a: keep_inside</span></strong><br><span class="zh">叫醒它的 3 个测试 → 红 → 用 <code>if / elif</code> 写函数 → 绿。</span><span class="en">Wake its 3 tests → red → write it with <code>if / elif</code> → green.</span></li>
  <li><strong><span class="zh">🧱 必做 1b：飞船用上它</span><span class="en">🧱 Must-have 1b: the ship uses it</span></strong><br><span class="zh"><code>go_left</code> 和 <code>go_right</code> 都把新的 x 先交给 <code>keep_inside</code>。测：一直按 ←，飞船停在边上。</span><span class="en">Both <code>go_left</code> and <code>go_right</code> pass the new x through <code>keep_inside</code> first. Test: hold ←, the ship stops at the edge.</span></li>
  <li><strong><span class="zh">💥 必做 2a：撞上扣命</span><span class="en">💥 Must-have 2a: crashes cost lives</span></strong><br><span class="zh">在 <code>for</code> 里面加 <code>if hit(…):</code>，命 -1，<b>这颗陨石回到上面</b>（不然每一拍都会再扣一次！）。<code>tick()</code> 要 <code>global score, lives</code>。</span><span class="en">Inside the <code>for</code>, add <code>if hit(…):</code> → lives −1 and <b>send that rock back to the top</b> (or it'll take a life every beat!). <code>tick()</code> needs <code>global score, lives</code>.</span></li>
  <li><strong><span class="zh">🛑 必做 2b：GAME OVER</span><span class="en">🛑 Must-have 2b: GAME OVER</span></strong><br><span class="zh"><code>tick()</code> 最后：还有命才 <code>ontimer</code>，没命就写 GAME OVER（想想例 2 的第 3 个 quest）。</span><span class="en">At the end of <code>tick()</code>: only <code>ontimer</code> if lives are left; otherwise write GAME OVER (remember example 2's third quest).</span></li>
  <li><strong><span class="zh">⚡ 必做 3：越来越快</span><span class="en">⚡ Must-have 3: faster and faster</span></strong><br><span class="zh">叫醒 <code>speed_for</code> 的 3 个测试 → 红 → 写函数（别忘了上限）→ 绿。玩一局，感觉到变快了吗？</span><span class="en">Wake <code>speed_for</code>'s 3 tests → red → write it (don't forget the top speed) → green. Play: can you feel it speed up?</span></li>
  <li><strong><span class="zh">🧪 自己的边界测试 + 存档</span><span class="en">🧪 Your own edge test + save</span></strong><br><span class="zh">比如 <code>assert keep_inside(EDGE) == EDGE</code>。玩 3 遍，存 <code>week11-project</code>。</span><span class="en">E.g. <code>assert keep_inside(EDGE) == EDGE</code>. Play 3 times, save <code>week11-project</code>.</span></li>
</ol>
</details>

<details class="hint"><summary><b>🛰️ <span class="zh">我选了：任务控制中心</span><span class="en">I picked: Mission Control</span></b></summary>
<ol class="steps">
  <li><strong><span class="zh">🦴 运行骨架，读懂 poll() 和 checks</span><span class="en">🦴 Run the skeleton, understand poll() and checks</span></strong><br><span class="zh">运行 2–3 次（输入 1、2 或 3）。<code>checks</code> 字典的键和值是什么？<code>log_event</code> 做了哪两件事？</span><span class="en">Run it 2–3 times (type 1, 2 or 3). What are the keys and values in the <code>checks</code> dict? What two things does <code>log_event</code> do?</span></li>
  <li><strong><span class="zh">🔴🟢 必做 1a：all_systems_go</span><span class="en">🔴🟢 Must-have 1a: all_systems_go</span></strong><br><span class="zh">叫醒 2 个测试 → 红 → 用 <code>for</code> + <code>if</code> 写函数 → 绿。小心：<code>return True</code> 要放在 for <b>外面</b>。</span><span class="en">Wake 2 tests → red → write it with <code>for</code> + <code>if</code> → green. Careful: <code>return True</code> goes <b>outside</b> the for.</span></li>
  <li><strong><span class="zh">🛑 必做 1b：GO 才发射，不然 SCRUB</span><span class="en">🛑 Must-have 1b: launch only on GO, otherwise SCRUB</span></strong><br><span class="zh">主程序最后：<code>if all_systems_go(checks):</code> 才 <code>onkey</code>；<code>else</code> 打印「🛑 推迟发射」并 <code>log_event</code>。多运行几次，两种都要看到。</span><span class="en">End of the main program: <code>onkey</code> only <code>if all_systems_go(checks):</code>; <code>else</code> print "🛑 SCRUB" and <code>log_event</code> it. Run several times and see both.</span></li>
  <li><strong><span class="zh">⏱️ 必做 2a：倒数（先用 print）</span><span class="en">⏱️ Must-have 2a: countdown (print first)</span></strong><br><span class="zh">新变量 <code>count = 10</code>，新函数 <code>countdown()</code>：打印 count，减 1，还没到 0 就 <code>screen.ontimer(countdown, 500)</code>；到 0 就 <code>fly()</code>。<code>launch()</code> 改成叫 <code>countdown()</code>。</span><span class="en">New variable <code>count = 10</code>, new function <code>countdown()</code>: print count, subtract 1, and if not 0 yet <code>screen.ontimer(countdown, 500)</code>; at 0 call <code>fly()</code>. Make <code>launch()</code> call <code>countdown()</code>.</span></li>
  <li><strong><span class="zh">🖊️ 必做 2b：写到画布中间</span><span class="en">🖊️ Must-have 2b: on the canvas</span></strong><br><span class="zh">再做一只隐藏的海龟（比如 <code>big</code>），每次 <code>clear()</code> 再 <code>write(f"T-{count}", …)</code>。</span><span class="en">Make another hidden turtle (e.g. <code>big</code>); each time <code>clear()</code> then <code>write(f"T-{count}", …)</code>.</span></li>
  <li><strong><span class="zh">✌️ 必做 2c：按两次空格只发射一次</span><span class="en">✌️ Must-have 2c: two presses, one launch</span></strong><br><span class="zh">测：倒数时再按空格——火箭是不是飞得特别快？加一个 <code>launched = False</code> 变量挡住第二次。</span><span class="en">Test: press space again during the countdown — does the rocket go super fast? Add a <code>launched = False</code> variable to block the second press.</span></li>
  <li><strong><span class="zh">🔴🟢 必做 3a：stage_for</span><span class="en">🔴🟢 Must-have 3a: stage_for</span></strong><br><span class="zh">叫醒 2 个测试 → 红 → 写函数 → 绿。</span><span class="en">Wake 2 tests → red → write it → green.</span></li>
  <li><strong><span class="zh">🧩 必做 3b：一二级分离</span><span class="en">🧩 Must-have 3b: stage separation</span></strong><br><span class="zh">新变量 <code>stage = 1</code>。在 <code>fly()</code> 里：<code>stage_for</code> 说 2 而 <code>stage</code> 还是 1 → 改成 2 并记日志（这样只记<b>一次</b>）。<code>stage</code> 是 1 时 booster 才跟着火箭，是 2 时让它往下掉。</span><span class="en">New variable <code>stage = 1</code>. In <code>fly()</code>: if <code>stage_for</code> says 2 while <code>stage</code> is still 1 → set it to 2 and log it (so it logs only <b>once</b>). The booster follows the rocket only while <code>stage</code> is 1; at 2 it falls.</span></li>
  <li><strong><span class="zh">🧪 自己的边界测试 + 存档</span><span class="en">🧪 Your own edge test + save</span></strong><br><span class="zh">比如 <code>assert stage_for(SEPARATION) == 2</code>。跑 3 次（有时 SCRUB，正常！），存 <code>week11-project</code>。</span><span class="en">E.g. <code>assert stage_for(SEPARATION) == 2</code>. Run 3 times (sometimes it scrubs — normal!), save <code>week11-project</code>.</span></li>
</ol>
</details>

### 🧪 <span class="zh">测试清单：别人会怎么弄坏它？</span><span class="en">Test checklist: how would someone break it?</span>
{: #tests}

<div class="two">
  <div class="card"><b>🚀 <span class="zh">助推器回家</span><span class="en">Booster landing</span></b>
    <ul style="font-size:.95rem;margin:.4em 0;padding-left:1.2em">
      <li><span class="zh">燃料会变成负数吗？</span><span class="en">Can fuel go negative?</span></li>
      <li><span class="zh">一直按 ↑，助推器飞出画布顶部会怎样？</span><span class="en">Hold ↑: what if it flies off the top?</span></li>
      <li><span class="zh">刚好落在甲板边上算成功吗？该不该？</span><span class="en">Landing exactly on the deck's edge: success? Should it be?</span></li>
      <li><span class="zh">落地以后按键还有反应吗？</span><span class="en">Do keys still do something after touchdown?</span></li>
    </ul>
  </div>
  <div class="card"><b>☄️ <span class="zh">陨石大躲避</span><span class="en">Asteroid dodger</span></b>
    <ul style="font-size:.95rem;margin:.4em 0;padding-left:1.2em">
      <li><span class="zh">一直按同一个键，飞船会出去吗？</span><span class="en">Hold one key: does the ship escape?</span></li>
      <li><span class="zh">撞一次扣几条命？命会变成负数吗？</span><span class="en">One crash = how many lives? Can lives go negative?</span></li>
      <li><span class="zh">GAME OVER 以后还能动吗？该不该？</span><span class="en">Can you move after GAME OVER? Should you?</span></li>
      <li><span class="zh">玩到很高分，速度会停在上限吗？</span><span class="en">At a high score, does the speed stop at the top speed?</span></li>
    </ul>
  </div>
  <div class="card"><b>🛰️ <span class="zh">任务控制中心</span><span class="en">Mission control</span></b>
    <ul style="font-size:.95rem;margin:.4em 0;padding-left:1.2em">
      <li><span class="zh">选载荷时输入「abc」或什么都不输？</span><span class="en">Type "abc" or nothing for the payload?</span></li>
      <li><span class="zh">SCRUB 以后按空格会发射吗？</span><span class="en">After a SCRUB, does space still launch?</span></li>
      <li><span class="zh">倒数时连按空格？</span><span class="en">Mash space during the countdown?</span></li>
      <li><span class="zh">日志里每件事是不是只出现一次、顺序对吗？</span><span class="en">Does each event appear once, in the right order, in the log?</span></li>
    </ul>
  </div>
  <div class="card"><b>🧪 <span class="zh">所有任务</span><span class="en">Every mission</span></b>
    <ul style="font-size:.95rem;margin:.4em 0;padding-left:1.2em">
      <li><span class="zh">「↺ 还原」以后粘贴最新版，从头运行一次</span><span class="en">After "↺ Reset", paste the latest version and run from scratch</span></li>
      <li><span class="zh"><code>test()</code> 全部通过，没有「睡着的测试」了</span><span class="en"><code>test()</code> all pass, no "sleeping tests" left</span></li>
      <li><span class="zh">第一行注释有标题和作者</span><span class="en">First comment line has title and author</span></li>
    </ul>
  </div>
</div>

---

## 🤖 <span class="zh">和 AI 一起：制作周的规矩</span><span class="en">With AI: rules for build week</span>

<div class="box box-rule">
<span class="zh">这周 AI 可以：<b>解释报错</b>、<b>给提示</b>、<b>当小黄鸭</b>、<b>解释一行你看不懂的代码</b>。<br>AI 不可以：替你写整个功能。<b>如果 AI 给了整段代码，你要能给老师解释每一行，才能用。</b>解释不了的，删掉。</span>
<span class="en">This week AI may: <b>explain errors</b>, <b>give hints</b>, <b>be the duck</b>, <b>explain one line you don't get</b>.<br>AI may not: write a whole feature for you. <b>If AI gives you a block of code, you may only use it if you can explain every line to the teacher.</b> Can't explain it? Delete it.</span>
</div>

<div class="chat">
  <div class="bubble me"><span class="zh">我在做助推器着陆游戏。我想让每次点火燃料少 1，但运行时报错：UnboundLocalError: local variable 'fuel' referenced before assignment。我的函数是：def engine(): global vy; vy = vy + THRUST; fuel = use_fuel(fuel)。请给我一个提示，不要直接给答案。</span><span class="en">I'm making a booster landing game. I want each burn to use 1 fuel, but I get: UnboundLocalError: local variable 'fuel' referenced before assignment. My function: def engine(): global vy; vy = vy + THRUST; fuel = use_fuel(fuel). Please give me a hint, not the answer.</span></div>
  <div class="bubble ai"><span class="zh">提示：你已经告诉电脑 vy 是外面那个了。那 fuel 呢？看看你函数第一行，是不是少说了一个名字 😉</span><span class="en">Hint: you've already told the computer that vy is the outside one. What about fuel? Look at your function's first line — is a name missing? 😉</span></div>
  <div class="bubble me"><span class="zh">要写 <code>global vy, fuel</code>！谢谢，我自己改。</span><span class="en">It should be <code>global vy, fuel</code>! Thanks, I'll fix it myself.</span></div>
</div>

<p><span class="zh">👆 好的问法：说了<b>在做什么</b>、<b>想要什么</b>、<b>报错原话</b>、<b>相关的几行</b>，并且要的是<b>提示</b>。</span><span class="en">👆 A good question says <b>what you're making</b>, <b>what you want</b>, <b>the exact error</b>, <b>the few lines involved</b>, and asks for a <b>hint</b>.</span></p>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>🔍 <span class="zh">print 侦探</span><span class="en">print detective</span></b><code>print("到这里了", fuel)</code><span><span class="zh">没报错但答案不对 / 游戏卡住：让程序把心里的数说出来</span><span class="en">No error but wrong answer / frozen game: make it say what it's thinking</span></span></div>
  <div class="k"><b>📜 <span class="zh">读报错</span><span class="en">Read the error</span></b><code><span class="zh">第几行 → 错误种类 → 原话 → 看那行 → 这个值从哪来？</span><span class="en">line → kind → message → look at the line → where did this value come from?</span></code><span><span class="zh">报错在 A，bug 可能在 B</span><span class="en">The error is at A; the bug may be at B</span></span></div>
  <div class="k"><b>🦆 <span class="zh">小黄鸭</span><span class="en">Rubber duck</span></b><code><span class="zh">"第 3 行是说……"</span><span class="en">"Line 3 says…"</span></code><span><span class="zh">念出来，自己就发现了</span><span class="en">Say it out loud and you'll see it</span></span></div>
  <div class="k"><b>✂️ <span class="zh">二分法</span><span class="en">Halving</span></b><code><span class="zh"># 注释掉一半</span><span class="en"># comment out half</span></code><span><span class="zh">对 → 问题在另一半</span><span class="en">Works → the bug is in the other half</span></span></div>
  <div class="k"><b>⌨️ <span class="zh">键盘</span><span class="en">Keys</span></b><code>screen.onkey(engine, "Up")
screen.listen()</code><span><span class="zh">函数名不加括号</span><span class="en">Function name, no brackets</span></span></div>
  <div class="k"><b>⏱️ <span class="zh">心跳</span><span class="en">Heartbeat</span></b><code>def tick():
    ...
    screen.ontimer(tick, 50)
tick()</code><span><span class="zh">自己叫自己 = 一直跑；不叫 = 停</span><span class="en">Calls itself = keeps going; doesn't = stops</span></span></div>
  <div class="k"><b>🚀 <span class="zh">速度</span><span class="en">Velocity</span></b><code>vy = vy - GRAVITY
rocket.sety(rocket.ycor() + vy)</code><span><span class="zh">重力改速度，速度改位置</span><span class="en">Gravity changes velocity; velocity changes position</span></span></div>
  <div class="k"><b>🧮 global</b><code>def engine():
    global vy, fuel
    fuel = fuel - 1</code><span><span class="zh">函数里改外面的变量</span><span class="en">Change outside variables inside a function</span></span></div>
  <div class="k"><b>🔴→🟢</b><code><span class="zh">叫醒测试 → 红 → 写函数 → 绿</span><span class="en">wake test → red → write function → green</span></code><span><span class="zh">先写「怎样才算对」</span><span class="en">Decide "what counts as right" first</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令在 <a href="{{ '/cheatsheet/' | relative_url }}#l11">📖 小词典 · 第 11 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l11">📖 cheat sheet · Lesson 11</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/11/homework/' | relative_url }}"><span class="zh">下一步：把任务做完 🏠 →</span><span class="en">Next: finish the mission 🏠 →</span></a></p>
