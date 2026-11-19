---
title: 第 9 课 · 学一学
title_en: Lesson 9 · Learn
lesson: "09"
tab: learn
playground: true
---

# 📖 <span class="zh">第 9 课：字典 + AI 侦探</span><span class="en">Lesson 9: Dictionaries + AI detective</span>

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">第 7 课的<b>函数</b> + 第 8 课的 <b>.strip().lower()</b>：数一数上节课一个玩家出了几次石头。打字很乱，要先整理！</span><span class="en"><b>Functions</b> (Lesson 7) + <b>.strip().lower()</b> (Lesson 8): count how often a player played rock last lesson. The typing is messy — tidy it first!</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/warmup.py' | relative_url }}" data-title="🔁 热身：数一数" data-title-en="🔁 Warm-up: count them" data-canvas="no" data-save="count-moves" data-rows="10"></div>

<ul class="quests" data-key="l9-warm">
  <li><span class="zh">填好空，三行结果是 4、2、1 吗？</span><span class="en">Fill the blank. Are the three results 4, 2, 1?</span></li>
  <li>🤔 <span class="zh">想一想：要数 3 种拳，我们喊了 3 次 <code>count_move</code>，每次都把整个列表从头看一遍。如果有 100 种不同的词呢？——今天的新魔法能<b>只看一遍</b>就全部数完（例 4）。</span><span class="en">🤔 Think: to count 3 moves we called <code>count_move</code> 3 times, each time reading the whole list from the start. What about 100 different words? — today's new magic counts them all in <b>one pass</b> (Example 4).</span></li>
</ul>

---

