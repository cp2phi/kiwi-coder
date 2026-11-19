---
title: 接水果
title_en: Fruit Catcher
playground: true
---

# 🍎 <span class="zh">接水果</span><span class="en">Fruit Catcher</span>

<p class="zh">这是一个<b>真正能玩</b>的键盘游戏：水果从天上掉下来，你用 ← → 移动篮子去接。它是用你学过的东西做的——变量、if、函数、键盘事件 <code>onkey</code> 和计时器 <code>ontimer</code>。第 1 关先玩，后面每一关都要<b>改代码</b>，把游戏变成你的：更快、更花、更多命、两个水果、你自己的点子……第 7–9 关是<b>高手关</b>：再来一局、炸弹、连击和越来越快。</p>
<p class="en">A <b>real, playable</b> keyboard game: fruit falls from the sky and you move the basket with ← → to catch it. It's built from things you've learned — variables, if, functions, the keyboard event <code>onkey</code> and the timer <code>ontimer</code>. Level 1 is just playing; every level after that asks you to <b>change the code</b> to make the game yours: faster, prettier, more lives, two fruits, your own idea… Levels 7–9 are <b>pro levels</b>: play again, bombs, combos and speeding up.</p>

<div class="box box-warn"><span class="zh">🎮 <b>怎么玩：</b>点 ▶ 运行 → <b>点一下画布</b>（让它听键盘）→ 按 ← →。玩完点「■ 结束游戏」。改了代码要重新运行。</span><span class="en">🎮 <b>How to play:</b> click ▶ Run → <b>click the canvas</b> (so it listens to the keyboard) → press ← →. Click "■ End game" when done. After changing the code, run it again.</span></div>

<div class="cmds small">
  <div class="cmd"><code>screen.onkey(move_left, "Left")</code><span><span class="zh">按 ← 的时候，运行 move_left 函数</span><span class="en">When ← is pressed, run the move_left function</span></span></div>
  <div class="cmd"><code>screen.listen()</code><span><span class="zh">开始听键盘</span><span class="en">Start listening to the keyboard</span></span></div>
  <div class="cmd"><code>screen.ontimer(tick, 50)</code><span><span class="zh">50 毫秒后运行一次 tick（tick 里再叫一次自己 = 游戏循环）</span><span class="en">Run tick in 50 ms (tick calls itself again = the game loop)</span></span></div>
  <div class="cmd"><code>global score</code><span><span class="zh">在函数里改外面的变量，要先说这一句</span><span class="en">Say this before changing an outside variable inside a function</span></span></div>
</div>

<div class="levels-bar">
  <a href="#lv1" data-badge-id="catch-1">1</a><a href="#lv2" data-badge-id="catch-2">2</a><a href="#lv3" data-badge-id="catch-3">3</a><a href="#lv4" data-badge-id="catch-4">4</a><a href="#lv5" data-badge-id="catch-5">5</a><a href="#lv6" data-badge-id="catch-6">6</a><a href="#lv7" data-badge-id="catch-7">7</a><a href="#lv8" data-badge-id="catch-8">8</a><a href="#lv9" data-badge-id="catch-9">9</a>
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

<div class="box box-rule"><span class="box-title"><span class="zh">🧪 第 7–9 关：检查会真的「玩」你的函数</span><span class="en">🧪 Levels 7–9: the checker really "plays" your functions</span></span>
<span class="zh">这三关的过关检查像第 10 课的测试一样：它会把一个水果放到篮子上面、放到地上，然后<b>真的调用</b>你的 <code>fall(f)</code>、<code>restart()</code>……看分数和命对不对。所以函数和变量的名字要和任务里写的一样。每关开头的代码就是上一关的答案——先读懂再改！</span>
<span class="en">For these three levels the checker works like the tests in Lesson 10: it puts a fruit right on the basket or right at the ground and <b>really calls</b> your <code>fall(f)</code>, <code>restart()</code>… then checks the score and lives. So keep the function and variable names exactly as the task says. Each level starts from the previous level's answer — read it before you change it!</span></div>

