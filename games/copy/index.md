---
title: 图案复刻
title_en: Copy the Pattern
playground: true
---

# 🎨 <span class="zh">图案复刻</span><span class="en">Copy the Pattern</span>

<p class="zh">每一关的画板上方有一个<b>🎯 目标图案</b>。你写代码画一个<b>一样的</b>，点 ▶ 运行，画板会告诉你<b>相似度</b>。相似度达到 <b>85%</b> 就过关（第 7–9 关要求更高，因为图案更精细）！海龟都从画布正中间、脸朝右开始，所以照着目标的数字画就对了。</p>
<p class="en">Every level shows a <b>🎯 target drawing</b> above the playground. Write code to draw the <b>same thing</b>, click ▶ Run, and the playground tells you how <b>similar</b> it is. Reach <b>85%</b> to win (levels 7–9 need more, because the patterns are more detailed)! The turtle always starts in the middle facing right, so follow the target's numbers.</p>

<div class="box box-tip"><span class="zh">💡 比较的是<b>线条的位置</b>，不看颜色——所以颜色随你喜欢！差一点点？看看是不是数字、角度或者圈数不一样。</span><span class="en">💡 Only the <b>position of the lines</b> is compared, not colour — so pick any colours you like! Almost there? Check the numbers, angles or how many repeats.</span></div>

<div class="levels-bar">
  <a href="#lv1" data-badge-id="copy-1">1</a><a href="#lv2" data-badge-id="copy-2">2</a><a href="#lv3" data-badge-id="copy-3">3</a><a href="#lv4" data-badge-id="copy-4">4</a><a href="#lv5" data-badge-id="copy-5">5</a><a href="#lv6" data-badge-id="copy-6">6</a><a href="#lv7" data-badge-id="copy-7">7</a><a href="#lv8" data-badge-id="copy-8">8</a><a href="#lv9" data-badge-id="copy-9">9</a>
</div>

<div class="cmds small">
  <div class="cmd"><code>t.forward(100)</code><span><span class="zh">往前走</span><span class="en">Move forward</span></span></div>
  <div class="cmd"><code>t.backward(100)</code><span><span class="zh">倒退</span><span class="en">Move backward</span></span></div>
  <div class="cmd"><code>t.left(90)</code> / <code>t.right(90)</code><span><span class="zh">左转 / 右转</span><span class="en">Turn left / right</span></span></div>
  <div class="cmd"><code>t.circle(60)</code><span><span class="zh">画一个半径 60 的圆</span><span class="en">A circle with radius 60</span></span></div>
  <div class="cmd"><code>t.penup()</code> <code>t.goto(0, 120)</code> <code>t.pendown()</code><span><span class="zh">抬笔 → 搬家 → 落笔</span><span class="en">Pen up → move → pen down</span></span></div>
  <div class="cmd"><code>for i in range(6):</code><span><span class="zh">重复 6 次（第 3 课）</span><span class="en">Repeat 6 times (Lesson 3)</span></span></div>
</div>

<div class="level-head" id="lv1" data-badge-id="copy-1"><span class="lv"><span class="zh">第 1 关</span><span class="en">Level 1</span></span><b><span class="zh">正方形</span><span class="en">Square</span></b><span class="pill">📘 <span class="zh">需要第 1 课</span><span class="en">Needs Lesson 1</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">一个边长 <b>150</b> 的正方形。起始代码画了一条边并转了弯，把剩下的补完。</span><span class="en">A square with sides of <b>150</b>. The starter draws one side and turns — finish the rest.</span></div>
<div class="playground" data-src="{{ '/games/copy/code/level1-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level1-target.py' | relative_url }}" data-badge="copy-1" data-draft="copy-1" data-title="🎨 第 1 关" data-title-en="🎨 Level 1" data-save="copy-level-1" data-rows="10"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">正方形有 4 条边，每条边后面都左转 90。</span><span class="en">A square has 4 sides, with a left turn of 90 after each one.</span></details>