## ✨ <span class="zh">今天的新魔法：字典</span><span class="en">Today's new magic: dictionaries</span>
{: #dict}

<p class="zh">列表是一排<b>编号</b>的格子（0、1、2……）。<b>字典</b>是一排<b>贴了标签</b>的抽屉：标签叫<b>键</b>（key），抽屉里的东西叫<b>值</b>（value）。你不用记「第几个」，直接说标签就能拿到东西——就像真正的词典，查「kai」就得到「food」。</p>
<p class="en">A list is a row of <b>numbered</b> boxes (0, 1, 2…). A <b>dictionary</b> is a row of <b>labelled</b> drawers: the label is the <b>key</b>, the thing inside is the <b>value</b>. You don't remember "which number" — you say the label and get the thing. Just like a real dictionary: look up "kai", get "food".</p>

<div class="cmds">
  <div class="cmd"><code>d = {"kai": "food"}</code><span><span class="zh">做一个字典：标签: 东西</span><span class="en">Make a dict: label: thing</span></span></div>
  <div class="cmd"><code>d["kai"]</code><span><span class="zh">用标签拿东西</span><span class="en">Get the thing by its label</span></span></div>
  <div class="cmd"><code>d["ra"] = "sun"</code><span><span class="zh">放进新抽屉；标签已经有了就<b>换掉</b>里面的东西</span><span class="en">Add a drawer; if the label exists, <b>replace</b> what's inside</span></span></div>
  <div class="cmd"><code>"kai" in d</code><span><span class="zh">有这个标签吗？True / False</span><span class="en">Is this label there? True / False</span></span></div>
  <div class="cmd"><code>d.get("x", "没有")</code><span><span class="zh">安全地拿：没有就给默认值</span><span class="en">Safe get: a default if missing</span></span></div>
  <div class="cmd"><code>for k in d:</code><span><span class="zh">一个标签一个标签地看</span><span class="en">Go through every label</span></span></div>
  <div class="cmd"><code>for k, v in d.items():</code><span><span class="zh">标签和东西一起拿（例 3）</span><span class="en">Label and thing together (Example 3)</span></span></div>
  <div class="cmd"><code>d[k] = d.get(k, 0) + 1</code><span><span class="zh">数数的魔法公式（例 4）</span><span class="en">The magic counting line (Example 4)</span></span></div>
</div>

### 🤔 <span class="zh">先猜，再运行</span><span class="en">Guess first, then run</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的代码里，<code>print(maori["kai"])</code> 会显示什么？</span><span class="en">In the code below, what does <code>print(maori["kai"])</code> show?</span></p>
  <div class="opts"><button>kai</button><button>food</button><button>2</button></div>
  <div class="why"><span class="zh">"kai" 是标签，抽屉里装的是 "food"。字典总是「标签 → 东西」。</span><span class="en">"kai" is the label; the drawer holds "food". A dict is always "label → thing".</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/09/code/dict1.py' | relative_url }}" data-title="📖 例 1：我的第一个字典" data-title-en="📖 Example 1: my first dictionary" data-canvas="no" data-save="my-dict" data-rows="10"></div>

### 🔍 <span class="zh">改一改</span><span class="en">Change it</span>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">如果把 <code># print(maori["sun"])</code> 前面的 <code>#</code> 去掉，会怎样？</span><span class="en">If you remove the <code>#</code> before <code># print(maori["sun"])</code>, what happens?</span></p>
  <div class="opts"><button><span class="zh">显示 sun</span><span class="en">Shows sun</span></button><button><span class="zh">显示空白</span><span class="en">Shows nothing</span></button><button><span class="zh">报错 KeyError</span><span class="en">KeyError</span></button></div>
  <div class="why"><span class="zh">没有「sun」这个标签，电脑会说 <b>KeyError</b>（找不到钥匙）。安全的拿法是 <code>.get("sun", "不知道")</code>。</span><span class="en">There's no "sun" label, so the computer says <b>KeyError</b> (key not found). The safe way is <code>.get("sun", "don't know")</code>.</span></div>
</div>

<div class="quiz" data-answer="4">
  <p class="q"><span class="zh">🧠 追踪题（先在纸上一行一行算）：</span><span class="en">🧠 Trace it (work line by line on paper):</span></p>
<pre>snacks = {"kiwi": 3, "feijoa": 1}
snacks["kiwi"] = snacks["kiwi"] + 2
snacks["apple"] = 4
snacks["feijoa"] = snacks.get("feijoa", 0) + snacks.get("mango", 0)
print(len(snacks), snacks["kiwi"], snacks["feijoa"])</pre>
  <div class="opts"><button>2 5 1</button><button>3 2 1</button><button><span class="zh">报错 KeyError（没有 mango）</span><span class="en">KeyError (no mango)</span></button><button>3 5 1</button></div>
  <div class="why"><span class="zh">kiwi：3 + 2 = <b>5</b>（标签一样 = 换掉旧的）。apple 是新抽屉，现在一共 <b>3</b> 个。mango 不存在，但用的是 <code>.get</code>，给默认值 0，所以 feijoa = 1 + 0 = <b>1</b>，不会报错。</span><span class="en">kiwi: 3 + 2 = <b>5</b> (same label = replace). apple is a new drawer, so <b>3</b> drawers now. mango doesn't exist, but <code>.get</code> gives the default 0, so feijoa = 1 + 0 = <b>1</b>, no error.</span></div>
</div>

<ul class="quests" data-key="l9-ex1">
  <li><span class="zh">去掉 <code>#</code>，运行，读一读红框里的话，再把 <code>#</code> 加回去。</span><span class="en">Remove the <code>#</code>, run it, read the red box, then put the <code>#</code> back.</span></li>
  <li><span class="zh">加一个新词：<code>maori["rā"] = "sun"</code>，再 <code>print(maori["rā"])</code>。<code>len(maori)</code> 变成几了？</span><span class="en">Add a word: <code>maori["rā"] = "sun"</code>, then <code>print(maori["rā"])</code>. What is <code>len(maori)</code> now?</span></li>
  <li><span class="zh">加一行 <code>print("kai" in maori)</code> 和 <code>print("food" in maori)</code>。第二个为什么是 False？（<code>in</code> 只看<b>标签</b>！）</span><span class="en">Add <code>print("kai" in maori)</code> and <code>print("food" in maori)</code>. Why is the second False? (<code>in</code> only looks at <b>labels</b>!)</span></li>
</ul>

### 🧪 <span class="zh">例 2：翻译机 app（会学新词！）</span><span class="en">Example 2: translator app (it learns new words!)</span>

<p><span class="zh">第 6 课的 <code>while True</code> + 第 8 课的 <code>.strip().lower()</code> + 今天的字典 = 一个真正的 app。不认识的词，它会问你，然后<b>记住</b>。</span><span class="en"><code>while True</code> (Lesson 6) + <code>.strip().lower()</code> (Lesson 8) + today's dict = a real app. Words it doesn't know, it asks you about, then <b>remembers</b>.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/translator.py' | relative_url }}" data-title="🗣️ 例 2：翻译机" data-title-en="🗣️ Example 2: translator" data-canvas="no" data-save="translator" data-draft="l9-translator" data-rows="14"></div>

<ul class="quests" data-key="l9-ex2">
  <li><span class="zh">输入 <code>kai</code>，再输入一个它不认识的词，教它，然后再输一次同一个词——它记住了吗？</span><span class="en">Type <code>kai</code>, then a word it doesn't know, teach it, then type that word again — did it remember?</span></li>
  <li><span class="zh">✍️ 加一个命令：输入 <code>全部</code> 就把现在会的词全部打印出来（不用等到结束）。</span><span class="en">✍️ Add a command: typing <code>全部</code> prints every word it knows right now (without waiting for the end).</span></li>
  <li><span class="zh">✍️ 再加一个命令：输入 <code>改</code>，问哪个词、新的意思是什么，然后<b>更新</b>它。如果那个词根本不存在，要说一声，不要偷偷加进去。</span><span class="en">✍️ Add another command: <code>改</code> (edit) asks which word and its new meaning, then <b>updates</b> it. If the word doesn't exist, say so — don't secretly add it.</span></li>
  <li>🐞 <span class="zh">把 <code>if word in maori:</code> 改成 <code>if word in "maori":</code>，猜猜会怎样？（引号让它变成了一段文字！）</span><span class="en">Change <code>if word in maori:</code> to <code>if word in "maori":</code>. What happens? (The quotes make it a piece of text!)</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 「全部」和「改」的提示</span><span class="en">💡 Hint for 全部 and 改</span></summary><span class="zh">在 <code>if word == "再见":</code> 后面接 <code>elif word == "全部":</code>（用最后那个 for 循环）和 <code>elif word == "改":</code>。「改」里面：<code>w = input(...)</code> → <code>if w in maori:</code> 才 <code>maori[w] = input(...)</code>，<code>else:</code> 打印「没有这个词」。原来的 <code>if word in maori:</code> 要变成 <code>elif</code>。</span><span class="en">After <code>if word == "再见":</code> add <code>elif word == "全部":</code> (reuse the for loop at the end) and <code>elif word == "改":</code>. Inside 改: <code>w = input(...)</code> → only <code>if w in maori:</code> do <code>maori[w] = input(...)</code>, <code>else:</code> print "no such word". The old <code>if word in maori:</code> becomes an <code>elif</code>.</span></details>

### 🪐 <span class="zh">例 3（进阶）：行星资料库——抽屉里放列表，<code>.items()</code> 一起拿</span><span class="en">Example 3 (stretch): planet database — lists in the drawers, <code>.items()</code> to grab both</span>
{: #planets}

<p><span class="zh">字典的「东西」可以是<b>任何东西</b>，包括一整个列表！<code>moons["火星"]</code> 就是 <code>["火卫一", "火卫二"]</code>。<code>for planet, moon_list in moons.items():</code> 每一圈同时拿到<b>标签和东西</b>，不用再写 <code>moons[planet]</code>。</span><span class="en">A drawer can hold <b>anything</b>, even a whole list! <code>moons["火星"]</code> is <code>["火卫一", "火卫二"]</code> (Phobos and Deimos). <code>for planet, moon_list in moons.items():</code> gives you <b>the label and the thing</b> each time round — no more <code>moons[planet]</code>.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/planets.py' | relative_url }}" data-title="🪐 例 3：行星资料库" data-title-en="🪐 Example 3: planet database" data-canvas="no" data-save="planets" data-draft="l9-planets" data-rows="14"></div>

<ul class="quests" data-key="l9-planets">
  <li><span class="zh"><code>moons["火星"][0]</code> 是什么？<code>len(moons["地球"])</code> 呢？先猜，再加一行 print 验证。</span><span class="en">What is <code>moons["火星"][0]</code>? And <code>len(moons["地球"])</code>? Guess, then add a print to check.</span></li>
  <li><span class="zh">✍️ 再做一个字典 <code>order</code>：行星 → 离太阳第几近（水星 1、金星 2、地球 3、火星 4）。用 <code>.items()</code> 打印「地球 是第 3 颗行星」这样的句子。</span><span class="en">✍️ Make another dict <code>order</code>: planet → its position from the Sun (Mercury 1, Venus 2, Earth 3, Mars 4). Use <code>.items()</code> to print sentences like "Earth is planet number 3".</span></li>
  <li><span class="zh">✍️ 写一个函数 <code>most_moons(moons)</code>：交回卫星最多的那颗行星（就像上节课的 favourite()）。</span><span class="en">✍️ Write a function <code>most_moons(moons)</code> that returns the planet with the most moons (just like last lesson's favourite()).</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 most_moons 提示</span><span class="en">💡 most_moons hint</span></summary><span class="zh"><code>best = ""</code> → <code>for planet, moon_list in moons.items():</code> → <code>if best == "" or len(moon_list) &gt; len(moons[best]):</code> → <code>best = planet</code> → 最后 <code>return best</code>。</span><span class="en"><code>best = ""</code> → <code>for planet, moon_list in moons.items():</code> → <code>if best == "" or len(moon_list) &gt; len(moons[best]):</code> → <code>best = planet</code> → finally <code>return best</code>.</span></details>

<div class="box box-tip"><span class="zh">🔭 为什么只写了 4 颗行星？木星和土星的卫星<b>非常多</b>，而且天文学家还在不断发现新的，数字一直在变——这种会变的数字，最容易让 AI 说错（它可能记的是旧数字）。真想知道，就去查最新的资料！</span><span class="en">🔭 Why only 4 planets? Jupiter and Saturn have <b>lots</b> of moons, and astronomers keep discovering new ones, so the number keeps changing — exactly the kind of fact AI gets wrong (it might remember an old number). If you want to know, look up an up-to-date source!</span></div>

### 🔢 <span class="zh">例 4（进阶）：用字典数数</span><span class="en">Example 4 (stretch): counting with a dictionary</span>
{: #count}

<p><span class="zh">上节课的会学习的电脑用 <code>counts = [0, 0, 0]</code>，还得记住「第 0 个是石头」。用字典，<b>标签就是名字本身</b>。这一行是今天最有用的魔法：</span><span class="en">Last lesson's learning computer used <code>counts = [0, 0, 0]</code> and had to remember "slot 0 = rock". With a dict, <b>the label is the name itself</b>. This line is today's most useful magic:</span></p>

<pre>counts[m] = counts.get(m, 0) + 1</pre>

<p><span class="zh">读法：「m 原来有几个？（没有就当 0）加 1，再放回 m 的抽屉。」</span><span class="en">Read it as: "how many m's so far? (0 if none) add 1, put it back in m's drawer."</span></p>

<div class="quiz" data-answer="1">
  <p class="q"><span class="zh"><code>moves = ["布", "石头", "布", "布", "剪刀"]</code>，用上面的公式数完之后，<code>print(counts["布"], len(counts))</code> 打印什么？</span><span class="en"><code>moves = ["布", "石头", "布", "布", "剪刀"]</code>. After counting with the line above, what does <code>print(counts["布"], len(counts))</code> print?</span></p>
  <div class="opts"><button>3 3</button><button>3 5</button><button>1 3</button><button><span class="zh">报错 KeyError</span><span class="en">KeyError</span></button></div>
  <div class="why"><span class="zh">布出现 3 次 → 3。字典里只有 3 个<b>不同的</b>标签（布、石头、剪刀）→ len 是 3，不是 5。第一次见到「布」时抽屉还不存在，但 <code>.get(m, 0)</code> 给了 0，所以不会报错。</span><span class="en">布 appears 3 times → 3. The dict only has 3 <b>different</b> labels (布, 石头, 剪刀) → len is 3, not 5. The first time 布 shows up its drawer doesn't exist yet, but <code>.get(m, 0)</code> gives 0, so no error.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/09/code/counter.py' | relative_url }}" data-title="🔢 例 4：用字典数数" data-title-en="🔢 Example 4: counting with a dict" data-canvas="no" data-save="dict-counter" data-draft="l9-counter" data-rows="14"></div>

<ul class="quests" data-key="l9-count">
  <li><span class="zh">看打印出来的每一行：字典是怎么一步一步长大的？</span><span class="en">Look at each printed line: how does the dict grow step by step?</span></li>
  <li><span class="zh">✍️ 把 <code>moves</code> 换成热身里那串乱七八糟的英文拳（<code>"Rock"</code>、<code>" paper"</code>……），用<b>同一个循环</b>数出 rock 4、paper 2、scissors 1。（数之前先整理！）</span><span class="en">✍️ Replace <code>moves</code> with the messy English list from the warm-up (<code>"Rock"</code>, <code>" paper"</code>…) and count rock 4, paper 2, scissors 1 with <b>the same loop</b>. (Tidy before counting!)</span></li>
  <li>🐞 <span class="zh">把公式改成 <code>counts[m] = counts[m] + 1</code>，运行。报什么错？为什么第一个词就出事？</span><span class="en">Change the line to <code>counts[m] = counts[m] + 1</code> and run. What error? Why does it break on the very first word?</span></li>
</ul>

### 🏆 <span class="zh">例 5（选做）：字典版石头剪刀布</span><span class="en">Example 5 (optional): Rock Paper Scissors with dicts</span>

<p><span class="zh">上节课的 <code>beats_what()</code>、<code>winner_against()</code>、<code>counts</code>，<b>全部变成了字典</b>。和第 8 课的代码比一比，短了多少？</span><span class="en">Last lesson's <code>beats_what()</code>, <code>winner_against()</code> and <code>counts</code> — <b>all dictionaries now</b>. Compare with Lesson 8: how much shorter is it?</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/score.py' | relative_url }}" data-title="🏆 例 5：字典版石头剪刀布" data-title-en="🏆 Example 5: RPS with dicts" data-canvas="no" data-save="rps-dict" data-draft="l9-score" data-rows="14"></div>

