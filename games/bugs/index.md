---
title: 虫虫医院
title_en: Bug Hospital
playground: true
---

# 🐞 <span class="zh">虫虫医院</span><span class="en">Bug Hospital</span>

<p class="zh">欢迎，医生！这里的每一段代码都<b>生病了</b>——里面藏着 1 到 3 只 bug（错误）。你的任务：运行它、<b>读红色的报错框</b>、找到 bug、治好它，让程序打印出和「需要的输出」一模一样的东西。治好一个病号得一颗星 ⭐。</p>
<p class="en">Welcome, doctor! Every program here is <b>sick</b> — it has 1 to 3 bugs hiding inside. Your job: run it, <b>read the red error box</b>, find the bug, fix it, and make the program print exactly the "wanted output". Each patient you cure earns a star ⭐.</p>

## 🩺 <span class="zh">报错怎么读</span><span class="en">How to read an error</span>

<p><span class="zh">红框会告诉你三件事。按这个顺序看：</span><span class="en">The red box tells you three things. Read them in this order:</span></p>
<ol class="code-walk">
  <li><code>🐞 第 7 行出了个小问题</code><span><span class="zh"><b>第几行</b>——先去看那一行（有时候真正的错在<b>上一行</b>）</span><span class="en"><b>Which line</b> — look there first (sometimes the real bug is on the <b>line above</b>)</span></span></li>
  <li><code>电脑看不懂这一行的写法…</code><span><span class="zh"><b>用你的话说的解释</b>——它会提醒你检查什么</span><span class="en"><b>An explanation in plain words</b> — it tells you what to check</span></span></li>
  <li><code>SyntaxError: bad input</code><span><span class="zh"><b>电脑的原话</b>——报错的<b>名字</b>（SyntaxError = 写法不对，NameError = 不认识这个名字，IndexError = 列表没这一格，TypeError = 种类搞混了）</span><span class="en"><b>What the computer said</b> — the error's <b>name</b> (SyntaxError = badly written, NameError = unknown name, IndexError = no such list item, TypeError = wrong kind of thing)</span></span></li>
</ol>
<div class="box box-good"><span class="zh">💡 一次只治一只 bug：改一点 → 运行 → 看看报错变了没有 → 再改。<b>报错变了就是进步！</b></span><span class="en">💡 Cure one bug at a time: change a little → run → did the error change? → change again. <b>A different error means progress!</b></span></div>

<div class="levels-bar">
  <a href="#lv1" data-badge-id="bugs-1">1</a><a href="#lv2" data-badge-id="bugs-2">2</a><a href="#lv3" data-badge-id="bugs-3">3</a><a href="#lv4" data-badge-id="bugs-4">4</a><a href="#lv5" data-badge-id="bugs-5">5</a><a href="#lv6" data-badge-id="bugs-6">6</a>
</div>

<div class="level-head" id="lv1" data-badge-id="bugs-1"><span class="lv"><span class="zh">病号 1</span><span class="en">Patient 1</span></span><b><span class="zh">少了点什么</span><span class="en">Something is missing</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">需要的输出：两行 <code>Hello, bug hunter!</code> 和 <code>Welcome to the Bug Hospital</code>。里面有 <b>2</b> 只 bug。</span><span class="en">Wanted output: two lines, <code>Hello, bug hunter!</code> and <code>Welcome to the Bug Hospital</code>. There are <b>2</b> bugs.</span></div>
<div class="playground" data-src="{{ '/games/bugs/code/level1-start.py' | relative_url }}" data-title="🐞 病号 1" data-title-en="🐞 Patient 1" data-save="bugs-1" data-draft="bugs-1" data-rows="8" data-canvas="no" data-expect="Hello, bug hunter!\nWelcome to the Bug Hospital" data-badge="bugs-1"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">引号 <code>"</code> 和括号 <code>( )</code> 都是<b>成对</b>出现的。数一数每一行有几个。</span><span class="en">Quotes <code>"</code> and brackets <code>( )</code> always come in <b>pairs</b>. Count them on each line.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">第一行少一个 <code>"</code>，第二行少一个 <code>)</code>。</span><span class="en">The first line is missing a <code>"</code>; the second is missing a <code>)</code>.</span></details>

