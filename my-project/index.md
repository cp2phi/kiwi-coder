---
title: 我的项目
title_en: My Project
playground: true
# 👉 ④ 画板读 my-work 文件夹里的哪个文件？只改冒号后面的文件名，不要加引号。
#    第 11 课是 week11-project.py，第 12 课改成 week12-showcase.py
# 👉 ④ Which file in my-work should the playground load? Only change the name after the colon, no quotes.
project_file: week11-project.py
# 👉 三个太空任务（🚀 ☄️ 🛰️）都要画布，下一行不用管。只有「只用 print / input、没有画布」的项目，才把下一行开头的 # 和空格删掉
# 👉 All three space missions (🚀 ☄️ 🛰️) need the canvas: leave the next line alone. Only a print / input project with no canvas deletes the # and space at its start
# project_canvas: no
---
{% assign pf = page.project_file | default: 'week11-project.py' | strip %}
{% assign pf_end = pf | slice: -3, 3 %}
{% if pf_end != '.py' %}{% assign pf = pf | append: '.py' %}{% endif %}
{% assign pf_url = '/my-work/' | append: pf | relative_url %}
<!-- 👉 这是你的项目展示页！只改带 👉 的地方。改完点绿色的 Commit changes，等 1 分钟刷新。 -->
<!-- 👉 This is your project page! Only change the parts marked 👉. Commit, wait a minute, refresh. -->

<!-- 👉 ① 项目名字：把「（项目名字）」换掉，emoji 也可以换（🚀 ☄️ 🛰️ 🌕 …） -->
# 🚀 <span class="zh">（项目名字）</span><span class="en">(Project name)</span>

<p class="muted"><span class="zh">作者：{{ site.data.me.nickname }} · 用 Python 做的 · Kiwi Coder 第 10–12 课太空任务</span><span class="en">By {{ site.data.me.nickname }} · made with Python · Kiwi Coder Lessons 10–12 space mission</span></p>

<!-- 👉 ② 它是做什么的？用 2～3 句话说清楚（想想：给一个没见过它的人介绍） -->
<div class="box box-tip">
<span class="box-title"><span class="zh">🤔 它是做什么的？</span><span class="en">🤔 What does it do?</span></span>
<span class="zh">（在这里写：这是一个______。你可以______。灵感来自______。）</span>
<span class="en">(Write here: This is a ______. You can ______. It was inspired by ______.)</span>
</div>

<!-- 👉 ③ 怎么玩 / 怎么用：一步一步写，别人看了就会用 -->
## 🕹️ <span class="zh">怎么玩 / 怎么用</span><span class="en">How to play / use</span>

<ol class="steps">
  <li><span class="zh">点下面的 <b>▶ 运行</b>。</span><span class="en">Click <b>▶ Run</b> below.</span></li>
  <li><span class="zh">（🚀 / ☄️ 游戏：先点一下画布，然后按 ↑ ← → 键……）</span><span class="en">(🚀 / ☄️ game: click the canvas first, then press ↑ ← → …)</span></li>
  <li><span class="zh">（🛰️ 任务控制：在黄色输入框里输入 1、2 或 3，按回车；全部 GO 的话，点一下画布，按空格发射……）</span><span class="en">(🛰️ mission control: type 1, 2 or 3 in the yellow box and press Enter; if it's all GO, click the canvas and press space to launch…)</span></li>
</ol>

## ▶️ <span class="zh">来玩吧！</span><span class="en">Play it!</span>

<!-- ④ 画板读哪个文件，在这个文件最上面的 project_file: 那一行改，不在这里改 -->
<!-- ④ Change which file the playground loads in the project_file: line at the very top, not here -->
<div class="playground" data-src="{{ pf_url | escape }}" data-title="▶ 玩我的项目" data-title-en="▶ Play my project" data-save="week12-showcase" data-rows="16"{% if page.project_canvas == false or page.project_canvas == 'no' %} data-canvas="no"{% else %} data-images{% endif %}></div>

<div class="box box-warn"><span class="zh">⚠️ 如果上面写着「没找到代码文件」：说明 <code>my-work/</code> 里还没有 <code>{{ pf | escape }}</code>。两个办法：① 去作业画板点 <b>📤 存到作品墙</b>，名字用 <code>{{ pf | remove: '.py' | escape }}</code>；② 或者把这个文件最上面的 <code>project_file:</code> 改成作品墙上<b>真的有</b>的文件名。改好、等 1 分钟、刷新这一页。</span><span class="en">⚠️ If it says "code file not found": <code>my-work/</code> doesn't have <code>{{ pf | escape }}</code> yet. Two fixes: ① click <b>📤 Save to Gallery</b> on the homework playground and name it <code>{{ pf | remove: '.py' | escape }}</code>; or ② change <code>project_file:</code> at the very top of this file to a name that <b>really is</b> on your Gallery. Then wait a minute and refresh this page.</span></div>

<!-- 👉 ⑤ 可选：放一张截图。先把 PNG 上传到 my-work 文件夹（GitHub → my-work → Add file → Upload files），然后把下面那一行开头的「注释开始」和结尾的「注释结束」标记删掉，再改文件名 -->
<!-- <p><img src="{{ '/my-work/screenshot.png' | relative_url }}" alt="我的项目截图" style="max-width:420px;border-radius:14px;border:2px solid var(--line)"></p> -->

<!-- 👉 ⑥ 最骄傲的一行：从你的代码里挑一行（也可以是一个 assert 测试），说说为什么 -->
## 💎 <span class="zh">我最骄傲的一行代码</span><span class="en">The line I'm proudest of</span>

<pre>（把那一行代码粘贴到这里 / paste the line here）</pre>

<p><span class="zh">为什么：（因为它______ / 我花了______才弄对）</span><span class="en">Why: (because it ______ / it took me ______ to get right)</span></p>

<!-- 👉 ⑦ 我学到了：3 条 -->
## 🧠 <span class="zh">做这个项目我学到了</span><span class="en">What I learned making this</span>

<ul>
  <li><span class="zh">（比如：重力改速度，速度改位置）</span><span class="en">(e.g. gravity changes velocity, velocity changes position)</span></li>
  <li><span class="zh">（比如：先叫醒测试看它变红，再写函数让它变绿）</span><span class="en">(e.g. wake the test and watch it go red, then write the function to make it green)</span></li>
  <li><span class="zh">（比如：卡住了先读报错，再问 AI 要提示）</span><span class="en">(e.g. when stuck, read the error first, then ask AI for a hint)</span></li>
</ul>

<!-- 👉 ⑧ 最难的 bug：讲个故事 -->
## 🐞 <span class="zh">最难的 bug</span><span class="en">The hardest bug</span>

<p><span class="zh">（它是什么样的 → 我用了哪一招（print 侦探 / 读报错 / 小黄鸭 / 二分法）→ 原来是______）</span><span class="en">(What happened → which trick I used (print detective / read the error / rubber duck / halving) → it turned out ______)</span></p>

---

<p style="text-align:center"><a class="pg-btn run" style="text-decoration:none" href="{{ '/gallery/' | relative_url }}">🎨 <span class="zh">看我的其他作品</span><span class="en">See my other works</span></a> &nbsp; <a class="pg-btn" style="text-decoration:none" href="{{ '/' | relative_url }}">🏠 <span class="zh">回首页</span><span class="en">Home</span></a></p>
