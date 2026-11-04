---
title: 第 9 课 · 学一学
title_en: Lesson 9 · Learn
lesson: "09"
tab: learn
playground: true
---

# 📖 <span class="zh">第 9 课：字典 + AI 侦探</span><span class="en">Lesson 9: Dictionaries + AI detective</span>

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>

<p><span class="zh">第 7 课的<b>函数</b>和第 5 课的<b>列表</b>一起上场：一个画星星的函数，一个颜色列表。</span><span class="en"><b>Functions</b> (Lesson 7) and <b>lists</b> (Lesson 5) together: a star function and a colour list.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/warmup.py' | relative_url }}" data-title="🔁 热身：一排星星" data-title-en="🔁 Warm-up: a row of stars" data-save="star-row" data-rows="8"></div>

<ul class="quests" data-key="l9-warm">
  <li><span class="zh">在列表里再加两个颜色，运行。多了几颗星？为什么？</span><span class="en">Add two more colours to the list and run. How many extra stars? Why?</span></li>
  <li><span class="zh">把 <code>star(x, 0, 60, c)</code> 的 60 改成 <code>x + 200</code>，猜猜会怎样。</span><span class="en">Change the 60 in <code>star(x, 0, 60, c)</code> to <code>x + 200</code>. Guess first!</span></li>
</ul>

---

