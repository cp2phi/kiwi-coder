---
title: 第 1 课 · Codex
title_en: Lesson 1 · Codex
lesson: "01"
tab: codex
---

# 🤖 <span class="zh">Codex：会写代码的 AI 搭档</span><span class="en">Codex: your AI coding buddy</span>

## <span class="zh">是什么？为什么用？</span><span class="en">What is it? Why use it?</span>

<p class="zh"><b>Codex</b> 是一个 AI 编程助手。你用<b>说话的方式</b>（中文也行）告诉它想做什么，它帮你<b>写代码、解释代码、找 bug</b>。</p>
<p class="en"><b>Codex</b> is an AI coding assistant. You tell it what you want <b>in normal words</b> (Chinese works too), and it helps you <b>write code, explain code and find bugs</b>.</p>

<div class="flow">
  <div class="f"><span class="e">💭</span><b><span class="zh">你有个想法</span><span class="en">You have an idea</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">⌨️</span><b><span class="zh">用文字告诉它</span><span class="en">Tell it in words</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🤖</span><b><span class="zh">它写代码</span><span class="en">It writes code</span></b></div>
  <div class="arrow">→</div>
  <div class="f"><span class="e">🔍</span><b><span class="zh">你检查、运行</span><span class="en">You check and run it</span></b></div>
</div>

<div class="box box-think"><span class="zh"><b>🧑‍✈️ 你是队长，AI 是队员。</b>AI 很厉害，但<b>会犯错</b>，所以队长要检查。</span><span class="en"><b>🧑‍✈️ You're the captain, AI is on your team.</b> AI is clever, but it <b>makes mistakes</b>, so the captain checks its work.</span></div>

## <span class="zh">三条守则</span><span class="en">Three rules</span>

<div class="box box-rule">
<span class="zh">① <b>学习时要提示，不要答案</b>：「给我一个提示」比「直接帮我写」学到的多。<br>
② <b>AI 说的要检验</b>：代码运行了才算数。<br>
③ <b>不告诉 AI 隐私</b>：真名、地址、学校、密码都不说。</span>
<span class="en">① <b>Ask for hints, not answers</b>: "give me a hint" teaches you more than "just write it for me".<br>
② <b>Check what AI says</b>: code only counts when it runs.<br>
③ <b>Keep private things private</b>: never tell AI your real name, address, school or passwords.</span>
</div>

## <span class="zh">怎么用？</span><span class="en">How do I use it?</span>

<div class="mock">
  <div class="mock-bar"><i></i><i></i><i></i><span class="mock-url">Codex</span></div>
  <div class="mock-body">
    <div class="bubble me"><span class="zh">用小学生能听懂的话，解释 turtle 里的 forward 是什么意思？</span><span class="en">Explain what forward means in turtle, in words a kid can understand.</span></div>
    <div class="bubble ai"><span class="dot" style="float:right">2</span><b>Codex:</b> <span class="zh">forward 就是让海龟<b>往前走</b>！比如 <code>t.forward(100)</code> 就是走 100 步。</span><span class="en">forward makes the turtle <b>move ahead</b>! <code>t.forward(100)</code> means walk 100 steps.</span></div>
    <div class="mock-row" style="margin-top:10px"><span class="dot">1</span><div class="mock-input" style="flex:1"><span class="zh">告诉 Codex 你想做什么……</span><span class="en">Tell Codex what you want…</span></div><span class="mock-btn dark"><span class="zh">发送</span><span class="en">Send</span></span></div>
  </div>
</div>

<ul class="legend">
  <li><span class="dot">1</span><div><span class="zh">在<b>输入框</b>里写你想问的、想做的，发送。</span><span class="en">Type your question or idea in the <b>box</b> and send it.</span></div></li>
  <li><span class="dot">2</span><div><span class="zh">读 Codex 的回答。要代码的话，<b>复制</b>它，贴到我们的画板里运行。</span><span class="en">Read Codex's answer. If it gives you code, <b>copy</b> it and paste it into our playground to run.</span></div></li>
</ul>

<p class="muted"><span class="zh">（Codex 有网页版、电脑 App 和 VS Code 插件，样子不太一样，但用法都是：写指令 → 看回答 → 检查。）</span><span class="en">(Codex has a website, a desktop app and a VS Code extension. They look a bit different, but they all work the same way: give instructions → read the answer → check it.)</span></p>

## <span class="zh">说清楚，AI 才做得好</span><span class="en">Be clear, and AI does better</span>

<div class="table-wrap">
<table>
  <tr><th><span class="zh">😕 说不清楚</span><span class="en">😕 Not clear</span></th><th><span class="zh">😃 说得清楚</span><span class="en">😃 Clear</span></th></tr>
  <tr><td><span class="zh">画个画</span><span class="en">Draw something</span></td><td><span class="zh">用 turtle 画一个<b>金色</b>的<b>五角星</b>，背景是<b>黑色</b></span><span class="en">Use turtle to draw a <b>gold star</b> on a <b>black</b> background</span></td></tr>
  <tr><td><span class="zh">代码坏了</span><span class="en">My code is broken</span></td><td><span class="zh">第 5 行报错了：（贴上报错），请给我一个提示</span><span class="en">Line 5 has an error: (paste the error). Please give me a hint</span></td></tr>
</table>
</div>

## 🎮 <span class="zh">任务：问 Codex 两个问题</span><span class="en">Mission: ask Codex two questions</span>

<ul class="quests" data-key="l1-codex">
  <li><span class="zh">「用小学生能听懂的话，解释一下什么是 Python？」</span><span class="en">"Explain what Python is, in words a kid can understand."</span></li>
  <li><span class="zh">「你会犯错吗？我怎么知道你说得对不对？」</span><span class="en">"Do you make mistakes? How can I tell if you're right?"</span></li>
</ul>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/01/python/' | relative_url }}"><span class="zh">下一步：开始写 Python 🐍 →</span><span class="en">Next: start coding Python 🐍 →</span></a></p>
