---
title: 读心术
title_en: Mind Reader
playground: true
---

# 🔮 <span class="zh">读心术</span><span class="en">Mind Reader</span>

<p class="zh">真正的程序员有一种超能力：<b>不运行，光看代码就知道它会做什么</b>。这个游戏练的就是这个。每一题：① 先读代码，② 猜它会打印什么，③ 点一个答案，④ 再点 ▶ 运行验证。猜错了也没关系——想一想为什么，比猜对更重要。每关 3 题，答对最后一题得星 ⭐。</p>
<p class="en">Real programmers have a superpower: <b>they can tell what code does just by reading it</b>. This game trains that. For each question: (1) read the code, (2) guess what it prints, (3) click an answer, (4) click ▶ Run to check. Wrong guesses are fine — working out why matters more. 3 questions per level; the last one earns the star ⭐.</p>

<div class="box box-tip"><span class="zh">🕵️ 读代码的秘诀：<b>一行一行</b>，像电脑一样老实。用手指着每一行，嘴里说出「现在 x 是多少」。</span><span class="en">🕵️ The secret to reading code: go <b>one line at a time</b>, as literally as the computer does. Point at each line and say out loud "right now x is …".</span></div>

<div class="box box-think"><span class="zh">🧗 第 7–9 关更难：代码里有<b>循环套循环、break、return、会变的列表</b>。光靠「看一眼」不够了——拿张纸，画一张表，把每个变量每一步的值写下来（这叫<b>追踪</b>）。</span><span class="en">🧗 Levels 7–9 are harder: <b>loops inside loops, break, return, and lists that change</b>. A quick glance won't do — grab paper, draw a table, and write down every variable's value at every step (that's called <b>tracing</b>).</span></div>

<div class="levels-bar">
<a href="#lv1" data-badge-id="reader-1">1</a><a href="#lv2" data-badge-id="reader-2">2</a><a href="#lv3" data-badge-id="reader-3">3</a><a href="#lv4" data-badge-id="reader-4">4</a><a href="#lv5" data-badge-id="reader-5">5</a><a href="#lv6" data-badge-id="reader-6">6</a><a href="#lv7" data-badge-id="reader-7">7</a><a href="#lv8" data-badge-id="reader-8">8</a><a href="#lv9" data-badge-id="reader-9">9</a>
</div>

<div class="level-head" id="lv1" data-badge-id="reader-1"><span class="lv"><span class="zh">第 1 关</span><span class="en">Level 1</span></span><b><span class="zh">打招呼和变量</span><span class="en">Hello and variables</span></b><span class="pill">📘 <span class="zh">需要第 2 课</span><span class="en">Needs Lesson 2</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>name = &quot;Kiwi&quot;
print(&quot;Hi&quot;, name)
print(&quot;Hi name&quot;)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>Hi Kiwi<br>Hi Kiwi</button><button>Hi Kiwi<br>Hi name</button><button>Hi name<br>Hi name</button></div>
  <div class="why"><span class="zh">第 2 行的 name 没有引号，是变量，会换成 Kiwi；第 3 行的 name 在引号里，就只是普通的字。</span><span class="en">On line 2, name has no quotes, so it's the variable and becomes Kiwi; on line 3 it's inside quotes, so it's just text.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-1-1" data-rows="4" data-canvas="no"><textarea>name = &quot;Kiwi&quot;
print(&quot;Hi&quot;, name)
print(&quot;Hi name&quot;)
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>a = 5
b = 3
print(a + b)
print(&quot;a + b&quot;)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>8<br>8</button><button>8<br>a + b</button><button>53<br>a + b</button><button>5 + 3<br>a + b</button></div>
  <div class="why"><span class="zh">a + b 没引号就是算数，5 + 3 = 8；加了引号就原样打印。</span><span class="en">Without quotes a + b is maths: 5 + 3 = 8. With quotes it prints as written.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-1-2" data-rows="4" data-canvas="no"><textarea>a = 5
b = 3
print(a + b)
print(&quot;a + b&quot;)
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>x = 10
x = x + 5
y = x
x = 1
print(x, y)</pre>
</div><div>
<div class="quiz" data-answer="1" data-badge="reader-1">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>1 15</button><button>1 1</button><button>15 15</button><button>10 15</button></div>
  <div class="why"><span class="zh">y = x 的时候 x 是 15，所以 y 记住了 15。后来 x 变成 1，y 不会跟着变。</span><span class="en">When y = x runs, x is 15, so y remembers 15. Changing x to 1 later doesn't change y.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-1-3" data-rows="4" data-canvas="no"><textarea>x = 10
x = x + 5
y = x
x = 1
print(x, y)
</textarea></div>

<div class="level-head" id="lv2" data-badge-id="reader-2"><span class="lv"><span class="zh">第 2 关</span><span class="en">Level 2</span></span><b><span class="zh">for 循环</span><span class="en">for loops</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>for i in range(3):
    print(&quot;Hop&quot;)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>Hop<br>Hop</button><button>Hop<br>Hop<br>Hop</button><button>Hop<br>Hop<br>Hop<br>Hop</button></div>
  <div class="why"><span class="zh">range(3) 是 0、1、2，一共 3 次。</span><span class="en">range(3) gives 0, 1, 2 — three times.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-2-1" data-rows="4" data-canvas="no"><textarea>for i in range(3):
    print(&quot;Hop&quot;)
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>for i in range(1, 4):
    print(i)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>1<br>2<br>3<br>4</button><button>1<br>2<br>3</button><button>0<br>1<br>2<br>3</button></div>
  <div class="why"><span class="zh">range(1, 4) 从 1 开始，到 4 之前停：1、2、3。最后那个数不算！</span><span class="en">range(1, 4) starts at 1 and stops before 4: 1, 2, 3. The end number is left out!</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-2-2" data-rows="4" data-canvas="no"><textarea>for i in range(1, 4):
    print(i)
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>total = 0
for i in range(5):
    total = total + i
print(total)</pre>
</div><div>
<div class="quiz" data-answer="2" data-badge="reader-2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>15</button><button>10</button><button>5</button><button>4</button></div>
  <div class="why"><span class="zh">range(5) 是 0+1+2+3+4 = 10（没有 5）。</span><span class="en">range(5) is 0+1+2+3+4 = 10 (there's no 5).</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-2-3" data-rows="4" data-canvas="no"><textarea>total = 0
for i in range(5):
    total = total + i
print(total)
</textarea></div>

<div class="level-head" id="lv3" data-badge-id="reader-3"><span class="lv"><span class="zh">第 3 关</span><span class="en">Level 3</span></span><b><span class="zh">if / elif / else</span><span class="en">if / elif / else</span></b><span class="pill">📘 <span class="zh">需要第 4 课</span><span class="en">Needs Lesson 4</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>score = 7
if score &gt; 7:
    print(&quot;Great&quot;)
else:
    print(&quot;OK&quot;)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>Great</button><button>OK</button><button><span class="zh">（什么都不打印）</span><span class="en">(prints nothing)</span></button></div>
  <div class="why"><span class="zh">7 > 7 是 False（7 不比 7 大），所以走 else。</span><span class="en">7 > 7 is False (7 isn't bigger than 7), so it goes to else.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-3-1" data-rows="4" data-canvas="no"><textarea>score = 7
if score &gt; 7:
    print(&quot;Great&quot;)
else:
    print(&quot;OK&quot;)
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>t = 25
if t &gt; 30:
    print(&quot;Hot&quot;)
elif t &gt; 20:
    print(&quot;Warm&quot;)
elif t &gt; 10:
    print(&quot;Cool&quot;)
else:
    print(&quot;Cold&quot;)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>Hot</button><button>Warm</button><button>Cool</button><button>Warm<br>Cool</button></div>
  <div class="why"><span class="zh">25 > 30 不对，25 > 20 对 → 打印 Warm，然后整个 if 就结束了，不会再看后面的 elif。</span><span class="en">25 > 30 is False, 25 > 20 is True → Warm. Then the whole if is finished; the later elifs are skipped.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-3-2" data-rows="4" data-canvas="no"><textarea>t = 25
if t &gt; 30:
    print(&quot;Hot&quot;)
elif t &gt; 20:
    print(&quot;Warm&quot;)
elif t &gt; 10:
    print(&quot;Cool&quot;)
else:
    print(&quot;Cold&quot;)
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>n = 12
if n % 2 == 0:
    print(&quot;even&quot;)
if n &gt; 10:
    print(&quot;big&quot;)
print(&quot;done&quot;)</pre>
</div><div>
<div class="quiz" data-answer="2" data-badge="reader-3">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>even<br>done</button><button>even<br>big<br>done</button><button>big<br>done</button></div>
  <div class="why"><span class="zh">这是两个独立的 if（不是 elif），两个都会检查：12 是偶数，12 也大于 10。</span><span class="en">These are two separate ifs (not elif), so both are checked: 12 is even and 12 is bigger than 10.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-3-3" data-rows="4" data-canvas="no"><textarea>n = 12
if n % 2 == 0:
    print(&quot;even&quot;)
if n &gt; 10:
    print(&quot;big&quot;)
print(&quot;done&quot;)
</textarea></div>

<div class="level-head" id="lv4" data-badge-id="reader-4"><span class="lv"><span class="zh">第 4 关</span><span class="en">Level 4</span></span><b><span class="zh">列表</span><span class="en">Lists</span></b><span class="pill">📘 <span class="zh">需要第 5 课</span><span class="en">Needs Lesson 5</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>pets = [&quot;cat&quot;, &quot;dog&quot;, &quot;fish&quot;]
print(pets[1])
print(len(pets))</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>cat<br>3</button><button>dog<br>3</button><button>dog<br>2</button></div>
  <div class="why"><span class="zh">格子从 0 数起：[0] cat、[1] dog、[2] fish。len 数的是有几样东西：3。</span><span class="en">Slots start at 0: [0] cat, [1] dog, [2] fish. len counts how many things: 3.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-4-1" data-rows="4" data-canvas="no"><textarea>pets = [&quot;cat&quot;, &quot;dog&quot;, &quot;fish&quot;]
print(pets[1])
print(len(pets))
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>nums = [4, 8, 15]
nums.append(16)
print(nums[-1])
print(nums[0] + nums[1])</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>15<br>12</button><button>16<br>12</button><button>16<br>4 8</button></div>
  <div class="why"><span class="zh">append 把 16 加到最后，[-1] 就是最后一个。nums[0] + nums[1] 是数字相加 4 + 8 = 12。</span><span class="en">append puts 16 at the end, and [-1] is the last one. nums[0] + nums[1] adds numbers: 4 + 8 = 12.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-4-2" data-rows="4" data-canvas="no"><textarea>nums = [4, 8, 15]
nums.append(16)
print(nums[-1])
print(nums[0] + nums[1])
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>colours = [&quot;red&quot;, &quot;gold&quot;, &quot;blue&quot;]
for c in colours:
    print(c.upper())
print(colours)</pre>
</div><div>
<div class="quiz" data-answer="2" data-badge="reader-4">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>red<br>gold<br>blue<br>[&#x27;red&#x27;, &#x27;gold&#x27;, &#x27;blue&#x27;]</button><button>RED<br>GOLD<br>BLUE<br>[&#x27;red&#x27;, &#x27;gold&#x27;, &#x27;blue&#x27;]</button><button>RED<br>GOLD<br>BLUE<br>[&#x27;RED&#x27;, &#x27;GOLD&#x27;, &#x27;BLUE&#x27;]</button></div>
  <div class="why"><span class="zh">c.upper() 只是打印大写的那一刻，列表里的字没有被改。</span><span class="en">c.upper() only makes a capital copy for printing; the words in the list are not changed.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-4-3" data-rows="4" data-canvas="no"><textarea>colours = [&quot;red&quot;, &quot;gold&quot;, &quot;blue&quot;]
for c in colours:
    print(c.upper())
print(colours)
</textarea></div>

<div class="level-head" id="lv5" data-badge-id="reader-5"><span class="lv"><span class="zh">第 5 关</span><span class="en">Level 5</span></span><b><span class="zh">while 和 and / or</span><span class="en">while and and / or</span></b><span class="pill">📘 <span class="zh">需要第 6 课</span><span class="en">Needs Lesson 6</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>n = 1
while n &lt; 5:
    n = n + 2
print(n)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>4</button><button>5</button><button>7</button><button>3</button></div>
  <div class="why"><span class="zh">n 是 1 → 3 → 5。到 5 的时候 5 < 5 不成立，循环停下，打印 5。</span><span class="en">n goes 1 → 3 → 5. When it's 5, 5 < 5 is False, the loop stops, and 5 is printed.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-5-1" data-rows="4" data-canvas="no"><textarea>n = 1
while n &lt; 5:
    n = n + 2
print(n)
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>count = 0
while count &lt; 3:
    print(&quot;tick&quot;, count)
    count += 1
print(&quot;end&quot;)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>tick 1<br>tick 2<br>tick 3<br>end</button><button>tick 0<br>tick 1<br>tick 2<br>end</button><button>tick 0<br>tick 1<br>tick 2<br>tick 3<br>end</button></div>
  <div class="why"><span class="zh">count 从 0 开始，打印后才加 1；到 3 的时候 3 < 3 不成立就停了。</span><span class="en">count starts at 0 and grows after printing; at 3, 3 < 3 is False so it stops.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-5-2" data-rows="4" data-canvas="no"><textarea>count = 0
while count &lt; 3:
    print(&quot;tick&quot;, count)
    count += 1
print(&quot;end&quot;)
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>age = 11
has_ticket = False
if age &gt; 10 and has_ticket:
    print(&quot;Enter&quot;)
elif age &gt; 10 or has_ticket:
    print(&quot;Almost&quot;)
else:
    print(&quot;No&quot;)</pre>
</div><div>
<div class="quiz" data-answer="2" data-badge="reader-5">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>Enter</button><button>Almost</button><button>No</button></div>
  <div class="why"><span class="zh">and 要两边都对：有票是 False，所以第一个不行。or 只要一边对：年龄够了，所以 Almost。</span><span class="en">and needs both sides True: has_ticket is False, so no. or needs just one side: the age is fine, so Almost.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-5-3" data-rows="4" data-canvas="no"><textarea>age = 11
has_ticket = False
if age &gt; 10 and has_ticket:
    print(&quot;Enter&quot;)
elif age &gt; 10 or has_ticket:
    print(&quot;Almost&quot;)
else:
    print(&quot;No&quot;)
</textarea></div>

<div class="level-head" id="lv6" data-badge-id="reader-6"><span class="lv"><span class="zh">第 6 关</span><span class="en">Level 6</span></span><b><span class="zh">函数和字典</span><span class="en">Functions and dictionaries</span></b><span class="pill">📘 <span class="zh">需要第 7 + 9 课</span><span class="en">Needs Lessons 7 + 9</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>def greet(name):
    return &quot;Hi &quot; + name

msg = greet(&quot;Kiwi&quot;)
print(msg)
print(greet(&quot;Tui&quot;))</pre>
</div><div>
<div class="quiz" data-answer="1">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>Hi Kiwi<br>Hi Tui</button><button>Hi name<br>Hi name</button><button>Hi Kiwi<br>Hi Kiwi</button></div>
  <div class="why"><span class="zh">每次调用 greet，name 就是括号里给的那个词，return 把拼好的句子交回来。</span><span class="en">Each time greet is called, name is the word in the brackets, and return hands back the finished sentence.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-6-1" data-rows="4" data-canvas="no"><textarea>def greet(name):
    return &quot;Hi &quot; + name

msg = greet(&quot;Kiwi&quot;)
print(msg)
print(greet(&quot;Tui&quot;))
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>def add(a, b):
    return a + b

x = add(2, 3)
y = add(x, x)
print(y)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>5</button><button>10</button><button>2 3</button><button>25</button></div>
  <div class="why"><span class="zh">x = add(2, 3) = 5，然后 y = add(5, 5) = 10。</span><span class="en">x = add(2, 3) = 5, then y = add(5, 5) = 10.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-6-2" data-rows="4" data-canvas="no"><textarea>def add(a, b):
    return a + b

x = add(2, 3)
y = add(x, x)
print(y)
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>words = {&quot;kia ora&quot;: &quot;hello&quot;, &quot;ka pai&quot;: &quot;good&quot;}
print(words[&quot;ka pai&quot;])
print(len(words))
print(&quot;hello&quot; in words)</pre>
</div><div>
<div class="quiz" data-answer="2" data-badge="reader-6">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>good<br>2<br>True</button><button>good<br>2<br>False</button><button>hello<br>2<br>False</button></div>
  <div class="why"><span class="zh">字典用钥匙（左边）找值（右边）。in 只检查钥匙：hello 是值不是钥匙，所以 False。</span><span class="en">A dictionary uses keys (left) to find values (right). in only checks the keys: hello is a value, not a key, so False.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-6-3" data-rows="4" data-canvas="no"><textarea>words = {&quot;kia ora&quot;: &quot;hello&quot;, &quot;ka pai&quot;: &quot;good&quot;}
print(words[&quot;ka pai&quot;])
print(len(words))
print(&quot;hello&quot; in words)
</textarea></div>

<div class="level-head" id="lv7" data-badge-id="reader-7"><span class="lv"><span class="zh">第 7 关</span><span class="en">Level 7</span></span><b><span class="zh">循环里的循环</span><span class="en">Loops inside loops</span></b><span class="pill">📘 <span class="zh">需要第 3 + 4 课</span><span class="en">Needs Lessons 3 + 4</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>count = 0
for i in range(3):
    for j in range(4):
        count = count + 1
print(count)</pre>
</div><div>
<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>7</button><button>4</button><button>12</button><button>3</button></div>
  <div class="why"><span class="zh">外面转 3 圈，<b>每一圈</b>里面都要转满 4 次：3 × 4 = 12。不是 3 + 4！</span><span class="en">The outer loop runs 3 times, and <b>each time</b> the inner loop runs 4 times: 3 × 4 = 12. Not 3 + 4!</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-7-1" data-rows="4" data-canvas="no"><textarea>count = 0
for i in range(3):
    for j in range(4):
        count = count + 1
print(count)
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>for i in range(3):
    for j in range(i):
        print(i, j)</pre>
</div><div>
<div class="quiz" data-answer="1">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>1 0<br>2 0<br>2 1</button><button>0 0<br>1 0<br>1 1<br>2 0<br>2 1<br>2 2</button><button>1 1<br>2 1<br>2 2</button><button>0 0<br>1 0<br>2 0</button></div>
  <div class="why"><span class="zh">里面的 range(i) 跟着 i 变：i = 0 时 range(0) 是空的，一次都不跑；i = 1 时 j 只有 0；i = 2 时 j 是 0、1。range 的最后一个数不算！</span><span class="en">The inner range(i) changes with i: when i = 0, range(0) is empty and runs zero times; when i = 1, j is only 0; when i = 2, j is 0, 1. The end number of range is left out!</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-7-2" data-rows="4" data-canvas="no"><textarea>for i in range(3):
    for j in range(i):
        print(i, j)
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>total = 0
for i in range(1, 4):
    for j in range(1, 4):
        if j == i:
            break
        total = total + j
print(total)</pre>
</div><div>
<div class="quiz" data-answer="2" data-badge="reader-7">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>0</button><button>4</button><button>10</button><button>12</button></div>
  <div class="why"><span class="zh">break 只跳出<b>它所在的那一层</b>（里面的循环），外面的循环继续。i = 1：j = 1 马上 break，加 0；i = 2：加 1，然后 break；i = 3：加 1 和 2，然后 break。0 + 1 + 3 = 4。break 在加法前面，所以 j == i 那一次不加。</span><span class="en">break only leaves <b>the loop it is in</b> (the inner one); the outer loop keeps going. i = 1: j = 1 breaks straight away, adds 0; i = 2: adds 1, then breaks; i = 3: adds 1 and 2, then breaks. 0 + 1 + 3 = 4. The break comes before the adding, so the j == i round adds nothing.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-7-3" data-rows="4" data-canvas="no"><textarea>total = 0
for i in range(1, 4):
    for j in range(1, 4):
        if j == i:
            break
        total = total + j
print(total)
</textarea></div>

<div class="level-head" id="lv8" data-badge-id="reader-8"><span class="lv"><span class="zh">第 8 关</span><span class="en">Level 8</span></span><b><span class="zh">while、break 和函数</span><span class="en">while, break and functions</span></b><span class="pill">📘 <span class="zh">需要第 6 + 7 课</span><span class="en">Needs Lessons 6 + 7</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>n = 1
while True:
    n = n * 2
    if n &gt; 20:
        break
    print(n)
print(&quot;end&quot;, n)</pre>
</div><div>
<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>2<br>4<br>8<br>16<br>end 16</button><button>2<br>4<br>8<br>16<br>32<br>end 32</button><button>2<br>4<br>8<br>16<br>end 32</button><button>1<br>2<br>4<br>8<br>16<br>end 32</button></div>
  <div class="why"><span class="zh">顺序很重要：先乘 2，再检查，最后才 print。n 变成 32 的时候，32 > 20，break 马上跳出——32 来不及 print。但 n 已经是 32 了，所以最后是 end 32。</span><span class="en">Order matters: double first, then check, and only then print. When n becomes 32, 32 > 20 and break jumps out at once — 32 never gets printed. But n is already 32, so the last line is end 32.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-8-1" data-rows="4" data-canvas="no"><textarea>n = 1
while True:
    n = n * 2
    if n &gt; 20:
        break
    print(n)
print(&quot;end&quot;, n)
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>def grow(x):
    x = x + 10
    return x

x = 5
y = grow(grow(x))
print(x, y)</pre>
</div><div>
<div class="quiz" data-answer="4">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>25 25</button><button>5 15</button><button>15 25</button><button>5 25</button></div>
  <div class="why"><span class="zh">grow(grow(5))：里面的先算，grow(5) = 15，再 grow(15) = 25。函数里的 x 是<b>它自己的</b>x（参数），改它不会改外面的 x，所以外面的 x 还是 5。</span><span class="en">grow(grow(5)): the inner one runs first, grow(5) = 15, then grow(15) = 25. The x inside the function is <b>its own</b> x (the parameter); changing it doesn't touch the x outside, which stays 5.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-8-2" data-rows="4" data-canvas="no"><textarea>def grow(x):
    x = x + 10
    return x

x = 5
y = grow(grow(x))
print(x, y)
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>def check(n):
    for i in range(2, n):
        if n % i == 0:
            return &quot;no&quot;
    return &quot;yes&quot;

print(check(7), check(9), check(2))</pre>
</div><div>
<div class="quiz" data-answer="3" data-badge="reader-8">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>yes no no</button><button>yes<br>no<br>yes</button><button>yes no yes</button><button>yes yes yes</button></div>
  <div class="why"><span class="zh">return 一执行，函数<b>马上结束</b>。check(9)：i = 3 时 9 % 3 == 0，立刻 return "no"。check(7)：2–6 都除不尽，循环跑完才 return "yes"。check(2)：range(2, 2) 是空的，循环一次都不跑，直接 return "yes"。一个 print 里用逗号分开，所以在同一行。</span><span class="en">As soon as return runs, the function <b>ends</b>. check(9): at i = 3, 9 % 3 == 0, so it returns "no" right away. check(7): nothing from 2 to 6 divides it, so the loop finishes and it returns "yes". check(2): range(2, 2) is empty, the loop never runs, and it returns "yes". One print with commas puts them on one line.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-8-3" data-rows="4" data-canvas="no"><textarea>def check(n):
    for i in range(2, n):
        if n % i == 0:
            return &quot;no&quot;
    return &quot;yes&quot;

print(check(7), check(9), check(2))
</textarea></div>

<div class="level-head" id="lv9" data-badge-id="reader-9"><span class="lv"><span class="zh">第 9 关</span><span class="en">Level 9</span></span><b><span class="zh">列表、字符串和字典</span><span class="en">Lists, strings and dictionaries</span></b><span class="pill">📘 <span class="zh">需要第 5 + 8 + 9 课</span><span class="en">Needs Lessons 5 + 8 + 9</span></span><span class="done-mark">⭐</span></div>
<h3>🔮 <span class="zh">第 1 题</span><span class="en">Question 1</span></h3>
<div class="two"><div>
<pre>nums = [3, 1, 4]
for x in nums:
    x = x * 10
print(nums)
for i in range(len(nums)):
    nums[i] = nums[i] * 10
print(nums)</pre>
</div><div>
<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>[30, 10, 40]<br>[300, 100, 400]</button><button>[3, 1, 4]<br>[30, 10, 40]</button><button>[30, 10, 40]<br>[30, 10, 40]</button><button>[3, 1, 4]<br>[3, 1, 4]</button></div>
  <div class="why"><span class="zh">第一个循环里，x 只是从列表里<b>抄出来</b>的一个数，x = x * 10 改的是抄本，列表没变。第二个循环用 nums[i] = … 直接往列表的第 i 格里放新数，列表才真的变了。</span><span class="en">In the first loop, x is just a number <b>copied out</b> of the list; x = x * 10 changes the copy, not the list. The second loop uses nums[i] = … to put a new number straight into slot i, so the list really changes.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 1 题" data-title-en="▶ Check question 1" data-save="reader-9-1" data-rows="4" data-canvas="no"><textarea>nums = [3, 1, 4]
for x in nums:
    x = x * 10
print(nums)
for i in range(len(nums)):
    nums[i] = nums[i] * 10
print(nums)
</textarea></div>

<h3>🔮 <span class="zh">第 2 题</span><span class="en">Question 2</span></h3>
<div class="two"><div>
<pre>answers = [&quot; Yes&quot;, &quot;NO &quot;, &quot;yes&quot;, &quot;maybe&quot;]
count = 0
for a in answers:
    a = a.strip().lower()
    if a == &quot;yes&quot;:
        count = count + 1
    elif a == &quot;no&quot;:
        count = count - 1
print(count)
print(answers[0] == &quot;yes&quot;)</pre>
</div><div>
<div class="quiz" data-answer="1">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>1<br>False</button><button>1<br>True</button><button>2<br>False</button><button>0<br>False</button></div>
  <div class="why"><span class="zh">strip() 去掉两头空格、lower() 变小写：" Yes" → "yes"（+1），"NO " → "no"（-1），"yes"（+1），"maybe" 都不是。1 - 1 + 1 = 1。但 a = … 只改了变量 a，列表里的 answers[0] 还是原来的 " Yes"，不等于 "yes"。</span><span class="en">strip() removes spaces at both ends and lower() makes it lowercase: " Yes" → "yes" (+1), "NO " → "no" (-1), "yes" (+1), "maybe" is neither. 1 - 1 + 1 = 1. But a = … only changes the variable a; answers[0] in the list is still " Yes", which is not "yes".</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 2 题" data-title-en="▶ Check question 2" data-save="reader-9-2" data-rows="4" data-canvas="no"><textarea>answers = [&quot; Yes&quot;, &quot;NO &quot;, &quot;yes&quot;, &quot;maybe&quot;]
count = 0
for a in answers:
    a = a.strip().lower()
    if a == &quot;yes&quot;:
        count = count + 1
    elif a == &quot;no&quot;:
        count = count - 1
print(count)
print(answers[0] == &quot;yes&quot;)
</textarea></div>

<h3>🔮 <span class="zh">第 3 题</span><span class="en">Question 3</span> <span class="pill">⭐</span></h3>
<div class="two"><div>
<pre>word = &quot;banana&quot;
counts = {}
for ch in word:
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1
print(counts[&quot;a&quot;], counts[&quot;n&quot;], len(counts))</pre>
</div><div>
<div class="quiz" data-answer="4" data-badge="reader-9">
  <p class="q"><span class="zh">这段代码会打印什么？</span><span class="en">What will this print?</span></p>
  <div class="opts"><button>3 2 6</button><button>1 1 3</button><button>2 3 3</button><button>3 2 3</button></div>
  <div class="why"><span class="zh">这是数数的经典写法：第一次见到一个字母就放 1，再见到就 +1。banana：b 1 次、a 3 次、n 2 次。len(counts) 数的是字典里有几个<b>钥匙</b>（b、a、n），不是有几个字母，所以是 3。</span><span class="en">This is the classic counting pattern: the first time a letter appears, store 1; after that, add 1. banana: b once, a 3 times, n twice. len(counts) counts the <b>keys</b> in the dictionary (b, a, n), not the letters, so it's 3.</span></div>
</div></div></div>
<div class="playground" data-title="▶ 验证第 3 题" data-title-en="▶ Check question 3" data-save="reader-9-3" data-rows="4" data-canvas="no"><textarea>word = &quot;banana&quot;
counts = {}
for ch in word:
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1
print(counts[&quot;a&quot;], counts[&quot;n&quot;], len(counts))
</textarea></div>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 九关都读透了？</span><span class="en">🧠 Read all nine levels?</span></span>
<span class="zh">去 <a href="{{ '/gallery/' | relative_url }}">作品墙</a> 随便打开一个作品，先不运行，给老师讲讲它每一行在做什么——这就是真正的读心术。</span>
<span class="en">Open any work in the <a href="{{ '/gallery/' | relative_url }}">Gallery</a>, don't run it, and explain to your teacher what each line does — that's real mind reading.</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
