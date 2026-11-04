---
title: 宝石机器人
title_en: Gem Robot
playground: true
---

# 💎 <span class="zh">宝石机器人</span><span class="en">Gem Robot</span>

<p class="zh">橙色的机器人站在格子世界里，脸朝右。<code>move()</code> 走一格，走到<b>蓝色宝石</b>上面用 <code>pick()</code> 捡起来（变成金色就是捡到了）。捡完<b>所有</b>宝石就过关！走出格子或撞到<b>灰色石头</b>会出现红点。关卡会越来越大——不用循环和函数，手会写酸的！</p>
<p class="en">The orange robot lives in a grid world, facing right. <code>move()</code> goes one cell; stand on a <b>blue gem</b> and <code>pick()</code> it up (it turns gold). Collect <b>all</b> the gems to win! Leaving the grid or hitting a <b>grey rock</b> shows a red dot. Levels get bigger — without loops and functions your fingers will get tired!</p>

<div class="levels-bar">
  <a href="#lv1" data-badge-id="robot-1">1</a><a href="#lv2" data-badge-id="robot-2">2</a><a href="#lv3" data-badge-id="robot-3">3</a><a href="#lv4" data-badge-id="robot-4">4</a><a href="#lv5" data-badge-id="robot-5">5</a><a href="#lv6" data-badge-id="robot-6">6</a>
</div>

<div class="cmds small">
  <div class="cmd"><code>move()</code><span><span class="zh">往前走一格</span><span class="en">Move one cell forward</span></span></div>
  <div class="cmd"><code>turn_left()</code><span><span class="zh">原地向左转</span><span class="en">Turn left on the spot</span></span></div>
  <div class="cmd"><code>turn_right()</code><span><span class="zh">原地向右转</span><span class="en">Turn right on the spot</span></span></div>
  <div class="cmd"><code>pick()</code><span><span class="zh">捡起脚下的宝石</span><span class="en">Pick up the gem under you</span></span></div>
  <div class="cmd"><code>for i in range(3):</code><span><span class="zh">下面缩进的指令重复 3 次</span><span class="en">Repeat the indented lines 3 times</span></span></div>
  <div class="cmd"><code>def 名字():</code><span><span class="zh">教机器人一招（第 7 课）</span><span class="en">Teach the robot a trick (Lesson 7)</span></span></div>
</div>

<div class="box box-tip"><span class="zh">💡 括号里<b>不用</b>放数字：<code>move()</code> 永远只走一格。想走 3 格就写 3 次，或者用循环。</span><span class="en">💡 <b>No</b> number goes in the brackets: <code>move()</code> always moves exactly one cell. To go 3 cells, write it 3 times — or use a loop.</span></div>

<div class="level-head" id="lv1" data-badge-id="robot-1"><span class="lv"><span class="zh">第 1 关</span><span class="en">Level 1</span></span><b><span class="zh">走过去，捡起来</span><span class="en">Walk and pick</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">宝石在前面 3 格。走到它上面，再 <code>pick()</code>。</span><span class="en">The gem is 3 cells ahead. Get onto it, then <code>pick()</code>.</span></div>
<div class="playground" data-src="{{ '/games/robot/code/level1-start.py' | relative_url }}" data-prelude="{{ '/games/robot/code/level1-setup.py' | relative_url }}" data-check="{{ '/games/robot/code/level1-check.py' | relative_url }}" data-badge="robot-1" data-draft="robot-1" data-title="💎 第 1 关" data-title-en="💎 Level 1" data-save="robot-level-1" data-rows="8"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">3 个 <code>move()</code> 加 1 个 <code>pick()</code>，一共 4 行。</span><span class="en">3 × <code>move()</code> plus 1 × <code>pick()</code>: 4 lines.</span></details>

