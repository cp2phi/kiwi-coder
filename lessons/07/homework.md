---
title: 第 7 课 · 作业
title_en: Lesson 7 · Homework
lesson: "07"
tab: homework
playground: true
---

# 🏙️ <span class="zh">第 7 课作业：海龟城市规划师</span><span class="en">Lesson 7 homework: Turtle City Planner</span>

<p><span class="zh">你是城市规划师！用<b>函数</b>规划一座城：房子、街道、火箭、星空……<b>每种东西只写一次</b>。</span><span class="en">You're the city planner! Design a city with <b>functions</b>: houses, streets, rockets, a starry sky… <b>write each thing only once</b>.</span> <span class="pill">⏱ <span class="zh">🥉 约 25 分钟，🥈🥇 再加 20–40 分钟</span><span class="en">🥉 about 25 min, 🥈🥇 another 20–40 min</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week07-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：屋顶 + random_colour() + street(n, y)</span><span class="en">Must do: roof + random_colour() + street(n, y)</span></h3>
    <p><span class="zh">画板里有 4 个 TODO：① 给 <code>house</code> 加屋顶（<b>先别看例子</b>，自己试）② 写 <code>random_colour()</code>，<code>return</code> 一个随机颜色 ③ 写 <code>street(n, y)</code>，里面喊 <code>house</code> 和 <code>random_colour()</code> ④ 喊 <code>street</code> 两次画两排。<b>只用第 1–7 课学过的东西</b>。</span><span class="en">The playground has 4 TODOs: ① give <code>house</code> a roof (<b>try without looking</b> at the examples) ② write <code>random_colour()</code> that <code>return</code>s a random colour ③ write <code>street(n, y)</code>, which calls <code>house</code> and <code>random_colour()</code> ④ call <code>street</code> twice for two rows. <b>Only Lesson 1–7 stuff needed</b>.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：rocket(x, y, size=80) + sky(is_night)</span><span class="en">Bonus: rocket(x, y, size=80) + sky(is_night)</span></h3>
    <p><span class="zh">写一个带<b>默认值</b>的 <code>rocket</code>（喊 <code>rocket(200, -150)</code> 和 <code>rocket(100, -150, 40)</code> 都要能画）。再写 <code>sky(is_night)</code>：True 画深蓝天、月亮和 <b>20 颗随机位置的星星</b>；False 画蓝天和太阳。</span><span class="en">Write a <code>rocket</code> with a <b>default value</b> (both <code>rocket(200, -150)</code> and <code>rocket(100, -150, 40)</code> must work). Then <code>sky(is_night)</code>: True draws a dark sky, a moon and <b>20 stars at random spots</b>; False draws a blue sky and a sun.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：城市规划电脑</span><span class="en">Challenge: the city-planning computer</span></h3>
    <p><span class="zh">让电脑<b>自己设计</b>城市！① <code>plan_city(n)</code> 交回一个列表，装 n 个随机的建筑名字（<code>"house"</code>、<code>"tree"</code>、<code>"rocket"</code>），规则：<b>最多 1 个 rocket</b>。② <code>draw_city(plan)</code> 看列表里每个名字，用 <code>if / elif</code> 喊对应的招式，从左往右排。运行 5 次，每次都是新城市，而且永远不会有 2 个火箭。<b>先在纸上画一画</b>你的招式谁喊谁，再写。</span><span class="en">Let the computer <b>design the city</b>! ① <code>plan_city(n)</code> returns a list of n random building names (<code>"house"</code>, <code>"tree"</code>, <code>"rocket"</code>), with the rule: <b>at most 1 rocket</b>. ② <code>draw_city(plan)</code> looks at each name and uses <code>if / elif</code> to call the matching trick, left to right. Run it 5 times: a new city every time, never 2 rockets. <b>Sketch on paper first</b> which trick calls which, then code.</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>return random.choice(colours)</code><span><span class="zh">交回一个随机颜色</span><span class="en">Return a random colour</span></span></div>
  <div class="cmd"><code>def rocket(x, y, size=80):</code><span><span class="zh">默认值：不递 size 就是 80</span><span class="en">Default: size is 80 unless you hand one in</span></span></div>
  <div class="cmd"><code>t.dot(4, "white")</code><span><span class="zh">画一个实心点（星星、月亮）</span><span class="en">A filled dot (stars, moon)</span></span></div>
  <div class="cmd"><code>random.randint(-300, 300)</code><span><span class="zh">随机位置（第 4 课）</span><span class="en">A random position (Lesson 4)</span></span></div>
  <div class="cmd"><code>plan.append("tree")</code><span><span class="zh">往列表里加东西（第 5 课）</span><span class="en">Add to a list (Lesson 5)</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上，关掉网页也不会丢。</span><span class="en">Your code is saved on this computer automatically, even if you close the page.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/homework.py' | relative_url }}" data-title="🏙️ 海龟城市规划师" data-title-en="🏙️ Turtle City Planner" data-save="week07-homework" data-draft="l7-homework" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 屋顶提示</span><span class="en">💡 Roof hint</span></summary><span class="zh">画完身体，海龟在左下角脸朝右。抬笔走到左上角 <code>(x, y + size)</code>，落笔，然后「forward(size)、left(120)」重复 3 次——等边三角形！</span><span class="en">After the body the turtle is at the bottom-left facing right. Pen up, go to the top-left <code>(x, y + size)</code>, pen down, then repeat "forward(size), left(120)" 3 times — an equilateral triangle!</span></details>
