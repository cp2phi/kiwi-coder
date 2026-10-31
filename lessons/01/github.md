---
title: 第 1 课 · GitHub
title_en: Lesson 1 · GitHub
lesson: "01"
tab: github
---

# 🐙 <span class="zh">GitHub：放代码的网上文件夹</span><span class="en">GitHub: an online folder for your code</span>

## <span class="zh">是什么？为什么用？</span><span class="en">What is it? Why use it?</span>

<div class="grid">
  <div class="card"><div class="big-emoji">📦</div><h3><span class="zh">网上的文件夹</span><span class="en">An online folder</span></h3><p><span class="zh">代码、作业、作品都放这里，换哪台电脑都能打开。<br><span class="muted">叫做<b>仓库</b>（repository）</span></span><span class="en">Your code, homework and creations live here. Open them from any computer.<br><span class="muted">It's called a <b>repository</b> (repo)</span></span></p></div>
  <div class="card"><div class="big-emoji">💾</div><h3><span class="zh">游戏存档</span><span class="en">Game save points</span></h3><p><span class="zh">每改一次就<b>存个档</b>，改坏了还能回去看以前的样子。<br><span class="muted">存档叫 <b>commit</b></span></span><span class="en">Every change gets <b>saved</b>. Broke something? Go back and see the old version.<br><span class="muted">A save is called a <b>commit</b></span></span></p></div>
  <div class="card"><div class="big-emoji">🌐</div><h3><span class="zh">自动变成网站</span><span class="en">Turns into a website</span></h3><p><span class="zh">仓库里的东西会自动变成网站——就是你正在看的这个！<br><span class="muted">叫做 <b>GitHub Pages</b></span></span><span class="en">Your repo automatically becomes a website — the one you're reading now!<br><span class="muted">It's called <b>GitHub Pages</b></span></span></p></div>
</div>

<div class="flow">
  <div class="f"><span class="e">✏️</span><b><span class="zh">改文件</span><span class="en">Edit a file</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">💾</span><b><span class="zh">Commit 存档</span><span class="en">Commit (save)</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">⏳</span><b><span class="zh">等 1 分钟</span><span class="en">Wait 1 minute</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🌐</span><b><span class="zh">网站变了！</span><span class="en">Website updated!</span></b></div>
</div>

## <span class="zh">仓库长什么样？</span><span class="en">What does a repo look like?</span>

<div class="mock">
  <div class="mock-bar"><i></i><i></i><i></i><span class="mock-url">github.com/{{ site.github_repo }}</span></div>
  <div class="mock-body">
    <div class="mock-row"><b style="font-size:1.05rem">📁 kiwi-coder</b><span style="margin-left:auto"></span><span class="dot">2</span><span class="mock-btn">Add file ▾</span></div>
    <div class="mock-files">
      <div>📁 _data <span class="msg"><span class="zh">我的名片在这里面</span><span class="en">My name card is in here</span></span></div>
      <div>📁 lessons <span class="msg"><span class="zh">老师放的教材</span><span class="en">Lessons from the teacher</span></span></div>
      <div>📁 my-work <span class="msg"><span class="zh">我的作品和作业</span><span class="en">My work and homework</span></span><span class="dot">1</span></div>
      <div>📄 notebook.md <span class="msg"><span class="zh">我的笔记本</span><span class="en">My notebook</span></span></div>
    </div>
  </div>
</div>

<ul class="legend">
  <li><span class="dot">1</span><div><span class="zh">点文件夹 📁 进去，点文件 📄 打开看。</span><span class="en">Click a folder 📁 to go in, click a file 📄 to open it.</span></div></li>
  <li><span class="dot">2</span><div><b>Add file</b><span class="zh">：新建或上传文件。</span><span class="en">: create or upload a file.</span></div></li>
</ul>

## 🎮 <span class="zh">任务：改我的名片</span><span class="en">Mission: edit my name card</span>

<ol class="steps">
  <li><strong><span class="zh">打开名片</span><span class="en">Open the name card</span></strong>: <a href="https://github.com/{{ site.github_repo }}/blob/{{ site.github_branch }}/_data/me.yml" target="_blank" rel="noopener"><span class="zh">点这里打开 _data/me.yml</span><span class="en">click here to open _data/me.yml</span></a></li>
  <li><strong><span class="zh">点右上角的 ✏️ 铅笔</span><span class="en">Click the ✏️ pencil at the top right</span></strong></li>
  <li><strong><span class="zh">改引号里的字</span><span class="en">Change the words inside the quotes</span></strong><span class="zh">：昵称、头像 emoji、喜欢的东西、「你觉得 AI 是什么」<br><span class="muted">⚠️ 冒号 <code>:</code> 和引号 <code>"</code> 要留着！不写真名全名和学校。</span></span><span class="en">: nickname, emoji avatar, things you like, "what I think AI is"<br><span class="muted">⚠️ Keep the colons <code>:</code> and quotes <code>"</code>! Don't write your full real name or your school.</span></span></li>
  <li><strong><span class="zh">点绿色的 Commit changes</span><span class="en">Click the green Commit changes</span></strong><span class="zh">，写一句「改了我的名片」，再点一次 Commit changes</span><span class="en">, write "updated my name card", then click Commit changes again</span></li>
  <li><strong><span class="zh">等 1 分钟，刷新<a href="{{ '/' | relative_url }}">首页</a></span><span class="en">Wait 1 minute, then refresh the <a href="{{ '/' | relative_url }}">home page</a></span></strong> 🎉 <span class="zh">你刚刚更新了一个真正的网站！</span><span class="en">You just updated a real website!</span></li>
</ol>

<div class="box box-tip"><span class="zh">💡 网站没变？点仓库上方的 <b>Actions</b>：🟡 还在做，✅ 好了，❌ 出错了（多半是冒号或引号被删了）。</span><span class="en">💡 Website didn't change? Click <b>Actions</b> at the top of the repo: 🟡 still working, ✅ done, ❌ something broke (usually a missing colon or quote).</span></div>

<div class="quiz" data-answer="1">
  <p class="q"><span class="zh">「commit」最像游戏里的什么？</span><span class="en">What is a "commit" most like in a game?</span></p>
  <div class="opts"><button><span class="zh">存档</span><span class="en">A save point</span> 💾</button><button><span class="zh">金币</span><span class="en">A coin</span> 🪙</button><button><span class="zh">怪物</span><span class="en">A monster</span> 👾</button></div>
  <div class="why"><span class="zh">对！commit 就是存档。</span><span class="en">Yes! A commit is a save point.</span></div>
</div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/01/codex/' | relative_url }}"><span class="zh">下一步：认识 Codex 🤖 →</span><span class="en">Next: meet Codex 🤖 →</span></a></p>
