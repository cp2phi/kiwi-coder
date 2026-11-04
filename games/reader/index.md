---
title: 读心术
title_en: Mind Reader
playground: true
---

# 🔮 <span class="zh">读心术</span><span class="en">Mind Reader</span>

<p class="zh">真正的程序员有一种超能力：<b>不运行，光看代码就知道它会做什么</b>。这个游戏练的就是这个。每一题：① 先读代码，② 猜它会打印什么，③ 点一个答案，④ 再点 ▶ 运行验证。猜错了也没关系——想一想为什么，比猜对更重要。每关 3 题，答对最后一题得星 ⭐。</p>
<p class="en">Real programmers have a superpower: <b>they can tell what code does just by reading it</b>. This game trains that. For each question: (1) read the code, (2) guess what it prints, (3) click an answer, (4) click ▶ Run to check. Wrong guesses are fine — working out why matters more. 3 questions per level; the last one earns the star ⭐.</p>

<div class="box box-tip"><span class="zh">🕵️ 读代码的秘诀：<b>一行一行</b>，像电脑一样老实。用手指着每一行，嘴里说出「现在 x 是多少」。</span><span class="en">🕵️ The secret to reading code: go <b>one line at a time</b>, as literally as the computer does. Point at each line and say out loud "right now x is …".</span></div>

<div class="levels-bar">
<a href="#lv1" data-badge-id="reader-1">1</a><a href="#lv2" data-badge-id="reader-2">2</a><a href="#lv3" data-badge-id="reader-3">3</a><a href="#lv4" data-badge-id="reader-4">4</a><a href="#lv5" data-badge-id="reader-5">5</a><a href="#lv6" data-badge-id="reader-6">6</a>
</div>

<div class="level-head" id="lv1" data-badge-id="reader-1"><span class="lv"><span class="zh">第 1 关</span><span class="en">Level 1</span></span><b><span class="zh">打招呼和变量</span><span class="en">Hello and variables</span></b><span class="done-mark">⭐</span></div>
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

<div class="level-head" id="lv2" data-badge-id="reader-2"><span class="lv"><span class="zh">第 2 关</span><span class="en">Level 2</span></span><b><span class="zh">for 循环</span><span class="en">for loops</span></b><span class="done-mark">⭐</span></div>
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

<div class="level-head" id="lv3" data-badge-id="reader-3"><span class="lv"><span class="zh">第 3 关</span><span class="en">Level 3</span></span><b><span class="zh">if / elif / else</span><span class="en">if / elif / else</span></b><span class="done-mark">⭐</span></div>
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

<div class="level-head" id="lv4" data-badge-id="reader-4"><span class="lv"><span class="zh">第 4 关</span><span class="en">Level 4</span></span><b><span class="zh">列表</span><span class="en">Lists</span></b><span class="done-mark">⭐</span></div>
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

<div class="level-head" id="lv5" data-badge-id="reader-5"><span class="lv"><span class="zh">第 5 关</span><span class="en">Level 5</span></span><b><span class="zh">while 和 and / or</span><span class="en">while and and / or</span></b><span class="done-mark">⭐</span></div>
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

<div class="level-head" id="lv6" data-badge-id="reader-6"><span class="lv"><span class="zh">第 6 关</span><span class="en">Level 6</span></span><b><span class="zh">函数和字典</span><span class="en">Functions and dictionaries</span></b><span class="done-mark">⭐</span></div>
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

<div class="box box-think"><span class="box-title"><span class="zh">🧠 六关都读透了？</span><span class="en">🧠 Read all six levels?</span></span>
<span class="zh">去 <a href="{{ '/gallery/' | relative_url }}">作品墙</a> 随便打开一个作品，先不运行，给老师讲讲它每一行在做什么——这就是真正的读心术。</span>
<span class="en">Open any work in the <a href="{{ '/gallery/' | relative_url }}">Gallery</a>, don't run it, and explain to your teacher what each line does — that's real mind reading.</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
