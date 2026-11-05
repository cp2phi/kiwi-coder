---
title: 海龟迷宫
title_en: Turtle Maze
playground: true
---

# 🐢 <span class="zh">海龟迷宫</span><span class="en">Turtle Maze</span>

<p class="zh">海龟站在<b>绿点</b>上，脸朝右。用 <code>forward()</code>、<code>left()</code>、<code>right()</code> 指挥它走到<b>金色星星</b>——别碰到灰色的墙！每写一行就点 <b>▶ 运行</b> 看看走到哪了。撞墙的地方会出现一个<b>红点</b>。</p>
<p class="en">The turtle starts on the <b>green dot</b>, facing right. Use <code>forward()</code>, <code>left()</code> and <code>right()</code> to guide it to the <b>gold star</b> without touching the grey walls! Click <b>▶ Run</b> after every line to see where it got to. A <b>red dot</b> shows where you crashed.</p>

<div class="levels-bar">
  <a href="#lv1" data-badge-id="maze-1">1</a><a href="#lv2" data-badge-id="maze-2">2</a><a href="#lv3" data-badge-id="maze-3">3</a><a href="#lv4" data-badge-id="maze-4">4</a><a href="#lv5" data-badge-id="maze-5">5</a><a href="#lv6" data-badge-id="maze-6">6</a>
</div>

<div class="cmds small">
  <div class="cmd"><code>forward(100)</code><span><span class="zh">往前走 100 步</span><span class="en">Move forward 100 steps</span></span></div>
  <div class="cmd"><code>backward(50)</code><span><span class="zh">倒退 50 步</span><span class="en">Move back 50 steps</span></span></div>
  <div class="cmd"><code>left(90)</code><span><span class="zh">向左转 90 度（原地转，不走）</span><span class="en">Turn left 90° (on the spot)</span></span></div>
  <div class="cmd"><code>right(90)</code><span><span class="zh">向右转 90 度</span><span class="en">Turn right 90°</span></span></div>
  <div class="cmd"><code>t.color("red")</code><span><span class="zh">海龟就是 t，想换颜色也可以</span><span class="en">The turtle is called t — change its colour if you like</span></span></div>
</div>

<div class="box box-tip"><span class="zh">💡 这里的指令<b>不用</b>写 <code>t.</code>——迷宫已经帮你准备好海龟了。星星在格子的中心，走到星星<b>附近</b>就算到。</span><span class="en">💡 Here you <b>don't</b> write <code>t.</code> — the maze has already made the turtle for you. Getting <b>near</b> the star counts as reaching it.</span></div>

<div class="level-head" id="lv1" data-badge-id="maze-1"><span class="lv"><span class="zh">第 1 关</span><span class="en">Level 1</span></span><b><span class="zh">直直地走</span><span class="en">Straight ahead</span></b><span class="pill">📘 <span class="zh">需要第 1 课</span><span class="en">Needs Lesson 1</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">星星就在正前方。把数字改大，一次走到！</span><span class="en">The star is straight ahead. Make the number bigger and get there in one go!</span></div>
<div class="playground" data-src="{{ '/games/maze/code/level1-start.py' | relative_url }}" data-prelude="{{ '/games/maze/code/level1-setup.py' | relative_url }}" data-check="{{ '/games/maze/code/level1-check.py' | relative_url }}" data-badge="maze-1" data-draft="maze-1" data-title="🐢 第 1 关" data-title-en="🐢 Level 1" data-save="maze-level-1" data-rows="8"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">运行一次，看提示说「还差多少步」，把那个数字加到 <code>forward()</code> 里。</span><span class="en">Run it once, read how many steps are left, and add that number inside <code>forward()</code>.</span></details>

