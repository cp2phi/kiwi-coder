---
title: 第 4 课 · 作业
title_en: Lesson 4 · Homework
lesson: "04"
tab: homework
playground: true
---

# 🎲 <span class="zh">第 4 课作业：猜数字豪华版</span><span class="en">Lesson 4 homework: Guess Deluxe</span>

<p><span class="zh">把课上的猜数字游戏升级成<b>豪华版</b>，然后让家人来挑战！</span><span class="en">Upgrade the guessing game to the <b>deluxe edition</b>, then challenge your family!</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week04-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：1 到 20，6 次机会，记录次数</span><span class="en">Must do: 1–20, 6 tries, count the tries</span></h3>
    <p><span class="zh">画板里的游戏已经差不多了：范围 1–20，6 次机会，<code>count</code> 记录猜了几次。<b>TODO 1</b>：猜小了的时候该说什么？填好，玩一局，让家人也玩一局。</span><span class="en">The game is almost done: range 1–20, 6 tries, <code>count</code> counts guesses. <b>TODO 1</b>: what should it say when the guess is too small? Fill it in, play a round, let a family member play too.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：猜对放烟花 + 再玩一次？</span><span class="en">Bonus: fireworks + play again?</span></h3>
    <p><span class="zh"><b>TODO 2</b>：猜对的时候，让海龟画一个<b>随机颜色</b>的庆祝图案（螺旋、花、随机散步都行）。<b>TODO 3</b>：最后问「再玩一次吗？(y/n)」，用 <code>if answer == "y":</code> 做点什么。</span><span class="en"><b>TODO 2</b>: when the guess is right, the turtle draws a celebration in <b>random colours</b> (spiral, flower, random walk — anything). <b>TODO 3</b>: at the end ask "play again? (y/n)" and do something with <code>if answer == "y":</code>.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战（选做）：冷热提示</span><span class="en">Challenge (optional): hot &amp; cold</span></h3>
    <p><span class="zh"><b>TODO 4</b>：不只说大了小了，还说「差多少」：差 ≤ 2 是 🔥 很热，差 ≤ 5 是 🌤 温的，不然 🧊 很冷。提示：<code>abs(guess - secret)</code>。卡住了？用四步法，问 AI 要<b>提示</b>不要答案，把它给的提示写在代码第 3 行。</span><span class="en"><b>TODO 4</b>: besides big/small, say how close: ≤ 2 away is 🔥 hot, ≤ 5 is 🌤 warm, otherwise 🧊 cold. Hint: <code>abs(guess - secret)</code>. Stuck? Use the 4 steps; ask AI for a <b>hint</b>, not the answer, and write its hint on line 3.</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>count = count + 1</code><span><span class="zh">盒子里的数加 1</span><span class="en">Add 1 to the box</span></span></div>
  <div class="cmd"><code>abs(guess - secret)</code><span><span class="zh">差多少（永远是正数）</span><span class="en">How far apart (always positive)</span></span></div>
  <div class="cmd"><code>answer = input("再玩一次吗? (y/n) ")</code><span><span class="zh">问 y 还是 n</span><span class="en">Ask y or n</span></span></div>
  <div class="cmd"><code>colors[random.randint(0, 2)]</code><span><span class="zh">从 3 个颜色里随机挑（下标 0、1、2）</span><span class="en">Pick one of 3 colours (positions 0, 1, 2)</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。每做完一个 TODO 就运行一次、玩一局。</span><span class="en">Your code is saved on this computer automatically. Run and play a round after every TODO.</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/homework.py' | relative_url }}" data-title="🎲 猜数字豪华版" data-title-en="🎲 Guess Deluxe" data-save="week04-homework" data-draft="l4-homework" data-rows="16"></div>

<details class="hint"><summary><span class="zh">💡 TODO 1 提示</span><span class="en">💡 TODO 1 hint</span></summary><span class="zh">和「太大了」那行一样，只是文字不同。</span><span class="en">Same as the "too big" line, just different words.</span></details>
<details class="hint"><summary><span class="zh">💡 TODO 2 提示</span><span class="en">💡 TODO 2 hint</span></summary><span class="zh">先在最上面写 <code>colors = ["red", "gold", "cyan"]</code>，然后在「猜对了」的 if 里面（<code>break</code> 之前）放一个画画的循环：<code>t.color(colors[random.randint(0, 2)])</code>。</span><span class="en">Write <code>colors = ["red", "gold", "cyan"]</code> at the top, then inside the "you got it" if (before <code>break</code>) put a drawing loop with <code>t.color(colors[random.randint(0, 2)])</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 TODO 4 提示</span><span class="en">💡 TODO 4 hint</span></summary><span class="zh">在「太大了 / 太小了」之后再加：<code>diff = abs(guess - secret)</code>，然后 <code>if diff &lt;= 2:</code> … <code>elif diff &lt;= 5:</code> … <code>else:</code> …。注意缩进要和上面的 if 一样深。</span><span class="en">After the too big / too small part add <code>diff = abs(guess - secret)</code>, then <code>if diff &lt;= 2:</code> … <code>elif diff &lt;= 5:</code> … <code>else:</code> …. Match the indentation of the if above.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week04-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week04-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行 + 今天找到的 bug。</span><span class="en">Write 3 lines + today's bugs in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>例 3 里那个 <code>colors = [...]</code> 的魔法要揭秘了——<b>列表</b>！用它做一个<b>搞笑故事生成器</b>和<b>毛利语单词小测验</b>。想一想：你想让故事里出现哪些搞笑的词？</span><span class="en">🔮 <b>Next week:</b> the <code>colors = [...]</code> magic gets explained — <b>lists</b>! We'll build a <b>silly story maker</b> and a <b>te reo Māori word quiz</b>. Think: what silly words do you want in the story?</span></div>
