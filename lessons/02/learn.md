---
title: 第 2 课 · 学一学
title_en: Lesson 2 · Learn
lesson: "02"
tab: learn
playground: true
---

# 📖 <span class="zh">第 2 课：让程序记住东西、听你说话</span><span class="en">Lesson 2: programs that remember and listen</span>

<p class="zh">上周电脑只会<b>照着做</b>。今天它要学会两件事：<b>记住东西</b>（变量）和<b>听你说话</b>（input）。学完你就能做一个会聊天的机器人！</p>
<p class="en">Last week the computer only <b>followed orders</b>. Today it learns two things: <b>remembering</b> (variables) and <b>listening</b> (input). By the end you'll have a chatbot!</p>

---

## 🔁 <span class="zh">热身：上次学的还记得吗？</span><span class="en">Warm-up: remember last time?</span>
{: #warmup}

<p><span class="zh">不看小词典，试试这两个小任务。忘了？那就去 <a href="{{ '/cheatsheet/' | relative_url }}">📖 小词典</a> 查——查词典也是本事！</span><span class="en">Try these two without the cheat sheet. Forgot? Then look in the <a href="{{ '/cheatsheet/' | relative_url }}">📖 cheat sheet</a> — looking things up is a skill too!</span></p>

<div class="playground" data-src="{{ '/lessons/01/code/square.py' | relative_url }}" data-title="🔁 热身：正方形" data-title-en="🔁 Warm-up: square" data-save="warmup-2" data-rows="8"></div>

<ul class="quests" data-key="l2-warmup">
  <li><span class="zh">把正方形变成<b>红色</b>，笔变粗。</span><span class="en">Make the square <b>red</b> with a thicker pen.</span></li>
  <li><span class="zh">把它变成<b>三角形</b>（提示：改角度，删一组指令）。</span><span class="en">Turn it into a <b>triangle</b> (hint: change the angle, delete one pair of lines).</span></li>
</ul>

<div class="box box-think"><span class="zh">🤔 发现了吗？想把正方形变大，要改 <b>4 个</b> 100。如果有 100 条边呢……？今天的魔法就是解决这个的。</span><span class="en">🤔 Notice: to make the square bigger you change <b>four</b> 100s. What if it had 100 sides…? Today's magic fixes that.</span></div>

---

## ✨ <span class="zh">新魔法 1：变量 = 带名字的盒子</span><span class="en">New magic 1: a variable is a box with a name</span>
{: #variables}

<p class="zh">想象一个盒子，上面贴着名字标签。<code>name = "小海龟"</code> 就是：把「小海龟」放进叫 <b>name</b> 的盒子里。以后写 <code>name</code>，电脑就去盒子里拿。</p>
<p class="en">Imagine a box with a name label on it. <code>name = "小海龟"</code> means: put "小海龟" into the box called <b>name</b>. Whenever you write <code>name</code> later, the computer looks in the box.</p>

<div class="cmds">
  <div class="cmd"><code>name = "Kiwi"</code><span><span class="zh">做一个叫 name 的盒子，放进文字（要加引号）</span><span class="en">Make a box called name and put text in it (needs quotes)</span></span></div>
  <div class="cmd"><code>size = 100</code><span><span class="zh">盒子里放数字（不用引号）</span><span class="en">Put a number in a box (no quotes)</span></span></div>
  <div class="cmd"><code>print(f"你好 {name}")</code><span><span class="zh">f 开头的句子里，{盒子} 会换成盒子里的东西</span><span class="en">In a sentence starting with f, {box} becomes what's inside</span></span></div>
</div>

### 🤔 <span class="zh">① 先猜 → ② 运行</span><span class="en">① Predict → ② Run</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的程序，第一行会打印什么？</span><span class="en">What will the first line print?</span></p>
  <div class="opts"><button><span class="zh">你好，我是 {name}！</span><span class="en">你好，我是 {name}！</span></button><button><span class="zh">你好，我是 小海龟！</span><span class="en">你好，我是 小海龟！</span></button><button><span class="zh">你好，我是 name！</span><span class="en">你好，我是 name！</span></button></div>
  <div class="why"><span class="zh">因为句子前面有 <b>f</b>，大括号里的 <code>name</code> 会被换成盒子里的「小海龟」。没有 f 的话，就会原样打印 {name}！</span><span class="en">Because the sentence starts with <b>f</b>, <code>name</code> in the braces is swapped for what's in the box: 小海龟. Without the f it would print {name} as-is!</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/02/code/hello-var.py' | relative_url }}" data-canvas="no" data-title="📦 例 1：盒子里有什么" data-title-en="📦 Example 1: what's in the box" data-save="hello-var" data-rows="8"></div>

