---
title: 接水果
title_en: Fruit Catcher
playground: true
---

# 🍎 <span class="zh">接水果</span><span class="en">Fruit Catcher</span>

<p class="zh">这是一个<b>真正能玩</b>的键盘游戏：水果从天上掉下来，你用 ← → 移动篮子去接。它是用你学过的东西做的——变量、if、函数、键盘事件 <code>onkey</code> 和计时器 <code>ontimer</code>。第 1 关先玩，后面每一关都要<b>改代码</b>，把游戏变成你的：更快、更花、更多命、两个水果……最后加上你自己的点子。</p>
<p class="en">A <b>real, playable</b> keyboard game: fruit falls from the sky and you move the basket with ← → to catch it. It's built from things you've learned — variables, if, functions, the keyboard event <code>onkey</code> and the timer <code>ontimer</code>. Level 1 is just playing; every level after that asks you to <b>change the code</b> to make the game yours: faster, prettier, more lives, two fruits… and finally your own idea.</p>

<div class="box box-warn"><span class="zh">🎮 <b>怎么玩：</b>点 ▶ 运行 → <b>点一下画布</b>（让它听键盘）→ 按 ← →。玩完点「■ 结束游戏」。改了代码要重新运行。</span><span class="en">🎮 <b>How to play:</b> click ▶ Run → <b>click the canvas</b> (so it listens to the keyboard) → press ← →. Click "■ End game" when done. After changing the code, run it again.</span></div>

<div class="cmds small">
  <div class="cmd"><code>screen.onkey(move_left, "Left")</code><span><span class="zh">按 ← 的时候，运行 move_left 函数</span><span class="en">When ← is pressed, run the move_left function</span></span></div>
  <div class="cmd"><code>screen.listen()</code><span><span class="zh">开始听键盘</span><span class="en">Start listening to the keyboard</span></span></div>
  <div class="cmd"><code>screen.ontimer(tick, 50)</code><span><span class="zh">50 毫秒后运行一次 tick（tick 里再叫一次自己 = 游戏循环）</span><span class="en">Run tick in 50 ms (tick calls itself again = the game loop)</span></span></div>
  <div class="cmd"><code>global score</code><span><span class="zh">在函数里改外面的变量，要先说这一句</span><span class="en">Say this before changing an outside variable inside a function</span></span></div>
</div>

<div class="levels-bar">
  <a href="#lv1" data-badge-id="catch-1">1</a><a href="#lv2" data-badge-id="catch-2">2</a><a href="#lv3" data-badge-id="catch-3">3</a><a href="#lv4" data-badge-id="catch-4">4</a><a href="#lv5" data-badge-id="catch-5">5</a><a href="#lv6" data-badge-id="catch-6">6</a>
</div>

<div class="level-head" id="lv1" data-badge-id="catch-1"><span class="lv"><span class="zh">第 1 关</span><span class="en">Level 1</span></span><b><span class="zh">先玩一局</span><span class="en">Just play</span></b><span class="pill">📘 <span class="zh">需要第 1 课</span><span class="en">Needs Lesson 1</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">运行并玩一局（目标：接住 <b>5 个</b>，诚实规则——自己数！运行起来就算过关）。然后<b>读一遍代码</b>：找到「水果往下掉」和「接住了」分别是哪几行。</span><span class="en">Run it and play a round (aim: <b>5</b> catches, honour rule — count them yourself! Running it passes the level). Then <b>read the code</b>: find the lines for "fruit falls" and "caught it".</span></div>
<div class="playground" data-src="{{ '/games/catch/code/level1-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level1-check.py' | relative_url }}" data-title="🍎 第 1 关" data-title-en="🍎 Level 1" data-save="catch-1" data-draft="catch-1" data-rows="14" data-badge="catch-1"></div>
<details class="hint"><summary>💡 <span class="zh">代码太长看不懂？</span><span class="en">Too much code?</span></summary><span class="zh">只看三块就够了：① 最上面的<b>大写变量</b>（可以改的数字和颜色）；② <code>def tick():</code>——每 50 毫秒发生一次的事；③ 最下面 4 行——把键盘和函数连起来。中间那些 <code>turtle.Turtle()</code> 你在第 1 课就认识。</span><span class="en">Just look at three parts: (1) the <b>CAPITAL variables</b> at the top (numbers and colours you can change); (2) <code>def tick():</code> — what happens every 50 ms; (3) the last 4 lines — wiring the keyboard to the functions. The <code>turtle.Turtle()</code> bits you've known since Lesson 1.</span></details>