<ul class="quests" data-key="l9-ex5">
  <li><span class="zh">为什么 <code>beats[me] == computer</code> 就是「我赢了」？<code>beats</code> 和 <code>winner_against</code> 有什么关系？</span><span class="en">Why does <code>beats[me] == computer</code> mean "I win"? How are <code>beats</code> and <code>winner_against</code> related?</span></li>
</ul>

### 🏆 <span class="zh">挑战：我的资料库 app</span><span class="en">Challenge: my database app</span>

<p><span class="zh">做一个<b>你自己的</b>资料库：宝可梦 → 属性？游戏角色 → 技能？朋友昵称 → 最爱的食物？要有 4 个功能（写在画板最上面）：<b>查、加 / 改、全部、统计</b>——统计要用<b>第二个字典</b>数每个词被查了几次。满意了就 📤 存到作品墙。</span><span class="en">Build <b>your own</b> database: Pokémon → type? game character → skill? friend's nickname → favourite food? It needs 4 features (listed at the top of the playground): <b>look up, add / update, list all, stats</b> — stats uses <b>a second dict</b> to count how often each word is looked up. Happy with it? 📤 Save to Gallery.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/challenge.py' | relative_url }}" data-title="🏆 挑战：我的资料库" data-title-en="🏆 Challenge: my database" data-canvas="no" data-save="my-dict-app" data-draft="l9-challenge" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 「要换掉吗？」怎么写</span><span class="en">💡 How to do "replace it?"</span></summary><span class="zh">先问标签和内容。<code>if word in my_dict:</code> → 再问一句 y / n，是 y 才 <code>my_dict[word] = value</code>；<code>else:</code> 直接放进去。</span><span class="en">Ask for the label and the value. <code>if word in my_dict:</code> → ask y / n, and only on y do <code>my_dict[word] = value</code>; <code>else:</code> just put it in.</span></details>