### 🔍 <span class="zh">③ 改一改</span><span class="en">③ Change it</span>

<ul class="quests" data-key="l2-var-modify">
  <li><span class="zh">把 <code>"小海龟"</code> 换成你的昵称，把 <code>"猫"</code> 换成你喜欢的动物。看，三句话一起变了！</span><span class="en">Change <code>"小海龟"</code> to your nickname and <code>"猫"</code> to your favourite animal. All three lines change together!</span></li>
  <li><span class="zh">把某一行的 <code>f</code> 删掉，运行。打印出什么？（这就是 f 的作用）</span><span class="en">Delete the <code>f</code> on one line and run. What prints? (That's what the f does)</span></li>
  <li>🐞 <span class="zh">把 <code>{name}</code> 改成 <code>{nmae}</code>，读一读报错：电脑说它不认识谁？</span><span class="en">Change <code>{name}</code> to <code>{nmae}</code> and read the error: what name doesn't the computer know?</span></li>
</ul>

### 🧪 <span class="zh">例 2：改 1 个数字，整个正方形一起变</span><span class="en">Example 2: change 1 number, the whole square changes</span>

<p><span class="zh">这就是变量最厉害的地方。<code>size</code> 这个盒子用了 4 次，但只要改<b>一次</b>。</span><span class="en">This is the superpower of variables. The box <code>size</code> is used 4 times, but you only change it <b>once</b>.</span></p>

<div class="playground" data-src="{{ '/lessons/02/code/square-var.py' | relative_url }}" data-title="📏 例 2：用变量画正方形" data-title-en="📏 Example 2: square with a variable" data-save="square-var"></div>

<ul class="quests" data-key="l2-square">
  <li><span class="zh">把 <code>size = 100</code> 改成 <code>size = 200</code>，再改成 <code>30</code>。只改了一个地方！</span><span class="en">Change <code>size = 100</code> to <code>200</code>, then to <code>30</code>. Only one edit!</span></li>
  <li><span class="zh">再做一个盒子 <code>colour = "gold"</code>，然后把 <code>t.color("deepskyblue")</code> 改成 <code>t.color(colour)</code>。</span><span class="en">Make another box <code>colour = "gold"</code>, then change <code>t.color("deepskyblue")</code> to <code>t.color(colour)</code>.</span></li>
</ul>

<div class="box box-tip"><span class="zh">⚠️ <code>size = 100</code> 要写在<b>用它之前</b>（上面）。先用后做盒子，电脑会说 <code>NameError</code>：不认识这个名字。</span><span class="en">⚠️ <code>size = 100</code> must come <b>before</b> you use it (above). Use it first and the computer says <code>NameError</code>: unknown name.</span></div>

### 🧪 <span class="zh">例 3：两个盒子，填一填</span><span class="en">Example 3: two boxes, fill in the blank</span>

<div class="playground" data-src="{{ '/lessons/02/code/shape-var.py' | relative_url }}" data-title="🔺 例 3：side 和 turn" data-title-en="🔺 Example 3: side and turn" data-save="shape-var" data-draft="l2-shape"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">想画正方形，每次转 90。想画三角形呢？上周的提示：360 ÷ 边数。</span><span class="en">For a square, turn 90 each time. For a triangle? Last week's hint: 360 ÷ number of sides.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2</span><span class="en">💡 Hint 2</span></summary><span class="zh">填 <code>turn = 120</code>，程序画 4 条边，第 4 条会和第 1 条重叠——没关系，还是三角形！试试 <code>turn = 144</code> 会怎样？</span><span class="en">Put <code>turn = 120</code>. The program draws 4 sides and the 4th overlaps the 1st — that's fine, it's still a triangle! What does <code>turn = 144</code> do?</span></details>

---

## ✨ <span class="zh">新魔法 2：input() 让程序听你说话</span><span class="en">New magic 2: input() makes the program listen</span>
{: #input}

<p class="zh"><code>input("你叫什么？ ")</code> 会先显示问题，然后<b>停下来等你打字</b>。你打的字就会放进盒子里。这就是聊天机器人的秘密！</p>
<p class="en"><code>input("你叫什么？ ")</code> shows the question, then <b>stops and waits for you to type</b>. Whatever you type goes into the box. That's the secret of chatbots!</p>

<div class="cmds">
  <div class="cmd"><code>name = input("你叫什么？ ")</code><span><span class="zh">问一个问题，答案放进 name 盒子</span><span class="en">Ask a question, the answer goes in the name box</span></span></div>
  <div class="cmd"><code>age = int(input("几岁？ "))</code><span><span class="zh">input 给的是文字，int() 把它变成数字</span><span class="en">input gives text; int() turns it into a number</span></span></div>
</div>

### 🤔 <span class="zh">① 先猜 → ② 运行</span><span class="en">① Predict → ② Run</span>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">运行下面的程序，如果你回答「小海龟」和「猫」，最后一行会打印什么？</span><span class="en">If you answer 小海龟 and 猫, what does the last line print?</span></p>
  <div class="opts"><button>再见，name！下次再聊～</button><button>再见，猫！下次再聊～</button><button>再见，小海龟！下次再聊～</button></div>
  <div class="why"><span class="zh">你打的「小海龟」被放进了 <code>name</code> 盒子，最后一行从盒子里拿出来用。</span><span class="en">What you typed (小海龟) went into the <code>name</code> box, and the last line takes it back out.</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/02/code/chatbot.py' | relative_url }}" data-canvas="no" data-title="💬 例 4：聊天机器人" data-title-en="💬 Example 4: chatbot" data-save="chatbot" data-draft="l2-chatbot"></div>

<p class="muted"><span class="zh">运行后，输入框会出现在黑色区域下面——在那里打字，按回车。</span><span class="en">After you click Run, a text box appears under the black area — type there and press Enter.</span></p>

### 🔍 <span class="zh">③ 改一改</span><span class="en">③ Change it</span>

<ul class="quests" data-key="l2-chat-modify">
  <li><span class="zh">加<b>第 3 个问题</b>：「你最喜欢什么游戏？」，并用 <code>f"…"</code> 回应。</span><span class="en">Add a <b>3rd question</b>: "What's your favourite game?" and reply with <code>f"…"</code>.</span></li>
  <li><span class="zh">让机器人在最后一句里<b>同时</b>用上名字和动物。</span><span class="en">Make the last line use <b>both</b> the name and the animal.</span></li>
  <li><span class="zh">把机器人的名字改成你自己取的。</span><span class="en">Give the chatbot a name you invented.</span></li>
</ul>

### 🧪 <span class="zh">例 5：int() 让程序会算数</span><span class="en">Example 5: int() lets the program do maths</span>

<p><span class="zh">先猜：如果你输入 12，会打印什么？</span><span class="en">Guess first: if you type 12, what prints?</span></p>

<div class="playground" data-src="{{ '/lessons/02/code/age.py' | relative_url }}" data-canvas="no" data-title="🔢 例 5：你几岁" data-title-en="🔢 Example 5: how old are you" data-save="age" data-rows="7"></div>

<ul class="quests" data-key="l2-age">
  <li><span class="zh">加一行：算出你活了大约多少个月（<code>age * 12</code>）。</span><span class="en">Add a line: roughly how many months you've lived (<code>age * 12</code>).</span></li>
  <li><span class="zh">把 <code>int(</code> 和它的 <code>)</code> 删掉再运行，输入 12。报错了？读一读红色的解释。</span><span class="en">Delete <code>int(</code> and its <code>)</code>, run, type 12. Error? Read the red explanation.</span></li>
</ul>

### 🐞 <span class="zh">故意的错误：文字 + 数字</span><span class="en">A bug on purpose: text + number</span>

<p><span class="zh">这个程序一定会出错。<b>先猜它会说什么</b>，再运行，然后修好它（提示：int）。</span><span class="en">This program is guaranteed to fail. <b>Guess what it will say</b>, run it, then fix it (hint: int).</span></p>

<div class="playground" data-src="{{ '/lessons/02/code/bug-text-plus.py' | relative_url }}" data-canvas="no" data-title="🐞 文字 + 数字" data-title-en="🐞 Text + number" data-save="bug-fix" data-rows="5"></div>

<div class="box box-good"><span class="zh">💡 <code>"5"</code>（有引号）是<b>文字</b>，<code>5</code>（没引号）是<b>数字</b>。文字不能和数字相加。input() 给你的永远是文字，所以算数前要 <code>int()</code>。</span><span class="en">💡 <code>"5"</code> (with quotes) is <b>text</b>; <code>5</code> (no quotes) is a <b>number</b>. You can't add text and numbers. input() always gives text, so use <code>int()</code> before doing maths.</span></div>

---

## 🧪 <span class="zh">例 6（综合）：名字画家</span><span class="en">Example 6 (all together): Name Painter</span>
{: #name-art}

<p><span class="zh">把两个魔法合起来，再加上上周的海龟：程序问你名字和颜色，海龟用那个颜色画一个相框，把你的名字写在中间。</span><span class="en">Both magics together, plus last week's turtle: the program asks your name and colour, then the turtle draws a frame in that colour and writes your name inside.</span></p>

<div class="playground" data-src="{{ '/lessons/02/code/name-art.py' | relative_url }}" data-title="🎨 例 6：名字画家" data-title-en="🎨 Example 6: Name Painter" data-save="name-art" data-draft="l2-name-art"></div>

<ul class="quests" data-key="l2-name-art">
  <li><span class="zh">把 <code>size = 300</code> 改小、改大。相框跟着变了吗？</span><span class="en">Make <code>size = 300</code> smaller and bigger. Does the frame follow?</span></li>
  <li><span class="zh">在 <code>font=("Arial", 32, "bold")</code> 里把 32 改成 60。</span><span class="en">In <code>font=("Arial", 32, "bold")</code> change 32 to 60.</span></li>
  <li><span class="zh">再问一个问题 <code>word = input("说一句口号？ ")</code>，用 <code>t.write</code> 写在名字下面（提示：先 <code>t.goto(0, -70)</code>）。</span><span class="en">Ask one more question <code>word = input("A motto? ")</code> and <code>t.write</code> it under the name (hint: <code>t.goto(0, -70)</code> first).</span></li>
</ul>

<div class="swatches" data-colors="red orange gold limegreen deepskyblue blue purple hotpink brown black"></div>

---

## 🏆 <span class="zh">④ 自己写：三个问题的聊天机器人</span><span class="en">④ Make your own: a 3-question chatbot</span>

<p><span class="zh">设计一个<b>关于你的爱好</b>的聊天机器人：问 3 个问题，每个都用 <code>f"…"</code> 回应，最后一句话总结。满意了就 📤 存到作品墙！</span><span class="en">Design a chatbot <b>about your hobby</b>: ask 3 questions, reply to each with <code>f"…"</code>, and finish with a summary line. Happy with it? 📤 Save to Gallery!</span></p>

<div class="playground" data-src="{{ '/lessons/02/code/challenge.py' | relative_url }}" data-canvas="no" data-title="🏆 挑战：爱好聊天机器人" data-title-en="🏆 Challenge: hobby chatbot" data-save="hobby-bot" data-draft="l2-challenge"></div>

<details class="hint"><summary><span class="zh">💡 提示 1</span><span class="en">💡 Hint 1</span></summary><span class="zh">一个问题 = 两行：一行 <code>盒子 = input("问题？ ")</code>，一行 <code>print(f"回应 {盒子}")</code>。复制粘贴再改字就行。</span><span class="en">One question = two lines: <code>box = input("Question? ")</code> and <code>print(f"Reply {box}")</code>. Copy, paste, change the words.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2</span><span class="en">💡 Hint 2</span></summary><span class="zh">总结那句可以同时放两三个盒子：<code>print(f"你喜欢{hobby}，{when}做，和{who}一起。")</code></span><span class="en">The summary can use two or three boxes at once: <code>print(f"You like {hobby}, do it {when}, with {who}.")</code></span></details>

---

## 🤖 <span class="zh">和 AI 一起</span><span class="en">With AI</span>

<p><span class="zh">看不懂的代码，可以<b>指着具体的一行</b>问 AI。比一比下面两种问法：</span><span class="en">When you don't understand code, ask AI <b>about one specific line</b>. Compare these two ways of asking:</span></p>

<div class="chat">
  <div class="bubble me">😕 <span class="zh">这段代码是什么意思？</span><span class="en">What does this code mean?</span></div>
  <div class="bubble ai"><span class="zh">（AI 解释了 10 行，你还是不知道 f 是干嘛的……）</span><span class="en">(AI explains 10 lines and you still don't know what f does…)</span></div>
  <div class="bubble me">😃 <span class="zh">第 7 行 <code>print(f"你好，{name}")</code> 里的 <b>f</b> 和 <b>{ }</b> 是什么意思？用小学生能听懂的话解释，再举一个小例子。</span><span class="en">On line 7 <code>print(f"你好，{name}")</code>, what do the <b>f</b> and the <b>{ }</b> mean? Explain simply and give a small example.</span></div>
  <div class="bubble ai"><span class="zh">f 告诉 Python「这句话里有要填的空」，{name} 就是空，会换成 name 盒子里的东西。例子：<code>pet = "狗"</code> → <code>print(f"我有一只{pet}")</code> 打印「我有一只狗」。</span><span class="en">The f tells Python "this sentence has blanks to fill", and {name} is a blank filled with what's in the name box. Example: <code>pet = "dog"</code> → <code>print(f"I have a {pet}")</code> prints "I have a dog".</span></div>
</div>

<pre style="white-space:pre-wrap">第 ___ 行的 ______ 是什么意思？请用小学生能听懂的话解释，再举一个小例子。</pre>
<button class="pg-btn copy-prev">📋 <span class="zh">复制这个问法</span><span class="en">Copy this question</span></button>

<div class="box box-think"><span class="box-title"><span class="zh">🤔 我的机器人 vs 真正的 AI</span><span class="en">🤔 My chatbot vs real AI</span></span>
<span class="zh">你的聊天机器人只会说<b>你写好的话</b>——问它「今天天气怎么样」它完全不懂。真正的 AI（比如 Codex）为什么什么都能聊？因为它读过<b>超级多的文字</b>，从里面学会了接话。第 6 课我们会亲手试一试 AI 是怎么学的。</span>
<span class="en">Your chatbot only says <b>what you wrote</b> — ask it about the weather and it has no idea. Why can real AI (like Codex) chat about anything? Because it has read <b>a huge amount of text</b> and learned how to reply from it. In Lesson 6 we'll see how AI learns.</span>
</div>

---

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b><span class="zh">变量</span><span class="en">Variable</span></b><code>name = "Kiwi"
size = 100</code><span><span class="zh">带名字的盒子。文字加引号，数字不加</span><span class="en">A box with a name. Text in quotes, numbers without</span></span></div>
  <div class="k"><b>f-string</b><code>print(f"你好 {name}")</code><span><span class="zh">f 开头，{盒子} 换成里面的东西</span><span class="en">Starts with f; {box} becomes its contents</span></span></div>
  <div class="k"><b>input()</b><code>pet = input("什么动物？ ")</code><span><span class="zh">问问题，等你打字，答案放进盒子</span><span class="en">Ask, wait for typing, store the answer</span></span></div>
  <div class="k"><b>int()</b><code>age = int(input("几岁？ "))
print(age + 1)</code><span><span class="zh">文字变数字，才能算数</span><span class="en">Text → number so you can do maths</span></span></div>
  <div class="k"><b>t.write()</b><code>t.write(name, align="center",
  font=("Arial", 32, "bold"))</code><span><span class="zh">海龟在画布上写字</span><span class="en">The turtle writes on the canvas</span></span></div>
  <div class="k"><b><span class="zh">顺序很重要</span><span class="en">Order matters</span></b><code>size = 100   # 先做盒子
t.forward(size)  # 再用</code><span><span class="zh">先放进盒子，才能拿出来用</span><span class="en">Put it in the box before you take it out</span></span></div>
</div>

<p><span class="zh">全部指令都在 <a href="{{ '/cheatsheet/' | relative_url }}#l02">📖 小词典 · 第 2 课</a>。</span><span class="en">Everything is in the <a href="{{ '/cheatsheet/' | relative_url }}#l02">📖 cheat sheet · Lesson 2</a>.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/02/homework/' | relative_url }}"><span class="zh">下一步：作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