<div class="level-head" id="lv7" data-badge-id="catch-7"><span class="lv"><span class="zh">第 7 关</span><span class="en">Level 7</span></span><b><span class="zh">生命值 + 再来一局</span><span class="en">Lives + play again</span></b><span class="pill">📘 <span class="zh">需要第 7 + 11 课</span><span class="en">Needs Lessons 7 + 11</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">把「漏掉几个」改成<b>命</b>：① <code>lives</code> 一开始是 3，<code>game_over = False</code>；② 写 <code>lose_life()</code>：命少 1，到 0 时 <code>game_over = True</code>，漏掉水果时调用它；③ <code>game_over</code> 以后什么都不再掉；④ 写 <code>restart()</code>，按<b>空格</b>调用：只有游戏<b>已经结束</b>时才重新开始（分数 0、命回满、水果重新掉）。游戏中途按空格要<b>没反应</b>——不然谁都能清零作弊！</span><span class="en">Turn "misses" into <b>lives</b>: (1) <code>lives</code> starts at 3 and <code>game_over = False</code>; (2) write <code>lose_life()</code>: one less life, and at 0 set <code>game_over = True</code>; call it when a fruit is missed; (3) after <code>game_over</code> nothing falls any more; (4) write <code>restart()</code>, called by <b>space</b>: only when the game is <b>already over</b> does it start again (score 0, full lives, fruit falling). Space in the middle of a game must <b>do nothing</b> — otherwise anyone could cheat by resetting!</span></div>
<div class="playground" data-src="{{ '/games/catch/code/level7-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level7-check.py' | relative_url }}" data-title="🍎 第 7 关" data-title-en="🍎 Level 7" data-save="catch-7" data-draft="catch-7" data-rows="16" data-badge="catch-7"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1：两个新变量和 lose_life</span><span class="en">Hint 1: two new variables and lose_life</span></summary><pre>MAX_LIVES = 3
lives = MAX_LIVES
game_over = False

def lose_life():
    global lives, game_over
    lives = lives - 1
    if lives &lt;= 0:
        game_over = True</pre><span class="zh">然后在 <code>fall(f)</code> 里，把 <code>misses += 1</code> 换成 <code>lose_life()</code>，<code>show_score()</code> 里的 Missed 也换成 Lives。</span><span class="en">Then in <code>fall(f)</code>, replace <code>misses += 1</code> with <code>lose_life()</code>, and show Lives instead of Missed in <code>show_score()</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2：tick 要会停</span><span class="en">Hint 2: tick must know when to stop</span></summary><pre>def tick():
    if game_over:
        return              # 结束了：不动，也不再约下一次 / over: no moving, no next tick
    fall(fruit)
    show_score()
    if game_over:
        pen.goto(-120, 0)
        pen.write("GAME OVER", font=("Arial", 28, "bold"))
    else:
        screen.ontimer(tick, 50)</pre><span class="zh">想一想：心跳是怎么停下来的？（不再 <code>ontimer</code>，就没有下一次了。）</span><span class="en">Think: how does the heartbeat stop? (No more <code>ontimer</code> means no next time.)</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3：restart 的四步</span><span class="en">Hint 3: four steps for restart</span></summary><span class="zh">① <code>global score, lives, game_over</code>；② <code>if not game_over: return</code>（游戏中按空格：直接走人）；③ 把 score、lives、game_over 放回一开始的样子，<code>new_fruit(fruit)</code>；④ 最后叫一次 <code>tick()</code>，心跳重新开始。别忘了最下面加 <code>screen.onkey(restart, "space")</code>。</span><span class="en">(1) <code>global score, lives, game_over</code>; (2) <code>if not game_over: return</code> (space during a game: just leave); (3) put score, lives and game_over back to how they started, and <code>new_fruit(fruit)</code>; (4) finally call <code>tick()</code> to restart the heartbeat. Don't forget <code>screen.onkey(restart, "space")</code> at the bottom.</span></details>

