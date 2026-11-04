---
title: 第 3 课 · 作业
title_en: Lesson 3 · Homework
lesson: "03"
tab: homework
playground: true
---

# 🏭 <span class="zh">第 3 课作业：万花筒工厂</span><span class="en">Lesson 3 homework: Kaleidoscope Factory</span>

<p><span class="zh">开一家工厂，让 for 循环替你干活！</span><span class="en">Open a factory where for loops do the work for you!</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week03-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：倒计时 + 我的多边形</span><span class="en">Must do: countdown + my polygon</span></h3>
    <p><span class="zh">① 用 <code>for</code> 和 <code>range(3, 0, -1)</code> 打印 3、2、1，再打印「开工！」。② 画板里已经有一个五边形，把 <code>sides</code> 改成<b>你喜欢的边数</b>，换个颜色。</span><span class="en">① Use <code>for</code> with <code>range(3, 0, -1)</code> to print 3, 2, 1, then "Go!". ② The playground has a pentagon — change <code>sides</code> to <b>your favourite number</b> and pick a colour.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：彩色螺旋，笔越来越粗</span><span class="en">Bonus: a colourful spiral with a growing pen</span></h3>
    <p><span class="zh">画一个螺旋，<b>至少 2 种颜色</b>轮流用（提示：<code>colors[i % 2]</code>），而且笔越来越粗：<code>t.pensize(i / 10)</code>。</span><span class="en">Draw a spiral with <b>at least 2 colours</b> taking turns (hint: <code>colors[i % 2]</code>) and a pen that gets thicker: <code>t.pensize(i / 10)</code>.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战（选做）：我设计的万花筒</span><span class="en">Challenge (optional): my own kaleidoscope</span></h3>
    <p><span class="zh">用<b>循环里面有循环</b>设计一个你自己的图案（里面可以是三角形、圆、星星……）。然后问 AI「请解释第 __ 行」，把它的解释写成一行注释。</span><span class="en">Design your own pattern with <b>a loop inside a loop</b> (the inner shape can be a triangle, circle, star…). Then ask AI "explain line __" and write its answer as a comment.</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>for i in range(3, 0, -1):</code><span><span class="zh">倒着数 3、2、1</span><span class="en">Count down 3, 2, 1</span></span></div>
  <div class="cmd"><code>t.pensize(i / 10)</code><span><span class="zh">笔的粗细跟着 i 变</span><span class="en">Pen thickness follows i</span></span></div>
  <div class="cmd"><code>colors[i % 2]</code><span><span class="zh">两种颜色轮流（列表里放 2 个颜色）</span><span class="en">Two colours in turn (put 2 colours in the list)</span></span></div>
  <div class="cmd"><code>t.circle(50)</code><span><span class="zh">里面的循环也可以画圆</span><span class="en">The inner loop can draw circles too</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。每做完一个 TODO 就运行一次。</span><span class="en">Your code is saved on this computer automatically. Run after every TODO.</span></p>

<div class="playground" data-src="{{ '/lessons/03/code/homework.py' | relative_url }}" data-title="🏭 万花筒工厂" data-title-en="🏭 Kaleidoscope Factory" data-save="week03-homework" data-draft="l3-homework" data-rows="14"></div>

<details class="hint"><summary><span class="zh">💡 倒计时提示</span><span class="en">💡 Countdown hint</span></summary><span class="zh">和课上的 <code>range(5, 0, -1)</code> 一样，只是从 3 开始。<code>print("开工！")</code> 要写在循环<b>外面</b>（不缩进），不然会打印 3 次。</span><span class="en">Same as <code>range(5, 0, -1)</code> in class, but starting at 3. <code>print("Go!")</code> goes <b>outside</b> the loop (no indent), or it prints 3 times.</span></details>
<details class="hint"><summary><span class="zh">💡 螺旋提示</span><span class="en">💡 Spiral hint</span></summary><span class="zh">把课上例 3 的螺旋复制过来，列表改成 <code>colors = ["red", "gold"]</code>，循环里加 <code>t.pensize(i / 10)</code>。记得先 <code>t.penup()</code> 跳到别的地方再画，不然会和多边形叠在一起。</span><span class="en">Copy the spiral from Example 3, change the list to <code>colors = ["red", "gold"]</code>, and add <code>t.pensize(i / 10)</code> inside the loop. <code>t.penup()</code> and jump somewhere else first, or it draws over the polygon.</span></details>
<details class="hint"><summary><span class="zh">💡 万花筒提示</span><span class="en">💡 Kaleidoscope hint</span></summary><span class="zh">外面 <code>for i in range(次数):</code>，里面画一个形状，然后 <code>t.left(360 / 次数)</code>。里面的形状如果是圆，只要一行 <code>t.circle(60)</code>。</span><span class="en">Outer <code>for i in range(times):</code>, draw one shape inside, then <code>t.left(360 / times)</code>. If the inner shape is a circle, it's just one line: <code>t.circle(60)</code>.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week03-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week03-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行：学会了什么 / 卡在哪里 / 怎么解决的。</span><span class="en">Write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what I learned / where I got stuck / how I fixed it.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>程序要学会<b>自己做决定</b>了——「如果猜对了就庆祝，不然就再猜」。我们要做一个<b>猜数字游戏</b>！想一想：你希望电脑怎么提示你猜大了还是猜小了？</span><span class="en">🔮 <b>Next week:</b> programs learn to <b>make decisions</b> — "if the guess is right, celebrate, otherwise guess again". We'll build a <b>guess-the-number game</b>! Think: how should the computer hint that you're too high or too low?</span></div>
