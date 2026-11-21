---
title: 第 8 课 · 学一学
title_en: Lesson 8 · Learn
lesson: "08"
tab: learn
playground: true
---

# ✊ <span class="zh">迷你项目：石头剪刀布，一步一步搭起来</span><span class="en">Mini project: Rock Paper Scissors, step by step</span>

<p class="zh">今天没有大的「新魔法」——你已经有了全部零件：变量、input、if、random、while、列表、函数。今天学的是<b>怎么把零件拼成一个真正的游戏</b>，而且<b>大部分招式你自己写</b>。最后还会做一个<b>会学习的电脑对手</b>！</p>
<p class="en">No big new magic today — you already have every part: variables, input, if, random, while, lists, functions. Today you learn <b>how to assemble the parts into a real game</b>, and <b>you write most of the tricks yourself</b>. At the end you'll build a <b>computer opponent that learns</b>!</p>

<div class="flow">
  <div class="f"><span class="e">🤖</span><b>1 <span class="zh">电脑出拳</span><span class="en">computer plays</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🙋</span><b>2 <span class="zh">你出拳</span><span class="en">you play</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">⚖️</span><b>3 judge()</b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🔢</span><b>4 <span class="zh">N 局几胜</span><span class="en">best of N</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🧠</span><b>5 <span class="zh">会学习的电脑</span><span class="en">learning AI</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🦎</span><b>6 <span class="zh">加料</span><span class="en">extras</span></b></div>
</div>

<div class="box box-tip"><span class="box-title">📌 <span class="zh">今天会遇到的新东西</span><span class="en">New things you'll meet today</span></span>
<span class="zh">不用背，遇到的时候回来看一眼就行：</span><span class="en">No need to memorise — just come back and peek when you meet them:</span>
<ul>
  <li><code>.strip()</code> / <code>.lower()</code> — <span class="zh">去掉两头的空格 / 全变小写，整理输入（第 2 步）。<b>要存回去</b>：<code>me = me.strip()</code></span><span class="en">remove spaces at both ends / make it all lowercase, to tidy input (step 2). <b>Store it back</b>: <code>me = me.strip()</code></span></li>
  <li><code>if me in choices:</code> — <span class="zh">问「me 在不在这个列表里？」得到 True / False（第 2 步）</span><span class="en">asks "is me in this list?" and gives True / False (step 2)</span></li>
  <li><span class="zh"><code>while True</code> 里的 <code>return</code> — 直接跳出循环<b>和</b>招式（第 2 步）</span><span class="en"><code>return</code> inside <code>while True</code> — jumps out of the loop <b>and</b> the trick (step 2)</span></li>
  <li><code>int(wins / rounds * 100)</code> — <span class="zh">算百分比，<code>int()</code> 去掉小数（第 4 步）</span><span class="en">work out a percentage; <code>int()</code> drops the decimals (step 4)</span></li>
  <li><code>return a, b, c</code> — <span class="zh">一次交回好几个东西，外面用 <code>x, y, z = play_game()</code> 接住（作业，先当魔法用）</span><span class="en">hand back several things at once; catch them with <code>x, y, z = play_game()</code> (homework, treat as magic for now)</span></li>
  <li><code>continue</code>、<code>" / ".join(choices)</code>、<code>t.setheading(120)</code> — <span class="zh">只在第 6 步的加料里出现，代码旁边有注释</span><span class="en">only appear in the step 6 extras, with comments next to them</span></li>
</ul>
</div>

<div class="box box-rule"><span class="zh">📏 <b>每一步的规矩：</b>先猜会发生什么 → 运行 → <b>自己写</b>那一小块 → <b>测试</b> → 能跑了再去下一步。看到 ✍️ 就是「照说明自己写」。</span><span class="en">📏 <b>The rule for every step:</b> guess what happens → run → <b>write</b> that small piece yourself → <b>test</b> → only move on when it runs. A ✍️ means "write it yourself from the description".</span></div>

---

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">第 7 课的「交回一个列表」+ 第 5 课的 <code>append</code> + random。只有一个空，但那一行要你<b>自己想</b>。</span><span class="en">Lesson 7's "return a list" + Lesson 5's <code>append</code> + random. Just one blank, but you have to <b>work out</b> that whole line yourself.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/warmup.py' | relative_url }}" data-canvas="no" data-title="🔁 热身：随机水果篮" data-title-en="🔁 Warm-up: random fruit basket" data-save="warmup-8" data-rows="10"></div>