<div class="level-head" id="lv8" data-badge-id="catch-8"><span class="lv"><span class="zh">第 8 关</span><span class="en">Level 8</span></span><b><span class="zh">小心炸弹！</span><span class="en">Watch out for bombs!</span></b><span class="pill">📘 <span class="zh">需要第 5 + 7 课</span><span class="en">Needs Lessons 5 + 7</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">现在<b>同时掉 3 个</b>东西，有的是<b>黑色炸弹</b>（<code>is_bomb(f)</code> 已经帮你写好）。① 做一个列表 <code>things</code>，用循环放进 3 个 <code>make_thing()</code>；② <code>tick()</code> 让列表里<b>每一个</b>都 <code>fall</code>；③ 改 <code>fall(f)</code>：<b>同一件事，水果和炸弹结果相反</b>——</span><span class="en">Now <b>3 things fall at once</b>, and some are <b>black bombs</b> (<code>is_bomb(f)</code> is already written for you). (1) Make a list <code>things</code> and use a loop to put 3 <code>make_thing()</code> in it; (2) make <code>tick()</code> call <code>fall</code> for <b>every</b> thing in the list; (3) change <code>fall(f)</code>: <b>the same event has opposite results for fruit and bombs</b> —</span></div>
<table>
<tr><th></th><th><span class="zh">🍎 水果</span><span class="en">🍎 Fruit</span></th><th><span class="zh">💣 炸弹</span><span class="en">💣 Bomb</span></th></tr>
<tr><td><span class="zh">碰到篮子</span><span class="en">Touches the basket</span></td><td>+1 <span class="zh">分</span><span class="en">point</span></td><td>−1 <span class="zh">命</span><span class="en">life</span></td></tr>
<tr><td><span class="zh">掉到地上</span><span class="en">Hits the ground</span></td><td>−1 <span class="zh">命</span><span class="en">life</span></td><td><span class="zh">没事</span><span class="en">Nothing</span></td></tr>
</table>
<p class="zh">④ <code>restart()</code> 里把<b>每一个</b>都放回天上。</p><p class="en">(4) In <code>restart()</code>, put <b>every</b> thing back in the sky.</p>
<div class="playground" data-src="{{ '/games/catch/code/level8-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level8-check.py' | relative_url }}" data-title="🍎 第 8 关" data-title-en="🍎 Level 8" data-save="catch-8" data-draft="catch-8" data-rows="16" data-badge="catch-8"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1：一列表的海龟</span><span class="en">Hint 1: a list of turtles</span></summary><pre>things = []
for i in range(3):
    things.append(make_thing())</pre><span class="zh">然后 <code>tick()</code> 里 <code>fall(fruit)</code> 换成 <code>for f in things:</code> + <code>fall(f)</code>。<code>restart()</code> 也一样。原来那行 <code>fruit = make_thing()</code> 可以删掉。</span><span class="en">Then in <code>tick()</code> replace <code>fall(fruit)</code> with <code>for f in things:</code> + <code>fall(f)</code>. Same in <code>restart()</code>. The old <code>fruit = make_thing()</code> line can go.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2：表格变成 if</span><span class="en">Hint 2: turn the table into ifs</span></summary><span class="zh">表格有两行（篮子 / 地上），每一行又分两种（水果 / 炸弹）。所以是<b>if 里面再套 if</b>：在「碰到篮子」那一段里写 <code>if is_bomb(f):</code> 少命，<code>else:</code> 加分；在「掉到地上」那一段里写 <code>if not is_bomb(f):</code> 少命。两段最后都要 <code>new_thing(f)</code>。</span><span class="en">The table has two rows (basket / ground), and each row splits into two (fruit / bomb). So it's an <b>if inside an if</b>: in the "touches the basket" part write <code>if is_bomb(f):</code> lose a life, <code>else:</code> add a point; in the "hits the ground" part write <code>if not is_bomb(f):</code> lose a life. Both parts end with <code>new_thing(f)</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3：多掉几个？</span><span class="en">Hint 3: more falling things?</span></summary><span class="zh">过关以后试试：把 <code>range(3)</code> 改成 <code>range(5)</code>，或者在 <code>KINDS</code> 里多放几个 <code>"black"</code>。因为你用了列表和循环，改<b>一个数字</b>就够了——这就是列表的威力。</span><span class="en">After you pass, try changing <code>range(3)</code> to <code>range(5)</code>, or add more <code>"black"</code> to <code>KINDS</code>. Because you used a list and a loop, changing <b>one number</b> is enough — that's the power of lists.</span></details>

