---
title: 第 1 课 · 作业
lesson: "01"
tab: homework
playground: true
---

# 🏠 第 1 课作业：海龟建筑师

用海龟画一座**你的房子**！<span class="pill">⏱ 大约 30 分钟</span> <span class="pill pill-brand">📅 下节课前交</span>

{% assign hw = site.static_files | where: "path", "/my-work/week01-homework.py" | first %}
{% if hw %}
<div class="box box-good">✅ <b>作业已经交啦！</b>点下面的 ▶ 运行看看。</div>
{% else %}
<div class="box box-warn">⏳ <b>还没交</b>：做完后按最下面的步骤提交，这里会变成 ✅。</div>
{% endif %}

## 🎖️ 三个等级

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3>必做：加屋顶</h3>
    <p>画板里已经有正方形的房子了，在它<b>上面</b>加一个<b>三角形屋顶</b>。</p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3>加分：涂颜色 + 太阳</h3>
    <p>用下面的「新指令」给房子<b>涂满颜色</b>，再画一个<b>太阳</b>。这些指令课上没教，<b>自己试一试</b>它们是干嘛的！</p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3>挑战（选做）：问 AI 学一招</h3>
    <p>问 Codex 要一个<b>提示</b>，学会一个新指令用到画里（比如在画上写字）。在代码里写一行注释：AI 教了我什么。</p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>t.circle(50)</code><span>画一个圆</span></div>
  <div class="cmd"><code>t.begin_fill()</code> … <code>t.end_fill()</code><span>中间画的图形会被涂满</span></div>
  <div class="cmd"><code>t.fillcolor("yellow")</code><span>涂什么颜色</span></div>
  <div class="cmd"><code>t.penup()</code> <code>t.goto(150, 200)</code> <code>t.pendown()</code><span>抬笔 → 走到某个地方 → 落笔</span></div>
</div>

## 🧪 作业画板

<p class="muted">写的代码会自动记在这台电脑上，关掉网页也不会丢。</p>

<div class="playground" data-src="{% if hw %}{{ '/my-work/week01-homework.py' | relative_url }}{% else %}{{ '/lessons/01/code/homework.py' | relative_url }}{% endif %}" data-title="🏠 海龟建筑师" data-save="week01-homework" data-draft="l1-homework"></div>

<details class="hint"><summary>💡 屋顶提示 1</summary>画完正方形，海龟回到了<b>左下角</b>，脸朝<b>右</b>。屋顶要从<b>左上角</b>开始画。</details>
<details class="hint"><summary>💡 屋顶提示 2</summary>先 <code>left(90)</code> 再 <code>forward(150)</code> 就到左上角了，但这时脸朝上——要先转回朝右，再画三角形。</details>

## 📤 怎么交

<ol class="steps">
  <li>在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week01-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</li>
  <li>在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行：学会了什么 / 卡在哪里 / 怎么解决的。</li>
</ol>

<div class="box box-think">🔮 <b>下周预告：</b>我们要做一个<b>会聊天的程序</b>。想一想：你希望电脑问你什么问题？</div>
