---
title: 图案复刻
title_en: Copy the Pattern
playground: true
---

# 🎨 <span class="zh">图案复刻</span><span class="en">Copy the Pattern</span>

<p class="zh">每一关的画板上方有一个<b>🎯 目标图案</b>。你写代码画一个<b>一样的</b>，点 ▶ 运行，画板会告诉你<b>相似度</b>。相似度达到 <b>85%</b> 就过关！海龟都从画布正中间、脸朝右开始，所以照着目标的数字画就对了。</p>
<p class="en">Every level shows a <b>🎯 target drawing</b> above the playground. Write code to draw the <b>same thing</b>, click ▶ Run, and the playground tells you how <b>similar</b> it is. Reach <b>85%</b> to win! The turtle always starts in the middle facing right, so follow the target's numbers.</p>

<div class="box box-tip"><span class="zh">💡 比较的是<b>线条的位置</b>，不看颜色——所以颜色随你喜欢！差一点点？看看是不是数字、角度或者圈数不一样。</span><span class="en">💡 Only the <b>position of the lines</b> is compared, not colour — so pick any colours you like! Almost there? Check the numbers, angles or how many repeats.</span></div>

<div class="levels-bar">
  <a href="#lv1" data-badge-id="copy-1">1</a><a href="#lv2" data-badge-id="copy-2">2</a><a href="#lv3" data-badge-id="copy-3">3</a><a href="#lv4" data-badge-id="copy-4">4</a><a href="#lv5" data-badge-id="copy-5">5</a><a href="#lv6" data-badge-id="copy-6">6</a>
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

<div class="box box-think"><span class="box-title"><span class="zh">🧠 复刻完了？发明你自己的图案！</span><span class="en">🧠 Done copying? Invent your own pattern!</span></span>
<span class="zh">改改圈数、角度、半径，会出现意想不到的花纹。满意了就点 <b>📤 存到作品墙</b>。也可以把你的图案发给朋友，让他们来复刻！</span>
<span class="en">Change the repeats, angles or radius and surprising patterns appear. Happy with one? Click <b>📤 Save to Gallery</b>. Or send your pattern to a friend and challenge them to copy it!</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
