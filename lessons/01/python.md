---
title: 第 1 课 · Python
title_en: Lesson 1 · Python
lesson: "01"
tab: python
playground: true
---

# 🐍 <span class="zh">Python 第一课：让电脑听我的话</span><span class="en">Python Lesson 1: make the computer listen to me</span>

<p class="zh"><b>Python</b> 是一种和电脑说话的语言。今天不用装软件，<b>就在这个网页上写代码</b>：改左边的代码 → 点 <b>▶ 运行</b> → 看右边的结果。</p>
<p class="en"><b>Python</b> is a language for talking to computers. No installing today — <b>we code right on this page</b>: change the code on the left → click <b>▶ Run</b> → see the result on the right.</p>

---

## <span class="zh">第 1 步：Hello 👋</span><span class="en">Step 1: Hello 👋</span>

<p><span class="zh">几乎每个程序员学的第一个程序，都是让电脑打个招呼。</span><span class="en">Almost every programmer's first program makes the computer say hello.</span></p>

<div class="playground" data-src="{{ '/lessons/01/code/hello.py' | relative_url }}" data-canvas="no" data-title="👋 Hello 程序" data-title-en="👋 Hello program" data-save="hello"></div>

<ul class="quests" data-key="l1-hello">
  <li><span class="zh">把 <code>___</code> 换成你的昵称，运行。电脑听你的话了吗？</span><span class="en">Replace <code>___</code> with your nickname and run it. Did the computer listen?</span></li>
  <li><span class="zh">再加一行 <code>print("...")</code>，说出你最喜欢的游戏。</span><span class="en">Add another <code>print("...")</code> line with your favourite game.</span></li>
  <li>🐞 <span class="zh">故意删掉一个引号 <code>"</code>，运行，看电脑怎么「抱怨」，再修好它。</span><span class="en">Delete one quote <code>"</code> on purpose, run it, see how the computer complains, then fix it.</span></li>
</ul>

<div class="box box-good"><span class="zh">💡 <b>报错不是失败</b>，是电脑在告诉你：哪一行、出了什么问题。</span><span class="en">💡 <b>An error is not a failure</b> — the computer is telling you which line and what went wrong.</span></div>

---

## <span class="zh">第 2 步：海龟画正方形 🐢</span><span class="en">Step 2: draw a square with the turtle 🐢</span>

<p><span class="zh">Python 里有一只<b>拿着笔的海龟</b>：</span><span class="en">Python has a <b>turtle holding a pen</b>:</span></p>

<div class="cmds">
  <div class="cmd"><code>t.forward(100)</code><span><span class="zh">往前走 100 步（边走边画线）</span><span class="en">Move forward 100 steps (drawing a line)</span></span></div>
  <div class="cmd"><code>t.left(90)</code><span><span class="zh">向左转 90 度</span><span class="en">Turn left 90 degrees</span></span></div>
  <div class="cmd"><code>t.color("red")</code><span><span class="zh">换笔的颜色</span><span class="en">Change the pen colour</span></span></div>
  <div class="cmd"><code>t.pensize(5)</code><span><span class="zh">笔变粗</span><span class="en">Make the pen thicker</span></span></div>
</div>

### 🤔 <span class="zh">先猜，再运行</span><span class="en">Guess first, then run</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">下面的代码，海龟会画出什么？（先别点运行！）</span><span class="en">What will the turtle draw with the code below? (Don't click Run yet!)</span></p>
  <div class="opts"><button><span class="zh">一条直线</span><span class="en">A straight line</span></button><button><span class="zh">正方形</span><span class="en">A square</span></button><button><span class="zh">三角形</span><span class="en">A triangle</span></button></div>
  <div class="why"><span class="zh">走 100 → 左转 90° → 一共 4 次，每次转直角，就是正方形！</span><span class="en">Move 100 → turn left 90° → 4 times, a right angle each time: that's a square!</span></div>
</div>

<div class="playground" data-src="{{ '/lessons/01/code/square.py' | relative_url }}" data-title="🟩 正方形" data-title-en="🟩 Square" data-save="my-square"></div>

### 🔍 <span class="zh">改一改</span><span class="en">Change it</span>

<div class="quiz" data-answer="2">
  <p class="q"><span class="zh">如果把<b>所有的 90</b> 都改成 <b>120</b>，会画出什么？先猜，再去上面改了试试！</span><span class="en">If you change <b>every 90</b> to <b>120</b>, what will it draw? Guess first, then try it above!</span></p>
  <div class="opts"><button><span class="zh">还是正方形</span><span class="en">Still a square</span></button><button><span class="zh">三角形</span><span class="en">A triangle</span></button><button><span class="zh">一团乱线</span><span class="en">A messy scribble</span></button></div>
  <div class="why"><span class="zh">三角形！每次转 120°，转 3 次正好一圈（360°），海龟回到起点，第 4 条边和第 1 条重叠了。</span><span class="en">A triangle! Turning 120° three times is exactly one full turn (360°), so the turtle is back at the start — the 4th side goes over the 1st.</span></div>
</div>

<ul class="quests" data-key="l1-modify">
  <li>🎨 <span class="zh">加一行 <code>t.color("hotpink")</code> 换颜色（试试 red、gold、blue、purple）</span><span class="en">Add <code>t.color("hotpink")</code> to change colour (try red, gold, blue, purple)</span></li>
  <li>✏️ <span class="zh">加一行 <code>t.pensize(8)</code> 让线变粗</span><span class="en">Add <code>t.pensize(8)</code> for a thicker line</span></li>
  <li>📏 <span class="zh">把 100 改成 200，让正方形变大</span><span class="en">Change 100 to 200 to make it bigger</span></li>
