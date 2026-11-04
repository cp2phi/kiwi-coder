---
title: 第 6 课 · 作业
title_en: Lesson 6 · Homework
lesson: "06"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 6 课作业：动物侦探</span><span class="en">Lesson 6 homework: Animal Detective</span>

<p><span class="zh">把课上的动物猜猜猜变成一个<b>真正的侦探</b>——认识更多动物、会数问题，再在家训练一个会学习的 AI。</span><span class="en">Turn the animal guesser into a <b>real detective</b> — more animals, a question counter, and train a learning AI at home.</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week06-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：至少 5 种动物 + 再来一次</span><span class="en">Must do: at least 5 animals + play again</span></h3>
    <p><span class="zh">画板里的侦探只认识 4 种动物。加 <code>elif</code> 让它认识<b>至少 5 种</b>（蝙蝠？企鹅？狗？需要新问题就加 <code>input</code>）。<code>while again == "yes":</code> 已经写好了，确认回答 no 能停下来。</span><span class="en">The detective only knows 4 animals. Add <code>elif</code> rules so it knows <b>at least 5</b> (bat? penguin? dog? add an <code>input</code> if you need a new question). The <code>while again == "yes":</code> loop is there — check that answering no stops it.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：问题计数器</span><span class="en">Bonus: question counter</span></h3>
    <p><span class="zh"><code>questions_asked</code> 已经在数了。如果你加了第 4 个问题，<code>+= 3</code> 要改成几？再加一个 <code>rounds</code> 计数器数玩了几局，最后一起打印。</span><span class="en"><code>questions_asked</code> is already counting. If you added a 4th question, what should <code>+= 3</code> become? Add a <code>rounds</code> counter for how many games were played and print both at the end.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：训练一个 AI + 用 while 画画</span><span class="en">Challenge: train an AI + draw with while</span></h3>
    <p><span class="zh">① 在家用 <a href="https://teachablemachine.withgoogle.com/train/image" target="_blank" rel="noopener">Teachable Machine</a> 训练一个你自己的模型（认两样东西，比如你的两个玩具；没有摄像头就用 Upload 上传照片；不拍脸），在代码<b>最上面的注释</b>里写：教它认什么、每类几张图、它认错过吗。② 把第 3 部分的 <code>while</code> 画改成你自己的（越来越大的正方形？画到边上的彩色螺旋？）。</span><span class="en">① At home, train your own model on <a href="https://teachablemachine.withgoogle.com/train/image" target="_blank" rel="noopener">Teachable Machine</a> (two things, like two of your toys; no camera? use Upload; no faces). In the <b>comment at the top</b> of the code write: what you taught it, how many photos per class, and whether it ever got it wrong. ② Change the <code>while</code> drawing in Part 3 into your own (growing squares? a colourful spiral to the edge?).</span></p>
  </div></div>
</div>

<div class="cmds small">
  <div class="cmd"><code>while again == "yes":</code><span><span class="zh">回答 yes 就再来一次</span><span class="en">Play again while the answer is yes</span></span></div>
  <div class="cmd"><code>elif fur == "yes" and bark == "yes":</code><span><span class="zh">两个条件都对</span><span class="en">Both conditions true</span></span></div>
  <div class="cmd"><code>count += 1</code><span><span class="zh">计数器加一</span><span class="en">Counter plus one</span></span></div>
  <div class="cmd"><code>while r &lt; 120:</code><span><span class="zh">r 还小就继续画</span><span class="en">Keep drawing while r is small</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。回答问题请打 <code>yes</code> 或 <code>no</code>（小写）。</span><span class="en">Your code is saved on this computer automatically. Answer with <code>yes</code> or <code>no</code> (lowercase).</span></p>

<div class="playground" data-src="{{ '/lessons/06/code/homework.py' | relative_url }}" data-title="🕵️ 动物侦探" data-title-en="🕵️ Animal Detective" data-save="week06-homework" data-draft="l6-homework" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 提示 1：顺序很重要</span><span class="en">💡 Hint 1: order matters</span></summary><span class="zh"><code>if / elif</code> 是从上往下检查，<b>第一个对的就停</b>。如果「有毛 + 不会飞 → 猫」排在「有毛 + 会叫 → 狗」前面，狗永远会被猜成猫。把更具体的规则放前面。</span><span class="en"><code>if / elif</code> checks top to bottom and <b>stops at the first match</b>. If "fur + can't fly → cat" comes before "fur + barks → dog", a dog is always called a cat. Put the more specific rules first.</span></details>
<details class="hint"><summary><span class="zh">💡 提示 2：企鹅</span><span class="en">💡 Hint 2: penguin</span></summary><span class="zh">企鹅没有毛、不会飞、住在水边……和 kiwi 的回答一样！需要一个新问题，比如「它会游泳吗？」</span><span class="en">A penguin has no fur, can't fly, lives near water… the same answers as a kiwi! You need a new question, like "Can it swim?"</span></details>
<details class="hint"><summary><span class="zh">💡 提示 3：停不下来？</span><span class="en">💡 Hint 3: won't stop?</span></summary><span class="zh">检查 <code>again = input(...)</code> 是不是在 <code>while</code> <b>里面</b>（缩进 4 个空格）。在外面的话 again 永远是 yes。</span><span class="en">Check that <code>again = input(...)</code> is <b>inside</b> the <code>while</code> (indented 4 spaces). Outside, again stays yes forever.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week06-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week06-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh this page — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行 + 1 行：「写规则」和「从数据学」有什么不同？</span><span class="en">Write 3 lines + 1 in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what's the difference between "writing rules" and "learning from data"?</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>我们的程序越来越长了。下周学 <code>def</code>——把一段代码<b>打包</b>起来起个名字，想用的时候喊一声就行。用它画一整条街！</span><span class="en">🔮 <b>Next week:</b> our programs are getting long. Next we learn <code>def</code> — <b>pack</b> a chunk of code, give it a name, and call it whenever you like. We'll draw a whole street with it!</span></div>