## ✨ <span class="zh">今天的新魔法：字典</span><span class="en">Today's new magic: dictionaries</span>
{: #dict}

<p class="zh">列表是一排<b>编号</b>的格子（0、1、2……）。<b>字典</b>是一排<b>贴了标签</b>的抽屉：标签叫<b>键</b>（key），抽屉里的东西叫<b>值</b>（value）。你不用记「第几个」，直接说标签就能拿到东西——就像真正的词典，查「kai」就得到「food」。</p>
<p class="en">A list is a row of <b>numbered</b> boxes (0, 1, 2…). A <b>dictionary</b> is a row of <b>labelled</b> drawers: the label is the <b>key</b>, the thing inside is the <b>value</b>. You don't remember "which number" — you say the label and get the thing. Just like a real dictionary: look up "kai", get "food".</p>

<div class="cmds">
  <div class="cmd"><code>d = {"kai": "food"}</code><span><span class="zh">做一个字典：标签: 东西</span><span class="en">Make a dict: label: thing</span></span></div>
  <div class="cmd"><code>d["kai"]</code><span><span class="zh">用标签拿东西</span><span class="en">Get the thing by its label</span></span></div>
  <div class="cmd"><code>d["ra"] = "sun"</code><span><span class="zh">放进一个新抽屉（或换掉旧的）</span><span class="en">Add a new drawer (or replace the old one)</span></span></div>
  <div class="cmd"><code>"kai" in d</code><span><span class="zh">有这个标签吗？True / False</span><span class="en">Is this label there? True / False</span></span></div>
  <div class="cmd"><code>d.get("x", "没有")</code><span><span class="zh">安全地拿：没有就给默认值</span><span class="en">Safe get: a default if missing</span></span></div>
  <div class="cmd"><code>for k in d:</code><span><span class="zh">一个标签一个标签地看</span><span class="en">Go through every label</span></span></div>
</div>

### 🤔 <span class="zh">先猜，再运行</span><span class="en">Guess first, then run</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的代码里，<code>print(maori["kai"])</code> 会显示什么？</span><span class="en">In the code below, what does <code>print(maori["kai"])</code> show?</span></p>
  <div class="opts"><button>kai</button><button>food</button><button>2</button></div>
  <div class="why"><span class="zh">"kai" 是标签，抽屉里装的是 "food"。字典总是「标签 → 东西」。</span><span class="en">"kai" is the label; the drawer holds "food". A dict is always "label → thing".</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/09/code/dict1.py' | relative_url }}" data-title="📖 例 1：我的第一个字典" data-title-en="📖 Example 1: my first dictionary" data-canvas="no" data-save="my-dict" data-rows="8"></div>

### 🔍 <span class="zh">改一改</span><span class="en">Change it</span>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">如果把 <code># print(maori["sun"])</code> 前面的 <code>#</code> 去掉，会怎样？</span><span class="en">If you remove the <code>#</code> before <code># print(maori["sun"])</code>, what happens?</span></p>
  <div class="opts"><button><span class="zh">显示 sun</span><span class="en">Shows sun</span></button><button><span class="zh">显示空白</span><span class="en">Shows nothing</span></button><button><span class="zh">报错 KeyError</span><span class="en">KeyError</span></button></div>
  <div class="why"><span class="zh">没有「sun」这个标签，电脑会说 <b>KeyError</b>（找不到钥匙）。安全的拿法是 <code>.get("sun", "不知道")</code>。</span><span class="en">There's no "sun" label, so the computer says <b>KeyError</b> (key not found). The safe way is <code>.get("sun", "don't know")</code>.</span></div>
</div>

<ul class="quests" data-key="l9-ex1">
  <li><span class="zh">去掉 <code>#</code>，运行，读一读红框里的话，再把 <code>#</code> 加回去。</span><span class="en">Remove the <code>#</code>, run it, read the red box, then put the <code>#</code> back.</span></li>
  <li><span class="zh">加一个新词：<code>maori["rā"] = "sun"</code>，再 <code>print(maori["rā"])</code>。</span><span class="en">Add a word: <code>maori["rā"] = "sun"</code>, then <code>print(maori["rā"])</code>.</span></li>
  <li><span class="zh">加一行 <code>print("kai" in maori)</code> 和 <code>print("pizza" in maori)</code>，看看 True / False。</span><span class="en">Add <code>print("kai" in maori)</code> and <code>print("pizza" in maori)</code> and look at the True / False.</span></li>
</ul>

### 🧪 <span class="zh">例 2：翻译机 app（会学新词！）</span><span class="en">Example 2: translator app (it learns new words!)</span>

<p><span class="zh">第 6 课的 <code>while True</code> + 第 2 课的 <code>input()</code> + 今天的字典 = 一个真正的 app。不认识的词，它会问你，然后<b>记住</b>。</span><span class="en"><code>while True</code> (Lesson 6) + <code>input()</code> (Lesson 2) + today's dict = a real app. Words it doesn't know, it asks you about, then <b>remembers</b>.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/translator.py' | relative_url }}" data-title="🗣️ 例 2：翻译机" data-title-en="🗣️ Example 2: translator" data-canvas="no" data-save="translator" data-draft="l9-translator" data-rows="12"></div>

<ul class="quests" data-key="l9-ex2">
  <li><span class="zh">输入 <code>kai</code>，再输入一个它不认识的词，教它，然后再输一次同一个词——它记住了吗？</span><span class="en">Type <code>kai</code>, then a word it doesn't know, teach it, then type that word again — did it remember?</span></li>
  <li><span class="zh">把结束的暗号 <code>再见</code> 改成你自己的暗号。</span><span class="en">Change the stop word <code>再见</code> to your own secret word.</span></li>
  <li>🐞 <span class="zh">把 <code>if word in maori:</code> 改成 <code>if word in "maori":</code>，猜猜会怎样？（引号让它变成了一段文字！）</span><span class="en">Change <code>if word in maori:</code> to <code>if word in "maori":</code>. What happens? (The quotes make it a piece of text!)</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 为什么最后要 <code>for k in maori</code>？</span><span class="en">💡 Why <code>for k in maori</code> at the end?</span></summary><span class="zh">循环字典时，每次拿到的是一个<b>标签</b> k；用 <code>maori[k]</code> 才能拿到抽屉里的东西。</span><span class="en">Looping a dict gives you one <b>label</b> k at a time; <code>maori[k]</code> gets the thing inside.</span></details>

### 🧪 <span class="zh">例 3：知识问答机</span><span class="en">Example 3: quiz machine</span>

<p><span class="zh">问题当标签，答案当东西。<code>for question in quiz:</code> 就能轮流问每一题——第 8 课的记分也回来了。</span><span class="en">Questions are labels, answers are the things. <code>for question in quiz:</code> asks every question in turn — and the score from Lesson 8 is back.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/quiz.py' | relative_url }}" data-title="🧠 例 3：问答机" data-title-en="🧠 Example 3: quiz machine" data-canvas="no" data-save="quiz-machine" data-draft="l9-quiz" data-rows="12"></div>

<ul class="quests" data-key="l9-ex3">
  <li><span class="zh">加两道<b>你自己的</b>题（关于你喜欢的游戏、动物都行）。</span><span class="en">Add two questions of <b>your own</b> (about your favourite game or animal).</span></li>
  <li><span class="zh">答错时显示「❌ 不对，是 XX」——把它改成更友好的话。</span><span class="en">When wrong it says "❌ 不对，是 XX" (Wrong, it's XX) — make it friendlier.</span></li>
  <li><span class="zh">最后加一个 <code>if score == len(quiz):</code> 显示「🏆 全对！」。</span><span class="en">Add <code>if score == len(quiz):</code> at the end to show "🏆 All correct!".</span></li>
</ul>

### 🧪 <span class="zh">例 4：按名字画图形（填空）</span><span class="en">Example 4: shapes by name (fill in)</span>

<p><span class="zh">字典不只装文字，也能装数字。<code>shapes["六边形"]</code> 是 6，再用第 3 课的 <code>360 / 边数</code> 就能画出来。</span><span class="en">Dicts can hold numbers too. <code>shapes["六边形"]</code> is 6, and <code>360 / sides</code> from Lesson 3 draws it.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/shapes.py' | relative_url }}" data-title="🔷 例 4：按名字画图形" data-title-en="🔷 Example 4: shapes by name" data-save="shapes-by-name" data-draft="l9-shapes" data-rows="12"></div>

<details class="hint"><summary><span class="zh">💡 提示</span><span class="en">💡 Hint</span></summary><span class="zh">八边形 = 八条边。填 8 之后，再试试加一个 <code>"十边形": 10</code> 并画出来。</span><span class="en">An octagon has eight sides. After filling in 8, add <code>"十边形": 10</code> and draw it too.</span></details>

### 🧪 <span class="zh">例 5：记分板字典</span><span class="en">Example 5: scoreboard dictionary</span>

<p><span class="zh">第 8 课的石头剪刀布，这次用<b>两个字典</b>：一个说「谁赢谁」，一个记分。看看代码短了多少！</span><span class="en">Rock Paper Scissors from Lesson 8, now with <b>two dicts</b>: one says what beats what, one keeps score. Look how much shorter it is!</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/score.py' | relative_url }}" data-title="🏆 例 5：记分板" data-title-en="🏆 Example 5: scoreboard" data-canvas="no" data-save="rps-dict" data-draft="l9-score" data-rows="12"></div>

<ul class="quests" data-key="l9-ex5">
  <li><span class="zh">找到 <code>beats</code> 字典。为什么 <code>beats.get(me) == computer</code> 就是「我赢了」？</span><span class="en">Find the <code>beats</code> dict. Why does <code>beats.get(me) == computer</code> mean "I win"?</span></li>
  <li><span class="zh">把 3 局改成 5 局，再给平局也记分：<code>score["平局"]</code>。</span><span class="en">Make it 5 rounds and count draws too: <code>score["平局"]</code>.</span></li>
</ul>

### 🏆 <span class="zh">挑战：我的小词典</span><span class="en">Challenge: my own dictionary</span>

<p><span class="zh">做一个<b>你自己的</b>字典 app：宝可梦 → 属性？游戏角色 → 技能？朋友昵称 → 最爱的食物？要能查、能加、最后能全部打印。满意了就 📤 存到作品墙。</span><span class="en">Build <b>your own</b> dictionary app: Pokémon → type? game character → skill? friend's nickname → favourite food? It should look up, add, and print everything at the end. Happy with it? 📤 Save to Gallery.</span></p>

<div class="playground" data-title="🏆 挑战：我的小词典" data-title-en="🏆 Challenge: my dictionary" data-canvas="no" data-save="my-dict-app" data-draft="l9-challenge" data-rows="12"><textarea># 🏆 我的小词典 My dictionary app
my_dict = {
    "皮卡丘": "电",
}

# 1. 查一个 / look one up

# 2. 加一个 / add one

# 3. 全部打印 / print them all
</textarea></div>

---

## 🕵️ <span class="zh">AI 侦探训练</span><span class="en">AI detective training</span>
{: #detective}

<p class="zh">AI 非常厉害，但它有个毛病：<b>不知道的时候，也会一本正经地编一个答案</b>，听起来特别像真的。程序员叫这个「幻觉」。聪明的 AI 用户不是不用 AI，而是<b>会检验</b>。</p>
<p class="en">AI is amazing, but it has a flaw: <b>when it doesn't know, it may confidently make something up</b> that sounds totally real. Programmers call this a "hallucination". A smart AI user doesn't avoid AI — they <b>check</b>.</p>

### ① <span class="zh">AI 会一本正经地编造</span><span class="en">① AI makes things up with a straight face</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面三句都是 AI 说的。哪一句是<b>错</b>的？</span><span class="en">All three were said by an AI. Which one is <b>wrong</b>?</span></p>
  <div class="opts"><button><span class="zh">新西兰的国鸟是几维鸟（kiwi）</span><span class="en">New Zealand's national bird is the kiwi</span></button><button><span class="zh">新西兰的首都是奥克兰</span><span class="en">New Zealand's capital is Auckland</span></button><button><span class="zh">Python 里 <code>len("kiwi")</code> 是 4</span><span class="en">In Python, <code>len("kiwi")</code> is 4</span></button></div>
  <div class="why"><span class="zh">首都是<b>惠灵顿</b>（Wellington）！奥克兰是最大的城市，所以很多人（和 AI）会搞混。听起来越「理所当然」的话，越要查一下。</span><span class="en">The capital is <b>Wellington</b>! Auckland is the biggest city, so people (and AI) mix them up. The more "obvious" something sounds, the more worth checking.</span></div>
</div>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">再来：哪一句是错的？</span><span class="en">Again: which one is wrong?</span></p>
  <div class="opts"><button><span class="zh">Python 的列表从 0 开始数</span><span class="en">Python lists start counting at 0</span></button><button><span class="zh">字典用 <code>{}</code>，列表用 <code>[]</code></span><span class="en">Dicts use <code>{}</code>, lists use <code>[]</code></span></button><button><span class="zh"><code>d.get("x")</code> 找不到会报错 KeyError</span><span class="en"><code>d.get("x")</code> gives a KeyError if missing</span></button></div>
  <div class="why"><span class="zh"><code>.get</code> 找不到<b>不会报错</b>，会给 None 或你写的默认值；会报错的是 <code>d["x"]</code>。你刚才在例 1 里亲手验证过——<b>运行代码</b>就是最好的核实方法。</span><span class="en"><code>.get</code> <b>doesn't error</b> when missing — it gives None or your default; <code>d["x"]</code> is the one that errors. You verified this in Example 1 — <b>running the code</b> is the best check.</span></div>
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
  <div class="chips" data-for="what"><button class="chip"><span class="zh">一个关于新西兰的 5 题问答机</span><span class="en">a 5-question quiz about New Zealand</span></button><button class="chip"><span class="zh">一个宝可梦属性查询器</span><span class="en">a Pokémon type lookup</span></button><button class="chip"><span class="zh">一个会学新词的翻译机</span><span class="en">a translator that learns new words</span></button></div>
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

<p class="zh">下面是一段 <b>AI 写的</b>问答机（我们真的问过 AI）。它看起来很棒，但里面<b>至少有一个答案是错的</b>。先运行它，然后用「三个来源」核实每一条答案，找出错误并改正。</p>
<p class="en">Below is a quiz <b>written by an AI</b> (we really asked one). It looks great, but <b>at least one answer is wrong</b>. Run it, then use the "three sources" to check every answer, find the mistake and fix it.</p>

<div class="chat">
  <div class="bubble me"><span class="zh">请用 Python 字典写一个 5 题的新西兰知识问答机，问题是键，答案是值。</span><span class="en">Write a 5-question New Zealand quiz in Python using a dict: question → answer.</span></div>
  <div class="bubble ai"><b>AI:</b> <span class="zh">好的！这是一个关于新西兰的问答机：<code>quiz = {"新西兰的首都是？": "奥克兰", …}</code></span><span class="en">Sure! Here's a New Zealand quiz: <code>quiz = {"新西兰的首都是？": "奥克兰", …}</code></span></div>
  <div class="bubble me"><span class="zh">🕵️ 等等……首都是奥克兰吗？我去查一下。</span><span class="en">🕵️ Wait… is the capital Auckland? Let me check.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/09/code/detective.py' | relative_url }}" data-title="🕵️ AI 写的问答机（有错！）" data-title-en="🕵️ The AI's quiz (has mistakes!)" data-canvas="no" data-save="ai-detective" data-draft="l9-detective" data-rows="14"></div>

<ul class="quests" data-key="l9-mission">
  <li><span class="zh">运行一遍，把 5 条答案<b>每一条</b>都核实（问老师 / 查书 / 换个问法问 AI）。</span><span class="en">Run it and check <b>every one</b> of the 5 answers (teacher / book / ask AI differently).</span></li>
  <li><span class="zh">改正错误的答案，在代码最上面加一行注释：<code># 🕵️ 我发现 AI 错在：……</code></span><span class="en">Fix the wrong answer(s) and add a comment at the top: <code># 🕵️ The AI was wrong about: …</code></span></li>
  <li><span class="zh">真正的侦探行动：<b>你自己</b>用上面的配方问 AI 要一个问答机，贴进来运行、核实。抓到错了吗？</span><span class="en">The real mission: ask an AI <b>yourself</b> with the recipe above, paste it here, run and check. Did you catch a mistake?</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 核实小提示</span><span class="en">💡 Checking hint</span></summary><span class="zh">一道题有两个「奥克兰」，是不是很可疑？《怀唐伊条约》那一题可以问老师或查书。</span><span class="en">Two answers say "Auckland" — suspicious? The Treaty of Waitangi one is worth asking a teacher or checking a book.</span></details>

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
  <div class="k"><b><span class="zh">拿 / 放</span><span class="en">Get / put</span></b><code>maori["kai"]
maori["rā"] = "sun"</code><span><span class="zh">用标签拿；等号放进新抽屉</span><span class="en">get by label; = puts in a new drawer</span></span></div>
  <div class="k"><b><span class="zh">安全地拿</span><span class="en">Safe get</span></b><code>maori.get("x", "不知道")</code><span><span class="zh">没有这个标签也不报错</span><span class="en">no error if the label is missing</span></span></div>
  <div class="k"><b><span class="zh">有没有？</span><span class="en">Is it there?</span></b><code>if "kai" in maori:</code><span><span class="zh">True / False</span><span class="en">True / False</span></span></div>
  <div class="k"><b><span class="zh">全部看一遍</span><span class="en">Go through all</span></b><code>for k in maori:
    print(k, maori[k])</code><span><span class="zh">k 是标签，maori[k] 是东西</span><span class="en">k is the label, maori[k] the thing</span></span></div>
  <div class="k"><b><span class="zh">AI 侦探三件套</span><span class="en">AI detective kit</span></b><code>▶ 运行  📚 问老师  🔄 换个问法</code><span><span class="zh">AI 说的话要检验；隐私不告诉 AI</span><span class="en">check what AI says; keep private things private</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l09">📖 小词典 · 第 9 课</a>。</span><span class="en">All commands are in the <a href="{{ '/cheatsheet/' | relative_url }}#l09">📖 cheat sheet · Lesson 9</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/09/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
