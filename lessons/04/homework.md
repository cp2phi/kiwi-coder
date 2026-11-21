---
title: 第 4 课 · 作业
title_en: Lesson 4 · Homework
lesson: "04"
tab: homework
playground: true
---

# 🎲 <span class="zh">第 4 课作业：猜数字豪华版</span><span class="en">Lesson 4 homework: Guess Deluxe</span>

<p><span class="zh">把课上的猜数字游戏升级成<b>豪华版</b>，然后让家人来挑战！这次大部分代码<b>你自己写</b>。</span><span class="en">Upgrade the guessing game to the <b>deluxe edition</b>, then challenge your family! This time you <b>write most of the code yourself</b>.</span> <span class="pill">⏱ <span class="zh">大约 30 分钟（🥇 另算）</span><span class="en">about 30 minutes (🥇 extra)</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week04-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：1 到 50，7 次机会，自己写判断</span><span class="en">Must do: 1–50, 7 tries, write the checks yourself</span></h3>
    <p><span class="zh">循环和 <code>input</code> 已经写好了。<b>TODO 1</b>：自己写 <code>if / elif / else</code>（猜对说用了几次并 <code>break</code>、太大、太小）。<b>TODO 2</b>：每次猜错打印「还剩 ? 次」。玩一局，再让家人玩一局。</span><span class="en">The loop and <code>input</code> are done. <b>TODO 1</b>: write the <code>if / elif / else</code> yourself (correct → say how many tries and <code>break</code>; too big; too small). <b>TODO 2</b>: after each wrong guess print "? tries left". Play a round, then let a family member play.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：更聪明的提示</span><span class="en">Bonus: smarter hints</span></h3>
    <p><span class="zh"><b>TODO 3</b>：差 3 以内说「🔥 很接近了」（if 套 if）。<b>TODO 4</b>：第 3、第 6 次送一条线索——答案是双数还是单数（<code>%</code>）。<b>TODO 5</b>：循环结束后说「🏆 你赢了」还是「😢 机会用完了」。</span><span class="en"><b>TODO 3</b>: within 3 → "🔥 very close" (if inside if). <b>TODO 4</b>: on guesses 3 and 6, a free clue — is the answer even or odd (<code>%</code>)? <b>TODO 5</b>: after the loop, say "🏆 you win" or "😢 out of tries".</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战（选做）：反过来，电脑猜你的数字</span><span class="en">Challenge (optional): reverse — the computer guesses yours</span></h3>
    <p><span class="zh">你想一个 1–100 的数，电脑来猜，你只回答 <code>big</code> / <code>small</code> / <code>yes</code>。电脑<b>最多 7 次</b>，而且<b>一定能猜中</b>。没有起始代码——<b>先在纸上写步骤</b>：电脑要记住哪两个数？每次怎么选？听到 big 以后要改哪个数？卡住了用四步法，问 AI 要<b>提示</b>，把它给的提示写在代码第 3 行。</span><span class="en">You think of a number 1–100, the computer guesses, and you only answer <code>big</code> / <code>small</code> / <code>yes</code>. It gets <b>at most 7 tries</b> and <b>must always win</b>. No starter code — <b>plan the steps on paper first</b>: which two numbers must it remember? How does it pick each guess? After "big", which number changes? Stuck? Use the 4 steps; ask AI for a <b>hint</b> and write its hint on line 3.</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>count = count + 1</code><span><span class="zh">盒子里的数加 1</span><span class="en">Add 1 to the box</span></span></div>
  <div class="cmd"><code>print(f"还剩 {7 - count} 次")</code><span><span class="zh">f-string 里面可以算数</span><span class="en">You can do maths inside an f-string</span></span></div>
  <div class="cmd"><code>if secret % 2 == 0:</code><span><span class="zh">答案是双数吗？</span><span class="en">Is the answer even?</span></span></div>
  <div class="cmd"><code>int((low + high) / 2)</code><span><span class="zh">两个数的正中间（去掉小数）</span><span class="en">Halfway between two numbers (decimals dropped)</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。每做完一个 TODO 就运行一次、玩一局。测试时猜不中？临时加一行 <code>print(secret)</code> 偷看答案——这是真正的程序员技巧，交作业前删掉。</span><span class="en">Your code is saved on this computer automatically. Run and play a round after every TODO. Can't win while testing? Add a temporary <code>print(secret)</code> to peek — a real programmer trick. Delete it before handing in.</span></p>