<div class="level-head" id="lv2" data-badge-id="copy-2"><span class="lv"><span class="zh">第 2 关</span><span class="en">Level 2</span></span><b><span class="zh">小房子</span><span class="en">Little house</span></b><span class="pill">📘 <span class="zh">需要第 1 课</span><span class="en">Needs Lesson 1</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">正方形 <b>120</b> 的房子，上面一个边长 <b>120</b> 的三角形屋顶。起始代码已经画好正方形，并把海龟搬到了左上角、转好了角度——画屋顶的两条边吧。</span><span class="en">A house: square <b>120</b> with a triangle roof of side <b>120</b>. The starter already draws the square and moves the turtle to the top-left corner at the right angle — draw the roof's two sides.</span></div>
<div class="playground" data-src="{{ '/games/copy/code/level2-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level2-target.py' | relative_url }}" data-badge="copy-2" data-draft="copy-2" data-title="🎨 第 2 关" data-title-en="🎨 Level 2" data-save="copy-level-2" data-rows="14"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">屋顶：走 120，左转 120，再走 120。</span><span class="en">Roof: forward 120, left 120, forward 120.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">三角形每个角要转 120 度（360 ÷ 3）。</span><span class="en">Each corner of a triangle turns 120 degrees (360 ÷ 3).</span></details>

<div class="level-head" id="lv3" data-badge-id="copy-3"><span class="lv"><span class="zh">第 3 关</span><span class="en">Level 3</span></span><b><span class="zh">八边形</span><span class="en">Octagon</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">一个边长 <b>70</b> 的八边形。填两个空：重复几次？每次转多少度？</span><span class="en">An octagon with sides of <b>70</b>. Fill two blanks: how many repeats? How many degrees per turn?</span></div>
<div class="playground" data-src="{{ '/games/copy/code/level3-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level3-target.py' | relative_url }}" data-badge="copy-3" data-draft="copy-3" data-title="🎨 第 3 关" data-title-en="🎨 Level 3" data-save="copy-level-3" data-rows="10"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">海龟绕一圈一共转 360 度。8 条边，360 ÷ 8 = ？</span><span class="en">The turtle turns 360 in total. 8 sides, so 360 ÷ 8 = ?</span></details>

<div class="level-head" id="lv4" data-badge-id="copy-4"><span class="lv"><span class="zh">第 4 关</span><span class="en">Level 4</span></span><b><span class="zh">太阳光</span><span class="en">Sunburst</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh"><b>36</b> 根长 <b>150</b> 的线从中心射出去。每根线：走出去、<b>退回来</b>、转一点点。转多少才能刚好转满一圈？</span><span class="en"><b>36</b> lines of <b>150</b> shooting out from the centre. Each line: go out, <b>come back</b>, turn a little. How much per turn to make exactly one full circle?</span></div>
<div class="playground" data-src="{{ '/games/copy/code/level4-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level4-target.py' | relative_url }}" data-badge="copy-4" data-draft="copy-4" data-title="🎨 第 4 关" data-title-en="🎨 Level 4" data-save="copy-level-4" data-rows="10"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">退回来的距离和走出去的一样。36 根线转满 360 度，每根转 360 ÷ 36。</span><span class="en">Come back the same distance you went out. 36 lines make 360 degrees, so each turn is 360 ÷ 36.</span></details>

<div class="level-head" id="lv5" data-badge-id="copy-5"><span class="lv"><span class="zh">第 5 关</span><span class="en">Level 5</span></span><b><span class="zh">彩虹螺旋</span><span class="en">Rainbow spiral</span></b><span class="pill">📘 <span class="zh">需要第 3 + 5 课</span><span class="en">Needs Lessons 3 + 5</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">一个方形螺旋：重复 <b>60</b> 次，第 <code>i</code> 次走 <code>i * 4</code> 步，每次左转 <b>91</b> 度。颜色列表已经帮你准备好了（第 5 课的魔法）。</span><span class="en">A square spiral: <b>60</b> repeats, step <code>i</code> goes <code>i * 4</code>, turning left <b>91</b> each time. The colour list is ready for you (Lesson 5 magic).</span></div>
<div class="playground" data-src="{{ '/games/copy/code/level5-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level5-target.py' | relative_url }}" data-threshold="80" data-badge="copy-5" data-draft="copy-5" data-title="🎨 第 5 关" data-title-en="🎨 Level 5" data-save="copy-level-5" data-rows="12"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">第一个空填 <code>i * 4</code>（<code>i</code> 是循环数到几），第二个空填角度。</span><span class="en">The first blank is <code>i * 4</code> (<code>i</code> is the loop counter), the second is the angle.</span></details>