<div class="level-head" id="lv9" data-badge-id="catch-9"><span class="lv"><span class="zh">第 9 关</span><span class="en">Level 9</span></span><b><span class="zh">越来越快 + 连击</span><span class="en">Faster and faster + combos</span></b><span class="pill">📘 <span class="zh">需要第 7 + 10 课</span><span class="en">Needs Lessons 7 + 10</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">① 写函数 <code>speed_for(score)</code>，<b>return</b> 下落速度：0 分时是 5，<b>每满 5 分快 1</b>，最快 12（比如 4 分 → 5，5 分 → 6，10 分 → 7，100 分 → 12）；② <code>fall(f)</code> 里用 <code>speed_for(score)</code> 代替 <code>SPEED</code>；③ 加变量 <code>combo</code>（连击）：接到水果先 <code>combo</code> 加 1，如果这时 <code>combo</code> 是 <b>3 或更多</b>，这个水果算 <b>2 分</b>，不然算 1 分；④ 漏掉水果或接到炸弹，<code>combo</code> 变回 0。躲开炸弹不算出错，<code>combo</code> 不变。</span><span class="en">(1) Write a function <code>speed_for(score)</code> that <b>returns</b> the falling speed: 5 at 0 points, <b>1 faster for every full 5 points</b>, 12 at most (e.g. 4 points → 5, 5 points → 6, 10 points → 7, 100 points → 12); (2) use <code>speed_for(score)</code> instead of <code>SPEED</code> in <code>fall(f)</code>; (3) add a variable <code>combo</code>: catching a fruit first adds 1 to <code>combo</code>, and if <code>combo</code> is now <b>3 or more</b> that fruit is worth <b>2 points</b>, otherwise 1; (4) missing a fruit or catching a bomb sets <code>combo</code> back to 0. Dodging a bomb isn't a mistake, so <code>combo</code> stays.</span></div>
<div class="playground" data-src="{{ '/games/catch/code/level9-start.py' | relative_url }}" data-check="{{ '/games/catch/code/level9-check.py' | relative_url }}" data-title="🍎 第 9 关" data-title-en="🍎 Level 9" data-save="my-catch-pro" data-draft="catch-9" data-rows="16" data-badge="catch-9"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1：speed_for 找规律</span><span class="en">Hint 1: the pattern in speed_for</span></summary><span class="zh">列个表：0–4 分 → 5，5–9 分 → 6，10–14 分 → 7……「满了几个 5」就是 <code>score // 5</code>（<code>//</code> 是整除，去掉小数：13 // 5 = 2）。所以速度 = <code>5 + score // 5</code>。最后再用 <code>if</code> 管住上限 12。写完先测一测：<code>print(speed_for(4), speed_for(5), speed_for(100))</code> 应该是 5 6 12——或者用第 10 课的 <code>assert speed_for(10) == 7</code>。</span><span class="en">Make a table: 0–4 points → 5, 5–9 → 6, 10–14 → 7… "how many full 5s" is <code>score // 5</code> (<code>//</code> divides and drops the decimals: 13 // 5 = 2). So speed = <code>5 + score // 5</code>. Then use an <code>if</code> to keep it at 12 at most. Test it before wiring it in: <code>print(speed_for(4), speed_for(5), speed_for(100))</code> should be 5 6 12 — or use Lesson 10's <code>assert speed_for(10) == 7</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2：combo 在哪里归 0？</span><span class="en">Hint 2: where does combo go back to 0?</span></summary><span class="zh">「漏掉水果」和「接到炸弹」有什么共同点？它们都会调用 <code>lose_life()</code>！所以只要在 <code>lose_life()</code> 里写一次 <code>combo = 0</code>，两种情况都管到了（记得 <code>global combo</code>）。这就是把代码拆成函数的好处。</span><span class="en">What do "missing a fruit" and "catching a bomb" have in common? Both call <code>lose_life()</code>! So writing <code>combo = 0</code> once inside <code>lose_life()</code> handles both cases (remember <code>global combo</code>). That's the payoff of splitting code into functions.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3：接到水果那一段</span><span class="en">Hint 3: the fruit-caught part</span></summary><pre>else:
    combo += 1
    if combo &gt;= 3:
        score += 2
    else:
        score += 1</pre><span class="zh">🥇 加分题：加一个 <code>best</code>（最高分），游戏结束时如果 <code>score &gt; best</code> 就更新它；<code>restart()</code> 不要把它清零。过关以后 <b>📤 存到作品墙</b>！</span><span class="en">🥇 Bonus: add <code>best</code> (high score) — when the game ends, update it if <code>score &gt; best</code>; <code>restart()</code> must not reset it. When you pass, <b>📤 save it to the Gallery</b>!</span></details>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 这就是你第 11 课要做的事</span><span class="en">🧠 This is what Lesson 11 is about</span></span>
<span class="zh">你刚刚做了程序员每天做的事：读别人的代码 → 改一点 → 测试 → 再改。第 10–12 课，你会从零开始做一个自己的游戏或 app，并把它放到网站上。接水果的代码可以当你的起点！</span>
<span class="en">You just did what programmers do every day: read someone's code → change a bit → test → change again. In Lessons 10–12 you'll build your own game or app from scratch and put it on your website. The fruit catcher code can be your starting point!</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