<ul class="quests" data-key="l8-warmup">
  <li><span class="zh">填好那一行，运行，输入 3。篮子里有 3 个水果吗？</span><span class="en">Fill in that line, run, type 3. Are there 3 fruits in the basket?</span></li>
  <li><span class="zh">✍️ 再写一个 <code>count_fruit(basket, name)</code>：交回 name 在篮子里出现了几次。试试 <code>print(count_fruit(my_basket, "kiwi"))</code>。（这个「数一数」今天还会用到！）</span><span class="en">✍️ Also write <code>count_fruit(basket, name)</code>: returns how many times name is in the basket. Try <code>print(count_fruit(my_basket, "kiwi"))</code>. (This kind of counting comes back later today!)</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">放进篮子：<code>basket.append(random.choice(fruits))</code>。数一数：<code>count = 0</code> → <code>for f in basket:</code> → 一样就 <code>count += 1</code> → 最后 <code>return count</code>。</span><span class="en">Into the basket: <code>basket.append(random.choice(fruits))</code>. Counting: <code>count = 0</code> → <code>for f in basket:</code> → if it matches, <code>count += 1</code> → finally <code>return count</code>.</span></details>

---

## 🪜 <span class="zh">第 1 步：电脑出拳</span><span class="en">Step 1: the computer plays</span>
{: #step1}

<div class="playground" data-src="{{ '/lessons/08/code/step1.py' | relative_url }}" data-canvas="no" data-title="🪜 第 1 步：电脑出拳" data-title-en="🪜 Step 1: computer plays" data-save="rps-step1" data-rows="8"></div>

<ul class="quests" data-key="l8-s1">
  <li><span class="zh">让 <code>computer_play()</code> 交回一个随机的拳（第 5 课的 random.choice），运行几次。5 次里出现过一样的吗？</span><span class="en">Make <code>computer_play()</code> return a random play (Lesson 5's random.choice) and run it a few times. Any repeats in the 5?</span></li>
</ul>

## 🪜 <span class="zh">第 2 步：你出拳——整理输入 + 不合格就再问</span><span class="en">Step 2: you play — tidy input + ask again until it's valid</span>

<p><span class="zh">人打字很随便：<code>" 石头 "</code>、<code>"Rock"</code>、<code>"ROCK"</code>……电脑却很较真。两个小帮手：<b><code>.strip()</code> 去掉两头的空格，<code>.lower()</code> 全变小写</b>。先猜下面每一行打印什么。</span><span class="en">People type messily: <code>" rock "</code>, <code>"Rock"</code>, <code>"ROCK"</code>… but computers are fussy. Two helpers: <b><code>.strip()</code> removes spaces at both ends, <code>.lower()</code> makes it all lowercase</b>. Guess what each line prints.</span></p>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">代码最后：<code>answer = "YES"</code>，然后单独一行 <code>answer.lower()</code>，再 <code>print(answer)</code>。打印什么？</span><span class="en">At the end of the code: <code>answer = "YES"</code>, then <code>answer.lower()</code> on its own line, then <code>print(answer)</code>. What prints?</span></p>
  <div class="opts"><button>yes</button><button><span class="zh">报错</span><span class="en">an error</span></button><button>YES</button></div>
  <div class="why"><span class="zh"><b>YES！</b><code>.lower()</code> 不会改原来的字，它<b>做出一个新的</b>小写字。你不把新的存起来（<code>answer = answer.lower()</code>），它就被扔掉了。这是今天最常见的 bug，虫虫医院的病号 2 就是它！</span><span class="en"><b>YES!</b> <code>.lower()</code> doesn't change the original text — it <b>makes a new</b> lowercase one. If you don't store it (<code>answer = answer.lower()</code>), it's thrown away. This is today's most common bug — Bug Hospital patient 2 has it!</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/08/code/lower-demo.py' | relative_url }}" data-canvas="no" data-title="🧹 .strip() 和 .lower()" data-title-en="🧹 .strip() and .lower()" data-save="strip-lower" data-rows="10"></div>

<p><span class="zh">现在让你出拳。<code>ask_player()</code> 用 <code>while True</code> <b>一直问，直到输入合格</b>，然后用 <code>return</code> 交回——<code>return</code> 会同时跳出循环和招式。</span><span class="en">Now you play. <code>ask_player()</code> uses <code>while True</code> to <b>keep asking until the input is valid</b>, then <code>return</code>s it — and <code>return</code> jumps out of the loop and the trick at the same time.</span></p>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">运行下面的 step 2，先输入 <code>香蕉</code>，再输入 <code>  布 </code>（两头有空格）。问题一共会问几次？最后 me 是什么？</span><span class="en">Run step 2 below and type <code>香蕉</code>, then <code>  布 </code> (spaces around it). How many times is the question asked? What is me at the end?</span></p>
  <div class="opts"><button><span class="zh">问 1 次，me = 香蕉</span><span class="en">Asked once, me = 香蕉</span></button><button><span class="zh">问 2 次，me = 布</span><span class="en">Asked twice, me = 布</span></button><button><span class="zh">问 2 次，me = "  布 "</span><span class="en">Asked twice, me = "  布 "</span></button><button><span class="zh">一直问，停不下来</span><span class="en">Asks forever</span></button></div>
  <div class="why"><span class="zh">香蕉不在列表里 → 打印提示，<code>while True</code> 再转一圈。<code>"  布 "</code> 先被 <code>.strip()</code> 变成 <code>"布"</code>，在列表里 → <code>return "布"</code>，循环和招式一起结束。</span><span class="en">香蕉 isn't in the list → it prints a warning and <code>while True</code> goes round again. <code>"  布 "</code> is stripped to <code>"布"</code>, which is in the list → <code>return "布"</code> ends the loop and the trick together.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/08/code/step2.py' | relative_url }}" data-canvas="no" data-title="🪜 第 2 步：你出拳" data-title-en="🪜 Step 2: you play" data-save="rps-step2" data-draft="l8-step2" data-rows="12"></div>