<div class="level-head" id="lv6" data-badge-id="copy-6"><span class="lv"><span class="zh">第 6 关</span><span class="en">Level 6</span></span><b><span class="zh">六瓣花</span><span class="en">Six-petal flower</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh"><b>6</b> 个半径 <b>60</b> 的圆，每画完一个左转 <b>60</b> 度，就变成一朵花。起始代码只画了一个圆——用循环把它变成 6 个。</span><span class="en"><b>6</b> circles of radius <b>60</b>, turning left <b>60</b> after each one, make a flower. The starter draws one circle — use a loop to make 6.</span></div>
<div class="playground" data-src="{{ '/games/copy/code/level6-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level6-target.py' | relative_url }}" data-badge="copy-6" data-draft="copy-6" data-title="🎨 第 6 关" data-title-en="🎨 Level 6" data-save="copy-level-6" data-rows="10"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh"><code>for i in range(6):</code> 下面放两行：画圆、左转 60。</span><span class="en">Under <code>for i in range(6):</code> put two lines: draw a circle, turn left 60.</span></details>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 第 7–9 关：先想规律，再写代码</span><span class="en">🧠 Levels 7–9: find the pattern first, then code</span></span>
<span class="zh">后面三关的线条太多，一条一条画会累死。先拿纸笔：<b>哪些东西在重复？每次重复，哪个数字在变？变化有什么规律？</b>想清楚了，代码只要十几行。</span>
<span class="en">The next three levels have far too many lines to draw one by one. Grab paper first: <b>what repeats? Which number changes each time? What's the rule for the change?</b> Once you know, the code is only a dozen lines.</span></div>

<div class="level-head" id="lv7" data-badge-id="copy-7"><span class="lv"><span class="zh">第 7 关</span><span class="en">Level 7</span></span><b><span class="zh">方块隧道</span><span class="en">Square tunnel</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh"><b>8</b> 个正方形，<b>中心都在画布正中间</b>。最小的边长 <b>30</b>，后面每个比前一个大 <b>30</b>（30、60、90……）。起始代码只画了最小的那个。难点：每个正方形的<b>起点（左下角）</b>都不一样——找出它和边长的关系！要 <b>93%</b> 才过关。</span><span class="en"><b>8</b> squares, <b>all centred on the middle of the canvas</b>. The smallest has sides of <b>30</b>, and each next one is <b>30</b> bigger (30, 60, 90…). The starter only draws the smallest. The tricky part: every square has a different <b>starting point (bottom-left corner)</b> — find how it relates to the side length! You need <b>93%</b> to win.</span></div>
<div class="playground" data-src="{{ '/games/copy/code/level7-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level7-target.py' | relative_url }}" data-threshold="93" data-badge="copy-7" data-draft="copy-7" data-title="🎨 第 7 关" data-title-en="🎨 Level 7" data-save="copy-level-7" data-rows="14"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1：找规律</span><span class="en">Hint 1: spot the pattern</span></summary><span class="zh">边长 30 的正方形，左下角在 (-15, -15)——往左、往下各走了<b>边长的一半</b>，正方形才会居中。那边长 60 的呢？边长 240 的呢？用 <code>size</code> 写出来：左下角 = (<code>-size / 2</code>, <code>-size / 2</code>)。</span><span class="en">The size-30 square starts at (-15, -15) — <b>half the side</b> to the left and half down, so it ends up centred. What about size 60? Size 240? Written with <code>size</code>: bottom-left = (<code>-size / 2</code>, <code>-size / 2</code>).</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2：循环套循环</span><span class="en">Hint 2: a loop inside a loop</span></summary><span class="zh">外面的循环数正方形（8 个），里面的循环画 4 条边。<code>for i in range(1, 9):</code> 让 i 是 1 到 8，那么 <code>size = i * 30</code> 就是 30 到 240。</span><span class="en">The outer loop counts squares (8 of them), the inner loop draws 4 sides. <code>for i in range(1, 9):</code> makes i go 1 to 8, so <code>size = i * 30</code> goes 30 to 240.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3：骨架</span><span class="en">Hint 3: the skeleton</span></summary><pre>for i in range(1, 9):
    size = i * 30
    t.penup()
    t.goto(___, ___)
    t.pendown()
    for k in range(4):
        t.forward(size)
        t.left(90)</pre><span class="zh">注意缩进：里面的循环要比外面的多缩进一层。</span><span class="en">Watch the indentation: the inner loop is indented one more level than the outer one.</span></details>