<div class="level-head" id="lv2" data-badge-id="robot-2"><span class="lv"><span class="zh">第 2 关</span><span class="en">Level 2</span></span><b><span class="zh">转个弯</span><span class="en">Take a turn</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">宝石在右上方：往右 3 格，左转，再往上 3 格。</span><span class="en">The gem is up and to the right: 3 cells right, turn left, 3 cells up.</span></div>
<div class="playground" data-src="{{ '/games/robot/code/level2-start.py' | relative_url }}" data-prelude="{{ '/games/robot/code/level2-setup.py' | relative_url }}" data-check="{{ '/games/robot/code/level2-check.py' | relative_url }}" data-badge="robot-2" data-draft="robot-2" data-title="💎 第 2 关" data-title-en="💎 Level 2" data-save="robot-level-2" data-rows="9"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">机器人转弯以后<b>不会自己走</b>，还要再 <code>move()</code>。数一数宝石在第几行。</span><span class="en">After turning the robot <b>doesn't move by itself</b> — you still need <code>move()</code>. Count which row the gem is in.</span></details>

<div class="level-head" id="lv3" data-badge-id="robot-3"><span class="lv"><span class="zh">第 3 关</span><span class="en">Level 3</span></span><b><span class="zh">一排宝石：用循环</span><span class="en">A row of gems: loop it</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">每隔一格就有一颗宝石，一共 3 颗。「走两步、捡一次」重复 3 次——填上 <code>range(___)</code>。</span><span class="en">A gem every second cell, 3 in total. "Two moves, one pick" × 3 — fill in <code>range(___)</code>.</span></div>
<div class="playground" data-src="{{ '/games/robot/code/level3-start.py' | relative_url }}" data-prelude="{{ '/games/robot/code/level3-setup.py' | relative_url }}" data-check="{{ '/games/robot/code/level3-check.py' | relative_url }}" data-badge="robot-3" data-draft="robot-3" data-title="💎 第 3 关" data-title-en="💎 Level 3" data-save="robot-level-3" data-rows="8"></div>
<details class="hint"><summary>💡 <span class="zh">提示</span><span class="en">Hint</span></summary><span class="zh">有几颗宝石，就重复几次。</span><span class="en">Repeat once for every gem.</span></details>

<div class="level-head" id="lv4" data-badge-id="robot-4"><span class="lv"><span class="zh">第 4 关</span><span class="en">Level 4</span></span><b><span class="zh">绕一圈：循环里的循环</span><span class="en">Around the square: a loop in a loop</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">四个角落各有一颗宝石（你脚下也有一颗！）。每条边走 5 格，捡一颗，左转——重复 4 次。中间有石头，别抄近路。</span><span class="en">A gem in each corner (including the one under you!). Each side: 5 moves, pick, turn left — 4 times. Rocks in the middle, no shortcuts.</span></div>
<div class="playground" data-src="{{ '/games/robot/code/level4-start.py' | relative_url }}" data-prelude="{{ '/games/robot/code/level4-setup.py' | relative_url }}" data-check="{{ '/games/robot/code/level4-check.py' | relative_url }}" data-badge="robot-4" data-draft="robot-4" data-title="💎 第 4 关" data-title-en="💎 Level 4" data-save="robot-level-4" data-rows="9"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">外面的循环管「4 条边」，里面的循环管「每条边走几格」。</span><span class="en">The outer loop handles "4 sides"; the inner loop handles "how many cells per side".</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">从第 1 格走到第 6 格，要走 5 步。</span><span class="en">Getting from cell 1 to cell 6 takes 5 moves.</span></details>

