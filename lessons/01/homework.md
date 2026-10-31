---
title: 第 1 课 · 作业
title_en: Lesson 1 · Homework
lesson: "01"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 1 课作业：海龟建筑师</span><span class="en">Lesson 1 homework: Turtle Builder</span>

<p><span class="zh">用海龟画一座<b>你的房子</b>！</span><span class="en">Use the turtle to draw <b>your house</b>!</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

{% assign hw = site.static_files | where: "path", "/my-work/week01-homework.py" | first %}
{% if hw %}
<div class="box box-good"><span class="zh">✅ <b>作业已经交啦！</b>点下面的 ▶ 运行看看。</span><span class="en">✅ <b>Homework handed in!</b> Click ▶ Run below to see it.</span></div>
{% else %}
<div class="box box-warn"><span class="zh">⏳ <b>还没交</b>：做完后按最下面的步骤提交，这里会变成 ✅。</span><span class="en">⏳ <b>Not handed in yet</b>: when you're done, follow the steps at the bottom and this turns into ✅.</span></div>
{% endif %}

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：加屋顶</span><span class="en">Must do: add a roof</span></h3>
    <p><span class="zh">画板里已经有正方形的房子了，在它<b>上面</b>加一个<b>三角形屋顶</b>。</span><span class="en">The square house is already in the playground. Add a <b>triangle roof</b> <b>on top</b> of it.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：涂颜色 + 太阳</span><span class="en">Bonus: colour it in + a sun</span></h3>
    <p><span class="zh">用下面的「新指令」给房子<b>涂满颜色</b>，再画一个<b>太阳</b>。这些指令课上没教，<b>自己试一试</b>它们是干嘛的！</span><span class="en">Use the "new commands" below to <b>fill the house with colour</b> and draw a <b>sun</b>. We didn't learn these in class — <b>try them out</b> and discover what they do!</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战（选做）：问 AI 学一招</span><span class="en">Challenge (optional): learn a trick from AI</span></h3>
    <p><span class="zh">问 Codex 要一个<b>提示</b>，学会一个新指令用到画里（比如在画上写字）。在代码里写一行注释：AI 教了我什么。</span><span class="en">Ask Codex for a <b>hint</b> and learn a new command to use in your drawing (like writing words on it). Add a comment in your code: what AI taught me.</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>t.circle(50)</code><span><span class="zh">画一个圆</span><span class="en">Draw a circle</span></span></div>
  <div class="cmd"><code>t.begin_fill()</code> … <code>t.end_fill()</code><span><span class="zh">中间画的图形会被涂满</span><span class="en">Shapes drawn in between get filled in</span></span></div>
  <div class="cmd"><code>t.fillcolor("yellow")</code><span><span class="zh">涂什么颜色</span><span class="en">The fill colour</span></span></div>
  <div class="cmd"><code>t.penup()</code> <code>t.goto(150, 200)</code> <code>t.pendown()</code><span><span class="zh">抬笔 → 走到某个地方 → 落笔</span><span class="en">Lift the pen → move somewhere → put the pen down</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上，关掉网页也不会丢。</span><span class="en">Your code is saved on this computer automatically, even if you close the page.</span></p>

<div class="playground" data-src="{% if hw %}{{ '/my-work/week01-homework.py' | relative_url }}{% else %}{{ '/lessons/01/code/homework.py' | relative_url }}{% endif %}" data-title="🏠 海龟建筑师" data-title-en="🏠 Turtle Builder" data-save="week01-homework" data-draft="l1-homework"></div>

<details class="hint"><summary><span class="zh">💡 屋顶提示 1</span><span class="en">💡 Roof hint 1</span></summary><span class="zh">画完正方形，海龟回到了<b>左下角</b>，脸朝<b>右</b>。屋顶要从<b>左上角</b>开始画。</span><span class="en">After the square, the turtle is back at the <b>bottom left</b>, facing <b>right</b>. The roof starts at the <b>top left</b>.</span></details>
<details class="hint"><summary><span class="zh">💡 屋顶提示 2</span><span class="en">💡 Roof hint 2</span></summary><span class="zh">先 <code>left(90)</code> 再 <code>forward(150)</code> 就到左上角了，但这时脸朝上——要先转回朝右，再画三角形。</span><span class="en"><code>left(90)</code> then <code>forward(150)</code> gets you to the top left — but now the turtle faces up. Turn it back to face right, then draw the triangle.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week01-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week01-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行：学会了什么 / 卡在哪里 / 怎么解决的。</span><span class="en">Write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what I learned / where I got stuck / how I fixed it.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>我们要做一个<b>会聊天的程序</b>。想一想：你希望电脑问你什么问题？</span><span class="en">🔮 <b>Next week:</b> we'll make a <b>program that chats</b>. Think: what questions would you like the computer to ask you?</span></div>