</ul>

<div class="box box-tip"><span class="zh">⚠️ 颜色要加<b>英文引号</b>：<code>"red"</code> ✅ &nbsp; <code>red</code> ❌ &nbsp; <code>“red”</code> ❌（中文引号）</span><span class="en">⚠️ Colours need <b>straight quotes</b>: <code>"red"</code> ✅ &nbsp; <code>red</code> ❌ &nbsp; <code>“red”</code> ❌ (curly/Chinese quotes)</span></div>

### 🏆 <span class="zh">挑战：三角形，然后五角星！</span><span class="en">Challenge: a triangle, then a star!</span>

<p><span class="zh">把 <code>___</code> 换成正确的数字，画出三角形。画好了？再改一改，试试<b>五角星</b>！</span><span class="en">Replace <code>___</code> with the right number to draw a triangle. Done? Now change it to make a <b>star</b>!</span></p>

<div class="playground" data-src="{{ '/lessons/01/code/challenge.py' | relative_url }}" data-title="🏆 挑战画板" data-title-en="🏆 Challenge" data-save="my-shapes" data-draft="l1-challenge"></div>

<details class="hint"><summary><span class="zh">💡 三角形提示</span><span class="en">💡 Triangle hint</span></summary><span class="zh">海龟走一圈一共转 360 度，三角形转 3 次，每次转 360 ÷ 3 = ？</span><span class="en">One full trip around is 360 degrees. A triangle turns 3 times, so each turn is 360 ÷ 3 = ?</span></details>
<details class="hint"><summary><span class="zh">🌟 五角星提示</span><span class="en">🌟 Star hint</span></summary><span class="zh">五角星走 5 次、转 5 次。每次转的角度在 130 到 150 之间，试试哪个能「合上」！</span><span class="en">A star has 5 lines and 5 turns. Each turn is between 130 and 150 degrees — find the one that closes up!</span></details>

---

## <span class="zh">第 3 步：✨ 让 AI 帮你画</span><span class="en">Step 3: ✨ draw with AI</span>
{: #ai-magic}

<p><span class="zh">正方形是你自己写的。现在请 <b>Codex</b> 帮你画一个更厉害的！记住：<b>你是队长，AI 是队员</b>。</span><span class="en">You wrote the square yourself. Now ask <b>Codex</b> to help with something fancier! Remember: <b>you're the captain, AI is on your team</b>.</span></p>

### ① <span class="zh">写一段清楚的指令</span><span class="en">Write clear instructions</span>

<div class="recipe">
  <label for="r-what">🎯 <span class="zh">画什么？</span><span class="en">What to draw?</span></label>
  <input id="r-what" name="what" data-ph-zh="比如：一朵有 8 片花瓣的花" data-ph-en="e.g. a flower with 8 petals" placeholder="比如：一朵有 8 片花瓣的花">
  <div class="chips" data-for="what"><button class="chip"><span class="zh">一朵有 8 片花瓣的花</span><span class="en">a flower with 8 petals</span></button><button class="chip"><span class="zh">一个彩色的螺旋</span><span class="en">a colourful spiral</span></button><button class="chip"><span class="zh">黑夜里的满天星星</span><span class="en">lots of stars in a night sky</span></button></div>
  <label for="r-detail">🔍 <span class="zh">细节（大小、数量……）</span><span class="en">Details (size, how many…)</span></label>
  <input id="r-detail" name="detail" data-ph-zh="比如：在画布中间，大大的" data-ph-en="e.g. big, in the middle" placeholder="比如：在画布中间，大大的">
  <label for="r-colors">🎨 <span class="zh">颜色</span><span class="en">Colours</span></label>
  <input id="r-colors" name="colors" data-ph-zh="比如：彩虹色，黑色背景" data-ph-en="e.g. rainbow colours, black background" placeholder="比如：彩虹色，黑色背景">
  <input type="hidden" name="extra" value="">
  <div class="result"></div>
  <div class="score"></div>
  <p><button class="pg-btn run copy-prompt"><span class="zh">📋 复制这段指令</span><span class="en">📋 Copy these instructions</span></button></p>
</div>

### ② <span class="zh">发给 Codex，把代码贴到这里运行</span><span class="en">Send it to Codex, then paste the code here and run it</span>

<div class="playground" data-title="✨ AI 画板" data-title-en="✨ AI Playground" data-save="ai-art-01" data-draft="l1-ai">
<textarea># 把 Codex 写的代码粘贴到这里（先删掉这两行），然后点 ▶ 运行
# Paste Codex's code here (delete these 2 lines first), then click ▶ Run
</textarea>
</div>

### ③ <span class="zh">当检查员</span><span class="en">Be the checker</span>

<ul class="quests" data-key="l1-ai">
  <li>🔢 <span class="zh">找 <b>1 个数字</b>改一改，看画有什么变化</span><span class="en">Change <b>one number</b> and see what happens</span></li>
  <li>❓ <span class="zh">找一行看不懂的，问 Codex：「这一行是什么意思？用小学生能懂的话解释」</span><span class="en">Find a line you don't understand and ask Codex: "What does this line mean? Explain it simply."</span></li>
  <li>📤 <span class="zh">满意了？点 <b>存到作品墙</b>！</span><span class="en">Happy with it? Click <b>Save to Gallery</b>!</span></li>
</ul>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none;font-size:1.1rem" href="{{ '/lessons/01/homework/' | relative_url }}"><span class="zh">下一步：看看作业 🏠 →</span><span class="en">Next: homework 🏠 →</span></a></p>