<details class="hint"><summary><span class="zh">💡 street 提示</span><span class="en">💡 street hint</span></summary><span class="zh">学一学例 6 的 street 几乎一样，只是颜色换成 <code>random_colour()</code>——<b>一个招式的结果直接递给另一个招式</b>：<code>house(..., random_colour())</code>。</span><span class="en">Almost the same as street in Learn Example 6, but the colour is <code>random_colour()</code> — <b>one trick's result handed straight into another</b>: <code>house(..., random_colour())</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 「最多 1 个火箭」提示</span><span class="en">💡 "At most 1 rocket" hint</span></summary><span class="zh">在 <code>plan_city</code> 里放一个计数器 <code>rockets = 0</code>。随机挑到 <code>"rocket"</code> 的时候：如果 <code>rockets</code> 已经是 1，就换成 <code>"house"</code>；不然 <code>rockets += 1</code>。最后 <code>return plan</code>。</span><span class="en">Keep a counter <code>rockets = 0</code> in <code>plan_city</code>. When you randomly pick <code>"rocket"</code>: if <code>rockets</code> is already 1, change it to <code>"house"</code>; otherwise <code>rockets += 1</code>. At the end <code>return plan</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 draw_city 提示</span><span class="en">💡 draw_city hint</span></summary><span class="zh"><code>x = -300</code> → <code>for building in plan:</code> → <code>if building == "house": house(x, -150, 70, random_colour())</code> → <code>elif</code> 树、火箭 → 每次最后 <code>x = x + 100</code>。</span><span class="en"><code>x = -300</code> → <code>for building in plan:</code> → <code>if building == "house": house(x, -150, 70, random_colour())</code> → <code>elif</code> tree, rocket → at the end of each loop <code>x = x + 100</code>.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week07-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week07-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面变成 ✅ 就交好了。</span><span class="en">Come back and refresh this page; when it shows ✅ you're done.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行：学会了什么 / 卡在哪里 / 怎么解决的。</span><span class="en">Write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what I learned / where I got stuck / how I fixed it.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>第一个<b>迷你项目</b>——石头剪刀布！大部分代码<b>你自己写</b>：三局两胜、五局三胜、胜率统计，还有一个会<b>偷偷学你出拳习惯</b>的电脑对手。你这周写的函数全都用得上。</span><span class="en">🔮 <b>Next week:</b> your first <b>mini project</b> — Rock Paper Scissors! <b>You write most of it</b>: best of 3, best of 5, win-rate stats, and a computer opponent that <b>secretly learns your habits</b>. Every kind of function you wrote this week will come in handy.</span></div>
