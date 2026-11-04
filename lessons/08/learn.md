---
title: 第 8 课 · 学一学
title_en: Lesson 8 · Learn
lesson: "08"
tab: learn
playground: true
---

# ✊ <span class="zh">迷你项目：石头剪刀布，6 步搭起来</span><span class="en">Mini project: Rock Paper Scissors in 6 steps</span>

<p class="zh">今天没有「新魔法」要背——你已经有了全部零件：变量、input、if、random、while、列表、函数。今天学的是<b>怎么把零件拼成一个真正的游戏</b>，还有两个整理文字的小帮手 <code>.strip()</code> 和 <code>.lower()</code>。</p>
<p class="en">No new magic to memorise today — you already have every part: variables, input, if, random, while, lists, functions. Today you learn <b>how to assemble the parts into a real game</b>, plus two little text helpers, <code>.strip()</code> and <code>.lower()</code>.</p>

<div class="flow">
  <div class="f"><span class="e">🤖</span><b>1 <span class="zh">电脑出拳</span><span class="en">computer plays</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🙋</span><b>2 <span class="zh">你出拳</span><span class="en">you play</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">⚖️</span><b>3 judge()</b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🔢</span><b>4 <span class="zh">记分循环</span><span class="en">score loop</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🐢</span><b>5 <span class="zh">庆祝</span><span class="en">celebrate</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🦎</span><b>6 <span class="zh">加料</span><span class="en">extras</span></b></div>
</div>

<div class="box box-rule"><span class="zh">📏 <b>每一步的规矩：</b>先猜会发生什么 → 运行 → 改一改 → 能跑了再去下一步。每一步的画板都从上一步的答案开始，但留了 <code>___</code> 或 TODO 给你。</span><span class="en">📏 <b>The rule for every step:</b> guess what happens → run → change it → only move on when it runs. Each step's playground starts from the previous step's answer, with <code>___</code> or TODOs left for you.</span></div>

---

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">函数 + 列表 + random，一次用上。填好两个空。</span><span class="en">Functions + lists + random, all at once. Fill in both blanks.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/warmup.py' | relative_url }}" data-canvas="no" data-title="🔁 热身：随机水果" data-title-en="🔁 Warm-up: random fruit" data-save="warmup-8" data-rows="8"></div>

<ul class="quests" data-key="l8-warmup">
  <li><span class="zh">填好空，运行，输入 3。打印了 3 个水果吗？</span><span class="en">Fill the blanks, run, type 3. Did it print 3 fruits?</span></li>
  <li><span class="zh">加一个水果到列表里。要改 <code>pick()</code> 吗？</span><span class="en">Add a fruit to the list. Do you need to change <code>pick()</code>?</span></li>
</ul>

---

