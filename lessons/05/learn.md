---
title: 第 5 课 · 学一学
title_en: Lesson 5 · Learn
lesson: "05"
tab: learn
playground: true
---

# 📦 <span class="zh">第 5 课：列表——一排带编号的抽屉</span><span class="en">Lesson 5: Lists — a row of numbered drawers</span>

<p class="zh">到现在为止，一个变量只能装<b>一样</b>东西。今天学的<b>列表</b>可以装一整排——然后让电脑随机抽一个！</p>
<p class="en">So far a variable holds <b>one</b> thing. Today's <b>list</b> holds a whole row of things — and then the computer can pick one at random!</p>

---

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">上节课的 <code>if / elif / else</code> 和 <code>random.randint</code>，加上第 3 课的 <code>for</code>。先猜：会打印几行？</span><span class="en">Last lesson's <code>if / elif / else</code> and <code>random.randint</code>, plus <code>for</code> from Lesson 3. Guess first: how many lines will it print?</span></p>

<div class="playground" data-src="{{ '/lessons/05/code/warmup.py' | relative_url }}" data-canvas="no" data-title="🎲 掷骰子 5 次" data-title-en="🎲 Roll 5 times" data-save="dice-5" data-rows="8"></div>

<ul class="quests" data-key="l5-warmup">
  <li><span class="zh">把 <code>range(5)</code> 改成 <code>range(20)</code>，数一数出现了几个 6。</span><span class="en">Change <code>range(5)</code> to <code>range(20)</code> and count how many sixes you get.</span></li>
  <li><span class="zh">加一个 <code>elif dice == 1:</code>，打印「💀 一点，惨」。</span><span class="en">Add <code>elif dice == 1:</code> that prints "💀 a one, ouch".</span></li>
</ul>

---