<div class="level-head" id="lv5" data-badge-id="robot-5"><span class="lv"><span class="zh">第 5 关</span><span class="en">Level 5</span></span><b><span class="zh">教机器人一招：grab_row()</span><span class="en">Teach a trick: grab_row()</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">三行宝石，每行 5 颗。先用 <code>def</code> 教机器人「扫一行」（走一格、捡一颗 × 5），然后像蛇一样一行一行扫：扫完 → 左转、走两格、左转 → 扫 → 右转、走两格、右转 → 扫。</span><span class="en">Three rows of gems, 5 each. First teach the robot "grab a row" with <code>def</code> (move, pick × 5), then sweep like a snake: row → turn left, 2 moves, turn left → row → turn right, 2 moves, turn right → row.</span></div>
<div class="playground" data-src="{{ '/games/robot/code/level5-start.py' | relative_url }}" data-prelude="{{ '/games/robot/code/level5-setup.py' | relative_url }}" data-check="{{ '/games/robot/code/level5-check.py' | relative_url }}" data-badge="robot-5" data-draft="robot-5" data-title="💎 第 5 关" data-title-en="💎 Level 5" data-save="robot-level-5" data-rows="14"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">函数里面的空：一行有 5 颗宝石，所以 <code>range(5)</code>；走一格之后要做什么？</span><span class="en">The blanks inside the function: 5 gems per row, so <code>range(5)</code>; and what do you do after each move?</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">起始代码扫了两行。第三行怎么去？这次要<b>右</b>转、走两格、再<b>右</b>转，然后再 <code>grab_row()</code>。</span><span class="en">The starter sweeps two rows. To reach the third: turn <b>right</b>, 2 moves, turn <b>right</b> again, then <code>grab_row()</code>.</span></details>

<div class="level-head" id="lv6" data-badge-id="robot-6"><span class="lv"><span class="zh">第 6 关</span><span class="en">Level 6</span></span><b><span class="zh">大地图：go(n)</span><span class="en">Big map: go(n)</span></b><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">6 颗宝石散在地图上，还有很多石头。先教机器人 <code>go(n)</code>（走 n 格），然后用 <code>go(3)</code>、<code>go(6)</code> 这样的指令规划一条路线，把宝石全捡完。路线自己设计！</span><span class="en">6 gems scattered around, plus lots of rocks. First teach the robot <code>go(n)</code> (move n cells), then plan a route with commands like <code>go(3)</code> and <code>go(6)</code> to collect them all. Design the route yourself!</span></div>
<div class="playground" data-src="{{ '/games/robot/code/level6-start.py' | relative_url }}" data-prelude="{{ '/games/robot/code/level6-setup.py' | relative_url }}" data-check="{{ '/games/robot/code/level6-check.py' | relative_url }}" data-badge="robot-6" data-draft="robot-6" data-title="💎 第 6 关" data-title-en="💎 Level 6" data-save="robot-level-6" data-rows="16"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh"><code>def go(n):</code> 里面的循环要重复 <code>n</code> 次——<code>range(n)</code>。</span><span class="en">The loop inside <code>def go(n):</code> repeats <code>n</code> times — <code>range(n)</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">一条可行的路线：右 3 → 上 3 → 左 3 → 上 3 → 右 6 → 下 4。每到一颗宝石就 <code>pick()</code>。用格子数一数每段要走几格。</span><span class="en">One route that works: right 3 → up 3 → left 3 → up 3 → right 6 → down 4. <code>pick()</code> at every gem. Count the cells for each stretch.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3</span><span class="en">Hint 3</span></summary><span class="zh">机器人在哪个方向，决定「上」是 <code>turn_left()</code> 还是 <code>turn_right()</code>。走错了就看红点，改上一行。</span><span class="en">Which way the robot faces decides whether "up" is <code>turn_left()</code> or <code>turn_right()</code>. Crashed? Look at the red dot and fix the line before.</span></details>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 你发明了更好的走法吗？</span><span class="en">🧠 Found a better route?</span></span>
<span class="zh">第 6 关有很多种路线。你的最短吗？点 <b>📤 存到作品墙</b> 给大家看！想做自己的地图？把关卡代码里的 <code>gems</code> 和 <code>rocks</code> 列表复制到 <a href="{{ '/playground/' | relative_url }}">自由画板</a> 里改一改。</span>
<span class="en">Level 6 has many possible routes. Is yours the shortest? Click <b>📤 Save to Gallery</b> to show everyone! Want your own map? Copy the level code's <code>gems</code> and <code>rocks</code> lists into the <a href="{{ '/playground/' | relative_url }}">Playground</a> and change them.</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
