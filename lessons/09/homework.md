---
title: 第 9 课 · 作业
title_en: Lesson 9 · Homework
lesson: "09"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 9 课作业：我的翻译 app</span><span class="en">Lesson 9 homework: My Translator app</span>

<p><span class="zh">做一个<b>属于你的</b>翻译 app：你教它什么语言都行——毛利语、英语、火星语！</span><span class="en">Build a translator app that's <b>yours</b>: teach it any language — te reo Māori, English, Martian!</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week09-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：8 个词的翻译机</span><span class="en">Must do: an 8-word translator</span></h3>
    <p><span class="zh">字典里放<b>至少 8 个词</b>，循环问词、用 <code>.get</code> 查，查不到说一句友好的话。（只用今天 + 以前学的东西，起始代码已经帮你搭好了。）</span><span class="en">Put <b>at least 8 words</b> in the dict, loop asking for words, look them up with <code>.get</code>, and say something friendly if it's not there. (Only today's + earlier magic; the starter code is set up for you.)</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：教我新词 + 小测验模式</span><span class="en">Bonus: teach me + quiz mode</span></h3>
    <p><span class="zh">查不到的词，让它问你意思并<b>记住</b>（<code>words[word] = …</code>）。再加一个<b>测验模式</b>：把字典里的词轮流考你，记分。</span><span class="en">If a word is unknown, ask for its meaning and <b>remember it</b> (<code>words[word] = …</code>). Then add a <b>quiz mode</b> that tests you on the words and keeps score.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：AI 侦探报告</span><span class="en">Challenge: AI detective report</span></h3>
    <p><span class="zh">请 AI 给你 10 个毛利语（或别的语言）单词和意思。<b>挑 3 个</b>用词典或问老师核实。在代码最上面的「AI 侦探报告」注释里写：哪几个对、哪几个错、你是怎么查的。</span><span class="en">Ask an AI for 10 te reo Māori (or other) words with meanings. <b>Pick 3</b> and verify them with a dictionary or your teacher. In the "AI detective report" comment at the top write: which were right, which wrong, and how you checked.</span></p>
  </div></div>
</div>

<div class="cmds small">
  <div class="cmd"><code>words.get(word, "不知道")</code><span><span class="zh">查词，查不到给默认的话</span><span class="en">look up, with a default</span></span></div>
  <div class="cmd"><code>words[word] = input("意思？")</code><span><span class="zh">教它新词</span><span class="en">teach it a word</span></span></div>
  <div class="cmd"><code>for k in words:</code><span><span class="zh">测验模式：轮流考每个词</span><span class="en">quiz mode: test every word</span></span></div>
  <div class="cmd"><code>random.choice(list(words))</code><span><span class="zh">随机抽一个词考（要 import random）</span><span class="en">pick a random word (import random)</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上，关掉网页也不会丢。</span><span class="en">Your code is saved on this computer automatically, even if you close the page.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/homework.py' | relative_url }}" data-title="🏠 我的翻译 app" data-title-en="🏠 My Translator app" data-canvas="no" data-save="week09-homework" data-draft="l9-homework" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：查不到的词怎么教它？</span><span class="en">💡 Hint 1: teaching unknown words</span></summary><span class="zh">把 <code>print("👉", words.get(...))</code> 换成 <code>if word in words:</code> … <code>else:</code> … 两种情况。else 里面用 <code>input()</code> 问意思，再 <code>words[word] = 意思</code>。第 9 课的例 2 就是这样写的。</span><span class="en">Replace <code>print("👉", words.get(...))</code> with two cases: <code>if word in words:</code> … <code>else:</code> …. In the else, <code>input()</code> the meaning, then <code>words[word] = meaning</code>. Example 2 in the lesson does exactly this.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：测验模式</span><span class="en">💡 Hint 2: quiz mode</span></summary><span class="zh">先问一句 <code>mode = input("翻译 还是 测验？")</code>。如果是测验，就用例 3 的问答机代码，把 <code>quiz</code> 换成 <code>words</code>。</span><span class="en">First ask <code>mode = input("translate or quiz?")</code>. For quiz, use the quiz-machine code from Example 3 with <code>quiz</code> replaced by <code>words</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：卡住了？</span><span class="en">💡 Hint 3: stuck?</span></summary><span class="zh">四步法：读报错（KeyError = 标签不存在）→ 翻 <a href="{{ '/notebook/' | relative_url }}">笔记本</a> → 用「问 AI 要提示」按钮 → 问老师。</span><span class="en">The 4 steps: read the error (KeyError = label missing) → check your <a href="{{ '/notebook/' | relative_url }}">notebook</a> → use the "hint please" button → ask your teacher.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week09-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week09-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行 + 「我抓到 AI 的一个错误」。</span><span class="en">Write 3 lines + "an AI mistake I caught" in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>你要<b>自己选一个项目</b>（游戏 / app / 互动画画），学真正的程序员怎么做项目：计划 → 写 → 测 → 修 → 发布。先想一想：你最想做什么？</span><span class="en">🔮 <b>Next week:</b> you'll <b>choose your own project</b> (game / app / interactive art) and learn how real programmers work: plan → code → test → fix → ship. Start thinking: what do you most want to make?</span></div>