<ul class="quests" data-key="l8-s2">
  <li><span class="zh">验证上面的猜一猜：输入 <code>香蕉</code>，再输入 <code>  布 </code>。再把 <code>.strip()</code> 删掉试一次——还认得吗？</span><span class="en">Check the quiz: type <code>香蕉</code>, then <code>  布 </code>. Then delete <code>.strip()</code> and try again — still accepted?</span></li>
  <li><span class="zh">✍️ 让 <code>ask_player()</code> 数一数你试了几次，合格时打印「你试了 3 次才出对」这样的话。</span><span class="en">✍️ Make <code>ask_player()</code> count your tries and, when valid, print something like "it took you 3 tries".</span></li>
</ul>

## 🪜 <span class="zh">第 3 步：judge() 判断输赢——测试先行</span><span class="en">Step 3: judge() decides — tests first</span>

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

<p><span class="zh">这次<b>没有填空</b>。画板里先写好了 6 个<b>测试</b>：现在运行，会看到 3 个 ❌。你的任务：在 judge 里写三种「赢」，让 6 个测试<b>全部变 ✅</b>。真正的程序员就是这样工作的：先写测试，再写代码。</span><span class="en">This time there are <b>no blanks</b>. The playground already has 6 <b>tests</b>: run it now and you'll see 3 ❌. Your job: write the three "win" cases in judge so all 6 tests <b>turn ✅</b>. That's how real programmers work: tests first, then code.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/step3.py' | relative_url }}" data-canvas="no" data-title="🪜 第 3 步：judge() + 测试" data-title-en="🪜 Step 3: judge() + tests" data-save="rps-step3" data-draft="l8-step3" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">一种「赢」写两行：<code>elif me == "石头" and computer == "剪刀":</code> 下一行 <code>return "赢"</code>。（第一个 <code>if</code> 已经有了，后面接 <code>elif</code> 或者再写 <code>if</code> 都行——因为 return 之后招式就结束了。）</span><span class="en">One "win" is two lines: <code>elif me == "石头" and computer == "剪刀":</code> then <code>return "赢"</code>. (Following the first <code>if</code> with <code>elif</code> or another <code>if</code> both work — return ends the trick anyway.)</span></details>
<details class="hint"><summary><span class="zh">💡 为什么「输」不用写三行？</span><span class="en">💡 Why doesn't "lose" need three lines?</span></summary><span class="zh">平和赢都检查过了，<b>剩下的只能是输</b>——最后一行 <code>return "输"</code> 接住所有其他情况。</span><span class="en">Tie and win are already checked, so <b>whatever's left must be a loss</b> — the last line <code>return "输"</code> catches everything else.</span></details>

<ul class="quests" data-key="l8-s3">
  <li><span class="zh">6 个测试全部 ✅ 了吗？</span><span class="en">Are all 6 tests ✅?</span></li>
  <li>🐞 <span class="zh">故意把一个 <code>and</code> 改成 <code>or</code>。哪个测试变红了？为什么？测试就是这样<b>帮你抓 bug</b> 的。</span><span class="en">Change one <code>and</code> to <code>or</code> on purpose. Which test turns red? Why? That's how tests <b>catch bugs for you</b>.</span></li>
</ul>

### 🔧 <span class="zh">进阶：把规则装进一个招式</span><span class="en">Stretch: put the rules in one trick</span>

