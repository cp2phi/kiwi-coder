---
title: 第 9 课 · 作业
title_en: Lesson 9 · Homework
lesson: "09"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 9 课作业：我的翻译 app</span><span class="en">Lesson 9 homework: My Translator app</span>

<p><span class="zh">做一个<b>属于你的</b>翻译 app：你教它什么语言都行——毛利语、英语、火星语！</span><span class="en">Build a translator app that's <b>yours</b>: teach it any language — te reo Māori, English, Martian!</span> <span class="pill">⏱ <span class="zh">🥉 约 25 分钟，🥈🥇 再加 20–40 分钟</span><span class="en">🥉 about 25 min, 🥈🥇 another 20–40 min</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week09-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：会学新词的翻译机</span><span class="en">Must do: a translator that learns</span></h3>
    <p><span class="zh">① 字典里<b>至少 8 个词</b>；② 查不到的词，问意思并<b>记住</b>（<code>words[word] = …</code>）；③ 输入 <code>全部</code> 用 <code>.items()</code> 打印所有的词；④ 结束时打印「这次教会了它 N 个新词」。循环里要分<b>三种情况</b>：全部 / 查到了 / 查不到。</span><span class="en">① At least <b>8 words</b> in the dict; ② for unknown words, ask the meaning and <b>remember it</b> (<code>words[word] = …</code>); ③ typing <code>全部</code> prints every word with <code>.items()</code>; ④ at the end print "you taught it N new words this time". The loop needs <b>three cases</b>: 全部 / found / not found.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：测验模式 + 错题本</span><span class="en">Bonus: quiz mode + a mistakes book</span></h3>
    <p><span class="zh">开头问「翻译 还是 测验？」。测验：<b>随机</b>考 5 个词、记分。再做一个<b>错题本字典</b> <code>mistakes</code>：答错就用数数公式加 1，最后打印「你最容易错的词是 ___」。</span><span class="en">Start by asking "translate or quiz?". Quiz: test 5 <b>random</b> words and keep score. Add a <b>mistakes dict</b> <code>mistakes</code>: on a wrong answer add 1 with the counting line, then print "your hardest word is ___".</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：AI 侦探报告（用程序写！）</span><span class="en">Challenge: an AI detective report (as a program!)</span></h3>
    <p><span class="zh">请 AI 给你 10 个毛利语（或别的语言）单词和意思，放进字典 <code>ai_words</code>。<b>至少挑 3 个</b>用词典或问老师核实，结果放进第二个字典 <code>checked</code>（对 True、错 False）。让程序打印一份报告：查过的词 ✅ / ❌，没查过的 ❓，最后算出「AI 在查过的词里对了 ___%」。想一想：只查 3 个，能说 AI「70% 对」吗？</span><span class="en">Ask an AI for 10 te reo Māori (or other) words with meanings and put them in a dict <code>ai_words</code>. Check <b>at least 3</b> with a dictionary or your teacher, and record the results in a second dict <code>checked</code> (True right, False wrong). Make the program print a report: ✅ / ❌ for checked words, ❓ for unchecked ones, and "AI was right on ___% of the words I checked". Think: after checking just 3, can you say AI is "70% right"?</span></p>
  </div></div>
</div>

<div class="cmds small">
  <div class="cmd"><code>words.get(word, "不知道")</code><span><span class="zh">查词，查不到给默认的话</span><span class="en">look up, with a default</span></span></div>
  <div class="cmd"><code>words[word] = input("意思？")</code><span><span class="zh">教它新词</span><span class="en">teach it a word</span></span></div>
  <div class="cmd"><code>for w, meaning in words.items():</code><span><span class="zh">「全部」：标签和意思一起拿</span><span class="en">全部: label and meaning together</span></span></div>
  <div class="cmd"><code>mistakes[w] = mistakes.get(w, 0) + 1</code><span><span class="zh">错题本：数数公式</span><span class="en">mistakes book: the counting line</span></span></div>
  <div class="cmd"><code>random.choice(list(words))</code><span><span class="zh">随机抽一个词考（<code>list(words)</code> = 把所有标签排成一个列表，random.choice 才能挑；先当魔法用）</span><span class="en">pick a random word (<code>list(words)</code> = put all the labels into a list so random.choice can pick one; treat as magic)</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上，关掉网页也不会丢。</span><span class="en">Your code is saved on this computer automatically, even if you close the page.</span></p>

<div class="playground" data-src="{{ '/lessons/09/code/homework.py' | relative_url }}" data-title="🏠 我的翻译 app" data-title-en="🏠 My Translator app" data-canvas="no" data-save="week09-homework" data-draft="l9-homework" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：三种情况怎么排？</span><span class="en">💡 Hint 1: ordering the three cases</span></summary><span class="zh">把 <code>print("👉", words.get(...))</code> 换成：<code>if word == "全部":</code>（for + .items()）<code>elif word in words:</code>（打印意思）<code>else:</code>（<code>input()</code> 问意思，<code>words[word] = 意思</code>，计数器 +1）。学一学例 2 的翻译机几乎一样。</span><span class="en">Replace <code>print("👉", words.get(...))</code> with: <code>if word == "全部":</code> (for + .items()) <code>elif word in words:</code> (print the meaning) <code>else:</code> (<code>input()</code> the meaning, <code>words[word] = meaning</code>, counter +1). Learn Example 2's translator is almost the same.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：「最容易错的词」</span><span class="en">💡 Hint 2: "hardest word"</span></summary><span class="zh">和例 4 找「最爱出的拳」一模一样：<code>hardest = ""</code> → <code>for w, n in mistakes.items():</code> → 更大就换。别忘了：一个都没错的时候 mistakes 是空的！</span><span class="en">Exactly like finding the favourite move in Example 4: <code>hardest = ""</code> → <code>for w, n in mistakes.items():</code> → switch when bigger. Don't forget: if you got nothing wrong, mistakes is empty!</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：🥇 的百分比</span><span class="en">💡 Hint 3: 🥇 percentage</span></summary><span class="zh">只算查过的：对的个数 ÷ <code>len(checked)</code> × 100，用 <code>int()</code>。<code>if w in checked:</code> 分出 ✅❌ 和 ❓。</span><span class="en">Only count checked words: right ÷ <code>len(checked)</code> × 100, with <code>int()</code>. Use <code>if w in checked:</code> to split ✅❌ from ❓.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 4：卡住了？</span><span class="en">💡 Hint 4: stuck?</span></summary><span class="zh">四步法：读报错（KeyError = 标签不存在）→ 翻 <a href="{{ '/notebook/' | relative_url }}">笔记本</a> → 用「问 AI 要提示」按钮 → 问老师。</span><span class="en">The 4 steps: read the error (KeyError = label missing) → check your <a href="{{ '/notebook/' | relative_url }}">notebook</a> → use the "hint please" button → ask your teacher.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week09-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week09-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行 + 「我抓到 AI 的一个错误」。</span><span class="en">Write 3 lines + "an AI mistake I caught" in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>你要<b>自己选一个项目</b>（游戏 / app / 互动画画），学真正的程序员怎么做项目：计划 → 写 → 测 → 修 → 发布。先想一想：你最想做什么？</span><span class="en">🔮 <b>Next week:</b> you'll <b>choose your own project</b> (game / app / interactive art) and learn how real programmers work: plan → code → test → fix → ship. Start thinking: what do you most want to make?</span></div>