<div class="level-head" id="lv8" data-badge-id="copy-8"><span class="lv"><span class="zh">第 8 关</span><span class="en">Level 8</span></span><b><span class="zh">多边形排排队</span><span class="en">Polygon parade</span></b><span class="pill">📘 <span class="zh">需要第 3 课（会第 7 课更好）</span><span class="en">Needs Lesson 3 (Lesson 7 helps)</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">三角形、正方形、五边形、六边形、七边形排成一排，边长都是 <b>45</b>。第一个从 <b>(-255, -40)</b> 开始，后面每个<b>往右挪 115</b>。起始代码只画了三角形。<b>边数</b>变了，还有哪个数字跟着变？用<b>一个</b>循环画完 5 个形状。要 <b>90%</b> 才过关。</span><span class="en">A triangle, square, pentagon, hexagon and heptagon in a row, all with sides of <b>45</b>. The first starts at <b>(-255, -40)</b> and each next one starts <b>115 further right</b>. The starter only draws the triangle. When the <b>number of sides</b> changes, which other number changes with it? Draw all 5 shapes with <b>one</b> loop. You need <b>90%</b> to win.</span></div>
<div class="playground" data-src="{{ '/games/copy/code/level8-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level8-target.py' | relative_url }}" data-threshold="90" data-badge="copy-8" data-draft="copy-8" data-title="🎨 第 8 关" data-title-en="🎨 Level 8" data-save="copy-level-8" data-rows="14"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1：列个表</span><span class="en">Hint 1: make a table</span></summary><span class="zh">3 条边 → 每个角转 120；4 条边 → 90；5 条边 → 72；6 条边 → 60。看出来了吗？转角 = <code>360 / 边数</code>。（海龟绕一圈总共转 360 度。）</span><span class="en">3 sides → turn 120 at each corner; 4 sides → 90; 5 sides → 72; 6 sides → 60. See it? Turn = <code>360 / sides</code>. (The turtle turns 360 in total to get all the way round.)</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2：让边数变成变量</span><span class="en">Hint 2: make the number of sides a variable</span></summary><span class="zh"><code>for sides in range(3, 8):</code> 让 sides 依次是 3、4、5、6、7。里面再套一个 <code>for k in range(sides):</code> 画每一条边。</span><span class="en"><code>for sides in range(3, 8):</code> makes sides go 3, 4, 5, 6, 7. Inside it, <code>for k in range(sides):</code> draws each side.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3：位置</span><span class="en">Hint 3: the position</span></summary><span class="zh">在循环外面写 <code>x = -255</code>；每画一个形状之前 <code>t.goto(x, -40)</code>（记得抬笔落笔），画完 <code>x = x + 115</code>。学过第 7 课？把画多边形写成 <code>def polygon(sides, length):</code> 会更清楚。</span><span class="en">Before the loop write <code>x = -255</code>; before each shape <code>t.goto(x, -40)</code> (pen up and down!), and after it <code>x = x + 115</code>. Done Lesson 7? Writing <code>def polygon(sides, length):</code> makes it even clearer.</span></details>