<div class="level-head" id="lv2" data-badge-id="catch-2"><span class="lv"><span class="zh">第 2 关</span><span class="en">Level 2</span></span><b><span class="zh">加速！</span><span class="en">Speed up!</span></b><span class="pill">📘 <span class="zh">需要第 2 课</span><span class="en">Needs Lesson 2</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">太简单了？把水果下落速度 <code>SPEED</code> 改成 <b>8 或更大</b>，然后运行。你最多能接几个？</span><span class="en">Too easy? Change the falling speed <code>SPEED</code> to <b>8 or more</b> and run it. How many can you catch?</span></div>
<div class="playground" data-src="{{ '/games/catch/code/level2-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level2-check.py' | relative_url }}" data-title="🍎 第 2 关" data-title-en="🍎 Level 2" data-save="catch-2" data-draft="catch-2" data-rows="14" data-badge="catch-2"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">找到 <code>SPEED = 5</code> 那一行，把 5 改掉。想一想：这个数字在 <code>tick()</code> 里是怎么被用的？（<code>fruit.sety(fruit.ycor() - SPEED)</code>：每一次往下 SPEED 步）</span><span class="en">Find the line <code>SPEED = 5</code> and change the 5. Think: how is this number used inside <code>tick()</code>? (<code>fruit.sety(fruit.ycor() - SPEED)</code>: down by SPEED each time)</span></details>

<div class="level-head" id="lv3" data-badge-id="catch-3"><span class="lv"><span class="zh">第 3 关</span><span class="en">Level 3</span></span><b><span class="zh">换个颜色</span><span class="en">New colours</span></b><span class="pill">📘 <span class="zh">需要第 2 课</span><span class="en">Needs Lesson 2</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">把水果 <code>FRUIT_COLOUR</code> 和篮子 <code>BASKET_COLOUR</code> 都换成别的颜色。加分：把背景 <code>lightblue</code> 也换掉，做一个夜晚版。</span><span class="en">Change both <code>FRUIT_COLOUR</code> and <code>BASKET_COLOUR</code> to new colours. Bonus: change the background <code>lightblue</code> too and make a night version.</span></div>
<div class="swatches" data-colors="gold orange limegreen purple hotpink deepskyblue navy black white"></div>
<div class="playground" data-src="{{ '/games/catch/code/level3-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level3-check.py' | relative_url }}" data-title="🍎 第 3 关" data-title-en="🍎 Level 3" data-save="catch-3" data-draft="catch-3" data-rows="14" data-badge="catch-3"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">颜色要用英文名加引号，比如 <code>"gold"</code>。点上面的颜色圆点就能复制。</span><span class="en">Colours are English names in quotes, like <code>"gold"</code>. Click a colour dot above to copy it.</span></details>

<div class="level-head" id="lv4" data-badge-id="catch-4"><span class="lv"><span class="zh">第 4 关</span><span class="en">Level 4</span></span><b><span class="zh">更多命</span><span class="en">More lives</span></b><span class="pill">📘 <span class="zh">需要第 2 课</span><span class="en">Needs Lesson 2</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">现在漏掉 3 个就结束。改成漏掉 <b>5 个</b>才结束。然后读 <code>tick()</code> 最后几行：<code>if misses &lt; MAX_MISSES</code> 在做什么？</span><span class="en">Right now 3 misses ends the game. Make it <b>5</b>. Then read the end of <code>tick()</code>: what does <code>if misses &lt; MAX_MISSES</code> do?</span></div>
<div class="playground" data-src="{{ '/games/catch/code/level4-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level4-check.py' | relative_url }}" data-title="🍎 第 4 关" data-title-en="🍎 Level 4" data-save="catch-4" data-draft="catch-4" data-rows="14" data-badge="catch-4"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh"><code>MAX_MISSES = 3</code> → 改成 5。只要 <code>misses</code> 还小于它，<code>tick</code> 就会再约一次自己（<code>ontimer</code>）；一旦不小于，就不再约，游戏停下，写 GAME OVER。</span><span class="en"><code>MAX_MISSES = 3</code> → make it 5. While <code>misses</code> is smaller, <code>tick</code> books itself again (<code>ontimer</code>); once it isn't, it stops booking, the game ends and GAME OVER is written.</span></details>

<div class="level-head" id="lv5" data-badge-id="catch-5"><span class="lv"><span class="zh">第 5 关</span><span class="en">Level 5</span></span><b><span class="zh">两个水果</span><span class="en">Two fruits</span></b><span class="pill">📘 <span class="zh">需要第 7 课</span><span class="en">Needs Lesson 7</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">加<b>第二个水果</b>，名字叫 <code>fruit2</code>。它也要往下掉、也能被接住。这一关要用到第 7 课的<b>函数</b>：做水果的那 6 行要写两遍？不如打包成 <code>make_fruit(colour)</code>！</span><span class="en">Add a <b>second fruit</b> called <code>fruit2</code>. It must fall and be catchable too. This level needs Lesson 7's <b>functions</b>: writing the 6 fruit lines twice? Pack them into <code>make_fruit(colour)</code> instead!</span></div>
<div class="playground" data-src="{{ '/games/catch/code/level5-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level5-check.py' | relative_url }}" data-title="🍎 第 5 关" data-title-en="🍎 Level 5" data-save="catch-5" data-draft="catch-5" data-rows="16" data-badge="catch-5"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1：做水果的函数</span><span class="en">Hint 1: a fruit-making function</span></summary><pre>def make_fruit(colour):
    f = turtle.Turtle()
    f.shape("circle")
    f.color(colour)
    f.penup()
    f.speed(0)
    f.goto(random.randint(-250, 250), 280)
    return f