<p><span class="zh">三个 elif 能用，但如果有 5 种拳呢？换个思路：写一个招式 <code>beats_what(play)</code>，<b>交回 play 能赢的那个拳</b>。judge 就只剩一个问题：「我能赢的，正好是电脑出的吗？」</span><span class="en">Three elifs work, but what about 5 plays? Another idea: write <code>beats_what(play)</code> that <b>returns the play that play beats</b>. Then judge asks just one question: "is what I beat exactly what the computer played?"</span></p>

<div class="quiz" data-answer="1">
  <p class="q"><span class="zh">追踪一下：<code>judge("石头", "布")</code> 里，<code>beats_what("石头")</code> 交回什么？最后 judge 交回什么？</span><span class="en">Trace it: inside <code>judge("石头", "布")</code>, what does <code>beats_what("石头")</code> return? What does judge return in the end?</span></p>
  <div class="opts"><button><span class="zh">剪刀；输</span><span class="en">剪刀; 输</span></button><button><span class="zh">布；赢</span><span class="en">布; 赢</span></button><button><span class="zh">剪刀；赢</span><span class="en">剪刀; 赢</span></button></div>
  <div class="why"><span class="zh">石头能赢剪刀，所以交回「剪刀」。「剪刀」≠ 电脑出的「布」，不是赢；也不是平——所以走到最后 <code>return "输"</code>。对照规则表：石头碰布，确实输！</span><span class="en">Rock beats scissors, so it returns 剪刀. 剪刀 ≠ the computer's 布, so not a win; not a tie either — so it reaches <code>return "输"</code>. Check the table: rock vs paper really is a loss!</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/08/code/step3-rules.py' | relative_url }}" data-canvas="no" data-title="🔧 规则招式 beats_what()" data-title-en="🔧 Rule trick beats_what()" data-save="rps-rules" data-draft="l8-rules" data-rows="14"></div>

<ul class="quests" data-key="l8-s3b">
  <li><span class="zh">✍️ 照着 <code>beats_what</code> 写 <code>winner_against(play)</code>：交回<b>能赢</b> play 的拳。测试：<code>winner_against("石头")</code> 应该是 布。第 5 步要用它！</span><span class="en">✍️ Following <code>beats_what</code>, write <code>winner_against(play)</code>: returns the play that <b>beats</b> play. Test: <code>winner_against("石头")</code> should be 布. Step 5 needs it!</span></li>
</ul>

<div class="box box-tip"><span class="box-title">🤖 <span class="zh">卡住了？用排错模板问 AI</span><span class="en">Stuck? Ask AI with the debugging template</span></span>
<span class="zh">红框里有「📋 复制问 AI 要提示的话」按钮——它会把报错和代码一起打包，<b>只要提示，不要答案</b>。没报错但测试是 ❌？这样问：</span><span class="en">The red error box has a "📋 Copy a hint-please message" button that packs the error and code together, asking for <b>a hint, not the answer</b>. No error but a test shows ❌? Ask like this:</span>
<pre class="zh" style="margin:.5em 0;white-space:pre-wrap">我在写石头剪刀布的 judge 函数。测试 judge("布", "石头") 应该是「赢」，但它交回「输」。
这是我的代码：（贴代码）
请告诉我该检查哪一行，不要直接给我改好的代码。</pre><pre class="en" style="margin:.5em 0;white-space:pre-wrap">I'm writing the judge function for Rock Paper Scissors. The test judge("布", "石头") should give "赢" (win), but it returns "输" (lose).
Here is my code: (paste code)
Please tell me which line to check — don't give me the fixed code.</pre><button class="pg-btn copy-prev">📋 <span class="zh">复制</span><span class="en">Copy</span></button>
</div>

---