<div class="level-head" id="lv2" data-badge-id="maze-2"><span class="lv"><span class="zh">第 2 关</span><span class="en">Level 2</span></span><b><span class="zh">转一个弯</span><span class="en">One turn</span></b><span class="pill">📘 <span class="zh">需要第 1 课</span><span class="en">Needs Lesson 1</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">走廊是 L 形的：先往右，再往上。把 <code>___</code> 填上。</span><span class="en">The corridor is L-shaped: go right, then up. Fill in the <code>___</code>.</span></div>
<div class="playground" data-src="{{ '/games/maze/code/level2-start.py' | relative_url }}" data-prelude="{{ '/games/maze/code/level2-setup.py' | relative_url }}" data-check="{{ '/games/maze/code/level2-check.py' | relative_url }}" data-badge="maze-2" data-draft="maze-2" data-title="🐢 第 2 关" data-title-en="🐢 Level 2" data-save="maze-level-2" data-rows="8"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">海龟脸朝右，想朝上要<b>向左</b>转一个直角。直角是多少度？</span><span class="en">The turtle faces right; to face up it must turn <b>left</b> by a right angle. How many degrees is that?</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">转好以后，先随便走 <code>forward(100)</code>，看提示还差多少，再加上去。</span><span class="en">After turning, try <code>forward(100)</code>, read how far is left, then add it on.</span></details>

<div class="level-head" id="lv3" data-badge-id="maze-3"><span class="lv"><span class="zh">第 3 关</span><span class="en">Level 3</span></span><b><span class="zh">两次右转</span><span class="en">Two right turns</span></b><span class="pill">📘 <span class="zh">需要第 1 课</span><span class="en">Needs Lesson 1</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">走廊像一个「コ」字：往右 → 往下 → 往左。这次要用 <code>right()</code>。</span><span class="en">The corridor is a reversed C: right → down → left. This time you need <code>right()</code>.</span></div>
<div class="playground" data-src="{{ '/games/maze/code/level3-start.py' | relative_url }}" data-prelude="{{ '/games/maze/code/level3-setup.py' | relative_url }}" data-check="{{ '/games/maze/code/level3-check.py' | relative_url }}" data-badge="maze-3" data-draft="maze-3" data-title="🐢 第 3 关" data-title-en="🐢 Level 3" data-save="maze-level-3" data-rows="8"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">每条走廊大约 200–300 步长。一次只加一行，运行看看。</span><span class="en">Each corridor is about 200–300 steps. Add one line at a time and run.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">一共 5 行：走、右转、走、右转、走。</span><span class="en">5 lines in total: move, turn right, move, turn right, move.</span></details>

<div class="level-head" id="lv4" data-badge-id="maze-4"><span class="lv"><span class="zh">第 4 关</span><span class="en">Level 4</span></span><b><span class="zh">斜着走</span><span class="en">Diagonals</span></b><span class="pill">📘 <span class="zh">需要第 1 课</span><span class="en">Needs Lesson 1</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">石头挡住了直路。用 <code>left(45)</code> 和 <code>right(45)</code> 斜着穿过去，到右上方的星星。</span><span class="en">Rocks block the straight way. Use <code>left(45)</code> and <code>right(45)</code> to zig-zag to the star at the top right.</span></div>
<div class="playground" data-src="{{ '/games/maze/code/level4-start.py' | relative_url }}" data-prelude="{{ '/games/maze/code/level4-setup.py' | relative_url }}" data-check="{{ '/games/maze/code/level4-check.py' | relative_url }}" data-badge="maze-4" data-draft="maze-4" data-title="🐢 第 4 关" data-title-en="🐢 Level 4" data-save="maze-level-4" data-rows="9"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">起始代码已经斜着走了一段。接下来 <code>right(45)</code> 变回朝右，走 100，再 <code>left(45)</code> 斜上去。</span><span class="en">The starter code already goes one diagonal. Next, <code>right(45)</code> to face right again, go 100, then <code>left(45)</code> to go up diagonally.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">撞墙了？红点告诉你撞在哪。把<b>上一行</b>的数字改小一点点。</span><span class="en">Crashed? The red dot shows where. Make the number on the <b>line before</b> a little smaller.</span></details>

