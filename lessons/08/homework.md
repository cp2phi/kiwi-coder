---
title: 第 8 课 · 作业
title_en: Lesson 8 · Homework
lesson: "08"
tab: homework
playground: true
---

# 🎮 <span class="zh">第 8 课作业：我的对战游戏</span><span class="en">Lesson 8 homework: My Battle Game</span>

<p><span class="zh">把课上的石头剪刀布<b>做完、做好、做成你自己的</b>，然后和家人对战！</span><span class="en">Finish the Rock Paper Scissors from class, <b>polish it, make it yours</b>, then challenge your family!</span> <span class="pill">⏱ <span class="zh">大约 30 分钟</span><span class="en">about 30 minutes</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week08-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：3 分制 + 记分 + 输入检查</span><span class="en">Must do: first-to-3 + scores + input checking</span></h3>
    <p><span class="zh">画板里 <code>judge()</code> 和加分的地方有 TODO。补上，玩一整局。<b>然后当捣蛋鬼测试它</b>：输入香蕉、输入空、带空格。</span><span class="en">The playground has TODOs in <code>judge()</code> and the scoring. Fill them in and play a whole game. <b>Then test it like a troublemaker</b>: type banana, type nothing, add spaces.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：「再来一局？」+ 统计</span><span class="en">Bonus: "play again?" + statistics</span></h3>
    <p><span class="zh">画板里已经有了「再来一局」的循环——<b>读懂它</b>：<code>play_game()</code> 交回两个数是怎么回事？最后那行 <code>你赢了 x 局，电脑赢了 y 局</code> 对吗？再加一个「平局」的统计。</span><span class="en">The "play again" loop is already there — <b>read it</b>: how does <code>play_game()</code> return two numbers? Is the final line <code>You won x, computer won y</code> right? Add a "ties" count too.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：发明你自己的玩法</span><span class="en">Challenge: invent your own variant</span></h3>
    <p><span class="zh">加蜥蜴和史波克；或者「猜拳 + 数字」；或者让海龟把比分画成柱状图；或者给电脑一个 30% 的「作弊」模式。<b>一个就够</b>。遇到 bug 用排错模板问 AI，把那次对话记在代码开头的注释里。</span><span class="en">Add lizard and Spock; or "RPS + numbers"; or make the turtle draw the score as a bar chart; or give the computer a 30% "cheat" mode. <b>One is enough</b>. When you hit a bug, ask AI with the debugging template and note the conversation in the comment at the top.</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>me = input("? ").strip().lower()</code><span><span class="zh">整理输入</span><span class="en">Tidy the input</span></span></div>
  <div class="cmd"><code>if me not in choices:</code><span><span class="zh">乱打就拒绝</span><span class="en">Refuse nonsense</span></span></div>
  <div class="cmd"><code>return a, b</code><span><span class="zh">一次交回两个数</span><span class="en">Return two numbers at once</span></span></div>
  <div class="cmd"><code>random.random() &lt; 0.3</code><span><span class="zh">30% 的时候是 True（作弊模式用）</span><span class="en">True 30% of the time (for cheat mode)</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上，关掉网页也不会丢。</span><span class="en">Your code is saved on this computer automatically, even if you close the page.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/homework.py' | relative_url }}" data-canvas="no" data-title="🎮 我的对战游戏" data-title-en="🎮 My Battle Game" data-save="week08-homework" data-draft="l8-homework" data-rows="18"></div>

<details class="hint"><summary><span class="zh">💡 judge 提示</span><span class="en">💡 judge hint</span></summary><span class="zh">三个「赢」各一行 <code>elif me == ... and computer == ...: return "赢"</code>。写完先用固定的拳 <code>print(judge("石头", "剪刀"))</code> 测一下。</span><span class="en">Three "win" lines: <code>elif me == ... and computer == ...: return "赢"</code>. Then test with fixed plays: <code>print(judge("石头", "剪刀"))</code>.</span></details>
<details class="hint"><summary><span class="zh">💡 加分提示</span><span class="en">💡 Scoring hint</span></summary><span class="zh"><code>if result == "赢": my_score = my_score + 1</code>，<code>elif result == "输": computer_score = computer_score + 1</code>。平局谁都不加。</span><span class="en"><code>if result == "赢": my_score = my_score + 1</code>, <code>elif result == "输": computer_score = computer_score + 1</code>. Nobody scores on a tie.</span></details>
<details class="hint"><summary><span class="zh">💡 平局统计提示</span><span class="en">💡 Tie count hint</span></summary><span class="zh">在 <code>play_game</code> 里加一个 <code>ties</code> 计数器，<code>return my_score, computer_score, ties</code> 交回三个数，外面用 <code>mine, theirs, t = play_game()</code> 接住。</span><span class="en">Add a <code>ties</code> counter inside <code>play_game</code>, <code>return my_score, computer_score, ties</code>, and catch it outside with <code>mine, theirs, t = play_game()</code>.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week08-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week08-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面变成 ✅ 就交好了。</span><span class="en">Come back and refresh this page; when it shows ✅ you're done.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行，特别写下 <b>AI 帮你排错的一次</b>。</span><span class="en">Write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>, especially <b>a time AI helped you debug</b>.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>字典 <code>{ "kiwi": "奇异鸟" }</code>——一本你自己写的翻译书！还要当 <b>AI 侦探</b>：AI 有时候会一本正经地编造，你能抓住它吗？</span><span class="en">🔮 <b>Next week:</b> dictionaries <code>{ "kiwi": "奇异鸟" }</code> — a translation book you write yourself! And you'll be an <b>AI detective</b>: AI sometimes makes things up with a straight face. Can you catch it?</span></div>