## 🪜 <span class="zh">第 4 步：N 局几胜 + 统计</span><span class="en">Step 4: best of N + stats</span>
{: #step4}

<p><span class="zh">「五局三胜」= 谁先到 3 分谁赢。<code>target = int(best_of / 2) + 1</code> 帮你算：5 → 3，7 → 4。这一步要你<b>自己写 3 块</b>：加分、宣布赢家、统计。</span><span class="en">"Best of 5" = first to 3 wins. <code>target = int(best_of / 2) + 1</code> works it out: 5 → 3, 7 → 4. This step needs you to <b>write 3 pieces yourself</b>: scoring, announcing the winner, and stats.</span></p>

<div class="quiz" data-answer="1">
  <p class="q"><span class="zh">五局三胜（target = 3）。每一轮的结果依次是：赢、平、输、赢、平、赢、输……循环在第几轮后停？那时 ties 是几？</span><span class="en">Best of 5 (target = 3). The results, round by round: win, tie, lose, win, tie, win, lose… After which round does the loop stop, and what is ties then?</span></p>
  <div class="opts"><button><span class="zh">第 6 轮后，比分 3:1，ties = 2</span><span class="en">After round 6, 3:1, ties = 2</span></button><button><span class="zh">第 5 轮后，比分 3:1，ties = 2</span><span class="en">After round 5, 3:1, ties = 2</span></button><button><span class="zh">第 7 轮后，比分 3:2，ties = 2</span><span class="en">After round 7, 3:2, ties = 2</span></button><button><span class="zh">第 3 轮后，比分 1:1，ties = 1</span><span class="en">After round 3, 1:1, ties = 1</span></button></div>
  <div class="why"><span class="zh">一轮一轮数：1 赢(1:0) 2 平(ties 1) 3 输(1:1) 4 赢(2:1) 5 平(ties 2) 6 赢(<b>3:1</b>)。my_score 到 3，<code>my_score &lt; target</code> 变 False，循环停——第 7 轮根本不会玩。</span><span class="en">Count round by round: 1 win (1:0) 2 tie (ties 1) 3 lose (1:1) 4 win (2:1) 5 tie (ties 2) 6 win (<b>3:1</b>). my_score hits 3, <code>my_score &lt; target</code> becomes False and the loop stops — round 7 never happens.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/08/code/step4.py' | relative_url }}" data-canvas="no" data-title="🪜 第 4 步：N 局几胜" data-title-en="🪜 Step 4: best of N" data-save="rps-step4" data-draft="l8-step4" data-rows="18"></div>

<ul class="quests" data-key="l8-s4">
  <li><span class="zh">✍️ TODO 1：加分（赢 → my_score，输 → computer_score，平 → ties）。玩一整局五局三胜。</span><span class="en">✍️ TODO 1: scoring (win → my_score, lose → computer_score, tie → ties). Play a whole best of 5.</span></li>
  <li><span class="zh">✍️ TODO 2 + 3：宣布赢家；打印一共几轮、平了几次、你的胜率 %。</span><span class="en">✍️ TODO 2 + 3: announce the winner; print rounds played, ties, and your win rate %.</span></li>
  <li><span class="zh">🤔 输入 <code>4</code>（四局几胜？）会怎样？<code>int(4 / 2) + 1</code> 是几？合理吗？（作业 🥈 会让你只接受 3、5、7。）</span><span class="en">🤔 What happens if you type <code>4</code>? What is <code>int(4 / 2) + 1</code>? Does that make sense? (Homework 🥈 makes you accept only 3, 5 or 7.)</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 胜率提示</span><span class="en">💡 Win-rate hint</span></summary><span class="zh">赢了 2 轮，一共 5 轮：<code>2 / 5 * 100</code> = 40.0。用 <code>int(my_score / rounds * 100)</code> 变成 40。为什么用 my_score？因为每赢一轮 my_score 才加 1。</span><span class="en">Won 2 of 5 rounds: <code>2 / 5 * 100</code> = 40.0. <code>int(my_score / rounds * 100)</code> makes it 40. Why my_score? Because it goes up by 1 for each round you win.</span></details>
<details class="hint"><summary><span class="zh">💡 rounds &lt; 20 是干嘛的？</span><span class="en">💡 What is rounds &lt; 20 for?</span></summary><span class="zh">安全带！万一一直平局，没人到 target，循环就永远不停。第 6 课说过：<b>while 一定要有办法停下来</b>。</span><span class="en">A seatbelt! If it's tie after tie, nobody reaches the target and the loop never ends. Lesson 6 rule: <b>a while loop must always have a way to stop</b>.</span></details>

---

## 🧠 <span class="zh">第 5 步（进阶）：会学习的电脑</span><span class="en">Step 5 (stretch): a computer that learns</span>
{: #step5}

<p><span class="zh">还记得第 6 课「从数据学习」吗？这个电脑对手有一个小本本 <code>counts = [0, 0, 0]</code>，偷偷记你出了几次石头、剪刀、布。3 轮之后，它就专门出<b>能赢你最爱的拳</b>。这就是一个最简单的「会学习的 AI」！</span><span class="en">Remember "learning from data" in Lesson 6? This opponent keeps a notebook <code>counts = [0, 0, 0]</code>, secretly counting how often you play rock, scissors and paper. After 3 rounds it always plays <b>what beats your favourite</b>. That's the simplest possible "learning AI"!</span></p>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">小心追踪 <code>favourite()</code>：如果 <code>counts = [2, 3, 3]</code>（石头 2 次、剪刀 3 次、布 3 次），它交回什么？电脑接着出什么？</span><span class="en">Trace <code>favourite()</code> carefully: if <code>counts = [2, 3, 3]</code> (rock 2, scissors 3, paper 3), what does it return? What does the computer play next?</span></p>
  <div class="opts"><button><span class="zh">布；电脑出剪刀</span><span class="en">布; computer plays 剪刀</span></button><button><span class="zh">石头；电脑出布</span><span class="en">石头; computer plays 布</span></button><button><span class="zh">剪刀；电脑出石头</span><span class="en">剪刀; computer plays 石头</span></button></div>
  <div class="why"><span class="zh">best 从 0 开始。i = 1：3 &gt; 2，best = 1。i = 2：3 &gt; 3？<b>不是</b>（一样大不算大于），best 还是 1。所以交回「剪刀」，<code>winner_against("剪刀")</code> = 石头。一样多的时候，排在前面的赢。</span><span class="en">best starts at 0. i = 1: 3 &gt; 2, best = 1. i = 2: is 3 &gt; 3? <b>No</b> (equal isn't greater), best stays 1. So it returns 剪刀, and <code>winner_against("剪刀")</code> = 石头. On a draw, the earlier one wins.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/08/code/step5.py' | relative_url }}" data-canvas="no" data-title="🧠 第 5 步：会学习的电脑" data-title-en="🧠 Step 5: a learning computer" data-save="rps-smart" data-draft="l8-smart" data-rows="18"></div>

<ul class="quests" data-key="l8-s5">
  <li><span class="zh">每轮都出石头。第 4 轮开始电脑出什么？你的比分怎么样？</span><span class="en">Play rock every round. From round 4, what does the computer play? How's your score?</span></li>
  <li><span class="zh">🕵️ 现在你知道它的秘密了——想办法<b>打败它</b>！（提示：它出的永远是能赢你「最爱」的拳……）</span><span class="en">🕵️ Now you know its secret — find a way to <b>beat it</b>! (Hint: it always plays what beats your "favourite"…)</span></li>
  <li><span class="zh">✍️ 最后加一行，打印你的胜率 %（和第 4 步一样算）。</span><span class="en">✍️ Add a line at the end that prints your win rate % (same as step 4).</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 怎么打败它？</span><span class="en">💡 How to beat it?</span></summary><span class="zh">如果你一直出石头，它就一直出布。那你出什么能赢布？出几轮之后你的「最爱」变了，它又会跟着变——这就是<b>你在和 AI 互相学习</b>。</span><span class="en">If you keep playing rock, it keeps playing paper. So what beats paper? After a few rounds your "favourite" changes, and it follows — <b>you and the AI are learning from each other</b>.</span></details>

---

## 🦎 <span class="zh">第 6 步：加料（选做）</span><span class="en">Step 6: extras (optional)</span>

<p><span class="zh"><b>蜥蜴和史波克：</b>5 种拳、10 条「谁赢谁」。<code>beats</code> 列表<b>用一行代替 10 个 elif</b>。这里还有 <code>continue</code>（跳过这一轮剩下的代码，回到 while 开头）和 <code>" / ".join(choices)</code>（把列表连成一句话）。</span><span class="en"><b>Lizard and Spock:</b> 5 plays, 10 "who beats whom" rules. The <code>beats</code> list <b>replaces 10 elifs with one line</b>. You'll also see <code>continue</code> (skip the rest of this round, back to the top of the while) and <code>" / ".join(choices)</code> (glue a list into one string).</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/step6.py' | relative_url }}" data-canvas="no" data-title="🦎 加料：蜥蜴史波克" data-title-en="🦎 Extra: Lizard Spock" data-save="rps-step6" data-draft="l8-step6" data-rows="14"></div>