<div class="level-head" id="lv2" data-badge-id="bugs-2"><span class="lv"><span class="zh">病号 2</span><span class="en">Patient 2</span></span><b><span class="zh">长得像，但不一样</span><span class="en">Looks the same, but isn't</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">需要的输出：<code>Hi Kiwi</code> 和 <code>You are a coder</code>。<b>2</b> 只 bug，都很会伪装！</span><span class="en">Wanted output: <code>Hi Kiwi</code> and <code>You are a coder</code>. <b>2</b> bugs, both in disguise!</span></div>
<div class="playground" data-src="{{ '/games/bugs/code/level2-start.py' | relative_url }}" data-title="🐞 病号 2" data-title-en="🐞 Patient 2" data-save="bugs-2" data-draft="bugs-2" data-rows="8" data-canvas="no" data-expect="Hi Kiwi\nYou are a coder" data-badge="bugs-2"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">电脑分大小写：<code>Print</code> 和 <code>print</code> 不是同一个东西。</span><span class="en">Computers care about capitals: <code>Print</code> and <code>print</code> are not the same.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">仔细看最后一行的括号：<code>（ ）</code> 是中文括号，电脑要的是英文的 <code>( )</code>。把输入法切到英文重新打。</span><span class="en">Look closely at the brackets on the last line: <code>（ ）</code> are Chinese brackets; the computer wants English <code>( )</code>. Switch your keyboard to English and retype them.</span></details>

<div class="level-head" id="lv3" data-badge-id="bugs-3"><span class="lv"><span class="zh">病号 3</span><span class="en">Patient 3</span></span><b><span class="zh">if 生病了</span><span class="en">A sick if</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">需要的输出：<code>Year 6!</code> 和 <code>Done</code>。<b>2</b> 只 bug，都在 <code>if</code> 那一行。</span><span class="en">Wanted output: <code>Year 6!</code> and <code>Done</code>. <b>2</b> bugs, both on the <code>if</code> line.</span></div>
<div class="playground" data-src="{{ '/games/bugs/code/level3-start.py' | relative_url }}" data-title="🐞 病号 3" data-title-en="🐞 Patient 3" data-save="bugs-3" data-draft="bugs-3" data-rows="10" data-canvas="no" data-expect="Year 6!\nDone" data-badge="bugs-3"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">一个 <code>=</code> 是「把右边放进左边」；问「是不是相等」要用<b>两个</b>：<code>==</code>。</span><span class="en">One <code>=</code> means "put the right side into the left"; asking "are they equal?" needs <b>two</b>: <code>==</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh"><code>if</code>、<code>else</code>、<code>for</code> 这些行的<b>最后</b>都要有冒号 <code>:</code>。看看 <code>else:</code> 有，<code>if</code> 那行呢？</span><span class="en"><code>if</code>, <code>else</code> and <code>for</code> lines all need a colon <code>:</code> at the <b>end</b>. <code>else:</code> has one — what about the <code>if</code> line?</span></details>

<div class="level-head" id="lv4" data-badge-id="bugs-4"><span class="lv"><span class="zh">病号 4</span><span class="en">Patient 4</span></span><b><span class="zh">倒数发射</span><span class="en">Countdown</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">需要的输出：<code>1 2 3 4 5</code> 每个一行，然后 <code>Blast off!</code>。<b>2</b> 只 bug：一只让它报错，另一只让它少数一个数。</span><span class="en">Wanted output: <code>1 2 3 4 5</code> one per line, then <code>Blast off!</code>. <b>2</b> bugs: one causes an error, the other makes it count one number short.</span></div>
<div class="playground" data-src="{{ '/games/bugs/code/level4-start.py' | relative_url }}" data-title="🐞 病号 4" data-title-en="🐞 Patient 4" data-save="bugs-4" data-draft="bugs-4" data-rows="8" data-canvas="no" data-expect="1\n2\n3\n4\n5\nBlast off!" data-badge="bugs-4"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">属于 <code>for</code> 的那一行要往右<b>缩进 4 个空格</b>。<code>Blast off!</code> 只打印一次，所以它<b>不</b>缩进。</span><span class="en">The line that belongs to the <code>for</code> must be <b>indented 4 spaces</b>. <code>Blast off!</code> prints only once, so it is <b>not</b> indented.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh"><code>range(1, 5)</code> 数的是 1、2、3、4——<b>最后那个数不算</b>！想数到 5，要写 <code>range(1, 6)</code>。</span><span class="en"><code>range(1, 5)</code> counts 1, 2, 3, 4 — <b>the last number is left out</b>! To reach 5, write <code>range(1, 6)</code>.</span></details>