<div class="level-head" id="lv5" data-badge-id="maze-5"><span class="lv"><span class="zh">第 5 关</span><span class="en">Level 5</span></span><b><span class="zh">楼梯（用循环！）</span><span class="en">Stairs (use a loop!)</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">楼梯有 4 级，每一级都是：走 60 → 左转 → 走 60 → 右转。写 16 行太累了——用 <code>for</code> 循环（第 3 课的魔法）只要 5 行！</span><span class="en">The staircase has 4 steps, each one: forward 60 → left → forward 60 → right. 16 lines is too many — a <code>for</code> loop (Lesson 3 magic) does it in 5!</span></div>
<div class="playground" data-src="{{ '/games/maze/code/level5-start.py' | relative_url }}" data-prelude="{{ '/games/maze/code/level5-setup.py' | relative_url }}" data-check="{{ '/games/maze/code/level5-check.py' | relative_url }}" data-badge="maze-5" data-draft="maze-5" data-title="🐢 第 5 关" data-title-en="🐢 Level 5" data-save="maze-level-5" data-rows="8"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh"><code>range(4)</code> 就是「重复 4 次」。循环里面的 4 行前面都要有 4 个空格。</span><span class="en"><code>range(4)</code> means "repeat 4 times". The 4 lines inside the loop all need 4 spaces in front.</span></details>

<div class="level-head" id="lv6" data-badge-id="maze-6"><span class="lv"><span class="zh">第 6 关</span><span class="en">Level 6</span></span><b><span class="zh">螺旋迷宫</span><span class="en">Spiral maze</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">海龟在正中间，星星在左下角。走廊绕着中心一圈圈变大：60、60、120、120、180、180、240、240，每走一段就左转。走到星星就过关。<b>🌟 加分挑战：代码 6 行以内</b>（不算注释，诚实规则——自己数！）。</span><span class="en">The turtle is in the middle, the star is bottom-left. The corridor spirals outwards: 60, 60, 120, 120, 180, 180, 240, 240, turning left after each. Reach the star to pass. <b>🌟 Bonus challenge: 6 lines of code or fewer</b> (comments don't count; honour rule — count them yourself!).</span></div>
<div class="playground" data-src="{{ '/games/maze/code/level6-start.py' | relative_url }}" data-prelude="{{ '/games/maze/code/level6-setup.py' | relative_url }}" data-check="{{ '/games/maze/code/level6-check.py' | relative_url }}" data-badge="maze-6" data-draft="maze-6" data-title="🐢 第 6 关" data-title-en="🐢 Level 6" data-save="maze-level-6" data-rows="8"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">起始代码每圈只走了<b>一段</b>就转弯。每圈其实要走<b>两段</b>一样长的。</span><span class="en">The starter code only does <b>one</b> stretch per lap. Each lap actually needs <b>two</b> stretches of the same length.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">在循环里再加一次 <code>forward(60 * i)</code> 和 <code>left(90)</code>。<code>i</code> 会从 1 数到 4。</span><span class="en">Add another <code>forward(60 * i)</code> and <code>left(90)</code> inside the loop. <code>i</code> counts from 1 to 4.</span></details>
<details class="hint"><summary>🌟 <span class="zh">另一种解法</span><span class="en">Another way</span></summary><span class="zh">第 5 课学了列表以后，试试 <code>for n in [60, 60, 120, 120, 180, 180, 240, 240]:</code> ——只要 3 行！</span><span class="en">After Lesson 5 (lists), try <code>for n in [60, 60, 120, 120, 180, 180, 240, 240]:</code> — just 3 lines!</span></details>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 你发明了更好的走法吗？</span><span class="en">🧠 Found a better route?</span></span>
<span class="zh">比如用更少的行、更漂亮的颜色，或者让海龟边走边画花纹——点 <b>📤 存到作品墙</b> 给大家看！想自己设计迷宫？把关卡代码复制到 <a href="{{ '/playground/' | relative_url }}">自由画板</a> 里改墙的位置。</span>
<span class="en">Fewer lines, nicer colours, or a turtle that draws patterns as it walks — click <b>📤 Save to Gallery</b> to show everyone! Want to design your own maze? Copy the level code into the <a href="{{ '/playground/' | relative_url }}">Playground</a> and move the walls.</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