<div class="level-head" id="lv9" data-badge-id="copy-9"><span class="lv"><span class="zh">第 9 关</span><span class="en">Level 9</span></span><b><span class="zh">棋盘</span><span class="en">Chessboard</span></b><span class="pill">📘 <span class="zh">需要第 4 + 7 课</span><span class="en">Needs Lessons 4 + 7</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh"><b>6 行 × 6 列</b>的棋盘，每格 <b>40</b>，棋盘左下角在 <b>(-120, -120)</b>。每一格都有黑框；<b>最左下那一格涂满</b>，然后涂满 / 空着轮流来。起始代码的 <code>square(x, y, size)</code> 只会画涂满的格子。你要：① 用<b>两层循环</b>算出 36 个格子的位置；② 找出「哪些格子要涂」的规律；③ 给函数加一个参数，让它能决定涂不涂。这次相似度要 <b>95%</b>！</span><span class="en">A <b>6 rows × 6 columns</b> board, each square <b>40</b>, with its bottom-left corner at <b>(-120, -120)</b>. Every square has a black outline; <b>the bottom-left square is filled</b>, then filled / empty take turns. The starter's <code>square(x, y, size)</code> can only draw filled squares. You need to: (1) use <b>two loops</b> to work out where the 36 squares go; (2) find the rule for which squares are filled; (3) give the function one more parameter so it can decide whether to fill. This one needs <b>95%</b>!</span></div>
<div class="cmds small">
  <div class="cmd"><code>t.color("black", "crimson")</code><span><span class="zh">线的颜色、涂的颜色</span><span class="en">Line colour, fill colour</span></span></div>
  <div class="cmd"><code>t.begin_fill()</code> … <code>t.end_fill()</code><span><span class="zh">中间画的形状会被涂满</span><span class="en">The shape drawn in between gets filled</span></span></div>
</div>
<div class="playground" data-src="{{ '/games/copy/code/level9-start.py' | relative_url }}" data-target="{{ '/games/copy/code/level9-target.py' | relative_url }}" data-threshold="95" data-badge="copy-9" data-draft="copy-9" data-title="🎨 第 9 关" data-title-en="🎨 Level 9" data-save="copy-level-9" data-rows="18"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1：哪些格子要涂？</span><span class="en">Hint 1: which squares are filled?</span></summary><span class="zh">给格子编号：行 <code>row</code> 从下往上 0–5，列 <code>col</code> 从左往右 0–5。涂满的有 (0,0) (0,2) (1,1) (1,3) (2,0)…… 把 <code>row + col</code> 算出来：0、2、2、4、2……全是<b>双数</b>！双数就是 <code>(row + col) % 2 == 0</code>（第 4 课的 %）。</span><span class="en">Number the squares: <code>row</code> 0–5 from bottom to top, <code>col</code> 0–5 from left to right. Filled ones are (0,0) (0,2) (1,1) (1,3) (2,0)… Work out <code>row + col</code>: 0, 2, 2, 4, 2… all <b>even</b>! Even means <code>(row + col) % 2 == 0</code> (the % from Lesson 4).</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2：位置</span><span class="en">Hint 2: positions</span></summary><span class="zh">第 <code>col</code> 列的 x 是 <code>-120 + col * 40</code>，第 <code>row</code> 行的 y 是 <code>-120 + row * 40</code>。两层循环：<code>for row in range(6):</code> 里面套 <code>for col in range(6):</code>。</span><span class="en">Column <code>col</code> has x = <code>-120 + col * 40</code>; row <code>row</code> has y = <code>-120 + row * 40</code>. Two loops: <code>for row in range(6):</code> with <code>for col in range(6):</code> inside.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3：函数多一个参数</span><span class="en">Hint 3: one more parameter</span></summary><pre>def square(x, y, size, filled):
    ...
    if filled:
        t.begin_fill()
    # 画 4 条边 / draw the 4 sides
    if filled:
        t.end_fill()</pre><span class="zh">调用的时候：<code>square(x, y, 40, (row + col) % 2 == 0)</code>——最后那个参数会是 True 或 False。</span><span class="en">Call it like <code>square(x, y, 40, (row + col) % 2 == 0)</code> — the last argument becomes True or False.</span></details>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 复刻完了？发明你自己的图案！</span><span class="en">🧠 Done copying? Invent your own pattern!</span></span>
<span class="zh">改改圈数、角度、半径，会出现意想不到的花纹。满意了就点 <b>📤 存到作品墙</b>。也可以把你的图案发给朋友，让他们来复刻！</span>
<span class="en">Change the repeats, angles or radius and surprising patterns appear. Happy with one? Click <b>📤 Save to Gallery</b>. Or send your pattern to a friend and challenge them to copy it!</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