<div class="level-head" id="lv5" data-badge-id="bugs-5"><span class="lv"><span class="zh">病号 5</span><span class="en">Patient 5</span></span><b><span class="zh">水果篮</span><span class="en">The fruit basket</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">需要的输出：<code>banana</code> 和 <code>I have 3 fruits</code>。<b>2</b> 只 bug，治好第一只才会看到第二只。</span><span class="en">Wanted output: <code>banana</code> and <code>I have 3 fruits</code>. <b>2</b> bugs — you'll only see the second after curing the first.</span></div>
<div class="playground" data-src="{{ '/games/bugs/code/level5-start.py' | relative_url }}" data-title="🐞 病号 5" data-title-en="🐞 Patient 5" data-save="bugs-5" data-draft="bugs-5" data-rows="8" data-canvas="no" data-expect="banana\nI have 3 fruits" data-badge="bugs-5"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">列表有 3 样东西，但格子的号码是 <code>0、1、2</code>——没有第 3 格！banana 在第几格？</span><span class="en">The list has 3 things, but the slots are numbered <code>0, 1, 2</code> — there is no slot 3! Which slot is banana in?</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">NameError 说「不认识 fruit」——列表的名字是 <code>fruits</code>，多了一个 s。</span><span class="en">The NameError says "fruit is not defined" — the list is called <code>fruits</code>, with an s.</span></details>

<div class="level-head" id="lv6" data-badge-id="bugs-6"><span class="lv"><span class="zh">病号 6</span><span class="en">Patient 6</span></span><b><span class="zh">两个 bug 的重病号</span><span class="en">A serious case</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">需要的输出：<code>Total: 12</code>（2 + 4 + 6）。<b>2</b> 只 bug：一只在函数里，一只在 <code>while</code> 里。⚠️ 治好第一只以后程序可能<b>停不下来</b>——点「■ 停下」，想想为什么。</span><span class="en">Wanted output: <code>Total: 12</code> (2 + 4 + 6). <b>2</b> bugs: one in the function, one in the <code>while</code>. ⚠️ After curing the first, the program may <b>never stop</b> — click "■ Stop" and think about why.</span></div>
<div class="playground" data-src="{{ '/games/bugs/code/level6-start.py' | relative_url }}" data-title="🐞 病号 6" data-title-en="🐞 Patient 6" data-save="bugs-6" data-draft="bugs-6" data-rows="12" data-canvas="no" data-expect="Total: 12" data-badge="bugs-6"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">TypeError 说「int 和 NoneType 不能相加」：函数 <code>double</code> 算了 <code>n * 2</code>，但<b>没有把结果交出来</b>。交出来要用 <code>return</code>。</span><span class="en">The TypeError says "can't add int and NoneType": the function <code>double</code> works out <code>n * 2</code> but <b>never hands it back</b>. Handing back needs <code>return</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">停不下来是因为 <code>count</code> 永远是 1，<code>count &lt;= 3</code> 永远是 True。在循环里让它每次加 1：<code>count += 1</code>（要缩进！）。</span><span class="en">It never stops because <code>count</code> stays 1, so <code>count &lt;= 3</code> is always True. Make it grow inside the loop: <code>count += 1</code> (indented!).</span></details>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 医生毕业了！</span><span class="en">🧠 Doctor, you've graduated!</span></span>
<span class="zh">把你今天认识的报错名字写进 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 的「我遇到过的报错」表格里。下次再看到它们，你就是专家。</span>
<span class="en">Write the error names you met today into the "Errors I've met" table in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>. Next time you see them, you're the expert.</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
