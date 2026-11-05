---
title: 第 12 课 · 学一学
title_en: Lesson 12 · Learn
lesson: "12"
tab: learn
playground: true
---

# 🏆 <span class="zh">第 12 课：上线、展示、回头看、往前看</span><span class="en">Lesson 12: go live, show it, look back, look ahead</span>

<p class="zh">程序员做完一个东西，最后一步叫<b>部署</b>（deploy）：把它放到网上，让别人用得到。今天你也要做这件事。然后我们一起回头看 12 周，再给你发证书 🎓。</p>
<p class="en">The last step of any programmer's project is called <b>deploying</b>: putting it online so other people can use it. Today you'll do exactly that. Then we'll look back over 12 weeks, and you'll get your certificate 🎓.</p>

---

## ✨ <span class="zh">先打磨：给项目一个「门面」</span><span class="en">First, polish: give your project a front door</span>
{: #polish}

<p><span class="zh">别人第一次打开你的项目，要马上知道<b>这是什么</b>、<b>怎么玩</b>。给它加一个标题画面（游戏 / 艺术）或者开场横幅（app）。</span><span class="en">When someone opens your project for the first time, they should instantly know <b>what it is</b> and <b>how to play</b>. Add a title screen (game / art) or an opening banner (app).</span></p>

<div class="two">
<div>
<div class="playground" data-src="{{ '/lessons/12/code/polish.py' | relative_url }}" data-title="✨ 标题画面（游戏 / 艺术）" data-title-en="✨ Title screen (game / art)" data-save="title-screen" data-draft="l12-polish" data-rows="12"></div>
</div>
<div>
<div class="playground" data-src="{{ '/lessons/12/code/banner.py' | relative_url }}" data-canvas="no" data-title="📢 开场横幅（app）" data-title-en="📢 Opening banner (app)" data-save="banner" data-draft="l12-banner" data-rows="12"></div>
</div>
</div>

<ul class="quests" data-key="l12-polish">
  <li><span class="zh">把 <code>___</code> 换成你的项目名和昵称，运行。</span><span class="en">Replace <code>___</code> with your project name and nickname, run it.</span></li>
  <li><span class="zh">把这几行<b>复制到你项目的最前面</b>（在 <a href="../homework/">作业画板</a>里）。标题用的是一只新海龟 <code>title_pen</code>，不会和你的 <code>pen</code>、角色撞名；最后一行 <code>screen.ontimer(title_pen.clear, 3000)</code> 让标题 3 秒后自己消失。改成 5000 试试？</span><span class="en">Copy these lines to the <b>top of your project</b> (in the <a href="../homework/">homework playground</a>). The title uses a new turtle, <code>title_pen</code>, so it won't clash with your <code>pen</code> or characters; the last line, <code>screen.ontimer(title_pen.clear, 3000)</code>, wipes the title after 3 seconds. Try 5000?</span></li>
  <li><span class="zh">把第 11 课留下的「侦探 print」删掉。从头运行一次，没有红字。</span><span class="en">Delete the "detective prints" left over from Lesson 11. Run from scratch, no red text.</span></li>
</ul>

<p class="muted" style="font-size:.9rem"><span class="zh">字体格式是 <code>("Arial", 大小, "bold" 或 "normal")</code>；<code>align="center"</code> 让字居中。</span><span class="en">The font is <code>("Arial", size, "bold" or "normal")</code>; <code>align="center"</code> centres the text.</span></p>

---

## 🚀 <span class="zh">什么是部署？</span><span class="en">What is deploying?</span>
{: #deploy}

<p><span class="zh">你早就在做了！还记得第 1 课改名片吗？<b>你现在看的这个网站，就是 GitHub 从你的仓库「部署」出来的。</b></span><span class="en">You've been doing it since day one! Remember editing your name card in Lesson 1? <b>This very website is "deployed" by GitHub from your repository.</b></span></p>

<div class="flow">
  <div class="f"><span class="e">✏️</span><b><span class="zh">改文件</span><span class="en">Edit a file</span></b><small><span class="zh">在 GitHub 上</span><span class="en">on GitHub</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">💾</span><b>Commit</b><small><span class="zh">存档 + 一句说明</span><span class="en">save + a note</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🤖</span><b>Actions</b><small><span class="zh">GitHub 的机器人把文件变成网页（转圈 1 分钟）</span><span class="en">GitHub's robot turns files into pages (spins for a minute)</span></small></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🌐</span><b><span class="zh">网站更新</span><span class="en">Site updated</span></b><small><span class="zh">全世界都能打开</span><span class="en">anyone can open it</span></small></div>
</div>

<div class="quiz" data-answer="3">
  <p class="q"><span class="zh">你手机上的游戏「更新了」，其实发生了什么？</span><span class="en">A game on your phone "got an update". What actually happened?</span></p>
  <div class="opts"><button><span class="zh">手机自己变聪明了</span><span class="en">The phone got smarter</span></button><button><span class="zh">有人来家里换了手机</span><span class="en">Someone swapped the phone</span></button><button><span class="zh">程序员改了代码 → 测试 → 部署了新版本，你的手机下载了它</span><span class="en">Programmers changed the code → tested → deployed a new version, and your phone downloaded it</span></button></div>
  <div class="why"><span class="zh">和你一样！程序员每天都在「改 → 测 → 部署」。大公司一天部署几百次。你今天做的事，和他们是同一件事。</span><span class="en">Same as you! Programmers "change → test → deploy" every day. Big companies deploy hundreds of times a day. What you're doing today is the very same thing.</span></div>
</div>

<div class="box box-tip"><span class="zh">📖 <b>部署前的检查清单</b>（程序员叫它 pre-flight check，像飞机起飞前）：① 从头运行没有红字 ② <code>test()</code> ✅ ③ 第一行注释有标题和作者 ④ 存到作品墙了 ⑤ 🔒 <b>没有个人信息</b>：网站是公开的，名片 <code>_data/me.yml</code>、笔记本、代码、截图里都不能有真名、学校、照片、地址。</span><span class="en">📖 <b>Pre-deploy checklist</b> (programmers call it a pre-flight check, like before a plane takes off): ① runs from scratch with no red text ② <code>test()</code> ✅ ③ first comment has title and author ④ saved to the gallery ⑤ 🔒 <b>no personal info</b>: the site is public, so no real name, school, photo or address in your name card <code>_data/me.yml</code>, notebook, code or screenshots.</span></div>

---

## 🌐 <span class="zh">做我的项目页，然后上线</span><span class="en">Build my project page and go live</span>
{: #page}

<p><span class="zh">仓库里有一个专门给你的页面：<a href="{{ '/my-project/' | relative_url }}" target="_blank" rel="noopener"><b>my-project</b></a>。现在它还是模板，你来把它填成自己的。</span><span class="en">There's a page in the repo just for you: <a href="{{ '/my-project/' | relative_url }}" target="_blank" rel="noopener"><b>my-project</b></a>. Right now it's a template — make it yours.</span></p>

<div class="box box-good"><span class="zh">⏱️ <b>课上只做「上线」这一小步</b>：存展示版 → 改一行 <code>project_file</code> → Commit → 打开链接。名字、介绍、最骄傲的一行这些<b>文字</b>（①②③⑥⑦⑧）回家慢慢写，是<a href="../homework/">毕业作业</a>的一部分。</span><span class="en">⏱️ <b>In class, only do the "go live" step</b>: save the showcase → change one line, <code>project_file</code> → Commit → open the link. The <b>words</b> — name, description, proudest line (①②③⑥⑦⑧) — you write at home as part of the <a href="../homework/">graduation homework</a>.</span></div>

<ol class="steps">
  <li><strong><span class="zh">先存展示版</span><span class="en">Save the showcase version first</span></strong><br><span class="zh">在 <a href="../homework/">作业画板</a>点 <b>📤 存到作品墙</b>，名字 <code>week12-showcase</code>，Commit。</span><span class="en">On the <a href="../homework/">homework playground</a> click <b>📤 Save to Gallery</b>, name it <code>week12-showcase</code>, Commit.</span></li>
  <li><strong><span class="zh">打开模板文件</span><span class="en">Open the template file</span></strong><br><a href="https://github.com/{{ site.github_repo }}/edit/{{ site.github_branch }}/my-project/index.md" target="_blank" rel="noopener"><span class="zh">点这里直接编辑 my-project/index.md</span><span class="en">click here to edit my-project/index.md</span></a><span class="zh">。文件里所有 <code>👉</code> 注释都在告诉你改哪里。</span><span class="en">. Every <code>👉</code> comment in the file tells you what to change.</span></li>
  <li><strong><span class="zh">改 ④：画板读哪个文件</span><span class="en">Change ④: which file the playground loads</span></strong><br><span class="zh">在文件<b>最上面</b>找到 <code>project_file: week11-project.py</code>，只把冒号后面的名字改成 <code>week12-showcase.py</code>（要和作品墙上的<b>一模一样</b>，不要加引号）。做的是文字 app？再把下面 <code># project_canvas: no</code> 开头的 <code>#</code> 和空格删掉，页面就不显示画布。</span><span class="en">At the <b>very top</b> of the file, find <code>project_file: week11-project.py</code> and change only the name after the colon to <code>week12-showcase.py</code> (it must match the gallery <b>exactly</b>; no quotes). Made a text app? Also delete the <code>#</code> and space at the start of <code># project_canvas: no</code> below it, so the page shows no canvas.</span></li>
  <li><strong>Commit changes</strong><br><span class="zh">说明写「我的项目页上线！」。然后去仓库的 <a href="https://github.com/{{ site.github_repo }}/actions" target="_blank" rel="noopener"><b>Actions</b></a> 看机器人转圈 → 变绿 ✅。</span><span class="en">Write "my project page is live!" as the note. Then watch the robot spin under <a href="https://github.com/{{ site.github_repo }}/actions" target="_blank" rel="noopener"><b>Actions</b></a> → green ✅.</span></li>
  <li><strong><span class="zh">打开链接，自己玩一次</span><span class="en">Open the link and play it yourself</span></strong><br><a href="{{ '/my-project/' | relative_url }}" target="_blank" rel="noopener">{{ site.url }}{{ site.baseurl }}/my-project/</a><span class="zh">。能玩 = <b>部署成功</b> 🎉。把这个链接发给家人！键盘游戏请他们<b>用电脑打开</b>——手机没有方向键。</span><span class="en">. It plays = <b>deployed</b> 🎉. Send the link to your family! For a keyboard game, ask them to <b>open it on a computer</b> — phones have no arrow keys.</span></li>
  <li><strong><span class="zh">🏠 回家再做：改 ①②③⑥⑦⑧</span><span class="en">🏠 At home: change ①②③⑥⑦⑧</span></strong><br><span class="zh">名字、是做什么的、怎么玩、最骄傲的一行、学到了、最难的 bug。只改 <code>&lt;span class="zh"&gt;</code> 和 <code>&lt;span class="en"&gt;</code> 里面的字，别动标签。英文不会写就先写中文，或者问 AI 帮你翻译（这是 AI 的好用法！）。翻翻你的<a href="{{ '/notebook/' | relative_url }}">笔记本</a>，第 10–11 课写了什么。</span><span class="en">Name, what it does, how to play, proudest line, what I learned, hardest bug. Only change the words inside <code>&lt;span class="zh"&gt;</code> and <code>&lt;span class="en"&gt;</code>; leave the tags. Can't write the English? Write Chinese first, or ask AI to translate (a great use of AI!). Check your <a href="{{ '/notebook/' | relative_url }}">notebook</a> for Lessons 10–11.</span></li>
</ol>

<div class="box box-warn"><span class="box-title"><span class="zh">🚑 Actions 出现红色 ❌？网站没更新？</span><span class="en">🚑 Red ❌ in Actions? Site not updating?</span></span>
<span class="zh">别慌，每一次 commit 都是一个存档，可以回去：① 打开 <a href="https://github.com/{{ site.github_repo }}/commits/{{ site.github_branch }}/my-project/index.md" target="_blank" rel="noopener">my-project/index.md 的 History（历史）</a>；② 找到<b>最后一个好的版本</b>（你这次 commit 下面那一个），点右边的 <b>&lt;&gt;</b>（看那时候的仓库）→ 点进 <code>my-project</code> → <code>index.md</code>；③ 把那一版的内容全部复制，回到 ✏️ 编辑页全部粘贴覆盖，Commit。或者请家长帮你 <b>revert</b>（撤回）那次 commit。</span>
<span class="en">Don't panic — every commit is a save point you can go back to: ① open <a href="https://github.com/{{ site.github_repo }}/commits/{{ site.github_branch }}/my-project/index.md" target="_blank" rel="noopener">the History of my-project/index.md</a>; ② find the <b>last good version</b> (the one just below your latest commit) and click <b>&lt;&gt;</b> on the right (the repo at that moment) → open <code>my-project</code> → <code>index.md</code>; ③ copy all of it, go back to the ✏️ edit page, paste over everything, Commit. Or ask a parent to <b>revert</b> that commit.</span>
</div>

<ul class="quests" data-key="l12-history">
  <li>🕰️ <span class="zh"><b>时光机任务</b>：在 GitHub 打开 <a href="https://github.com/{{ site.github_repo }}/commits/{{ site.github_branch }}/my-project/index.md" target="_blank" rel="noopener">my-project/index.md 的 History</a> → 找到你刚才那次 commit（就是你写的那句说明）→ 点开它，看看改了什么（绿色 = 加的，红色 = 删的）→ 再点它下面那一次右边的 <b>&lt;&gt;</b>，进 <code>my-project/index.md</code>，看看<b>上一版</b>长什么样。程序员管这个叫「版本控制」：改坏了也能回到过去。</span><span class="en"><b>Time-machine quest</b>: on GitHub open <a href="https://github.com/{{ site.github_repo }}/commits/{{ site.github_branch }}/my-project/index.md" target="_blank" rel="noopener">the History of my-project/index.md</a> → find the commit you just made (the note you wrote) → open it and see what changed (green = added, red = removed) → then click <b>&lt;&gt;</b> on the right of the one below it and open <code>my-project/index.md</code> to see the <b>previous version</b>. Programmers call this "version control": even if you break something, you can go back in time.</span></li>
</ul>

<details class="hint"><summary><span class="zh">💡 可选：加一张截图</span><span class="en">💡 Optional: add a screenshot</span></summary><span class="zh">① 运行你的项目，用电脑截图（Mac：⌘⇧4，Windows：Win+Shift+S），<b>只截画板那一块</b>：截图里不能有真名、学校、浏览器上的头像或账号名。② <b>先在电脑上</b>把截图文件改名为 <code>screenshot.png</code>（GitHub 上传的时候不能改名）。③ 在 GitHub 打开 <code>my-work</code> 文件夹 → Add file → Upload files → 拖进去 → Commit。④ 在 index.md 里按 ⑤ 的注释打开那一行。</span><span class="en">① Run your project and take a screenshot (Mac: ⌘⇧4, Windows: Win+Shift+S) of <b>just the playground</b>: no real name, school, or browser profile picture / account name in it. ② <b>On your computer first</b>, rename the file to <code>screenshot.png</code> (GitHub can't rename files while uploading). ③ On GitHub open the <code>my-work</code> folder → Add file → Upload files → drop it in → Commit. ④ Enable the line marked ⑤ in index.md.</span></details>
<details class="hint"><summary><span class="zh">💡 页面写着「没找到代码文件」？</span><span class="en">💡 Page says "code file not found"?</span></summary><span class="zh">网站不会坏，只是画板找不到文件。三个可能：① 还没存 <code>week12-showcase</code>；② <code>project_file:</code> 里的名字拼得不一样（大小写、横线）；③ 刚 commit，机器人还在转圈，等 1 分钟刷新。</span><span class="en">The site isn't broken — the playground just can't find the file. Three possibilities: ① you haven't saved <code>week12-showcase</code> yet; ② the name in <code>project_file:</code> is spelled differently (case, dashes); ③ you just committed and the robot is still spinning — wait a minute and refresh.</span></details>

---

## 🎤 <span class="zh">展示：3 分钟讲清楚</span><span class="en">Show time: explain it in 3 minutes</span>
{: #show}

<p><span class="zh">讲出来 = 真的学会了。用下面的稿子，照着说，每段 30–45 秒。</span><span class="en">Explaining it = really knowing it. Use the script below; 30–45 seconds per part.</span></p>

<div class="card">
<ol class="steps">
  <li><strong>🎯 <span class="zh">这是什么</span><span class="en">What it is</span></strong><br><span class="zh">「这是一个______。我做它是因为______。」</span><span class="en">"This is a ______. I made it because ______."</span></li>
  <li><strong>🕹️ <span class="zh">怎么玩（边玩边讲）</span><span class="en">How to play (demo while talking)</span></strong><br><span class="zh">「先______，然后______。看，______！」——<b>让观众自己玩 1 分钟。</b></span><span class="en">"First ______, then ______. Look, ______!" — <b>let the audience play for a minute.</b></span></li>
  <li><strong>🐞 <span class="zh">最难的 bug</span><span class="en">The hardest bug</span></strong><br><span class="zh">「有一次它______。我用了______（print 侦探 / 读报错 / 小黄鸭 / 二分法），发现原来是______。」</span><span class="en">"Once it ______. I used ______ (print detective / reading the error / rubber duck / halving) and found it was ______."</span></li>
  <li><strong>🧠 <span class="zh">我学到了</span><span class="en">What I learned</span></strong><br><span class="zh">「做这个我学会了______。下次我想______。」</span><span class="en">"Making this I learned ______. Next time I want to ______."</span></li>
</ol>
</div>

<div class="box box-tip"><span class="box-title"><span class="zh">👨‍👩‍👧 给观众的问题卡（家人请念）</span><span class="en">👨‍👩‍👧 Question cards for the audience (family, read these)</span></span>
<span class="zh">· 「如果我按两个键会怎样？」 · 「这一行代码是干嘛的？」（随便指一行）· 「你第一次做坏的时候怎么办的？」 · 「AI 帮了你什么？你怎么知道它说得对？」 · 「如果再有 1 小时，你会加什么？」</span>
<span class="en">· "What happens if I press two keys?" · "What does this line do?" (point at any line) · "What did you do the first time it broke?" · "How did AI help, and how did you know it was right?" · "With one more hour, what would you add?"</span>
</div>

---

## 🔭 <span class="zh">回头看：12 周走了多远</span><span class="en">Look back: how far in 12 weeks</span>
{: #review}

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">12 周前，在第 1 课的名片上，你写过「我觉得 AI 是……」。现在你会怎么说？</span><span class="en">12 weeks ago on your name card you wrote "I think AI is…". What would you say now?</span></p>
  <div class="opts"><button><span class="zh">一个什么都知道、从不出错的机器人</span><span class="en">A robot that knows everything and never errs</span></button><button><span class="zh">一个从例子里学习、会犯错、要我检查的学习伙伴</span><span class="en">A learning buddy that learns from examples, makes mistakes, and needs me to check</span></button><button><span class="zh">能替我写所有代码的工具</span><span class="en">A tool that writes all my code for me</span></button></div>
  <div class="why"><span class="zh">第 6 课你亲手训练过它（例子不好它就学不好），第 9 课你抓到过它编造。它很厉害，但<b>你是队长</b>。去首页把名片上的 <code>ai_is</code> 改成现在的想法吧！</span><span class="en">In Lesson 6 you trained one yourself (bad examples → bad learning); in Lesson 9 you caught it making things up. It's powerful, but <b>you're the captain</b>. Go update <code>ai_is</code> on your name card!</span></div>
</div>

<p><span class="zh">先用数字看看这 12 周：</span><span class="en">First, your 12 weeks in numbers:</span></p>

<div class="playground" data-src="{{ '/lessons/12/code/numbers.py' | relative_url }}" data-canvas="no" data-title="📊 我的 12 周" data-title-en="📊 My 12 weeks" data-save="my-12-weeks" data-draft="l12-numbers" data-rows="14"></div>

<h3>🐍 <span class="zh">我学会的 Python：自我检查</span><span class="en">The Python I know: self-check</span></h3>

<p><span class="zh">每一条，<b>不看词典</b>能写出一个例子就打勾。打不了勾的，就是你下一步要复习的——这不是考试，是地图。</span><span class="en">Tick each one you could write an example of <b>without the cheat sheet</b>. The ones you can't tick are your next review — this isn't a test, it's a map.</span></p>

<div class="progress" data-for="l12-skills"><span></span></div>
<ul class="quests" data-key="l12-skills">
  <li>🐢 <span class="zh"><b>第 1 课</b> <code>print()</code>、<code>import turtle</code>、让海龟走和转</span><span class="en"><b>L1</b> <code>print()</code>, <code>import turtle</code>, move and turn the turtle</span></li>
  <li>💬 <span class="zh"><b>第 2 课</b> 变量、<code>input()</code>、<code>f"…{x}…"</code>、<code>int()</code></span><span class="en"><b>L2</b> variables, <code>input()</code>, <code>f"…{x}…"</code>, <code>int()</code></span></li>
  <li>🌀 <span class="zh"><b>第 3 课</b> <code>for i in range(10):</code> 和缩进</span><span class="en"><b>L3</b> <code>for i in range(10):</code> and indentation</span></li>
  <li>🎲 <span class="zh"><b>第 4 课</b> <code>if / elif / else</code>、<code>==  &lt;  &gt;</code>、<code>random.randint()</code></span><span class="en"><b>L4</b> <code>if / elif / else</code>, <code>==  &lt;  &gt;</code>, <code>random.randint()</code></span></li>
  <li>🎰 <span class="zh"><b>第 5 课</b> 列表 <code>[ ]</code>、<code>[0]</code>、<code>append()</code>、<code>random.choice()</code></span><span class="en"><b>L5</b> lists <code>[ ]</code>, <code>[0]</code>, <code>append()</code>, <code>random.choice()</code></span></li>
  <li>🧠 <span class="zh"><b>第 6 课</b> <code>while</code>、<code>True / False</code>、<code>and / or / not</code></span><span class="en"><b>L6</b> <code>while</code>, <code>True / False</code>, <code>and / or / not</code></span></li>
  <li>📦 <span class="zh"><b>第 7 课</b> <code>def 名字(参数):</code> 和 <code>return</code></span><span class="en"><b>L7</b> <code>def name(params):</code> and <code>return</code></span></li>
  <li>✊ <span class="zh"><b>第 8 课</b> <code>.lower()</code>、<code>.strip()</code>，把所有东西合在一起</span><span class="en"><b>L8</b> <code>.lower()</code>, <code>.strip()</code>, putting it all together</span></li>
  <li>🕵️ <span class="zh"><b>第 9 课</b> 字典 <code>{"键": 值}</code>、<code>in</code>、<code>.get()</code></span><span class="en"><b>L9</b> dictionaries <code>{"key": value}</code>, <code>in</code>, <code>.get()</code></span></li>
  <li>🗺️ <span class="zh"><b>第 10 课</b> 看懂别人的代码、<code>assert</code> 测试、把项目拆小</span><span class="en"><b>L10</b> reading others' code, <code>assert</code> tests, splitting a project</span></li>
  <li>🛠️ <span class="zh"><b>第 11 课</b> 四招排错、<code>onkey</code> / <code>ontimer</code> / <code>onclick</code>、<code>global</code></span><span class="en"><b>L11</b> 4 debugging tricks, <code>onkey</code> / <code>ontimer</code> / <code>onclick</code>, <code>global</code></span></li>
  <li>🏆 <span class="zh"><b>第 12 课</b> 部署：改文件 → commit → 网站更新</span><span class="en"><b>L12</b> deploy: edit → commit → site updates</span></li>
</ul>

<p class="muted"><span class="zh">翻翻你的<a href="{{ '/notebook/' | relative_url }}">笔记本</a>：12 页「我卡在哪里 / 怎么解决的」——这就是你自己写的「钓鱼手册」。</span><span class="en">Flip through your <a href="{{ '/notebook/' | relative_url }}">notebook</a>: 12 pages of "where I got stuck / how I fixed it" — that's the fishing handbook you wrote yourself.</span></p>

---

## 🎓 <span class="zh">毕业证书</span><span class="en">Certificate</span>
{: #certificate}

<p><span class="zh">亮着的徽章是你在这台电脑上完成过的课（全部打勾的那些）。点 <b>🖨️ 打印</b> 可以打印出来贴墙上。</span><span class="en">Lit badges are lessons you completed on this computer (checklists fully ticked). Click <b>🖨️ Print</b> to print it for the wall.</span></p>

<div class="certificate" id="cert">
  <div class="stamp">🎓🥝🐢</div>
  <div class="muted" style="letter-spacing:.2em;font-size:.85rem">KIWI CODER · AI + PYTHON</div>
  <h2><span class="zh">毕业证书</span><span class="en">Certificate of Completion</span></h2>
  <p><span class="zh">兹证明</span><span class="en">This certifies that</span></p>
  <div class="name">{{ site.data.me.avatar }} {{ site.data.me.nickname }}</div>
  <p><span class="zh">完成了 12 节 AI + Python 课程，自己计划、制作并部署了一个项目，而且<b>知道卡住了怎么办</b>。</span><span class="en">completed 12 lessons of AI + Python, planned, built and deployed a project of their own, and <b>knows what to do when stuck</b>.</span></p>
  <div class="badge-shelf" style="justify-content:center">
    {% for l in site.data.lessons %}
    <span class="badge" data-badge-id="lesson-{{ l.n }}" title="{{ l.title }}"><span class="ico">{{ l.icon }}</span><span class="zh">第 {{ l.n }} 课</span><span class="en">L{{ l.n }}</span></span>
    {% endfor %}
  </div>
  <p class="muted" style="margin-top:1em"><span class="zh">日期：</span><span class="en">Date: </span><span id="cert-date"></span> · <span class="zh">老师签名：________</span><span class="en">Teacher: ________</span></p>
</div>
<p style="text-align:center"><button class="pg-btn run" onclick="window.print()">🖨️ <span class="zh">打印证书</span><span class="en">Print certificate</span></button></p>
<script>document.getElementById('cert-date').textContent = new Date().toLocaleDateString();</script>

---

## 🔮 <span class="zh">往前看：我的下一个项目</span><span class="en">Look ahead: my next project</span>
{: #next}

<p><span class="zh">课程结束了，但你的网站、画板、游戏都还在。下面是按难度排的点子，<b>选一个</b>。</span><span class="en">The course is over, but your site, playground and games stay. Here are ideas by difficulty — <b>pick one</b>.</span></p>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div><h3><span class="zh">就在这个网站上</span><span class="en">Right here on this site</span></h3><p><span class="zh">· 把<a href="{{ '/games/' | relative_url }}">游戏板块</a>所有关卡打满星 · 给石头剪刀布加「蜥蜴 / 史波克」 · 给你的项目加第 4、5 个功能 · 用 <code>onclick</code> 做一个画画 app</span><span class="en">· Get every star in the <a href="{{ '/games/' | relative_url }}">games</a> · add "lizard / Spock" to Rock Paper Scissors · add features 4 and 5 to your project · make a drawing app with <code>onclick</code></span></p></div></div>
  <div class="level"><div class="medal">🥈</div><div><h3><span class="zh">在自己的电脑上</span><span class="en">On your own computer</span></h3><p><span class="zh">· 装 <a href="https://thonny.org" target="_blank" rel="noopener">Thonny</a>，把作品墙的 .py 下载下来运行（海龟会出现在一个真的窗口里！）· 学 <code>open()</code> 把高分存进文件 · 用 <code>pygame</code> 做一个有图片和声音的游戏</span><span class="en">· Install <a href="https://thonny.org" target="_blank" rel="noopener">Thonny</a>, download your .py files and run them (the turtle gets a real window!) · learn <code>open()</code> to save high scores to a file · make a game with pictures and sound using <code>pygame</code></span></p></div></div>
  <div class="level"><div class="medal">🥇</div><div><h3><span class="zh">新的领域</span><span class="en">New territory</span></h3><p><span class="zh">· 用 HTML 做一个真正的网页（你已经在改 index.md 了，离它只差一步）· micro:bit：让 Python 控制一块真的电路板 · 做一个更大的游戏：贪吃蛇、打砖块、迷宫生成器 · 用 Teachable Machine + Python 做一个「看得见」的程序</span><span class="en">· Build a real web page with HTML (you're already editing index.md — one step away) · micro:bit: Python controlling a real circuit board · a bigger game: snake, breakout, a maze generator · Teachable Machine + Python for a program that can "see"</span></p></div></div>
</div>

<h3>📝 <span class="zh">我的下一个项目清单</span><span class="en">My next-project list</span></h3>

<div class="card" id="next-plan">
  <label style="display:block;font-weight:700;margin:10px 0 4px">🎯 <span class="zh">我想做</span><span class="en">I want to make</span></label>
  <input id="np-what" style="width:100%;font:inherit;font-size:1rem;padding:8px 12px;border-radius:10px;border:2px solid var(--line);background:var(--bg);color:var(--text);margin-top:4px" data-ph-zh="比如：贪吃蛇" data-ph-en="e.g. a snake game" placeholder="比如：贪吃蛇">
  <label style="display:block;font-weight:700;margin:10px 0 4px">🧩 <span class="zh">它的 3 个功能（最小的在前）</span><span class="en">Its 3 features (smallest first)</span></label>
  <input id="np-f1" style="width:100%;font:inherit;font-size:1rem;padding:8px 12px;border-radius:10px;border:2px solid var(--line);background:var(--bg);color:var(--text);margin-top:4px" data-ph-zh="功能 1" data-ph-en="feature 1" placeholder="功能 1">
  <input id="np-f2" style="width:100%;font:inherit;font-size:1rem;padding:8px 12px;border-radius:10px;border:2px solid var(--line);background:var(--bg);color:var(--text);margin-top:6px" data-ph-zh="功能 2" data-ph-en="feature 2" placeholder="功能 2">
  <input id="np-f3" style="width:100%;font:inherit;font-size:1rem;padding:8px 12px;border-radius:10px;border:2px solid var(--line);background:var(--bg);color:var(--text);margin-top:6px" data-ph-zh="功能 3" data-ph-en="feature 3" placeholder="功能 3">
  <label style="display:block;font-weight:700;margin:10px 0 4px">📚 <span class="zh">我需要学的新东西</span><span class="en">New things I need to learn</span></label>
  <input id="np-learn" style="width:100%;font:inherit;font-size:1rem;padding:8px 12px;border-radius:10px;border:2px solid var(--line);background:var(--bg);color:var(--text);margin-top:4px" data-ph-zh="比如：怎么存文件" data-ph-en="e.g. how to save a file" placeholder="比如：怎么存文件">
  <label style="display:block;font-weight:700;margin:10px 0 4px">📅 <span class="zh">每周什么时候做 30 分钟</span><span class="en">When I'll spend 30 minutes each week</span></label>
  <input id="np-when" style="width:100%;font:inherit;font-size:1rem;padding:8px 12px;border-radius:10px;border:2px solid var(--line);background:var(--bg);color:var(--text);margin-top:4px" data-ph-zh="比如：周六早上" data-ph-en="e.g. Saturday morning" placeholder="比如：周六早上">
  <pre id="np-out" style="white-space:pre-wrap;border:2px dashed var(--brand);margin-top:14px"></pre>
  <p><button class="pg-btn run" id="np-copy">📋 <span class="zh">复制清单（贴到笔记本第 12 课）</span><span class="en">Copy the list (paste into notebook Lesson 12)</span></button></p>
</div>
<script>
(function () {
  var ids = ['np-what', 'np-f1', 'np-f2', 'np-f3', 'np-learn', 'np-when'];
  var out = document.getElementById('np-out');
  function v(id) { return (document.getElementById(id).value || '___').trim() || '___'; }
  function build() {
    var en = window.KC && KC.lang() === 'en';
    out.textContent = en
      ? ['🔮 My next project: ' + v('np-what'), '1. ' + v('np-f1'), '2. ' + v('np-f2'), '3. ' + v('np-f3'), '📚 To learn: ' + v('np-learn'), '📅 When: ' + v('np-when'), '🛟 Stuck? Read the error → notebook → ask AI for a hint → ask someone'].join('\n')
      : ['🔮 我的下一个项目：' + v('np-what'), '1. ' + v('np-f1'), '2. ' + v('np-f2'), '3. ' + v('np-f3'), '📚 要学的：' + v('np-learn'), '📅 什么时候做：' + v('np-when'), '🛟 卡住了？读报错 → 翻笔记本 → 问 AI 要提示 → 问人'].join('\n');
  }
  ids.forEach(function (id) { document.getElementById(id).addEventListener('input', build); });
  document.addEventListener('kc-lang', build);
  document.getElementById('np-copy').addEventListener('click', function () {
    if (navigator.clipboard) navigator.clipboard.writeText(out.textContent).catch(function () {});
    if (window.kcToast) kcToast('📋 <span class="zh">复制好了，去贴到笔记本吧！</span><span class="en">Copied — paste it into your notebook!</span>', 2000);
  });
  build();
})();
</script>

<div class="box box-rule"><span class="box-title"><span class="zh">🛟 带走一辈子的四步法</span><span class="en">🛟 The 4 steps, for life</span></span>
<span class="zh">以后不管学什么——新的编程语言、数学题、修自行车——都是一样的：① <b>读清楚问题</b>（报错说什么）② <b>翻自己的笔记</b>（以前遇到过吗）③ <b>问 AI 要提示</b>（不要答案，还要检验）④ <b>问人</b>（带着前三步的发现去问）。这就是「钓鱼」。</span>
<span class="en">Whatever you learn next — a new language, a maths problem, fixing a bike — it's the same: ① <b>read the problem carefully</b> (what does the error say) ② <b>check your own notes</b> (seen it before?) ③ <b>ask AI for a hint</b> (not the answer, and check it) ④ <b>ask a person</b> (bringing what you found in steps 1–3). That's "fishing".</span>
</div>

## 📚 <span class="zh">知识卡片</span><span class="en">Knowledge cards</span>

<div class="know">
  <div class="k"><b>🚀 <span class="zh">部署</span><span class="en">Deploy</span></b><code><span class="zh">改文件 → commit → Actions → 网站更新</span><span class="en">edit file → commit → Actions → site updates</span></code><span><span class="zh">把程序放到网上让别人用</span><span class="en">Put the program online for others</span></span></div>
  <div class="k"><b>💾 commit</b><code>Commit changes + <span class="zh">一句说明</span><span class="en">a short note</span></code><span><span class="zh">存档，可以回到任何一版</span><span class="en">A save point you can return to</span></span></div>
  <div class="k"><b>🕰️ History</b><code><span class="zh">文件 → History → 上一版</span><span class="en">file → History → previous version</span></code><span><span class="zh">版本控制：改坏了也能回去</span><span class="en">Version control: go back if it breaks</span></span></div>
  <div class="k"><b>🤖 Actions</b><code><span class="zh">仓库 → Actions → 🟢</span><span class="en">repo → Actions → 🟢</span></code><span><span class="zh">GitHub 的机器人在干活</span><span class="en">GitHub's robot at work</span></span></div>
  <div class="k"><b>✨ <span class="zh">标题画面</span><span class="en">Title screen</span></b><code>title_pen.write("标题", align="center",
  font=("Arial", 32, "bold"))
screen.ontimer(title_pen.clear, 3000)</code><span><span class="zh">门面</span><span class="en">The front door</span></span></div>
  <div class="k"><b>✈️ <span class="zh">起飞前检查</span><span class="en">Pre-flight check</span></b><code><span class="zh">没红字 · test() ✅ · 有标题 · 存了 · 没真名</span><span class="en">no red · test() ✅ · has title · saved · no real name</span></code><span><span class="zh">部署前的清单</span><span class="en">Pre-deploy checklist</span></span></div>
  <div class="k"><b>🎤 <span class="zh">展示稿</span><span class="en">Demo script</span></b><code><span class="zh">是什么 → 怎么玩 → 最难的 bug → 学到了</span><span class="en">what → how to play → hardest bug → what I learned</span></code><span><span class="zh">3 分钟</span><span class="en">3 minutes</span></span></div>
</div>

<p class="muted"><span class="zh">全部指令在 <a href="{{ '/cheatsheet/' | relative_url }}">📖 小词典</a>——12 课的都在，随时回来查。</span><span class="en">Everything is in the <a href="{{ '/cheatsheet/' | relative_url }}">📖 cheat sheet</a> — all 12 lessons, come back any time.</span></p>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/12/homework/' | relative_url }}"><span class="zh">下一步：毕业作业 🏠 →</span><span class="en">Next: graduation homework 🏠 →</span></a></p>
