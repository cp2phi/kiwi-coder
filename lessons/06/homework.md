---
title: 第 6 课 · 作业
title_en: Lesson 6 · Homework
lesson: "06"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 6 课作业：动物侦探</span><span class="en">Lesson 6 homework: Animal Detective</span>

<p><span class="zh">把课上的动物猜猜猜变成一个<b>真正的侦探</b>——认识更多动物、会给自己打分，再在家训练一个会学习的 AI，比一比谁更准。</span><span class="en">Turn the animal guesser into a <b>real detective</b> — more animals, a score for itself, and a learning AI trained at home. Which one is more accurate?</span> <span class="pill">⏱ <span class="zh">大约 30 分钟（🥇 另算）</span><span class="en">about 30 minutes (🥇 extra)</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week06-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：至少 6 种动物（狗、蝙蝠、企鹅一定要有）</span><span class="en">Must do: at least 6 animals (dog, bat and penguin included)</span></h3>
    <p><span class="zh">画板里的侦探只认识 4 种动物。<b>TODO 1</b>：让它认出 🐶 狗、🦇 蝙蝠、🐧 企鹅——光加 <code>elif</code> 不够，你得<b>自己想新问题</b>（加 <code>input</code>），还要想好规则的<b>顺序</b>。把 6 种动物都试一遍，确认每种都能猜对；回答 no 能停下来。</span><span class="en">The detective only knows 4 animals. <b>TODO 1</b>: make it recognise 🐶 dog, 🦇 bat and 🐧 penguin — <code>elif</code> alone isn't enough; you must <b>invent new questions</b> (add <code>input</code>s) and get the rules in the right <b>order</b>. Test all 6 animals and make sure each one is guessed right; answering no must stop it.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：给 AI 打分</span><span class="en">Bonus: score the AIs</span></h3>
    <p><span class="zh"><b>TODO 2</b>：每局最后问「我猜对了吗？」，用 <code>rounds</code> 和 <code>right</code> 计数。<b>TODO 3</b>：最后打印「猜对了 right / rounds 局」，全对再说「🏆 完美侦探」。然后在家用 <a href="https://teachablemachine.withgoogle.com/train/image" target="_blank" rel="noopener">Teachable Machine</a> 训练一个你自己的模型（认两样东西，比如你的两个玩具；没有摄像头就用 Upload；不拍脸），<b>测试 10 次</b>，把结果写在代码第 3–4 行。哪个 AI 更准？为什么？</span><span class="en"><b>TODO 2</b>: after each round ask "Did I guess right?" and count with <code>rounds</code> and <code>right</code>. <b>TODO 3</b>: print "right / rounds" at the end, plus "🏆 perfect detective" if all correct. Then at home train your own <a href="https://teachablemachine.withgoogle.com/train/image" target="_blank" rel="noopener">Teachable Machine</a> model (two things, like two of your toys; no camera? use Upload; no faces), <b>test it 10 times</b>, and write the result on lines 3–4 of the code. Which AI is more accurate? Why?</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战（选做）：聪明侦探——只问需要的问题</span><span class="en">Challenge (optional): smart detective — only ask what's needed</span></h3>
    <p><span class="zh">现在的侦探每局都问一样多的问题。聪明的侦探<b>根据上一个回答决定下一个问题</b>：比如有毛的动物才问「会汪汪叫吗」。写一个新版本（if 里面再 <code>input</code>），用 <code>asked += 1</code> 数问了几个问题。先在纸上画一棵「问题树」，每个分叉是一个问题，每片叶子是一种动物。</span><span class="en">The detective asks the same number of questions every round. A smart one <b>picks the next question from the last answer</b>: e.g. only ask "does it bark?" about furry animals. Write a new version (an <code>input</code> inside an if) and count questions with <code>asked += 1</code>. Draw a "question tree" on paper first: each fork is a question, each leaf an animal.</span></p>
  </div></div>
</div>

<div class="cmds small">
  <div class="cmd"><code>while again == "yes":</code><span><span class="zh">回答 yes 就再来一次</span><span class="en">Play again while the answer is yes</span></span></div>
  <div class="cmd"><code>elif fur == "yes" and bark == "yes":</code><span><span class="zh">两个条件都对</span><span class="en">Both conditions true</span></span></div>
  <div class="cmd"><code>right += 1</code><span><span class="zh">计数器加一</span><span class="en">Counter plus one</span></span></div>
  <div class="cmd"><code>if right == rounds:</code><span><span class="zh">每局都对吗？</span><span class="en">Right every round?</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。回答问题请打 <code>yes</code> 或 <code>no</code>（小写）。</span><span class="en">Your code is saved on this computer automatically. Answer with <code>yes</code> or <code>no</code> (lowercase).</span></p>

<div class="playground" data-src="{{ '/lessons/06/code/homework.py' | relative_url }}" data-canvas="no" data-title="🕵️ 动物侦探" data-title-en="🕵️ Animal Detective" data-save="week06-homework" data-draft="l6-homework" data-rows="20"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：顺序很重要</span><span class="en">💡 Hint 1: order matters</span></summary><span class="zh"><code>if / elif</code> 是从上往下检查，<b>第一个对的就停</b>。如果「有毛 + 不会飞 → 猫」排在「有毛 + 会叫 → 狗」前面，狗永远会被猜成猫。把更具体的规则放前面。</span><span class="en"><code>if / elif</code> checks top to bottom and <b>stops at the first match</b>. If "fur + can't fly → cat" comes before "fur + barks → dog", a dog is always called a cat. Put the more specific rules first.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：企鹅</span><span class="en">💡 Hint 2: penguin</span></summary><span class="zh">企鹅没有毛、不会飞……和 kiwi 的回答一样！需要一个能把它们分开的新问题，比如「它会游泳吗？」。想一想：企鹅的规则要不要排在「住在水里 → 鲨鱼」前面？</span><span class="en">A penguin has no fur and can't fly… the same answers as a kiwi! You need a new question that tells them apart, like "Can it swim?". Think: should the penguin rule come before "lives in water → shark"?</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：停不下来？</span><span class="en">💡 Hint 3: won't stop?</span></summary><span class="zh">检查 <code>again = input(...)</code> 是不是在 <code>while</code> <b>里面</b>（缩进 4 个空格）。在外面的话 again 永远是 yes。</span><span class="en">Check that <code>again = input(...)</code> is <b>inside</b> the <code>while</code> (indented 4 spaces). Outside, again stays yes forever.</span></details>
<details class="hint"><summary><span class="zh">💡 🥇 提示：问题树的第一层</span><span class="en">💡 🥇 hint: the first level of the tree</span></summary><pre>asked = 0
fur = input("它有毛吗？")
asked += 1
if fur == "yes":
    bark = input("它会汪汪叫吗？")
    asked += 1
    ...
else:
    ...</pre></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week06-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week06-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh this page — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行 + 1 行：「写规则」和「从数据学」有什么不同？哪个 AI 的正确率更高？</span><span class="en">Write 3 lines + 1 in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what's the difference between "writing rules" and "learning from data"? Which AI was more accurate?</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>我们的程序越来越长了。下周学 <code>def</code>——把一段代码<b>打包</b>起来起个名字，想用的时候喊一声就行。用它画一整条街！</span><span class="en">🔮 <b>Next week:</b> our programs are getting long. Next we learn <code>def</code> — <b>pack</b> a chunk of code, give it a name, and call it whenever you like. We'll draw a whole street with it!</span></div>