## 🪜 <span class="zh">第 1 步：电脑出拳</span><span class="en">Step 1: the computer plays</span>
{: #step1}

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">运行 5 次，电脑会出一样的拳吗？</span><span class="en">Run it 5 times. Will the computer play the same thing each time?</span></p>
  <div class="opts"><button><span class="zh">一样，永远是石头</span><span class="en">Same, always rock</span></button><button><span class="zh">不一样，随机的</span><span class="en">Different, it's random</span></button><button><span class="zh">按顺序：石头、剪刀、布</span><span class="en">In order: rock, scissors, paper</span></button></div>
  <div class="why"><span class="zh">随机的！<code>random.choice(choices)</code> 每次从列表里随便挑一个（第 5 课）。</span><span class="en">Random! <code>random.choice(choices)</code> picks any item from the list each time (Lesson 5).</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/08/code/step1.py' | relative_url }}" data-canvas="no" data-title="🪜 第 1 步：电脑出拳" data-title-en="🪜 Step 1: computer plays" data-save="rps-step1" data-rows="6"></div>

<ul class="quests" data-key="l8-s1">
  <li><span class="zh">填好 <code>___</code>（从哪个列表里挑？），运行 5 次，看电脑出了什么。</span><span class="en">Fill in <code>___</code> (pick from which list?), run 5 times, see what the computer plays.</span></li>
  <li><span class="zh">用 <code>for i in range(10):</code> 让电脑一口气出 10 次。</span><span class="en">Use <code>for i in range(10):</code> to make it play 10 times in one go.</span></li>
</ul>

## 🪜 <span class="zh">第 2 步：你出拳 + 整理输入</span><span class="en">Step 2: you play + tidy the input</span>

<p><span class="zh">人打字很随便：<code>" 石头 "</code>、<code>"Rock"</code>、<code>"ROCK"</code>……电脑却很较真。两个小帮手：<b><code>.strip()</code> 去掉两头的空格，<code>.lower()</code> 全变小写</b>。先猜下面每一行打印什么。</span><span class="en">People type messily: <code>" rock "</code>, <code>"Rock"</code>, <code>"ROCK"</code>… but computers are fussy. Two helpers: <b><code>.strip()</code> removes spaces at both ends, <code>.lower()</code> makes it all lowercase</b>. Guess what each line prints.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/lower-demo.py' | relative_url }}" data-canvas="no" data-title="🧹 .strip() 和 .lower()" data-title-en="🧹 .strip() and .lower()" data-save="strip-lower" data-rows="8"></div>

<p><span class="zh">现在让你出拳。注意 <code>if me not in choices:</code>——<b>乱打的时候要礼貌地拒绝</b>，不然程序会乱掉。</span><span class="en">Now you play. Notice <code>if me not in choices:</code> — <b>politely refuse nonsense</b>, or the program gets confused.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/step2.py' | relative_url }}" data-canvas="no" data-title="🪜 第 2 步：你出拳" data-title-en="🪜 Step 2: you play" data-save="rps-step2" data-rows="10"></div>

<ul class="quests" data-key="l8-s2">
  <li><span class="zh">运行，输入「  石头 」（两头带空格）。被接受了吗？再把 <code>.strip()</code> 删掉试试。</span><span class="en">Run and type "  石头 " with spaces around it. Accepted? Now delete <code>.strip()</code> and try again.</span></li>
  <li><span class="zh">输入「香蕉」。程序礼貌地拒绝了吗？</span><span class="en">Type "banana". Did it refuse politely?</span></li>
  <li><span class="zh">想让英文也能玩？把列表改成 <code>["rock", "scissors", "paper"]</code>，<code>me = me.strip().lower()</code>，试试输入 <code>ROCK</code>。</span><span class="en">Want English to work? Change the list to <code>["rock", "scissors", "paper"]</code>, use <code>me = me.strip().lower()</code>, and try typing <code>ROCK</code>.</span></li>
</ul>

## 🪜 <span class="zh">第 3 步：judge() 判断输赢</span><span class="en">Step 3: judge() decides the winner</span>

<div class="table-wrap">
<table>
<tr><th><span class="zh">你出</span><span class="en">You</span></th><th><span class="zh">电脑出</span><span class="en">Computer</span></th><th><span class="zh">结果</span><span class="en">Result</span></th></tr>
<tr><td>石头 rock</td><td>剪刀 scissors</td><td>赢 win</td></tr>
<tr><td>剪刀 scissors</td><td>布 paper</td><td>赢 win</td></tr>
<tr><td>布 paper</td><td>石头 rock</td><td>赢 win</td></tr>
<tr><td><span class="zh">一样</span><span class="en">same</span></td><td><span class="zh">一样</span><span class="en">same</span></td><td>平 tie</td></tr>
<tr><td colspan="2"><span class="zh">其他所有情况</span><span class="en">everything else</span></td><td>输 lose</td></tr>
</table>
</div>

<p><span class="zh">把规则表变成一个<b>交回答案的招式</b>（第 7 课的 return！）。前面先用固定的拳<b>测试</b> judge——这样一眼就知道对不对。</span><span class="en">Turn the table into a <b>trick that returns an answer</b> (Lesson 7's return!). First <b>test</b> judge with fixed plays, so you can see at once if it's right.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/step3.py' | relative_url }}" data-canvas="no" data-title="🪜 第 3 步：judge()" data-title-en="🪜 Step 3: judge()" data-save="rps-step3" data-draft="l8-step3" data-rows="14"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">照着第一个「赢」写：<code>me == "剪刀" and computer == "布"</code>。第三行同理。</span><span class="en">Copy the first "win" line: <code>me == "剪刀" and computer == "布"</code>. Same idea for the third.</span></details>
<details class="hint"><summary><span class="zh">💡 为什么「输」不用写三行？</span><span class="en">💡 Why doesn't "lose" need three lines?</span></summary><span class="zh">因为平和赢都检查过了，<b>剩下的只能是输</b>——<code>else</code> 接住所有其他情况。</span><span class="en">Because tie and win are already checked, <b>whatever's left must be a loss</b> — <code>else</code> catches everything else.</span></details>

<ul class="quests" data-key="l8-s3">
  <li><span class="zh">填好 4 个空，运行。前三行测试都对吗（赢 / 平 / 输）？</span><span class="en">Fill the 4 blanks and run. Are the three test lines right (赢 / 平 / 输)?</span></li>
  <li>🐞 <span class="zh">故意把一个 <code>and</code> 改成 <code>or</code>。哪个测试坏了？为什么？</span><span class="en">Change one <code>and</code> to <code>or</code> on purpose. Which test breaks? Why?</span></li>
</ul>

<div class="box box-tip"><span class="box-title">🤖 <span class="zh">卡住了？用排错模板问 AI</span><span class="en">Stuck? Ask AI with the debugging template</span></span>
<span class="zh">红框里有「📋 复制问 AI 要提示的话」按钮——它会把报错和代码一起打包，<b>只要提示，不要答案</b>。没报错但结果不对？这样问：</span><span class="en">The red error box has a "📋 Copy a hint-please message" button that packs the error and code together, asking for <b>a hint, not the answer</b>. No error but wrong result? Ask like this:</span>
<pre style="margin:.5em 0;white-space:pre-wrap">我在写石头剪刀布的 judge 函数。我输入 布、电脑出 石头，应该是「赢」，但它说「输」。
这是我的代码：（贴代码）
请告诉我该检查哪一行，不要直接给我改好的代码。</pre><button class="pg-btn copy-prev">📋 <span class="zh">复制</span><span class="en">Copy</span></button>
</div>

---

## 🪜 <span class="zh">第 4 步：记分 + 一直玩到 3 分</span><span class="en">Step 4: scores + play until 3 points</span>
{: #step4}

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh"><code>while my_score &lt; 3 and computer_score &lt; 3:</code>——什么时候循环会停？</span><span class="en"><code>while my_score &lt; 3 and computer_score &lt; 3:</code> — when does the loop stop?</span></p>
  <div class="opts"><button><span class="zh">玩了 3 轮</span><span class="en">After 3 rounds</span></button><button><span class="zh">两个人都到 3 分</span><span class="en">When both reach 3</span></button><button><span class="zh">任何一个人到 3 分</span><span class="en">When either reaches 3</span></button></div>
  <div class="why"><span class="zh">任何一个到 3 分！<code>and</code> 要两边都 True 才继续；一边变 False（有人到 3）就停。</span><span class="en">When either reaches 3! <code>and</code> needs both sides True to continue; once one side is False (someone has 3) it stops.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/08/code/step4.py' | relative_url }}" data-canvas="no" data-title="🪜 第 4 步：记分循环" data-title-en="🪜 Step 4: score loop" data-save="rps-step4" data-draft="l8-step4" data-rows="16"></div>

<ul class="quests" data-key="l8-s4">
  <li><span class="zh">填好两个空，玩一整局到 3 分。</span><span class="en">Fill both blanks and play a whole game to 3.</span></li>
  <li><span class="zh"><code>continue</code> 是什么意思？故意输入「香蕉」，看 <code>rounds</code> 有没有加 1。</span><span class="en">What does <code>continue</code> do? Type "banana" on purpose and check whether <code>rounds</code> went up.</span></li>
  <li><span class="zh">改成 5 分制。要改几处？（提示：如果你写了 3 处，想想怎么用一个变量 <code>target = 5</code> 只改一处。）</span><span class="en">Make it first-to-5. How many places did you change? (Hint: if it's 3, think how a variable <code>target = 5</code> makes it one.)</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 rounds &lt; 15 是干嘛的？</span><span class="en">💡 What is rounds &lt; 15 for?</span></summary><span class="zh">安全带！万一一直平局，没人到 3 分，循环就永远不停。第 6 课说过：<b>while 一定要有办法停下来</b>。</span><span class="en">A seatbelt! If it's tie after tie, nobody reaches 3 and the loop never ends. Lesson 6 rule: <b>a while loop must always have a way to stop</b>.</span></details>

## 🪜 <span class="zh">第 5 步：海龟庆祝</span><span class="en">Step 5: the turtle celebrates</span>

<p><span class="zh">把第 7 课的招式请回来：每赢一次画一颗金星。你的任务：写 <code>sad_face(x, y)</code>，输的时候画。</span><span class="en">Bring back a Lesson 7 trick: a gold star for every win. Your job: write <code>sad_face(x, y)</code> for losses.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/step5.py' | relative_url }}" data-title="🪜 第 5 步：海龟庆祝" data-title-en="🪜 Step 5: turtle celebration" data-save="rps-step5" data-draft="l8-step5" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 sad_face 提示</span><span class="en">💡 sad_face hint</span></summary><span class="zh"><code>def sad_face(x, y):</code> → penup, goto(x, y), pendown → <code>t.circle(25)</code> 脸 → penup 挪到眼睛位置 <code>t.dot(6)</code> 两次 → 嘴巴：<code>t.setheading(60)</code> 然后 <code>t.circle(10, -120)</code>（负数 = 反方向弯）。喊它：<code>sad_face(-200 + computer_score * 100, -100)</code>。</span><span class="en"><code>def sad_face(x, y):</code> → penup, goto(x, y), pendown → <code>t.circle(25)</code> for the face → penup to the eyes, <code>t.dot(6)</code> twice → mouth: <code>t.setheading(60)</code> then <code>t.circle(10, -120)</code> (negative = bends the other way). Call it: <code>sad_face(-200 + computer_score * 100, -100)</code>.</span></details>

## 🪜 <span class="zh">第 6 步：加料（选做）——蜥蜴和史波克！</span><span class="en">Step 6: extras (optional) — lizard and Spock!</span>

<p><span class="zh">5 种拳，10 条「谁赢谁」。用 <code>elif</code> 要写 10 行——太累了。看看 <code>beats</code> 列表怎么<b>用一行代替 10 行</b>。</span><span class="en">5 plays, 10 "who beats whom" rules. With <code>elif</code> that's 10 lines — exhausting. See how the <code>beats</code> list <b>replaces 10 lines with one</b>.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/step6.py' | relative_url }}" data-canvas="no" data-title="🦎 第 6 步：蜥蜴史波克" data-title-en="🦎 Step 6: Lizard Spock" data-save="rps-step6" data-draft="l8-step6" data-rows="14"></div>

<ul class="quests" data-key="l8-s6">
  <li><span class="zh"><code>if [me, computer] in beats:</code> 这一行在问什么？用自己的话说。</span><span class="en">What is <code>if [me, computer] in beats:</code> asking? Say it in your own words.</span></li>
  <li><span class="zh">发明第 6 种拳（比如「海龟」），加进 <code>choices</code> 和 <code>beats</code>，让它赢两个、输三个。</span><span class="en">Invent a 6th play (like "turtle"), add it to <code>choices</code> and <code>beats</code>, so it beats two and loses to three.</span></li>
</ul>

---

## 🧪 <span class="zh">测试你的游戏：当一个捣蛋鬼</span><span class="en">Test your game: be a troublemaker</span>
{: #test}

<p><span class="zh">程序员写完代码不算完——要<b>试着弄坏它</b>。回到第 4 步的画板，挨个试：</span><span class="en">Writing code isn't the end — programmers <b>try to break it</b>. Go back to step 4 and try each one:</span></p>

<ul class="quests" data-key="l8-test">
  <li><span class="zh">🍌 输入「香蕉」——程序崩了还是礼貌拒绝？</span><span class="en">🍌 Type "banana" — crash, or polite refusal?</span></li>
  <li><span class="zh">⬜ 什么都不输直接回车——会怎样？</span><span class="en">⬜ Press Enter with nothing typed — what happens?</span></li>
  <li><span class="zh">🔠 输入「  布」（前面带空格）——被接受了吗？</span><span class="en">🔠 Type "  布" with spaces in front — accepted?</span></li>
  <li><span class="zh">🔁 一直出同一个拳玩 5 轮——比分对吗？每一轮都加对了吗？</span><span class="en">🔁 Play the same thing 5 rounds — are the scores right every round?</span></li>
  <li><span class="zh">🏁 游戏结束时，赢的人真的是分高的那个吗？</span><span class="en">🏁 At the end, is the winner really the one with more points?</span></li>
</ul>

### 🐞 <span class="zh">虫虫医院：两个病号</span><span class="en">Bug hospital: two patients</span>

<p><span class="zh">病号 1 <b>不报错</b>，但有一种情况判错了。期望的输出是 赢、赢、赢、输、平——找到那一行，治好它，输出一样就过关！</span><span class="en">Patient 1 <b>doesn't crash</b>, but one case is judged wrong. The wanted output is 赢, 赢, 赢, 输, 平 — find the line, cure it, match the output to win!</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/bug1.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 1：判错了" data-title-en="🐞 Patient 1: wrong verdict" data-save="bug1-fixed" data-expect="赢\n赢\n赢\n输\n平" data-badge="lesson8-bug1" data-rows="12"></div>

<p><span class="zh">病号 2 <b>直接报错</b>。读报错、看红色那一行。治好后应该打印「比分 1」。</span><span class="en">Patient 2 <b>crashes</b>. Read the error and look at the red line. Cured, it should print "比分 1".</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/bug2.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 2：报错了" data-title-en="🐞 Patient 2: it crashes" data-save="bug2-fixed" data-expect="比分 1" data-badge="lesson8-bug2" data-rows="12"></div>

<details class="hint"><summary><span class="zh">💡 病号 1 提示</span><span class="en">💡 Patient 1 hint</span></summary><span class="zh">对着规则表看第三个「赢」：布赢<b>谁</b>？</span><span class="en">Check the third "win" against the table: paper beats <b>what</b>?</span></details>
<details class="hint"><summary><span class="zh">💡 病号 2 提示</span><span class="en">💡 Patient 2 hint</span></summary><span class="zh">一个 <code>=</code> 是「放进去」，两个 <code>==</code> 是「一样吗？」。<code>if</code> 后面问的是问题。</span><span class="en">One <code>=</code> means "put in", two <code>==</code> means "is it the same?". An <code>if</code> asks a question.</span></details>

<p><span class="zh">想治更多病号？去 <a href="{{ '/games/bugs/' | relative_url }}">🐞 虫虫医院</a>！</span><span class="en">Want more patients? Go to the <a href="{{ '/games/bugs/' | relative_url }}">🐞 Bug Hospital</a>!</span></p>

---

## 🤖 <span class="zh">和 AI 一起：排错伙伴，不是代写机器</span><span class="en">With AI: a debugging buddy, not a writing machine</span>

<div class="chat">
  <div class="bubble me"><span class="zh">😃 <b>好问题：</b>我在做石头剪刀布，玩到第 3 轮比分应该是 2:1，但显示 1:1。我的代码：（贴代码）。我怀疑是加分那里。请给我一个提示，告诉我该看哪几行，不要直接给答案。</span><span class="en">😃 <b>Good ask:</b> I'm making Rock Paper Scissors. In round 3 the score should be 2:1 but it shows 1:1. My code: (paste). I suspect the scoring part. Please give me a hint about which lines to look at, not the answer.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">看看「输」的那个分支——你加的是哪个变量？</span><span class="en">Look at the "lose" branch — which variable are you adding to?</span></div>
  <div class="bubble me"><span class="zh">😕 <b>坏问题：</b>帮我写一个石头剪刀布游戏。——写出来了，但不是你的，你也不知道它对不对。</span><span class="en">😕 <b>Bad ask:</b> Write me a Rock Paper Scissors game. — You get one, but it isn't yours and you can't tell if it's right.</span></div>
</div>

<div class="box box-rule"><span class="zh">📜 <b>好问题的三件套：</b>① 我在做什么 ② 我期望 vs 实际发生了什么（带报错 / 带输出）③「给提示，不要答案」。AI 给的提示，<b>你自己改、自己运行</b>。</span><span class="en">📜 <b>A good ask has three parts:</b> ① what I'm making ② expected vs what actually happened (with the error / output) ③ "hint, not answer". Then <b>you make the fix and run it</b>.</span></div>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>.strip() / .lower()</b><code>me = input("? ").strip().lower()</code><span><span class="zh">去空格、变小写，整理输入。</span><span class="en">Remove spaces, lowercase: tidy input.</span></span></div>
  <div class="k"><b>in / not in</b><code>if me not in choices:
    print("只能出…")</code><span><span class="zh">在不在列表里？</span><span class="en">Is it in the list?</span></span></div>
  <div class="k"><b><span class="zh">游戏循环</span><span class="en">game loop</span></b><code>while a &lt; 3 and b &lt; 3:
    ...
    if result == "赢":
        a = a + 1</code><span><span class="zh">while + 计数器 + 停下条件。</span><span class="en">while + counters + a stop condition.</span></span></div>
  <div class="k"><b>continue</b><code>if me not in choices:
    print("...")
    continue</code><span><span class="zh">跳过这一轮，回到 while 开头。</span><span class="en">Skip this round, back to the top of while.</span></span></div>
  <div class="k"><b><span class="zh">交回答案的招式</span><span class="en">a trick that returns</span></b><code>def judge(me, computer):
    if ...: return "赢"
    return "输"</code><span><span class="zh">先用固定输入测试它。</span><span class="en">Test it with fixed inputs first.</span></span></div>
  <div class="k"><b><span class="zh">用列表代替一堆 elif</span><span class="en">a list instead of many elifs</span></b><code>beats = [["石头","剪刀"], ...]
if [me, computer] in beats:</code><span><span class="zh">规则多了就放进数据里。</span><span class="en">Lots of rules? Put them in data.</span></span></div>
</div>

<p><span class="zh">全部指令在 <a href="{{ '/cheatsheet/' | relative_url }}#l08">📖 小词典 · 第 8 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l08">📖 cheat sheet · Lesson 8</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/08/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