---

## 🕵️ <span class="zh">AI 侦探训练</span><span class="en">AI detective training</span>
{: #detective}

<p class="zh">AI 非常厉害，但它有个毛病：<b>不知道的时候，也会一本正经地编一个答案</b>，听起来特别像真的。程序员叫这个「幻觉」。聪明的 AI 用户不是不用 AI，而是<b>会检验</b>。</p>
<p class="en">AI is amazing, but it has a flaw: <b>when it doesn't know, it may confidently make something up</b> that sounds totally real. Programmers call this a "hallucination". A smart AI user doesn't avoid AI — they <b>check</b>.</p>

### ① <span class="zh">AI 会一本正经地编造</span><span class="en">① AI makes things up with a straight face</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面三句都是 AI 说的。哪一句是<b>错</b>的？</span><span class="en">All three were said by an AI. Which one is <b>wrong</b>?</span></p>
  <div class="opts"><button><span class="zh">新西兰最有名的象征鸟是几维鸟（kiwi）</span><span class="en">New Zealand's best-known symbol bird is the kiwi</span></button><button><span class="zh">新西兰的首都是奥克兰</span><span class="en">New Zealand's capital is Auckland</span></button><button><span class="zh">Python 里 <code>len("kiwi")</code> 是 4</span><span class="en">In Python, <code>len("kiwi")</code> is 4</span></button></div>
  <div class="why"><span class="zh">首都是<b>惠灵顿</b>（Wellington）！奥克兰是最大的城市，所以很多人（和 AI）会搞混。听起来越「理所当然」的话，越要查一下。</span><span class="en">The capital is <b>Wellington</b>! Auckland is the biggest city, so people (and AI) mix them up. The more "obvious" something sounds, the more worth checking.</span></div>
</div>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">再来：哪一句是错的？</span><span class="en">Again: which one is wrong?</span></p>
  <div class="opts"><button><span class="zh">Python 的列表从 0 开始数</span><span class="en">Python lists start counting at 0</span></button><button><span class="zh">字典用 <code>{}</code>，列表用 <code>[]</code></span><span class="en">Dicts use <code>{}</code>, lists use <code>[]</code></span></button><button><span class="zh"><code>d.get("x")</code> 找不到会报错 KeyError</span><span class="en"><code>d.get("x")</code> gives a KeyError if missing</span></button></div>
  <div class="why"><span class="zh"><code>.get</code> 找不到<b>不会报错</b>，会给 None 或你写的默认值；会报错的是 <code>d["x"]</code>。你刚才在例 1 里亲手验证过——<b>运行代码</b>就是最好的核实方法。</span><span class="en"><code>.get</code> <b>doesn't error</b> when missing — it gives None or your default; <code>d["x"]</code> is the one that errors. You verified this in Example 1 — <b>running the code</b> is the best check.</span></div>
</div>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">🚀 太空题：哪一句是错的？</span><span class="en">🚀 Space round: which one is wrong?</span></p>
  <div class="opts"><button><span class="zh">木星是太阳系最大的行星</span><span class="en">Jupiter is the biggest planet in the Solar System</span></button><button><span class="zh">1969 年，阿姆斯特朗成为第一个踏上月球的人</span><span class="en">In 1969, Neil Armstrong became the first person to walk on the Moon</span></button><button><span class="zh">火星没有卫星</span><span class="en">Mars has no moons</span></button></div>
  <div class="why"><span class="zh">火星有<b>两颗</b>小卫星：火卫一和火卫二——例 3 的资料库里就有。但是注意：例 3 也是「别人写的」！真正的侦探会再查一个<b>靠谱的来源</b>，比如天文书或 NASA 的网站。</span><span class="en">Mars has <b>two</b> small moons: Phobos and Deimos — they're in Example 3's database. But careful: Example 3 was also "written by someone else"! A real detective double-checks with a <b>trustworthy source</b>, like an astronomy book or NASA's website.</span></div>
</div>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">💻 代码题：AI 说「这段代码能数出每个词出现几次」。运行会怎样？</span><span class="en">💻 Code round: AI says "this code counts how often each word appears". What happens when you run it?</span></p>
<pre>words = ["kai", "moana", "kai"]
counts = {}
for w in words:
    counts[w] += 1
print(counts)</pre>
  <div class="opts"><button><span class="zh">打印 {'kai': 2, 'moana': 1}</span><span class="en">Prints {'kai': 2, 'moana': 1}</span></button><button><span class="zh">第一个词就报 KeyError</span><span class="en">KeyError on the very first word</span></button><button><span class="zh">打印 {}</span><span class="en">Prints {}</span></button></div>
  <div class="why"><span class="zh"><code>counts[w] += 1</code> 要先<b>拿出</b> counts["kai"]，但那个抽屉还不存在 → KeyError。AI 写的代码看起来很像对的，<b>一运行就露馅</b>。正确写法是例 4 的 <code>counts[w] = counts.get(w, 0) + 1</code>。</span><span class="en"><code>counts[w] += 1</code> first has to <b>read</b> counts["kai"], but that drawer doesn't exist yet → KeyError. AI's code looks right — <b>running it gives it away</b>. The correct line is Example 4's <code>counts[w] = counts.get(w, 0) + 1</code>.</span></div>
</div>

### ② <span class="zh">怎么核实？三个来源</span><span class="en">② How to check: three sources</span>

<div class="flow">
  <div class="f"><span class="e">▶️</span><b><span class="zh">运行代码</span><span class="en">Run the code</span></b><small><span class="zh">代码对不对，电脑最诚实</span><span class="en">the computer never lies about code</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">📚</span><b><span class="zh">问老师 / 查书</span><span class="en">Ask a teacher / a book</span></b><small><span class="zh">知识类的问题</span><span class="en">for facts</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🔄</span><b><span class="zh">换个问法再问一次</span><span class="en">Ask again differently</span></b><small><span class="zh">两次答案不一样 = 要小心</span><span class="en">different answers = be careful</span></small></div>
</div>

<div class="box box-tip"><span class="zh">💬 一句很好用的话：「<b>请检查你刚才的回答，哪里可能错了？</b>」AI 常常会自己找到错误。</span><span class="en">💬 A very useful line: "<b>Please check your last answer — what might be wrong?</b>" AI often finds its own mistakes.</span></div>

### ③ <span class="zh">隐私红线</span><span class="en">③ Privacy red lines</span>

<div class="quiz" data-answer="1">
  <p class="q"><span class="zh">这些东西里，哪一个<b>可以</b>告诉 AI？</span><span class="en">Which of these is <b>OK</b> to tell an AI?</span></p>
  <div class="opts"><button><span class="zh">我的昵称「小海龟」</span><span class="en">My nickname "Turtle"</span></button><button><span class="zh">我的真名全名 + 学校</span><span class="en">My full real name + school</span></button><button><span class="zh">妈妈的手机密码</span><span class="en">Mum's phone password</span></button><button><span class="zh">我和朋友的照片</span><span class="en">A photo of me and my friends</span></button></div>
  <div class="why"><span class="zh">昵称没关系。<b>真名全名、学校、地址、电话、密码、照片</b>——都不发给 AI（也不发给网站上的陌生人）。AI 记不住你是谁最好。</span><span class="en">A nickname is fine. <b>Full real name, school, address, phone, passwords, photos</b> — never to AI (or to strangers online). Best if AI can't tell who you are.</span></div>
</div>

### ④ <span class="zh">提好问题：坏问题 → 好问题</span><span class="en">④ Good questions: bad → good</span>

<div class="table-wrap">
<table>
  <tr><th><span class="zh">😕 坏问题</span><span class="en">😕 Bad</span></th><th><span class="zh">😃 好问题</span><span class="en">😃 Good</span></th></tr>
  <tr><td><span class="zh">帮我写个程序</span><span class="en">Write me a program</span></td><td><span class="zh">我是小学生，请写一个<b>毛利语翻译机</b>，用字典，<b>不超过 20 行</b>，每行加注释</span><span class="en">I'm a kid. Write a <b>te reo translator</b> using a dict, <b>under 20 lines</b>, with a comment on each line</span></td></tr>
  <tr><td><span class="zh">代码坏了</span><span class="en">It's broken</span></td><td><span class="zh">第 7 行报 KeyError（贴报错）。<b>给我一个提示</b>，不要直接改好</span><span class="en">Line 7 says KeyError (paste it). <b>Give me a hint</b>, don't fix it for me</span></td></tr>
  <tr><td><span class="zh">这对吗？</span><span class="en">Is this right?</span></td><td><span class="zh">请检查你刚才的回答，哪里<b>可能</b>错了？</span><span class="en">Check your last answer — what <b>might</b> be wrong?</span></td></tr>
</table>
</div>

<p><span class="zh">用配方做一段<b>文字程序</b>的指令（不是画画）：</span><span class="en">Use the recipe to build instructions for a <b>text program</b> (not a drawing):</span></p>

<div class="recipe" data-kind="text">
  <label for="r9-what">🎯 <span class="zh">做什么？</span><span class="en">Make what?</span></label>
  <input id="r9-what" name="what" data-ph-zh="比如：一个关于新西兰的 5 题问答机" data-ph-en="e.g. a 5-question quiz about New Zealand" placeholder="比如：一个关于新西兰的 5 题问答机">
  <div class="chips" data-for="what"><button class="chip"><span class="zh">一个关于新西兰的 5 题问答机</span><span class="en">a 5-question quiz about New Zealand</span></button><button class="chip"><span class="zh">一个宝可梦属性查询器</span><span class="en">a Pokémon type lookup</span></button><button class="chip"><span class="zh">一个太阳系行星资料库</span><span class="en">a Solar System planet database</span></button><button class="chip"><span class="zh">一个会学新词的翻译机</span><span class="en">a translator that learns new words</span></button></div>
  <label for="r9-detail">🔍 <span class="zh">细节</span><span class="en">Details</span></label>
  <input id="r9-detail" name="detail" data-ph-zh="比如：答对记 1 分，最后显示总分" data-ph-en="e.g. 1 point per correct answer, show the total at the end" placeholder="比如：答对记 1 分，最后显示总分">
  <label for="r9-colors">🧩 <span class="zh">要用到的知识</span><span class="en">Knowledge to use</span></label>
  <input id="r9-colors" name="colors" data-ph-zh="比如：字典、for 循环、input" data-ph-en="e.g. a dictionary, a for loop, input" placeholder="比如：字典、for 循环、input">
  <div class="chips" data-for="colors" data-multi><button class="chip"><span class="zh">字典</span><span class="en">dictionary</span></button><button class="chip"><span class="zh">for 循环</span><span class="en">for loop</span></button><button class="chip"><span class="zh">while 循环</span><span class="en">while loop</span></button><button class="chip"><span class="zh">函数</span><span class="en">functions</span></button></div>
  <input type="hidden" name="extra" value="">
  <div class="result"></div>
  <div class="score"></div>
  <p><button class="pg-btn run copy-prompt"><span class="zh">📋 复制这段指令</span><span class="en">📋 Copy these instructions</span></button></p>
</div>

### ⑤ <span class="zh">侦探行动：抓住 AI 的错</span><span class="en">⑤ Detective mission: catch the AI's mistake</span>
{: #mission}

<p class="zh">下面是一段<b>像 AI 写的</b>问答机（我们照着 AI 常犯的错准备的）。它看起来很棒，但 6 条答案里<b>不止一条是错的</b>。先运行它，然后用「三个来源」核实<b>每一条</b>，找出所有错误并改正。</p>
<p class="en">Below is a quiz <b>like one an AI might write</b> (we prepared it with typical AI mistakes). It looks great, but <b>more than one</b> of the 6 answers is wrong. Run it, then use the "three sources" to check <b>every one</b>, find all the mistakes and fix them.</p>

<div class="chat">
  <div class="bubble me"><span class="zh">请用 Python 字典写一个 6 题的问答机，关于新西兰和太空，问题是键，答案是值。</span><span class="en">Write a 6-question quiz about New Zealand and space in Python using a dict: question → answer.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">好的！这是一个关于新西兰和太空的问答机：<code>quiz = {"新西兰的首都是？": "奥克兰", …}</code></span><span class="en">Sure! Here's a New Zealand and space quiz: <code>quiz = {"新西兰的首都是？": "奥克兰", …}</code></span></div>
  <div class="bubble me"><span class="zh">🕵️ 等等……首都是奥克兰吗？我去查一下。</span><span class="en">🕵️ Wait… is the capital Auckland? Let me check.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/09/code/detective.py' | relative_url }}" data-title="🕵️ AI 写的问答机（有错！）" data-title-en="🕵️ The AI's quiz (has mistakes!)" data-canvas="no" data-save="ai-detective" data-draft="l9-detective" data-rows="14"></div>

<ul class="quests" data-key="l9-mission">
  <li><span class="zh">运行一遍，把 6 条答案<b>每一条</b>都核实（问老师 / 查书 / 换个问法问 AI）。在每个答案后面加注释 <code># ✅ 查过：……</code> 或 <code># ❌ 应该是……</code>，写上你用的来源。</span><span class="en">Run it and check <b>every one</b> of the 6 answers (teacher / book / ask AI differently). After each answer add a comment <code># ✅ checked: …</code> or <code># ❌ should be …</code> with the source you used.</span></li>
  <li><span class="zh">改正错误的答案，在代码最上面加一行注释：<code># 🕵️ 我发现 AI 错在：……</code></span><span class="en">Fix the wrong answer(s) and add a comment at the top: <code># 🕵️ The AI was wrong about: …</code></span></li>
  <li><span class="zh">真正的侦探行动：<b>你自己</b>用上面的配方问 AI 要一个问答机，贴进来运行、核实。抓到错了吗？</span><span class="en">The real mission: ask an AI <b>yourself</b> with the recipe above, paste it here, run and check. Did you catch a mistake?</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 核实小提示</span><span class="en">💡 Checking hint</span></summary><span class="zh">两道题的答案都是「奥克兰」，是不是很可疑？太空那两题，查天文书或 NASA 网站。《怀唐伊条约》那一题可以问老师或查书。一共有 <b>2 个</b>错。</span><span class="en">Two answers say "Auckland" — suspicious? For the two space questions, check an astronomy book or NASA's website. The Treaty of Waitangi one is worth asking a teacher or checking a book. There are <b>2</b> mistakes in total.</span></details>

---

## 🤖 <span class="zh">和 AI 一起</span><span class="en">Together with AI</span>

<p><span class="zh">这一课最重要的一句话，每次拿到 AI 的回答后都可以问：</span><span class="en">The most important line this lesson — ask it after every AI answer:</span></p>

<pre class="zh" style="white-space:pre-wrap">请检查你刚才的回答，哪里可能错了？
请列出你不太确定的地方，并告诉我怎么验证。</pre>
<pre class="en" style="white-space:pre-wrap">Please check your last answer: what might be wrong?
List the parts you're not sure about and tell me how I can verify them.</pre>
<button class="pg-btn copy-prev">📋 <span class="zh">复制</span><span class="en">Copy</span></button>

<div class="chat">
  <div class="bubble me"><span class="zh">这段代码里 <code>for k in quiz</code> 的 k 是什么？用小学生能懂的话解释。</span><span class="en">In this code, what is k in <code>for k in quiz</code>? Explain it simply.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">k 就是字典里的每一个<b>标签</b>（键）。循环每转一圈，k 就换成下一个标签，所以 <code>quiz[k]</code> 就是那一题的答案。</span><span class="en">k is each <b>label</b> (key) in the dict. Every loop k becomes the next label, so <code>quiz[k]</code> is that question's answer.</span></div>
</div>

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b><span class="zh">做字典</span><span class="en">Make a dict</span></b><code>maori = {"kai": "food", "moana": "sea"}</code><span><span class="zh">标签: 东西，用逗号隔开，外面是 { }</span><span class="en">label: thing, separated by commas, inside { }</span></span></div>
  <div class="k"><b><span class="zh">拿 / 放 / 改</span><span class="en">Get / put / update</span></b><code>maori["kai"]
maori["rā"] = "sun"</code><span><span class="zh">用标签拿；标签新 = 新抽屉，标签旧 = 换掉</span><span class="en">get by label; new label = new drawer, old label = replace</span></span></div>
  <div class="k"><b><span class="zh">安全地拿</span><span class="en">Safe get</span></b><code>maori.get("x", "不知道")</code><span><span class="zh">没有这个标签也不报错</span><span class="en">no error if the label is missing</span></span></div>
  <div class="k"><b><span class="zh">有没有？</span><span class="en">Is it there?</span></b><code>if "kai" in maori:</code><span><span class="zh">只看标签，不看东西</span><span class="en">checks labels only, not things</span></span></div>
  <div class="k"><b>.items()</b><code>for k, v in maori.items():
    print(k, v)</code><span><span class="zh">标签和东西一起拿</span><span class="en">label and thing together</span></span></div>
  <div class="k"><b><span class="zh">数数公式</span><span class="en">Counting line</span></b><code>counts = {}
for m in moves:
    counts[m] = counts.get(m, 0) + 1</code><span><span class="zh">没见过就从 0 开始，不会 KeyError</span><span class="en">starts from 0 if unseen, no KeyError</span></span></div>
  <div class="k"><b><span class="zh">抽屉里放列表</span><span class="en">Lists in drawers</span></b><code>moons = {"火星": ["火卫一", "火卫二"]}
len(moons["火星"])   # 2</code><span><span class="zh">值可以是任何东西</span><span class="en">a value can be anything</span></span></div>
  <div class="k"><b><span class="zh">AI 侦探三件套</span><span class="en">AI detective kit</span></b><code>▶ 运行  📚 问老师  🔄 换个问法</code><span><span class="zh">AI 说的话要检验；隐私不告诉 AI</span><span class="en">check what AI says; keep private things private</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l09">📖 小词典 · 第 9 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l09">📖 cheat sheet · Lesson 9</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/09/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
