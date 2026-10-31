---
title: 第 1 课 · GitHub
lesson: "01"
tab: github
---

# 🐙 GitHub：放代码的网上文件夹

## 是什么？为什么用？

<div class="grid">
  <div class="card"><div class="big-emoji">📦</div><h3>网上的文件夹</h3><p>代码、作业、作品都放这里，换哪台电脑都能打开。<br><span class="muted">叫做<b>仓库</b>（repository）</span></p></div>
  <div class="card"><div class="big-emoji">💾</div><h3>游戏存档</h3><p>每改一次就<b>存个档</b>，改坏了还能回去看以前的样子。<br><span class="muted">存档叫 <b>commit</b></span></p></div>
  <div class="card"><div class="big-emoji">🌐</div><h3>自动变成网站</h3><p>仓库里的东西会自动变成网站——就是你正在看的这个！<br><span class="muted">叫做 <b>GitHub Pages</b></span></p></div>
</div>

<div class="flow">
  <div class="f"><span class="e">✏️</span><b>改文件</b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">💾</span><b>Commit 存档</b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">⏳</span><b>等 1 分钟</b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🌐</span><b>网站变了！</b></div>
</div>

## 仓库长什么样？

<div class="mock">
  <div class="mock-bar"><i></i><i></i><i></i><span class="mock-url">github.com/{{ site.github_repo }}</span></div>
  <div class="mock-body">
    <div class="mock-row"><b style="font-size:1.05rem">📁 kiwi-coder</b><span style="margin-left:auto"></span><span class="dot">2</span><span class="mock-btn">Add file ▾</span></div>
    <div class="mock-files">
      <div>📁 _data <span class="msg">我的名片在这里面</span></div>
      <div>📁 lessons <span class="msg">老师放的教材</span></div>
      <div>📁 my-work <span class="msg">我的作品和作业</span><span class="dot">1</span></div>
      <div>📄 notebook.md <span class="msg">我的笔记本</span></div>
    </div>
  </div>
</div>

<ul class="legend">
  <li><span class="dot">1</span><div>点文件夹 📁 进去，点文件 📄 打开看。</div></li>
  <li><span class="dot">2</span><div><b>Add file</b>：新建或上传文件。</div></li>
</ul>

## 🎮 任务：改我的名片

<ol class="steps">
  <li><strong>打开名片</strong>：<a href="https://github.com/{{ site.github_repo }}/blob/{{ site.github_branch }}/_data/me.yml" target="_blank" rel="noopener">点这里打开 _data/me.yml</a></li>
  <li><strong>点右上角的 ✏️ 铅笔</strong></li>
  <li><strong>改引号里的字</strong>：昵称、头像 emoji、喜欢的东西、「你觉得 AI 是什么」<br><span class="muted">⚠️ 冒号 <code>:</code> 和引号 <code>"</code> 要留着！不写真名全名和学校。</span></li>
  <li><strong>点绿色的 Commit changes</strong>，写一句「改了我的名片」，再点一次 Commit changes</li>
  <li><strong>等 1 分钟，刷新<a href="{{ '/' | relative_url }}">首页</a></strong> 🎉 你刚刚更新了一个真正的网站！</li>
</ol>

<div class="box box-tip">💡 网站没变？点仓库上方的 <b>Actions</b>：🟡 还在做，✅ 好了，❌ 出错了（多半是冒号或引号被删了）。</div>

<div class="quiz" data-answer="1">
  <p class="q">「commit」最像游戏里的什么？</p>
  <div class="opts"><button>存档 💾</button><button>金币 🪙</button><button>怪物 👾</button></div>
  <div class="why">对！commit 就是存档。</div>
</div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/01/codex/' | relative_url }}">下一步：认识 Codex 🤖 →</a></p>