fruit = make_fruit(FRUIT_COLOUR)
fruit2 = make_fruit("gold")</pre><span class="zh">（把原来做 fruit 的 6 行换成这些）</span><span class="en">(replace the original 6 fruit lines with this)</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2：让两个都掉</span><span class="en">Hint 2: make both fall</span></summary><span class="zh">把 <code>tick()</code> 里「掉下来 + 接住 / 漏掉」那几行也打包成 <code>def fall(f):</code>（里面用 <code>f</code> 代替 <code>fruit</code>，记得 <code>global score, misses</code>），然后 <code>tick()</code> 里写 <code>fall(fruit)</code> 和 <code>fall(fruit2)</code>。</span><span class="en">Pack the "fall + caught / missed" lines of <code>tick()</code> into <code>def fall(f):</code> (use <code>f</code> instead of <code>fruit</code> inside, and keep <code>global score, misses</code>), then call <code>fall(fruit)</code> and <code>fall(fruit2)</code> inside <code>tick()</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3：完整参考</span><span class="en">Hint 3: full reference</span></summary><span class="zh">实在卡住了，看 <a href="{{ '/games/catch/code/level5-solution.py' | relative_url }}" target="_blank">参考答案</a>——但先自己试 10 分钟！</span><span class="en">Really stuck? Look at the <a href="{{ '/games/catch/code/level5-solution.py' | relative_url }}" target="_blank">reference solution</a> — but try for 10 minutes first!</span></details>

<div class="level-head" id="lv6" data-badge-id="catch-6"><span class="lv"><span class="zh">第 6 关</span><span class="en">Level 6</span></span><b><span class="zh">我的点子</span><span class="en">My idea</span></b><span class="pill">📘 <span class="zh">需要第 5 + 7 课</span><span class="en">Needs Lessons 5 + 7</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">① 做一个列表 <code>FRUITS</code>，放<b>至少 3 种</b>颜色，每个新水果用 <code>random.choice(FRUITS)</code> 随机选一种；② 写一个函数 <code>bonus()</code>，加一个<b>你自己的玩法</b>（比如金色水果 3 分、紫色水果扣分、每接 10 个加速……）。过关以后，<b>📤 存到作品墙</b>！</span><span class="en">(1) Make a list <code>FRUITS</code> with <b>at least 3</b> colours and pick one with <code>random.choice(FRUITS)</code> for each new fruit; (2) write a function <code>bonus()</code> that adds <b>your own rule</b> (gold fruit = 3 points, purple fruit loses points, speed up every 10 catches…). When you pass, <b>📤 save it to the Gallery</b>!</span></div>
<div class="playground" data-src="{{ '/games/catch/code/level6-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level6-check.py' | relative_url }}" data-title="🍎 第 6 关" data-title-en="🍎 Level 6" data-save="my-fruit-game" data-draft="catch-6" data-rows="16" data-badge="catch-6"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">列表写在最上面：<code>FRUITS = ["red", "gold", "purple"]</code>。在 <code>new_fruit()</code> 里加一行 <code>fruit.color(random.choice(FRUITS))</code>。</span><span class="en">Put the list at the top: <code>FRUITS = ["red", "gold", "purple"]</code>. Inside <code>new_fruit()</code> add <code>fruit.color(random.choice(FRUITS))</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">一个最简单的 bonus：<pre>def bonus():
    if fruit.pencolor() == "gold":
        return 3
    return 1</pre>然后接住的时候 <code>score += bonus()</code> 代替 <code>score += 1</code>。</span><span class="en">The simplest bonus: <pre>def bonus():
    if fruit.pencolor() == "gold":
        return 3
    return 1</pre> then use <code>score += bonus()</code> instead of <code>score += 1</code> when caught.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3：问 AI</span><span class="en">Hint 3: ask AI</span></summary><span class="zh">把你的代码发给 AI，这样问：「这是我的接水果游戏。我想加一个规则：______。请给我一个提示，告诉我该改哪个函数，不要直接给我代码。」</span><span class="en">Send your code to the AI and ask: "This is my fruit catcher game. I want to add a rule: ______. Give me a hint about which function to change — don't give me the code."</span></details>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 这就是你第 11 课要做的事</span><span class="en">🧠 This is what Lesson 11 is about</span></span>
<span class="zh">你刚刚做了程序员每天做的事：读别人的代码 → 改一点 → 测试 → 再改。第 10–12 课，你会从零开始做一个自己的游戏或 app，并把它放到网站上。接水果的代码可以当你的起点！</span>
<span class="en">You just did what programmers do every day: read someone's code → change a bit → test → change again. In Lessons 10–12 you'll build your own game or app from scratch and put it on your website. The fruit catcher code can be your starting point!</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