<ul class="quests" data-key="l8-s6">
  <li><span class="zh"><code>if [me, computer] in beats:</code> 这一行在问什么？用自己的话说。</span><span class="en">What is <code>if [me, computer] in beats:</code> asking? Say it in your own words.</span></li>
  <li><span class="zh">发明第 6 种拳（比如「火箭」），加进 <code>choices</code> 和 <code>beats</code>，让它赢两个、输两个、和一个……等等，这样公平吗？想一想 6 种拳怎么分才公平。</span><span class="en">Invent a 6th play (like "rocket"), add it to <code>choices</code> and <code>beats</code>… but how do you make 6 plays fair? Think about it.</span></li>
</ul>

<p><span class="zh"><b>海龟庆祝：</b>每赢一次画一颗金星。你的任务：写 <code>sad_face(x, y)</code>，输的时候画。</span><span class="en"><b>Turtle celebration:</b> a gold star for every win. Your job: write <code>sad_face(x, y)</code> for losses.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/celebrate.py' | relative_url }}" data-title="🐢 加料：海龟庆祝" data-title-en="🐢 Extra: turtle celebration" data-save="rps-celebrate" data-draft="l8-celebrate" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 sad_face 提示</span><span class="en">💡 sad_face hint</span></summary><span class="zh"><code>def sad_face(x, y):</code> → penup, goto(x, y), pendown → <code>t.circle(25)</code> 脸 → penup 挪到眼睛位置 <code>t.dot(6)</code> 两次 → 嘴巴：penup 挪到 <code>(x + 12, y + 12)</code>，pendown，<code>t.setheading(120)</code>（让海龟脸朝 120 度）然后 <code>t.circle(14, 120)</code>（只画 120 度的一段弧）——画出一座小山 ∩，就是不开心的嘴（画完 <code>t.setheading(0)</code> 转回来）。喊它：<code>sad_face(-200 + computer_score * 100, -100)</code>。</span><span class="en"><code>def sad_face(x, y):</code> → penup, goto(x, y), pendown → <code>t.circle(25)</code> for the face → penup to the eyes, <code>t.dot(6)</code> twice → mouth: penup to <code>(x + 12, y + 12)</code>, pendown, <code>t.setheading(120)</code> (point the turtle at 120°) then <code>t.circle(14, 120)</code> (draw only a 120° piece of circle) — a little hill ∩, an unhappy mouth (then <code>t.setheading(0)</code> to turn back). Call it: <code>sad_face(-200 + computer_score * 100, -100)</code>.</span></details>

