---
title: 第 11 课 · 学一学
title_en: Lesson 11 · Learn
lesson: "11"
tab: learn
playground: true
---

# 🛠️ <span class="zh">第 11 课：排错工具箱 + 让程序动起来</span><span class="en">Lesson 11: The debugging toolbox + making programs move</span>

<p class="zh">今天没有新的「大语法」。今天学的是程序员<b>每天都在用</b>的本事：<b>bug 不会自己消失，但有办法把它找出来。</b>然后，用键盘和定时器让你的项目「活」起来。</p>
<p class="en">No big new syntax today. Today is about the skill programmers <b>use every single day</b>: <b>bugs don't vanish on their own, but there are ways to hunt them down.</b> Then we'll use keys and timers to bring your project to life.</p>

---

## 🔁 <span class="zh">热身：治好 3 个 bug</span><span class="en">Warm-up: cure 3 bugs</span>
{: #warmup}

<p><span class="zh">这段程序生病了，一共 <b>3 个 bug</b>。它想打印两行：「小海龟 得了 3 分」和「太棒了！」。先<b>读</b>，再运行，一次治一个。全治好会 🏆！</span><span class="en">This program is sick with <b>3 bugs</b>. It should print two lines: "小海龟 得了 3 分" and "太棒了！". <b>Read</b> first, then run, fix one at a time. Cure them all for a 🏆!</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/warmup-bugs.py' | relative_url }}" data-canvas="no" data-title="🐞 三个 bug" data-title-en="🐞 Three bugs" data-save="three-bugs" data-draft="l11-warmup" data-expect="小海龟 得了 3 分\n太棒了！" data-badge="lesson-11-warmup" data-rows="12"></div>

<ul class="quests" data-key="l11-warmup">
  <li>🐞 <span class="zh">Bug 1：运行，读红框。<code>for</code> 那一行少了什么？</span><span class="en">Bug 1: run it, read the red box. What's missing on the <code>for</code> line?</span></li>
  <li>🐞 <span class="zh">Bug 2：又报错了？电脑说它<b>不认识一个名字</b>。和上面的变量名对一对，少了哪个字母？</span><span class="en">Bug 2: another error? The computer <b>doesn't know a name</b>. Compare it with the variable above — which letter is wrong?</span></li>
  <li>🐞 <span class="zh">Bug 3：「是不是等于」要用<b>两个</b>等号。</span><span class="en">Bug 3: "is it equal to" needs <b>two</b> equals signs.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 全部答案（先自己试！）</span><span class="en">💡 All answers (try first!)</span></summary><span class="zh">① <code>for i in range(3):</code> 最后要有冒号 ② <code>nmae</code> → <code>name</code> ③ <code>if score == 3:</code></span><span class="en">① <code>for i in range(3):</code> needs a colon ② <code>nmae</code> → <code>name</code> ③ <code>if score == 3:</code></span></details>

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

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">下面的程序算 3 + 5 + 2。运行后它会打印多少？</span><span class="en">The program below adds 3 + 5 + 2. What will it print?</span></p>
  <div class="opts"><button>10</button><button>0</button><button>2</button></div>
  <div class="why"><span class="zh">2！因为 <code>total = price</code> 是「把 total <b>换成</b> price」，不是「加上」。每一圈都把前面的忘了，最后只剩 2。</span><span class="en">2! Because <code>total = price</code> means "<b>replace</b> total with price", not "add". Every round forgets the earlier ones, so only 2 is left.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/11/code/detective.py' | relative_url }}" data-canvas="no" data-title="🔍 print 侦探" data-title-en="🔍 print detective" data-save="print-detective" data-draft="l11-detective" data-expect="一共 10 元" data-badge="lesson-11-detective" data-rows="10"></div>

<ul class="quests" data-key="l11-detective">
  <li><span class="zh">在 <code>total = price</code> 的<b>下面</b>加一行 <code>print("现在 total 是", total)</code>（记得缩进一样）。运行，看每一圈 total 是多少。</span><span class="en">Add <code>print("now total is", total)</code> <b>under</b> <code>total = price</code> (same indentation). Run and watch total each round.</span></li>
  <li><span class="zh">看出问题了吗？把那一行改对，让它打印「一共 10 元」。</span><span class="en">See the problem? Fix that line so it prints "一共 10 元".</span></li>
  <li><span class="zh">修好以后，把侦探 print 删掉（或者加 <code>#</code> 变成注释）。</span><span class="en">When it works, delete the detective print (or turn it into a comment with <code>#</code>).</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">「加上」要写 <code>total = total + price</code>（第 2 课的变量魔法！）。</span><span class="en">"Add to" is written <code>total = total + price</code> (variable magic from Lesson 2!).</span></details>

### 📜 <span class="zh">第 2 招：把报错当地图读</span><span class="en">Trick 2: read the error like a map</span>

<p><span class="zh">红字不是骂你，是一张<b>藏宝图</b>。先运行下面的程序，<b>别改</b>，我们一起读。</span><span class="en">Red text isn't telling you off — it's a <b>treasure map</b>. Run the program below, <b>don't fix it yet</b>, and let's read it together.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/traceback.py' | relative_url }}" data-canvas="no" data-title="📜 读报错" data-title-en="📜 Read the error" data-save="read-error" data-draft="l11-traceback" data-rows="9"></div>

<ol class="code-walk">
  <li><code>🐞 第 9 行出了个小问题</code><span><span class="zh"><b>先看行号</b>。画板已经帮你把那一行标红了。</span><span class="en"><b>Line number first</b>. The playground has already marked that line red.</span></span></li>
  <li><code>IndexError</code><span><span class="zh"><b>错误的种类</b>。Index = 位置。「位置错误」= 你要的位置不存在。</span><span class="en"><b>The kind of error</b>. Index = position. "Position error" = the spot you asked for doesn't exist.</span></span></li>
  <li><code>list index out of range</code><span><span class="zh"><b>电脑的原话</b>：列表的位置超出范围。3 个水果的位置是 0、1、2，没有 3！</span><span class="en"><b>The computer's words</b>: list position out of range. 3 fruits live at 0, 1, 2 — there's no 3!</span></span></li>
  <li><code>fruits[3]</code><span><span class="zh"><b>看那一行的代码</b>，找到和错误种类有关的东西。</span><span class="en"><b>Look at that line</b> and find the part that matches the error kind.</span></span></li>
</ol>

<div class="table-wrap">
<table>
<tr><th><span class="zh">错误种类</span><span class="en">Error kind</span></th><th><span class="zh">它在说</span><span class="en">It means</span></th><th><span class="zh">先检查</span><span class="en">Check first</span></th></tr>
<tr><td><code>NameError</code></td><td><span class="zh">不认识这个名字</span><span class="en">Unknown name</span></td><td><span class="zh">拼写、大小写、引号、有没有先创建</span><span class="en">Spelling, capitals, quotes, created yet?</span></td></tr>
<tr><td><code>SyntaxError</code></td><td><span class="zh">看不懂这一行的写法</span><span class="en">Can't read this line</span></td><td><span class="zh">冒号、括号成对、引号成对、上一行</span><span class="en">Colon, matching brackets and quotes, the line above</span></td></tr>
<tr><td><code>IndentationError</code></td><td><span class="zh">前面的空格不对</span><span class="en">Wrong spaces at the start</span></td><td><span class="zh">for / if / def 下面要缩 4 格</span><span class="en">4 spaces under for / if / def</span></td></tr>
<tr><td><code>TypeError</code></td><td><span class="zh">东西的种类搞混了</span><span class="en">Mixed-up kinds</span></td><td><span class="zh">文字 + 数字？用 f-string 或 int()</span><span class="en">Text + number? Use f-string or int()</span></td></tr>
<tr><td><code>IndexError</code> / <code>KeyError</code></td><td><span class="zh">列表 / 字典里没有这个</span><span class="en">List / dict doesn't have it</span></td><td><span class="zh">第一个是 [0]；键拼对了吗</span><span class="en">First is [0]; key spelled right?</span></td></tr>
</table>
</div>

<ul class="quests" data-key="l11-traceback">
  <li><span class="zh">现在修好它：要么删掉第 9 行，要么往列表里加第 4 种水果。</span><span class="en">Now fix it: delete line 9, or add a 4th fruit to the list.</span></li>
  <li><span class="zh">把这张表抄一行到你的<a href="{{ '/notebook/' | relative_url }}">笔记本</a>「我遇到过的报错」里。</span><span class="en">Copy one row of this table into the "Errors I've met" part of your <a href="{{ '/notebook/' | relative_url }}">notebook</a>.</span></li>
</ul>

### 🦆 <span class="zh">第 3 招：小黄鸭法</span><span class="en">Trick 3: the rubber duck</span>

<p><span class="zh">真的有程序员在桌上放一只橡皮小黄鸭 🦆。卡住的时候，<b>把代码一行一行念给鸭子听</b>，解释它在干嘛。神奇的是：念到一半，你自己就会「啊！」一声发现问题。因为<b>说出来</b>比<b>看</b>更认真。</span><span class="en">Real programmers keep a rubber duck 🦆 on their desk. When stuck, <b>explain the code to the duck line by line</b>. The magic: halfway through you go "oh!" and spot the problem yourself, because <b>saying it</b> is more careful than <b>looking</b>.</span></p>

<p><span class="zh">这个猜数字程序没有报错，但玩起来怪怪的。先玩一次（秘密数字是 7），然后念给鸭子听。</span><span class="en">This guessing game has no error, but feels wrong. Play it once (the secret is 7), then explain it to the duck.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/duck.py' | relative_url }}" data-canvas="no" data-title="🦆 念给鸭子听" data-title-en="🦆 Tell the duck" data-save="duck-game" data-draft="l11-duck" data-rows="14"></div>

<ul class="quests" data-key="l11-duck">
  <li><span class="zh">玩一次：猜 3，程序说什么？这句话对吗？</span><span class="en">Play: guess 3. What does it say? Is that right?</span></li>
  <li><span class="zh">念给鸭子（或者老师、弟弟妹妹）：「如果 guess 比 secret <b>大</b>，就说……」念到这里你发现了吗？</span><span class="en">Tell the duck (or the teacher, or a sibling): "If guess is <b>bigger</b> than secret, say…" — did you spot it?</span></li>
  <li><span class="zh">把两句话换回来。</span><span class="en">Swap the two messages back.</span></li>
</ul>

<div class="box box-tip"><span class="box-title"><span class="zh">🤖 没有鸭子？AI 也可以当鸭子</span><span class="en">🤖 No duck? AI can be the duck</span></span>
<span class="zh">复制下面的话发给 AI（注意：是<b>你</b>解释，AI 只负责听和提问）：</span><span class="en">Copy this to the AI (note: <b>you</b> explain, the AI only listens and asks):</span>
<pre style="white-space:pre-wrap;margin:.5em 0">我在排错。我会一行一行解释我的代码，请你当小黄鸭：只问我问题，不要告诉我答案。
我的代码：
（粘贴代码）
第 1 行：…</pre>
<button class="pg-btn copy-prev">📋 <span class="zh">复制</span><span class="en">Copy</span></button>
</div>

### ✂️ <span class="zh">第 4 招：二分法</span><span class="en">Trick 4: halving (binary search)</span>

<p><span class="zh">程序很长，画出来不对，不知道从哪看起？<b>把后一半注释掉</b>（每行前面加 <code>#</code>），运行：前一半对吗？对，问题在后一半；不对，问题在前一半。再把那一半分两半……像猜数字一样，几次就找到了。</span><span class="en">Long program, wrong picture, no idea where to look? <b>Comment out the second half</b> (put <code>#</code> in front of each line) and run: is the first half right? If yes, the problem is in the second half; if no, in the first. Halve again… like guess-the-number, a few rounds finds it.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/bisect.py' | relative_url }}" data-title="✂️ 二分法找 bug" data-title-en="✂️ Halving" data-save="bisect-house" data-draft="l11-bisect" data-rows="14"></div>

<ul class="quests" data-key="l11-bisect">
  <li><span class="zh">运行一次。房子、屋顶、太阳，哪个画错了？</span><span class="en">Run it once. House, roof, sun — which one is wrong?</span></li>
  <li><span class="zh">把「第 3 部分」全部加 <code>#</code>，再运行。错误还在吗？在 → 问题在 1 或 2 部分。</span><span class="en">Put <code>#</code> on all of "Part 3" and run. Still wrong? Yes → the problem is in part 1 or 2.</span></li>
  <li><span class="zh">再把「第 2 部分」注释掉。现在对了？那 bug 就在第 2 部分。盯着那几行找：是不是有一个「转弯」转反了？</span><span class="en">Now comment out "Part 2" too. Correct now? Then the bug is in part 2. Stare at those lines: is one turn going the wrong way?</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">屋顶要先走到左上角、<b>转回朝右</b>再画三角形。第 2 部分里第二个 <code>t.left(90)</code> 应该是 <code>t.right(90)</code>。</span><span class="en">The roof should go to the top-left corner, <b>turn back to face right</b>, then draw the triangle. The second <code>t.left(90)</code> in part 2 should be <code>t.right(90)</code>.</span></details>

---

## 🎮 <span class="zh">游戏专用魔法：让程序「活」起来</span><span class="en">Game magic: bringing programs to life</span>
{: #events}

<p><span class="zh">到现在为止，程序都是「从上跑到下，然后结束」。游戏不一样：程序要<b>等着</b>你按键、要<b>自己一拍一拍地动</b>。这就是「事件」。</span><span class="en">Until now, programs "run top to bottom and stop". Games are different: the program must <b>wait</b> for your keys and <b>move by itself, beat by beat</b>. These are "events".</span></p>

<div class="cmds">
  <div class="cmd"><code>screen = turtle.Screen()</code><span><span class="zh">拿到「屏幕」，事件都挂在它身上</span><span class="en">Get the "screen"; events hang on it</span></span></div>
  <div class="cmd"><code>screen.onkey(函数, "Left")</code><span><span class="zh">按 ← 就叫这个函数（注意：写函数名，<b>不加括号</b>）</span><span class="en">Press ← to call this function (function name, <b>no brackets</b>)</span></span></div>
  <div class="cmd"><code>screen.listen()</code><span><span class="zh">开始听键盘（忘了这行按键没反应）</span><span class="en">Start listening (forget this and keys do nothing)</span></span></div>
  <div class="cmd"><code>screen.ontimer(函数, 50)</code><span><span class="zh">50 毫秒后叫一次函数——函数里再叫一次，就成了心跳</span><span class="en">Call the function after 50 ms; call it again inside → a heartbeat</span></span></div>
  <div class="cmd"><code>screen.onclick(函数)</code><span><span class="zh">点画布就叫函数，电脑会把 x, y 交给它</span><span class="en">Click the canvas to call it; the computer hands it x, y</span></span></div>
</div>

<div class="box box-warn"><span class="box-title"><span class="zh">⚠️ 网页画板的三条规矩</span><span class="en">⚠️ Three rules for the web playground</span></span>
<span class="zh">① 用 <code>onkey</code>，不用 <code>onkeypress</code>（画板会自动帮你换，但电脑上的 Python 两个都行）。② 运行后<b>先点一下画布</b>，键盘才会被听到。③ 主程序跑完以后游戏还在跑，画板会显示「🎮 游戏开始了」；玩完点 <b>■ 结束游戏</b>。</span>
<span class="en">① Use <code>onkey</code>, not <code>onkeypress</code> (the playground swaps it for you; on a computer both work). ② After running, <b>click the canvas first</b> so keys are heard. ③ The game keeps going after the main program ends — the playground shows "🎮 Game on!"; click <b>■ End game</b> when done.</span>
</div>

### ⌨️ <span class="zh">例 1：方向键开车</span><span class="en">Example 1: drive with the arrow keys</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的程序里，<code>screen.onkey(go_left, "Left")</code> 为什么写 <code>go_left</code> 而不是 <code>go_left()</code>？</span><span class="en">Why does <code>screen.onkey(go_left, "Left")</code> say <code>go_left</code> and not <code>go_left()</code>?</span></p>
  <div class="opts"><button><span class="zh">写错了，应该加括号</span><span class="en">It's a typo, brackets needed</span></button><button><span class="zh">不加括号 = 把函数「交给」屏幕，按键时再运行</span><span class="en">No brackets = hand the function over; it runs when the key is pressed</span></button><button><span class="zh">加不加都一样</span><span class="en">Makes no difference</span></button></div>
  <div class="why"><span class="zh">加了括号会<b>马上</b>运行一次然后把结果（什么都没有）交给屏幕。不加括号才是把「函数本身」交给屏幕，等按键的时候用。</span><span class="en">With brackets it runs <b>right now</b> and hands over the result (nothing). Without brackets you hand over the "function itself", to be used when the key is pressed.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/11/code/keys.py' | relative_url }}" data-title="⌨️ 方向键开车" data-title-en="⌨️ Arrow-key driving" data-save="arrow-drive" data-draft="l11-keys" data-rows="14"></div>

<ul class="quests" data-key="l11-keys">
  <li><span class="zh">运行 → 点画布 → 按方向键。画出一个正方形！</span><span class="en">Run → click the canvas → press the arrows. Draw a square!</span></li>
  <li><span class="zh">把 <code>STEP</code> 改成 5，再改成 60。哪个手感好？</span><span class="en">Change <code>STEP</code> to 5, then 60. Which feels better?</span></li>
  <li><span class="zh">加一个空格键：<code>screen.onkey(清屏函数, "space")</code>，函数里写 <code>t.clear()</code>。</span><span class="en">Add a space bar: <code>screen.onkey(clear_fn, "space")</code> with <code>t.clear()</code> inside.</span></li>
</ul>

<p class="muted" style="font-size:.9rem"><span class="zh">按键名字：<code>"Left" "Right" "Up" "Down" "space" "a" "b"</code>（字母用小写）。</span><span class="en">Key names: <code>"Left" "Right" "Up" "Down" "space" "a" "b"</code> (letters in lower case).</span></p>

### ⭐ <span class="zh">例 2：掉落的星星（游戏的心跳）</span><span class="en">Example 2: the falling star (the game's heartbeat)</span>

<p><span class="zh"><code>tick()</code> 做三件事：动一下 → 检查到底没 → <b>叫自己下一拍再来</b>。几乎所有游戏都是这个心跳。</span><span class="en"><code>tick()</code> does three things: move a bit → check the bottom → <b>ask to be called again next beat</b>. Almost every game has this heartbeat.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/falling.py' | relative_url }}" data-title="⭐ 掉落的星星" data-title-en="⭐ Falling star" data-save="falling-star" data-draft="l11-falling" data-rows="14"></div>

<ul class="quests" data-key="l11-falling">
  <li><span class="zh"><code>SPEED</code> 改成 2，再改成 30。</span><span class="en">Change <code>SPEED</code> to 2, then 30.</span></li>
  <li><span class="zh"><code>BEAT</code> 改成 500。为什么变成一跳一跳的？</span><span class="en">Change <code>BEAT</code> to 500. Why does it jump?</span></li>
  <li>🏆 <span class="zh">把例 1 的方向键和这颗星星<b>合在一起</b>：一只海龟在底下左右移动，星星掉下来。加一行 <code>if star.distance(t) < 30:</code> 就能判断「接到了」！（这就是 <a href="{{ '/games/catch/' | relative_url }}">🍎 接水果</a> 的全部秘密）</span><span class="en">Combine example 1's keys with this star: a turtle moves left/right at the bottom, the star falls. Add <code>if star.distance(t) < 30:</code> to detect a catch! (That's the whole secret of <a href="{{ '/games/catch/' | relative_url }}">🍎 Fruit Catcher</a>)</span></li>
</ul>

### 🖱️ <span class="zh">例 3：点哪盖哪</span><span class="en">Example 3: click to stamp</span>

<div class="playground" data-src="{{ '/lessons/11/code/click.py' | relative_url }}" data-title="🖱️ 点击盖章" data-title-en="🖱️ Click to stamp" data-save="click-stamp" data-draft="l11-click" data-rows="12"></div>

<ul class="quests" data-key="l11-click">
  <li><span class="zh">把 <code>t.stamp()</code> 换成 <code>t.circle(20)</code>（记得先 <code>t.pendown()</code>）。</span><span class="en">Swap <code>t.stamp()</code> for <code>t.circle(20)</code> (remember <code>t.pendown()</code> first).</span></li>
  <li><span class="zh">让每次点击的海龟越来越大：<code>t.shapesize</code> 网页不支持，试试换成每次 <code>t.circle(半径)</code> 里的半径 +5（需要 <code>global</code>，看下面）。</span><span class="en">Make each click bigger: the web doesn't support <code>t.shapesize</code>, so try growing the radius in <code>t.circle(r)</code> by 5 each time (needs <code>global</code>, see below).</span></li>
</ul>

### 🧮 <span class="zh">小魔法：函数里改「外面的」分数要用 global</span><span class="en">Little magic: use global to change an outside score inside a function</span>

<div class="playground" data-src="{{ '/lessons/11/code/global.py' | relative_url }}" data-canvas="no" data-title="🧮 global 记分" data-title-en="🧮 global score" data-save="global-score" data-draft="l11-global" data-expect="得分： 1\n得分： 2\n得分： 3\n最后得分： 3" data-rows="10"></div>

<ul class="quests" data-key="l11-global">
  <li>🐞 <span class="zh">把 <code>global score</code> 那一行删掉，运行。读一读报错——这是游戏里最常见的 bug 之一！然后加回来。</span><span class="en">Delete the <code>global score</code> line and run. Read the error — one of the most common game bugs! Then put it back.</span></li>
</ul>

---

## 🏗️ <span class="zh">开工：做我的项目</span><span class="en">Build time: my project</span>
{: #build}

<p><span class="zh">打开你的计划（作品墙上的 <code>week10-plan</code>）和第 10 课的<a href="{{ '/lessons/10/learn/' | relative_url }}">骨架代码</a>。<b>一次只做一个功能</b>，做完就测、测完就存。</span><span class="en">Open your plan (<code>week10-plan</code> on the gallery) and the <a href="{{ '/lessons/10/learn/' | relative_url }}">skeleton code</a> from Lesson 10. <b>One feature at a time</b>: build it, test it, save it.</span></p>

<div class="progress" data-for="l11-build"><span></span></div>
<ul class="quests" data-key="l11-build">
  <li><b>📋 <span class="zh">打开我的计划</span><span class="en">Open my plan</span></b><br><span class="zh">功能 1、2、3 分别是什么？念一遍。</span><span class="en">What are features 1, 2, 3? Read them out.</span></li>
  <li><b>🦴 <span class="zh">打开骨架，粘贴到作业画板</span><span class="en">Open the skeleton, paste it into the homework playground</span></b><br><span class="zh">在 <a href="../homework/">作业页</a>的画板里。先运行一次，确认骨架能跑。</span><span class="en">In the playground on the <a href="../homework/">homework page</a>. Run it once to check it works.</span></li>
  <li><b>1️⃣ <span class="zh">做功能 1</span><span class="en">Build feature 1</span></b><br><span class="zh">最小的那个。只写让它<b>能跑</b>的代码，不要漂亮。</span><span class="en">The smallest one. Only enough code to make it <b>run</b>, not pretty.</span></li>
  <li><b>🧪 <span class="zh">测功能 1</span><span class="en">Test feature 1</span></b><br><span class="zh">按下面的测试清单试一遍 + 在 <code>test()</code> 里加一个 <code>assert</code>。</span><span class="en">Go through the test checklist below + add one <code>assert</code> in <code>test()</code>.</span></li>
  <li><b>📤 <span class="zh">存档</span><span class="en">Save</span></b><br><code>week11-project</code></li>
  <li><b>2️⃣ <span class="zh">做功能 2 → 测 → 存</span><span class="en">Feature 2 → test → save</span></b></li>
  <li><b>3️⃣ <span class="zh">做功能 3 → 测 → 存</span><span class="en">Feature 3 → test → save</span></b></li>
  <li><b>📓 <span class="zh">笔记本：最难的 bug 是什么，怎么解决的</span><span class="en">Notebook: the hardest bug and how you fixed it</span></b></li>
</ul>

### 🧪 <span class="zh">测试清单：别人会怎么弄坏它？</span><span class="en">Test checklist: how would someone break it?</span>
{: #tests}

<div class="two">
  <div class="card"><b>🎮 <span class="zh">游戏</span><span class="en">Game</span></b>
    <ul style="font-size:.95rem;margin:.4em 0;padding-left:1.2em">
      <li><span class="zh">一直按同一个键，海龟会跑出画布吗？</span><span class="en">Hold one key: does the turtle leave the canvas?</span></li>
      <li><span class="zh">同时按两个键会怎样？</span><span class="en">Two keys at once?</span></li>
      <li><span class="zh">分数会变成负数吗？</span><span class="en">Can the score go negative?</span></li>
      <li><span class="zh">游戏结束后还能动吗？该不该？</span><span class="en">Can you still move after game over? Should you?</span></li>
    </ul>
  </div>
  <div class="card"><b>📱 <span class="zh">App</span><span class="en">App</span></b>
    <ul style="font-size:.95rem;margin:.4em 0;padding-left:1.2em">
      <li><span class="zh">要数字的时候输入「abc」会崩吗？（<code>try / except</code> 或先检查 <code>isdigit()</code>）</span><span class="en">Type "abc" when it wants a number: crash? (<code>try / except</code> or check <code>isdigit()</code>)</span></li>
      <li><span class="zh">什么都不输直接回车？</span><span class="en">Press Enter with nothing typed?</span></li>
      <li><span class="zh">大写 / 小写 / 多打一个空格（<code>.lower().strip()</code>）</span><span class="en">Upper / lower case / extra space (<code>.lower().strip()</code>)</span></li>
      <li><span class="zh">问完最后一个问题，程序有好好结束吗？</span><span class="en">After the last question, does it end nicely?</span></li>
    </ul>
  </div>
  <div class="card"><b>🎨 <span class="zh">互动艺术</span><span class="en">Interactive art</span></b>
    <ul style="font-size:.95rem;margin:.4em 0;padding-left:1.2em">
      <li><span class="zh">在边角点击会画到外面去吗？</span><span class="en">Click in a corner: does it draw off-screen?</span></li>
      <li><span class="zh">点 100 次会不会越来越慢？</span><span class="en">100 clicks: does it get slow?</span></li>
      <li><span class="zh">有没有办法清空重来？</span><span class="en">Is there a way to clear and restart?</span></li>
    </ul>
  </div>
  <div class="card"><b>🧪 <span class="zh">所有项目</span><span class="en">Every project</span></b>
    <ul style="font-size:.95rem;margin:.4em 0;padding-left:1.2em">
      <li><span class="zh">还原代码，从头运行一次（不是接着上次）</span><span class="en">Reset and run from scratch (not continuing)</span></li>
      <li><span class="zh"><code>test()</code> 全部通过</span><span class="en"><code>test()</code> all pass</span></li>
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
  <div class="bubble me"><span class="zh">我在做接水果游戏。我想让分数每接到一个加 1，但运行时报错：UnboundLocalError: local variable 'score' referenced before assignment。我的函数是：def catch(): score = score + 1。请给我一个提示，不要直接给答案。</span><span class="en">I'm making a catch game. I want the score to go up by 1 each catch, but I get: UnboundLocalError: local variable 'score' referenced before assignment. My function: def catch(): score = score + 1. Please give me a hint, not the answer.</span></div>
  <div class="bubble ai"><span class="zh">提示：函数里面的 score 和外面的 score，电脑默认当成两个不同的东西。有一个关键字可以告诉电脑「我说的是外面那个」——你在第 11 课的小魔法里见过它 😉</span><span class="en">Hint: inside the function, the computer treats score as a brand-new variable, separate from the one outside. There's a keyword that says "I mean the outside one" — you met it in Lesson 11's little magic 😉</span></div>
  <div class="bubble me"><span class="zh">是 global！谢谢，我自己改。</span><span class="en">It's global! Thanks, I'll fix it myself.</span></div>
</div>

<p><span class="zh">👆 好的问法：说了<b>在做什么</b>、<b>想要什么</b>、<b>报错原话</b>、<b>相关的几行</b>，并且要的是<b>提示</b>。</span><span class="en">👆 A good question says <b>what you're making</b>, <b>what you want</b>, <b>the exact error</b>, <b>the few lines involved</b>, and asks for a <b>hint</b>.</span></p>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>🔍 print 侦探</b><code>print("到这里了", x)</code><span><span class="zh">没报错但答案不对：让程序把心里的数说出来</span><span class="en">No error but wrong answer: make it say what it's thinking</span></span></div>
  <div class="k"><b>📜 读报错</b><code>第几行 → 错误种类 → 原话 → 看那行</code><span><span class="zh">红字是藏宝图</span><span class="en">Red text is a treasure map</span></span></div>
  <div class="k"><b>🦆 小黄鸭</b><code>"第 3 行是说……"</code><span><span class="zh">念出来，自己就发现了</span><span class="en">Say it out loud and you'll see it</span></span></div>
  <div class="k"><b>✂️ 二分法</b><code># 注释掉一半</code><span><span class="zh">对 → 问题在另一半</span><span class="en">Works → the bug is in the other half</span></span></div>
  <div class="k"><b>⌨️ 键盘</b><code>screen.onkey(go, "Left")
screen.listen()</code><span><span class="zh">函数名不加括号</span><span class="en">Function name, no brackets</span></span></div>
  <div class="k"><b>⏱️ 心跳</b><code>def tick():
    ...
    screen.ontimer(tick, 50)
tick()</code><span><span class="zh">自己叫自己 = 一直跑</span><span class="en">Calls itself = keeps going</span></span></div>
  <div class="k"><b>🖱️ 点击</b><code>def hit(x, y): ...
screen.onclick(hit)</code><span><span class="zh">电脑把 x, y 交给你</span><span class="en">The computer hands you x, y</span></span></div>
  <div class="k"><b>🧮 global</b><code>def add():
    global score
    score += 1</code><span><span class="zh">函数里改外面的变量</span><span class="en">Change an outside variable inside a function</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令在 <a href="{{ '/cheatsheet/' | relative_url }}#l11">📖 小词典 · 第 11 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l11">📖 cheat sheet · Lesson 11</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/11/homework/' | relative_url }}"><span class="zh">下一步：把项目做完 🏠 →</span><span class="en">Next: finish the project 🏠 →</span></a></p>