## ✨ <span class="zh">今天的新魔法：列表 [ ]</span><span class="en">Today's new magic: lists [ ]</span>
{: #magic}

<p><span class="zh">想象一排<b>抽屉</b>，每个抽屉有一个<b>编号</b>。列表就是这样：用方括号 <code>[ ]</code> 装东西，用逗号隔开，用编号拿出来。<b>注意：编号从 0 开始！</b></span><span class="en">Imagine a row of <b>drawers</b>, each with a <b>number</b>. A list is exactly that: things inside square brackets <code>[ ]</code>, separated by commas, and you take them out by number. <b>Careful: numbering starts at 0!</b></span></p>

<div class="cmds">
  <div class="cmd"><code>animals = ["kiwi", "tui", "pukeko"]</code><span><span class="zh">做一个有 3 个抽屉的列表</span><span class="en">Make a list with 3 drawers</span></span></div>
  <div class="cmd"><code>animals[0]</code><span><span class="zh">第 0 个抽屉（第一个！）</span><span class="en">Drawer 0 (the first one!)</span></span></div>
  <div class="cmd"><code>len(animals)</code><span><span class="zh">一共几个抽屉</span><span class="en">How many drawers</span></span></div>
  <div class="cmd"><code>animals.append("weka")</code><span><span class="zh">在最后加一个抽屉</span><span class="en">Add a drawer at the end</span></span></div>
  <div class="cmd"><code>random.choice(animals)</code><span><span class="zh">随机抽一个</span><span class="en">Pick one at random</span></span></div>
  <div class="cmd"><code>for a in animals:</code><span><span class="zh">把抽屉一个一个拿出来</span><span class="en">Take them out one by one</span></span></div>
</div>

### 🤔 <span class="zh">先猜，再运行</span><span class="en">Guess first, then run</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh"><code>animals = ["kiwi", "tui", "pukeko"]</code>，那 <code>print(animals[1])</code> 会打印什么？</span><span class="en"><code>animals = ["kiwi", "tui", "pukeko"]</code> — what does <code>print(animals[1])</code> print?</span></p>
  <div class="opts"><button>kiwi</button><button>tui</button><button>pukeko</button></div>
  <div class="why"><span class="zh">编号从 0 开始：kiwi 是 [0]，tui 是 [1]，pukeko 是 [2]。</span><span class="en">Numbering starts at 0: kiwi is [0], tui is [1], pukeko is [2].</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/05/code/drawers.py' | relative_url }}" data-canvas="no" data-title="📦 三个抽屉" data-title-en="📦 Three drawers" data-save="drawers" data-rows="8"></div>

### 🔍 <span class="zh">改一改</span><span class="en">Change it</span>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">如果加一行 <code>print(animals[3])</code>，会怎样？</span><span class="en">What happens if you add <code>print(animals[3])</code>?</span></p>
  <div class="opts"><button><span class="zh">打印 pukeko</span><span class="en">Prints pukeko</span></button><button><span class="zh">打印空的</span><span class="en">Prints nothing</span></button><button><span class="zh">报错</span><span class="en">An error</span></button></div>
  <div class="why"><span class="zh">只有 0、1、2 三个抽屉，没有第 3 个！电脑会说 <code>IndexError</code>（编号错误）。试试看，看画板怎么解释。</span><span class="en">There are only drawers 0, 1 and 2 — no drawer 3! The computer says <code>IndexError</code>. Try it and see how the playground explains it.</span></div>
</div>

<ul class="quests" data-key="l5-modify">
  <li>🐞 <span class="zh">真的加一行 <code>print(animals[3])</code>，运行，读一读报错，再删掉。</span><span class="en">Really add <code>print(animals[3])</code>, run it, read the error, then delete it.</span></li>
  <li>➕ <span class="zh">加一行 <code>animals.append("weka")</code>，再打印 <code>len(animals)</code>——变成几了？</span><span class="en">Add <code>animals.append("weka")</code> and print <code>len(animals)</code> again — what is it now?</span></li>
  <li>🔙 <span class="zh">试试 <code>animals[-1]</code>。负数是从<b>后面</b>数！</span><span class="en">Try <code>animals[-1]</code>. Negative numbers count from the <b>end</b>!</span></li>
</ul>

---

## 🧪 <span class="zh">例 2：搞笑故事生成器</span><span class="en">Example 2: silly story maker</span>
{: #story}

<p><span class="zh">三个列表：<b>谁</b>、<b>在哪里</b>、<b>做了什么</b>。<code>random.choice</code> 从每个列表里随机抽一个，用 f-string 拼成一句话。每次运行都不一样！</span><span class="en">Three lists: <b>who</b>, <b>where</b>, <b>did what</b>. <code>random.choice</code> picks one from each, and an f-string joins them into a sentence. Different every time!</span></p>

<div class="playground" data-src="{{ '/lessons/05/code/story.py' | relative_url }}" data-canvas="no" data-title="🎲 故事生成器" data-title-en="🎲 Story maker" data-save="story-maker" data-draft="l5-story" data-rows="12"></div>

<ul class="quests" data-key="l5-story">
  <li><span class="zh">点 ▶ 运行 3 次，看看每次有什么不同。</span><span class="en">Click ▶ three times and see how it changes.</span></li>
  <li><span class="zh">每个列表加 2 样<b>你自己的</b>东西（你的宠物？你的老师？你最喜欢的游戏？）。英文也可以。</span><span class="en">Add 2 of <b>your own</b> items to each list (your pet? your teacher? your favourite game?). English is fine too.</span></li>
  <li><span class="zh">用第 3 课的 <code>for i in range(5):</code> 把最后 4 行包起来，一次讲 5 个故事。</span><span class="en">Wrap the last 4 lines in <code>for i in range(5):</code> from Lesson 3 to tell 5 stories at once.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 for 循环提示</span><span class="en">💡 for loop hint</span></summary><span class="zh">在 <code>a = random.choice(who)</code> 上面加 <code>for i in range(5):</code>，然后把下面 4 行都往右缩 4 个空格（选中它们按 Tab）。</span><span class="en">Add <code>for i in range(5):</code> above <code>a = random.choice(who)</code>, then push the 4 lines below in by 4 spaces (select them and press Tab).</span></details>

---

## 🧪 <span class="zh">例 3：海龟按列表换颜色</span><span class="en">Example 3: turtle colours from a list</span>
{: #rainbow}

<p><span class="zh"><code>for colour in colours:</code> 的意思是：<b>把列表里的颜色一个一个拿出来</b>，每拿一个，就跑一遍下面的代码。6 个颜色 → 6 条边 → 一个六边形！</span><span class="en"><code>for colour in colours:</code> means: <b>take the colours out of the list one by one</b>, and run the code below once for each. 6 colours → 6 sides → a hexagon!</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">列表里有 6 个颜色，每次转 60 度。海龟会画出什么？</span><span class="en">6 colours in the list, turning 60° each time. What does the turtle draw?</span></p>
  <div class="opts"><button><span class="zh">正方形</span><span class="en">A square</span></button><button><span class="zh">六边形</span><span class="en">A hexagon</span></button><button><span class="zh">一条彩色直线</span><span class="en">A colourful straight line</span></button></div>
  <div class="why"><span class="zh">6 × 60° = 360°，正好转一圈：六边形，每条边一个颜色。</span><span class="en">6 × 60° = 360°, exactly one full turn: a hexagon with one colour per side.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/05/code/rainbow.py' | relative_url }}" data-title="🌈 彩虹六边形" data-title-en="🌈 Rainbow hexagon" data-save="rainbow-hexagon" data-draft="l5-rainbow"></div>

<ul class="quests" data-key="l5-rainbow">
  <li><span class="zh">从列表里<b>删掉</b> 2 个颜色（变成 4 个），再把 60 改成 90。画出什么了？</span><span class="en"><b>Remove</b> 2 colours (leaving 4) and change 60 to 90. What do you get?</span></li>
  <li><span class="zh">在 <code>for</code> 外面再包一层 <code>for i in range(12):</code>，里面加 <code>t.left(30)</code>——万花筒！</span><span class="en">Wrap the whole <code>for</code> in another <code>for i in range(12):</code> and add <code>t.left(30)</code> — a kaleidoscope!</span></li>
</ul>

<div class="box box-think"><span class="box-title"><span class="zh">🔍 揭秘第 3 课的彩虹螺旋</span><span class="en">🔍 The Lesson 3 rainbow spiral, explained</span></span>
<span class="zh">还记得彩虹螺旋里的 <code>t.color(colors[i % 6])</code> 吗？<code>i % 6</code> 是「i 除以 6 的余数」，永远是 0～5——所以 i 一直变大，颜色编号却在 0～5 里转圈。现在你看懂了！</span>
<span class="en">Remember <code>t.color(colors[i % 6])</code> in the rainbow spiral? <code>i % 6</code> is "the remainder of i ÷ 6", always 0–5 — so i keeps growing but the colour number loops 0–5. Now you can read it!</span>
</div>

<div class="swatches" data-colors="red orange gold yellow limegreen green turquoise deepskyblue blue navy purple violet hotpink pink brown black white"></div>

---

## 🧪 <span class="zh">例 4：毛利语单词小测验（填空）</span><span class="en">Example 4: te reo Māori word quiz (fill in)</span>
{: #quiz}

<p><span class="zh">两个列表是<b>配对</b>的：<code>maori[0]</code> 是 kia ora，<code>english[0]</code> 是 hello。电脑随机选一个编号 <code>i</code>，问你 <code>maori[i]</code> 的意思，再和……哪个英文比？把 <code>___</code> 填上！</span><span class="en">The two lists are <b>paired</b>: <code>maori[0]</code> is kia ora, <code>english[0]</code> is hello. The computer picks a random number <code>i</code>, asks what <code>maori[i]</code> means, and compares your answer with… which English word? Fill in the <code>___</code>!</span></p>

<div class="playground" data-src="{{ '/lessons/05/code/quiz.py' | relative_url }}" data-canvas="no" data-title="🇳🇿 毛利语小测验" data-title-en="🇳🇿 Te reo quiz" data-save="maori-quiz" data-draft="l5-quiz" data-rows="14"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">问题用的是 <code>maori[i]</code>，答案就在 <code>english</code> 的<b>同一个</b>编号里。</span><span class="en">The question uses <code>maori[i]</code>, so the answer is at the <b>same</b> number in <code>english</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2（答案）</span><span class="en">💡 Hint 2 (answer)</span></summary><span class="zh"><code>english[i]</code>。</span><span class="en"><code>english[i]</code>.</span></details>

<ul class="quests" data-key="l5-quiz">
  <li><span class="zh">填好空，玩一局，拿到 5 / 5！</span><span class="en">Fill in the blank, play a round, get 5 / 5!</span></li>
  <li><span class="zh">把 <code>range(5)</code> 改成 <code>range(3)</code>，最后那行的 <code>/ 5</code> 也要改哦。</span><span class="en">Change <code>range(5)</code> to <code>range(3)</code> — and don't forget the <code>/ 5</code> on the last line.</span></li>
  <li><span class="zh">再加一对单词：<code>maori</code> 里加 <code>"ngā mihi"</code>，<code>english</code> 里加 <code>"thanks"</code>。<code>randint(0, 4)</code> 要改成几？</span><span class="en">Add a pair: <code>"ngā mihi"</code> to <code>maori</code> and <code>"thanks"</code> to <code>english</code>. What should <code>randint(0, 4)</code> become?</span></li>
</ul>

---

## 🧪 <span class="zh">例 5：愿望清单——用 append() 往里加</span><span class="en">Example 5: wish list — add with append()</span>
{: #wishes}

<p><span class="zh">列表可以一开始是<b>空的</b> <code>[]</code>，然后用 <code>.append()</code> 一个一个加进去。最后用 <code>range(len(wishes))</code> 把它们带编号打印出来。</span><span class="en">A list can start <b>empty</b> <code>[]</code>, then you <code>.append()</code> things one at a time. At the end, <code>range(len(wishes))</code> prints them with numbers.</span></p>

<div class="playground" data-src="{{ '/lessons/05/code/wishes.py' | relative_url }}" data-canvas="no" data-title="🌠 愿望清单" data-title-en="🌠 Wish list" data-save="wish-list" data-draft="l5-wishes" data-rows="10"></div>

<ul class="quests" data-key="l5-wishes">
  <li><span class="zh">为什么打印的是 <code>i + 1</code> 而不是 <code>i</code>？把 <code>+ 1</code> 删掉看看。</span><span class="en">Why print <code>i + 1</code> and not <code>i</code>? Delete the <code>+ 1</code> and see.</span></li>
  <li><span class="zh">改成问 5 个愿望，最后用 <code>random.choice(wishes)</code> 打印「今年先实现：……」（记得 <code>import random</code>）。</span><span class="en">Ask for 5 wishes, then print "This year, first: …" using <code>random.choice(wishes)</code> (remember <code>import random</code>).</span></li>
</ul>

---

## 🏆 <span class="zh">挑战：你的随机生成器</span><span class="en">Challenge: your own random generator</span>
{: #challenge}

<p><span class="zh">晚饭决定器只是个开头。做一个<b>你的</b>：队名生成器？超能力抽奖？「今天穿什么」机器？做好了存到作品墙！</span><span class="en">The dinner decider is just a start. Make <b>yours</b>: team name maker? superpower lottery? "what to wear today" machine? Save it to the Gallery!</span></p>

<div class="playground" data-src="{{ '/lessons/05/code/challenge.py' | relative_url }}" data-canvas="no" data-title="🏆 我的随机生成器" data-title-en="🏆 My random generator" data-save="my-generator" data-draft="l5-challenge" data-rows="10"></div>

---

## 🤖 <span class="zh">和 AI 一起：要单词，但要检验</span><span class="en">With AI: ask for words, then check them</span>

<p><span class="zh">请 AI 给你 5 个新的毛利语单词加进测验。但记住守则 ②：<b>AI 的话要检验</b>。所以我们还要让它说出「有多确定」，然后拿去问老师或查字典。</span><span class="en">Ask AI for 5 new te reo Māori words for your quiz. But remember rule ②: <b>check what AI says</b>. So we also make it say how sure it is, then check with the teacher or a dictionary.</span></p>

<div class="chat">
  <div class="bubble me"><span class="zh">我在做一个毛利语单词小测验（Python 列表）。请给我 5 个<b>简单的</b>毛利语单词和英文意思，写成两个 Python 列表。每个词<b>你有多确定</b>（很确定 / 不太确定）也告诉我。</span><span class="en">I'm making a te reo Māori word quiz (Python lists). Give me 5 <b>simple</b> Māori words with English meanings as two Python lists. For each word, tell me <b>how sure you are</b> (very sure / not sure).</span></div>
  <div class="bubble ai"><span class="zh">好的！maori = ["aroha", "wai", "maunga", …] english = ["love", "water", "mountain", …]。aroha：很确定……</span><span class="en">Sure! maori = ["aroha", "wai", "maunga", …] english = ["love", "water", "mountain", …]. aroha: very sure…</span></div>
</div>

<ul class="quests" data-key="l5-ai">
  <li><span class="zh">把 AI 给的两个列表贴进测验，玩一局。</span><span class="en">Paste the two lists into your quiz and play a round.</span></li>
  <li>🔍 <span class="zh">把 5 个词<b>拿去核对</b>（老师 / <a href="https://maoridictionary.co.nz" target="_blank" rel="noopener">Te Aka 字典</a>）。AI 全对吗？在笔记本里记下来。</span><span class="en"><b>Check</b> all 5 words (teacher / <a href="https://maoridictionary.co.nz" target="_blank" rel="noopener">Te Aka dictionary</a>). Was AI right every time? Write it in your notebook.</span></li>
</ul>

<div class="box box-warn"><span class="zh">😕 不好的问法：「给我一些毛利语单词」——AI 不知道你要几个、要多难、要什么格式。</span><span class="en">😕 A weak question: "give me some Māori words" — AI doesn't know how many, how hard, or in what format.</span></div>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b><span class="zh">做列表</span><span class="en">Make a list</span></b><code>fruits = ["apple", "kiwi", "pear"]</code><span><span class="zh">方括号 + 逗号</span><span class="en">Square brackets + commas</span></span></div>
  <div class="k"><b><span class="zh">拿一个</span><span class="en">Get one</span></b><code>fruits[0]   # apple
fruits[-1]  # pear</code><span><span class="zh">从 0 开始数；负数从后面数</span><span class="en">Count from 0; negatives count from the end</span></span></div>
  <div class="k"><b><span class="zh">有几个</span><span class="en">How many</span></b><code>len(fruits)   # 3</code><span><span class="zh">最后一个的编号是 len - 1</span><span class="en">The last number is len - 1</span></span></div>
  <div class="k"><b><span class="zh">加一个</span><span class="en">Add one</span></b><code>fruits.append("plum")</code><span><span class="zh">加在最后</span><span class="en">Goes on the end</span></span></div>
  <div class="k"><b><span class="zh">随机抽一个</span><span class="en">Pick at random</span></b><code>import random
random.choice(fruits)</code><span><span class="zh">每次可能不一样</span><span class="en">Could be different each time</span></span></div>
  <div class="k"><b><span class="zh">一个一个拿</span><span class="en">One by one</span></b><code>for f in fruits:
    print(f)</code><span><span class="zh">列表有几个，就跑几遍</span><span class="en">Runs once per item</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l05">📖 小词典 · 第 5 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l05">📖 cheat sheet · Lesson 5</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/05/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
