---
title: 第 5 课 · 作业
title_en: Lesson 5 · Homework
lesson: "05"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 5 课作业：故事机 3000</span><span class="en">Lesson 5 homework: Story Machine 3000</span>

<p><span class="zh">做一台会讲故事、会出题、会记错题的机器——全靠<b>列表</b>！这次每一部分都要<b>你自己写几行</b>。</span><span class="en">Build a machine that tells stories, asks quiz questions and remembers mistakes — all powered by <b>lists</b>! Every part needs <b>a few lines written by you</b>.</span> <span class="pill">⏱ <span class="zh">大约 30 分钟（🥇 另算）</span><span class="en">about 30 minutes (🥇 extra)</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week05-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：4 个列表的故事生成器</span><span class="en">Must do: a 4-list story maker</span></h3>
    <p><span class="zh"><b>TODO 1</b>：每个列表加 2 样你自己的，再做第 4 个列表 <code>when</code>。<b>TODO 2</b>：<b>自己写</b> for 循环，打印 3 个<b>带编号</b>的故事，每个都用到 4 个列表。</span><span class="en"><b>TODO 1</b>: add 2 of your own items to each list, then make a 4th list <code>when</code>. <b>TODO 2</b>: <b>write</b> a for loop that prints 3 <b>numbered</b> stories, each using all 4 lists.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：会记错题的测验</span><span class="en">Bonus: a quiz that remembers mistakes</span></h3>
    <p><span class="zh"><b>TODO 3</b>：自己写判断——答对加分；答错说出正确答案，并把毛利语和英文分别存进 <code>wrong</code> 和 <code>wrong_en</code>。<b>TODO 4</b>：最后把错题一行一行打印成「📌 kai = food」，全对就说「💯 满分」。想换成你自己想考的题（动物、太空、家人生日……）也可以，至少 5 题。</span><span class="en"><b>TODO 3</b>: write the check yourself — right adds a point; wrong shows the answer and stores the Māori and English words in <code>wrong</code> and <code>wrong_en</code>. <b>TODO 4</b>: at the end print each mistake on its own line like "📌 kai = food", or "💯 full marks" if none. You may swap in your own questions (animals, space, family birthdays…) — at least 5.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战（选做）：测验 2.0</span><span class="en">Challenge (optional): Quiz 2.0</span></h3>
    <p><span class="zh">再出一轮：<b>顺序随机、同一个词不问两次</b>；这一轮结束后，只把这一轮答错的词<b>再考一次</b>。没有起始代码——先在纸上写：需要几个列表？每问一题，哪个列表变短、哪个变长？</span><span class="en">Run another round: <b>random order, no word asked twice</b>; afterwards, give a <b>second chance</b> on just the words missed in that round. No starter code — plan on paper: how many lists do you need? With each question, which list gets shorter and which gets longer?</span></p>
  </div></div>
</div>

<div class="cmds small">
  <div class="cmd"><code>random.choice(列表)</code><span><span class="zh">随机抽一个</span><span class="en">Pick one</span></span></div>
  <div class="cmd"><code>列表.append(x)</code><span><span class="zh">加到最后</span><span class="en">Add to the end</span></span></div>
  <div class="cmd"><code>for k in range(len(wrong)):</code><span><span class="zh">用编号走一遍，两个配对列表一起用</span><span class="en">Go by number to use two paired lists together</span></span></div>
  <div class="cmd"><code>word = maori.pop(i)</code><span><span class="zh">拿走第 i 个，还交给你</span><span class="en">Take out item i and hand it to you</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。三个部分在同一个文件里，从上往下跑：先打印故事，再出题。</span><span class="en">Your code is saved on this computer automatically. All parts are in one file and run top to bottom: stories first, then the quiz.</span></p>

<div class="playground" data-src="{{ '/lessons/05/code/homework.py' | relative_url }}" data-canvas="no" data-title="🎰 故事机 3000" data-title-en="🎰 Story Machine 3000" data-save="week05-homework" data-draft="l5-homework" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：列表里的逗号</span><span class="en">💡 Hint 1: commas in lists</span></summary><span class="zh">每样东西之间要有逗号，最后一个后面不用。忘了逗号，电脑会说「看不懂这一行」——而且常常指向<b>下一行</b>。</span><span class="en">Every item needs a comma between it and the next; none after the last one. Miss a comma and the computer says it can't read the line — often pointing at the <b>next</b> line.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：带编号的故事</span><span class="en">💡 Hint 2: numbered stories</span></summary><span class="zh"><code>for i in range(3):</code>，下面一行：<code>print(f"{i + 1}. {random.choice(when)}{random.choice(who)}……")</code>。</span><span class="en"><code>for i in range(3):</code>, then on the next line: <code>print(f"{i + 1}. {random.choice(when)}{random.choice(who)}…")</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：打印错题</span><span class="en">💡 Hint 3: printing the mistakes</span></summary><span class="zh"><code>wrong[k]</code> 和 <code>wrong_en[k]</code> 是配对的。<code>if len(wrong) == 0:</code> 满分；<code>else:</code> 里面放 <code>for k in range(len(wrong)):</code>。</span><span class="en"><code>wrong[k]</code> and <code>wrong_en[k]</code> are a pair. <code>if len(wrong) == 0:</code> full marks; inside <code>else:</code> put <code>for k in range(len(wrong)):</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 🥇 提示：不重复的秘诀</span><span class="en">💡 🥇 hint: the no-repeat trick</span></summary><span class="zh">每一题：随机选编号 <code>i = random.randint(0, len(maori) - 1)</code>，然后<b>同时</b> <code>m = maori.pop(i)</code> 和 <code>e = english.pop(i)</code>——两个列表一起变短，配对就不会乱。答错的放进两个新列表，第二轮用它们。</span><span class="en">Each question: pick <code>i = random.randint(0, len(maori) - 1)</code>, then <b>both</b> <code>m = maori.pop(i)</code> and <code>e = english.pop(i)</code> — both lists shrink together so the pairs stay matched. Put misses into two new lists for the second round.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week05-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week05-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh this page — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行：学会了什么 / 卡在哪里 / 怎么解决的。</span><span class="en">Write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what I learned / where I got stuck / how I fixed it.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>一种新的重复——<code>while</code>，「没猜对就一直猜」。还有一个大问题：<b>AI 到底是怎么学习的？</b>我们会自己写一个「规则版 AI」，再和真正会学习的 AI 比一比。</span><span class="en">🔮 <b>Next week:</b> a new kind of repeating — <code>while</code>, "keep guessing until you're right". And a big question: <b>how does AI actually learn?</b> We'll write a "rule-based AI" and compare it with one that really learns.</span></div>