<div class="playground" data-src="{{ '/lessons/04/code/homework.py' | relative_url }}" data-title="🎲 猜数字豪华版" data-title-en="🎲 Guess Deluxe" data-save="week04-homework" data-draft="l4-homework" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 TODO 1 / 2 提示</span><span class="en">💡 TODO 1 / 2 hint</span></summary><span class="zh">和课上例 3 一样的样子，只是猜对的时候用 f-string 说出 <code>count</code>。TODO 2 的 print 放在 if/elif/else <b>下面</b>、和 <code>if</code> 对齐。猜对的时候 <code>break</code> 已经跳出去了，所以它不会出现——这就是 break 的妙处。</span><span class="en">Same shape as Example 3 in class; the correct branch uses an f-string to say <code>count</code>. Put TODO 2's print <b>below</b> the if/elif/else, lined up with <code>if</code>. On a correct guess <code>break</code> has already left the loop, so it never shows — that's the beauty of break.</span></details>
<details class="hint"><summary><span class="zh">💡 TODO 3 / 4 提示</span><span class="en">💡 TODO 3 / 4 hint</span></summary><span class="zh">TODO 3：在「太大了」的 print 下面（多缩进 4 格）写 <code>if guess - secret &lt;= 3:</code>；太小的那边用 <code>secret - guess</code>。TODO 4：在 TODO 2 旁边写 <code>if count % 3 == 0:</code>，里面<b>再</b>写 <code>if secret % 2 == 0:</code> … <code>else:</code> …。</span><span class="en">TODO 3: under the "too big" print (4 more spaces) write <code>if guess - secret &lt;= 3:</code>; on the too-small side use <code>secret - guess</code>. TODO 4: next to TODO 2 write <code>if count % 3 == 0:</code> and inside it <b>another</b> <code>if secret % 2 == 0:</code> … <code>else:</code> ….</span></details>
<details class="hint"><summary><span class="zh">💡 🥇 提示 1：电脑要记住什么</span><span class="en">💡 🥇 hint 1: what the computer remembers</span></summary><span class="zh">两个变量：<code>low = 1</code> 和 <code>high = 100</code>——「答案一定在 low 和 high 之间」。每次猜正中间：<code>guess = int((low + high) / 2)</code>。</span><span class="en">Two variables: <code>low = 1</code> and <code>high = 100</code> — "the answer is somewhere between low and high". Always guess the middle: <code>guess = int((low + high) / 2)</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 🥇 提示 2：听到回答以后</span><span class="en">💡 🥇 hint 2: after hearing the answer</span></summary><span class="zh">「big」= 电脑猜大了，答案比 guess 小，所以 <code>high = guess - 1</code>。「small」呢？「yes」就 🎉 + <code>break</code>。整个放进 <code>for tries in range(7):</code>。</span><span class="en">"big" = the guess was too big, so the answer is below it: <code>high = guess - 1</code>. And "small"? "yes" → 🎉 + <code>break</code>. Put it all inside <code>for tries in range(7):</code>.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week04-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week04-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面会变成 ✅。</span><span class="en">Come back and refresh — the box above turns ✅.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行 + 今天找到的 bug。</span><span class="en">Write 3 lines + today's bugs in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>第 3 课彩虹螺旋里那个 <code>colors = [...]</code> 的魔法要揭秘了——<b>列表</b>！用它做一个<b>搞笑故事生成器</b>和<b>毛利语单词小测验</b>。想一想：你想让故事里出现哪些搞笑的词？</span><span class="en">🔮 <b>Next week:</b> the <code>colors = [...]</code> magic from lesson 3's rainbow spiral gets explained — <b>lists</b>! We'll build a <b>silly story maker</b> and a <b>te reo Māori word quiz</b>. Think: what silly words do you want in the story?</span></div>
