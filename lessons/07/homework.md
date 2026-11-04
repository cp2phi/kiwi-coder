---
title: 第 7 课 · 作业
title_en: Lesson 7 · Homework
lesson: "07"
tab: homework
playground: true
---

# 🏙️ <span class="zh">第 7 课作业：海龟城市规划师</span><span class="en">Lesson 7 homework: Turtle City Planner</span>

<p><span class="zh">你是城市规划师！用<b>函数</b>规划一座城：房子、树、太阳……<b>每种东西只写一次</b>。</span><span class="en">You're the city planner! Design a city with <b>functions</b>: houses, trees, a sun… <b>write each thing only once</b>.</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week07-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：house() 加屋顶 + 一条 4 座房子的街</span><span class="en">Must do: house() with a roof + a street of 4</span></h3>
    <p><span class="zh">画板里 <code>house(x, y, size, colour)</code> 已经画了身体。给它<b>加上屋顶</b>（学一学例 3 有），然后用 <code>for</code> 循环喊 4 次。<b>只用第 1–7 课学过的东西</b>。</span><span class="en">In the playground, <code>house(x, y, size, colour)</code> draws the body. <b>Add the roof</b> (see Learn, Example 3), then call it 4 times with a <code>for</code> loop. <b>Only Lesson 1–7 stuff needed</b>.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：tree(x, y)、sun(x, y, r) 和白天 / 黑夜</span><span class="en">Bonus: tree(x, y), sun(x, y, r) and day / night</span></h3>
    <p><span class="zh">写两个新招式 <code>tree</code> 和 <code>sun</code>。画板里有一个 <code>is_night</code> 变量：<b>True 的时候画月亮和黑夜</b>，False 画太阳和蓝天（用 <code>if</code>！）。</span><span class="en">Write two new tricks, <code>tree</code> and <code>sun</code>. There's an <code>is_night</code> variable: <b>when True draw a moon and night sky</b>, when False a sun and blue sky (use <code>if</code>!).</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：会「交回」随机颜色的招式 + 问 AI 学一招</span><span class="en">Challenge: a trick that returns a random colour + learn a trick from AI</span></h3>
    <p><span class="zh">写 <code>def random_colour():</code>，用 <code>return random.choice(列表)</code> 交回一个颜色，然后<b>每座房子都用它</b>——每次运行都不一样！再问 AI 一个提示（比如怎么画窗户或烟囱），把 AI 教的写进代码注释。</span><span class="en">Write <code>def random_colour():</code> that uses <code>return random.choice(list)</code>, then <b>use it for every house</b> — different every run! Then ask AI for one hint (e.g. windows or a chimney) and note what it taught you in a comment.</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>t.fillcolor("gold")</code><span><span class="zh">涂的颜色</span><span class="en">Fill colour</span></span></div>
  <div class="cmd"><code>t.begin_fill() … t.end_fill()</code><span><span class="zh">中间的图形涂满</span><span class="en">Fill the shape in between</span></span></div>
  <div class="cmd"><code>t.dot(20, "yellow")</code><span><span class="zh">画一个实心点（月亮、路灯）</span><span class="en">A filled dot (moon, lamp)</span></span></div>
  <div class="cmd"><code>random.choice(colours)</code><span><span class="zh">从列表里随机挑一个（第 5 课）</span><span class="en">Pick one at random (Lesson 5)</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上，关掉网页也不会丢。</span><span class="en">Your code is saved on this computer automatically, even if you close the page.</span></p>

<div class="playground" data-src="{{ '/lessons/07/code/homework.py' | relative_url }}" data-title="🏙️ 海龟城市规划师" data-title-en="🏙️ Turtle City Planner" data-save="week07-homework" data-draft="l7-homework" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 屋顶提示</span><span class="en">💡 Roof hint</span></summary><span class="zh">画完身体，海龟在左下角脸朝右。<code>t.penup()</code> → <code>t.goto(x, y + size)</code> → <code>t.pendown()</code> 到左上角，然后 forward(size)、left(120) 三次。最后一次 left(120) 让它转回朝右。</span><span class="en">After the body the turtle is at the bottom-left facing right. <code>t.penup()</code> → <code>t.goto(x, y + size)</code> → <code>t.pendown()</code> gets to the top-left, then forward(size), left(120) three times. The last left(120) turns it back to face right.</span></details>
<details class="hint"><summary><span class="zh">💡 树的提示</span><span class="en">💡 Tree hint</span></summary><span class="zh">学一学例 5 的 <code>tree(x, y)</code> 可以直接用，但试着<b>自己敲一遍</b>——树干是一条粗线，树叶是一个涂满的圆。</span><span class="en">You can reuse <code>tree(x, y)</code> from Learn Example 5, but try <b>typing it yourself</b> — the trunk is a thick line, the leaves are a filled circle.</span></details>
<details class="hint"><summary><span class="zh">💡 黑夜提示</span><span class="en">💡 Night hint</span></summary><span class="zh"><code>if is_night:</code> 下面画 <code>t.dot(50, "lightyellow")</code> 当月亮，<code>else:</code> 下面喊 <code>sun(200, 180, 40)</code>。</span><span class="en">Under <code>if is_night:</code> draw <code>t.dot(50, "lightyellow")</code> as the moon; under <code>else:</code> call <code>sun(200, 180, 40)</code>.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week07-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week07-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面变成 ✅ 就交好了。</span><span class="en">Come back and refresh this page; when it shows ✅ you're done.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行：学会了什么 / 卡在哪里 / 怎么解决的。</span><span class="en">Write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what I learned / where I got stuck / how I fixed it.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>第一个<b>迷你项目</b>——石头剪刀布！大部分代码<b>你自己写</b>，老师只给提示，AI 当排错伙伴。变量、if、random、while、列表、函数……全都要用上。</span><span class="en">🔮 <b>Next week:</b> your first <b>mini project</b> — Rock Paper Scissors! <b>You write most of it</b>, the teacher only hints, and AI is your debugging buddy. Variables, if, random, while, lists, functions… all of it.</span></div>