---

## 🧪 <span class="zh">测试你的游戏：当一个捣蛋鬼</span><span class="en">Test your game: be a troublemaker</span>
{: #test}

<p><span class="zh">程序员写完代码不算完——要<b>试着弄坏它</b>。回到第 4 步的画板，挨个试：</span><span class="en">Writing code isn't the end — programmers <b>try to break it</b>. Go back to step 4 and try each one:</span></p>

<ul class="quests" data-key="l8-test">
  <li><span class="zh">🍌 输入「香蕉」——程序崩了还是礼貌地再问一次？</span><span class="en">🍌 Type "banana" — crash, or a polite ask-again?</span></li>
  <li><span class="zh">⬜ 什么都不输直接回车——会怎样？</span><span class="en">⬜ Press Enter with nothing typed — what happens?</span></li>
  <li><span class="zh">🔢 「几局几胜」那里输入 <code>abc</code>——会怎样？为什么？（读报错！作业 🥈 会修好它）</span><span class="en">🔢 Type <code>abc</code> for "best of" — what happens? Why? (Read the error! Homework 🥈 fixes it)</span></li>
  <li><span class="zh">🔁 一直出同一个拳——比分、平局数、胜率每一轮都对吗？</span><span class="en">🔁 Play the same move every time — are score, ties and win rate right every round?</span></li>
  <li><span class="zh">🏁 游戏结束时，赢的人真的是分高的那个吗？胜率加起来说得通吗？</span><span class="en">🏁 At the end, is the winner really the one with more points? Does the win rate make sense?</span></li>
</ul>

### 🐞 <span class="zh">虫虫医院：两个「不报错」的病号</span><span class="en">Bug hospital: two patients that don't crash</span>

<p><span class="zh">这两个病号都<b>不报错</b>——最难找的 bug！只能靠读代码、对答案。输出和期望的一模一样就过关。</span><span class="en">Neither patient <b>crashes</b> — the hardest kind of bug! You can only find them by reading the code and checking the output. Match the wanted output to win.</span></p>

<p><span class="zh">病号 1：期望的输出是 赢、赢、赢、输、平。</span><span class="en">Patient 1: the wanted output is 赢, 赢, 赢, 输, 平.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/bug1.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 1：判错了" data-title-en="🐞 Patient 1: wrong verdict" data-save="bug1-fixed" data-expect="赢\n赢\n赢\n输\n平" data-badge="lesson8-bug1" data-rows="12"></div>

<p><span class="zh">病号 2：整理输入的招式好像什么都没做。期望 <code>[rock]</code>、<code>[paper]</code>、<code>[scissors]</code>。</span><span class="en">Patient 2: the tidy-up trick seems to do nothing. Wanted: <code>[rock]</code>, <code>[paper]</code>, <code>[scissors]</code>.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/bug2.py' | relative_url }}" data-canvas="no" data-title="🐞 病号 2：整理失败" data-title-en="🐞 Patient 2: tidying fails" data-save="bug2-fixed" data-expect="[rock]\n[paper]\n[scissors]" data-badge="lesson8-bug2" data-rows="12"></div>

<details class="hint"><summary><span class="zh">💡 病号 1 提示</span><span class="en">💡 Patient 1 hint</span></summary><span class="zh">对着规则表看第三个「赢」：布赢<b>谁</b>？</span><span class="en">Check the third "win" against the table: paper beats <b>what</b>?</span></details>
<details class="hint"><summary><span class="zh">💡 病号 2 提示</span><span class="en">💡 Patient 2 hint</span></summary><span class="zh">回去看第 2 步的猜一猜：<code>answer.lower()</code> 单独一行，answer 变了吗？</span><span class="en">Go back to the step 2 quiz: with <code>answer.lower()</code> on its own line, did answer change?</span></details>

<p><span class="zh">想治更多病号？去 <a href="{{ '/games/bugs/' | relative_url }}">🐞 虫虫医院</a>！</span><span class="en">Want more patients? Go to the <a href="{{ '/games/bugs/' | relative_url }}">🐞 Bug Hospital</a>!</span></p>

---

## 🤖 <span class="zh">和 AI 一起：排错伙伴，不是代写机器</span><span class="en">With AI: a debugging buddy, not a writing machine</span>

<div class="chat">
  <div class="bubble me"><span class="zh">😃 <b>好问题：</b>我在做石头剪刀布，五局三胜。第 3 轮比分应该是 2:1，但显示 1:1，平局数也不对。我的代码：（贴代码）。我怀疑是加分那里。请给我一个提示，告诉我该看哪几行，不要直接给答案。</span><span class="en">😃 <b>Good ask:</b> I'm making best-of-5 Rock Paper Scissors. In round 3 the score should be 2:1 but it shows 1:1, and the tie count is wrong too. My code: (paste). I suspect the scoring part. Please give me a hint about which lines to look at, not the answer.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">看看「输」的那个分支——你加的是哪个变量？</span><span class="en">Look at the "lose" branch — which variable are you adding to?</span></div>
  <div class="bubble me"><span class="zh">😕 <b>坏问题：</b>帮我写一个石头剪刀布游戏。——写出来了，但不是你的，你也不知道它对不对。</span><span class="en">😕 <b>Bad ask:</b> Write me a Rock Paper Scissors game. — You get one, but it isn't yours and you can't tell if it's right.</span></div>
</div>

<div class="box box-rule"><span class="zh">📜 <b>好问题的三件套：</b>① 我在做什么 ② 我期望 vs 实际发生了什么（带报错 / 带输出 / 哪个测试是 ❌）③「给提示，不要答案」。AI 给的提示，<b>你自己改、自己运行</b>。</span><span class="en">📜 <b>A good ask has three parts:</b> ① what I'm making ② expected vs what actually happened (with the error / output / which test is ❌) ③ "hint, not answer". Then <b>you make the fix and run it</b>.</span></div>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>.strip() / .lower()</b><code>me = input("? ").strip().lower()</code><span><span class="zh">去空格、变小写。<b>要存回去！</b></span><span class="en">Remove spaces, lowercase. <b>Store it back!</b></span></span></div>
  <div class="k"><b>in / not in</b><code>if me in choices:
    return me</code><span><span class="zh">在不在列表里？True / False</span><span class="en">Is it in the list? True / False</span></span></div>
  <div class="k"><b><span class="zh">问到合格为止</span><span class="en">ask until valid</span></b><code>def ask_player():
    while True:
        me = input("? ").strip()
        if me in choices:
            return me</code><span><span class="zh">return 跳出循环和招式。</span><span class="en">return leaves the loop and the trick.</span></span></div>
  <div class="k"><b><span class="zh">测试先行</span><span class="en">tests first</span></b><code>print(judge("布", "石头") == "赢")</code><span><span class="zh">固定的输入 → 期望的输出。全 True 才放心。</span><span class="en">Fixed input → expected output. All True before you relax.</span></span></div>
  <div class="k"><b><span class="zh">规则招式</span><span class="en">a rule trick</span></b><code>if beats_what(me) == computer:
    return "赢"</code><span><span class="zh">一个招式代替一堆 elif。</span><span class="en">One trick instead of a pile of elifs.</span></span></div>
  <div class="k"><b><span class="zh">N 局几胜 + 胜率</span><span class="en">best of N + win rate</span></b><code>target = int(best_of / 2) + 1
rate = int(wins / rounds * 100)</code><span><span class="zh">5 → 先到 3；int() 去掉小数。</span><span class="en">5 → first to 3; int() drops decimals.</span></span></div>
  <div class="k"><b><span class="zh">用列表数数</span><span class="en">counting with a list</span></b><code>counts = [0, 0, 0]
counts[i] += 1</code><span><span class="zh">会学习的电脑的小本本。</span><span class="en">The learning computer's notebook.</span></span></div>
</div>

<p><span class="zh">全部指令在 <a href="{{ '/cheatsheet/' | relative_url }}#l08">📖 小词典 · 第 8 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l08">📖 cheat sheet · Lesson 8</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/08/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
