---
title: 第 8 课 · 作业
title_en: Lesson 8 · Homework
lesson: "08"
tab: homework
playground: true
---

# 🎮 <span class="zh">第 8 课作业：我的对战游戏</span><span class="en">Lesson 8 homework: My Battle Game</span>

<p><span class="zh">把课上的石头剪刀布<b>做完、做好、做成你自己的</b>，然后和家人对战！</span><span class="en">Finish the Rock Paper Scissors from class, <b>polish it, make it yours</b>, then challenge your family!</span> <span class="pill">⏱ <span class="zh">🥉 约 25 分钟，🥈🥇 再加 20–40 分钟</span><span class="en">🥉 about 25 min, 🥈🥇 another 20–40 min</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week08-homework.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：judge + 英文也能玩 + 记分</span><span class="en">Must do: judge + English input + scoring</span></h3>
    <p><span class="zh">画板里有 3 个 ✍️ TODO：① 用 <code>beats_what</code> 写 judge 的「赢」② 写 <code>to_chinese(word)</code>：<code>"  ROCK "</code>、<code>"Paper"</code> 这种乱七八糟的英文也能变成中文的拳 ③ 加分（平局记到 ties）。<b>两行测试全部是 True</b> 才去玩。最后当捣蛋鬼测一遍：香蕉、空、带空格、大写英文。</span><span class="en">The playground has 3 ✍️ TODOs: ① use <code>beats_what</code> for judge's "win" ② write <code>to_chinese(word)</code> so messy English like <code>"  ROCK "</code> or <code>"Paper"</code> becomes the Chinese play ③ scoring (ties go into ties). Only play once <b>both test lines are all True</b>. Then test like a troublemaker: banana, nothing, spaces, CAPITAL English.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：N 局几胜 + 再来一局 + 总统计</span><span class="en">Bonus: best of N + play again + overall stats</span></h3>
    <p><span class="zh">先问「几局几胜？」，<b>只接受 3、5、7</b>（不是就一直问——写一个像 <code>ask_player</code> 的招式）。用 <code>play_game(target)</code> 玩，玩完问「再来一局？」。最后打印：赢几局、输几局、一共平了几轮、你的<b>总胜率 %</b>。</span><span class="en">Ask "best of how many?" and <b>accept only 3, 5 or 7</b> (keep asking otherwise — write a trick like <code>ask_player</code>). Play with <code>play_game(target)</code>, then ask "play again?". At the end print games won, games lost, total tied rounds and your <b>overall win rate %</b>.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：会学习的对手 + 做一个小实验</span><span class="en">Challenge: a learning opponent + a mini experiment</span></h3>
    <p><span class="zh">加「简单 / 困难」两个模式：简单 = 随机；困难 = 像学一学第 5 步那样<b>数你的拳</b>，出能赢你最爱的拳。然后当科学家：两个模式<b>各玩 15 轮以上</b>，把你的胜率写进代码最上面的「实验记录」。哪个更难打？为什么？再想一招让困难模式更聪明（比如记住你<b>上一轮</b>出了什么）。</span><span class="en">Add "easy / hard" modes: easy = random; hard = <b>count your moves</b> like Learn step 5 and play what beats your favourite. Then be a scientist: play <b>15+ rounds in each mode</b> and write your win rates in the "experiment notes" at the top. Which is harder? Why? Then think of one more trick to make hard mode smarter (e.g. remember what you played <b>last round</b>).</span></p>
  </div></div>
</div>

<div class="cmds">
  <div class="cmd"><code>word = word.strip().lower()</code><span><span class="zh">整理输入（要存回去！）</span><span class="en">Tidy the input (store it back!)</span></span></div>
  <div class="cmd"><code>if beats_what(me) == computer:</code><span><span class="zh">用规则招式判断赢</span><span class="en">Spot a win with the rule trick</span></span></div>
  <div class="cmd"><code>return a, b, c</code><span><span class="zh">一次交回三个数（先当魔法用）</span><span class="en">Return three numbers at once (treat as magic)</span></span></div>
  <div class="cmd"><code>int(wins / rounds * 100)</code><span><span class="zh">胜率 %</span><span class="en">Win rate %</span></span></div>
  <div class="cmd"><code>counts[i] += 1</code><span><span class="zh">用列表数数（🥇）</span><span class="en">Count with a list (🥇)</span></span></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上，关掉网页也不会丢。</span><span class="en">Your code is saved on this computer automatically, even if you close the page.</span></p>

<div class="playground" data-src="{{ '/lessons/08/code/homework.py' | relative_url }}" data-canvas="no" data-title="🎮 我的对战游戏" data-title-en="🎮 My Battle Game" data-save="week08-homework" data-draft="l8-homework" data-rows="20"></div>

<details class="hint"><summary><span class="zh">💡 judge 提示</span><span class="en">💡 judge hint</span></summary><span class="zh">只要两行：<code>if beats_what(me) == computer:</code> 下一行 <code>return "赢"</code>。看学一学第 3 步的「进阶」。</span><span class="en">Just two lines: <code>if beats_what(me) == computer:</code> then <code>return "赢"</code>. See the stretch part of Learn step 3.</span></details>
<details class="hint"><summary><span class="zh">💡 to_chinese 提示</span><span class="en">💡 to_chinese hint</span></summary><span class="zh">第一行已经把 word 整理好了。然后 <code>if word == "rock": return "石头"</code>，再两个 <code>elif</code>。认不出的就走到最后的 <code>return word</code>——所以中文的「石头」也能原样通过。</span><span class="en">The first line already tidies word. Then <code>if word == "rock": return "石头"</code>, plus two <code>elif</code>s. Anything else reaches the final <code>return word</code> — so Chinese 石头 passes straight through too.</span></details>
<details class="hint"><summary><span class="zh">💡 🥈 只接受 3、5、7</span><span class="en">💡 🥈 accept only 3, 5, 7</span></summary><span class="zh">照着 <code>ask_player</code> 写 <code>ask_best_of()</code>：<code>while True</code> → <code>n = input(...).strip()</code> → <code>if n == "3" or n == "5" or n == "7": return int(n)</code>。先比较文字再 <code>int()</code>，输入 abc 也不会报错！</span><span class="en">Copy the shape of <code>ask_player</code> into <code>ask_best_of()</code>: <code>while True</code> → <code>n = input(...).strip()</code> → <code>if n == "3" or n == "5" or n == "7": return int(n)</code>. Compare the text first and <code>int()</code> afterwards, so typing abc can't crash it!</span></details>
<details class="hint"><summary><span class="zh">💡 🥇 困难模式</span><span class="en">💡 🥇 hard mode</span></summary><span class="zh">把学一学第 5 步的 <code>counts</code>、<code>winner_against</code>、<code>favourite</code> 搬过来。写 <code>computer_move(mode, rounds)</code>：<code>mode == "hard"</code> 而且 <code>rounds &gt;= 3</code> 时出 <code>winner_against(favourite())</code>，其他时候随机。</span><span class="en">Bring over <code>counts</code>, <code>winner_against</code> and <code>favourite</code> from Learn step 5. Write <code>computer_move(mode, rounds)</code>: when <code>mode == "hard"</code> and <code>rounds &gt;= 3</code> play <code>winner_against(favourite())</code>, otherwise random.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week08-homework</code>，在 GitHub 页面点 <b>Commit changes</b>。</span><span class="en">Click <b>📤 Save to Gallery</b> on the homework playground, name it <code>week08-homework</code>, then click <b>Commit changes</b> on GitHub.</span></li>
  <li><span class="zh">回到这一页刷新，上面变成 ✅ 就交好了。</span><span class="en">Come back and refresh this page; when it shows ✅ you're done.</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 写 3 行，特别写下 <b>AI 帮你排错的一次</b>。</span><span class="en">Write 3 lines in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>, especially <b>a time AI helped you debug</b>.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：</b>字典 <code>{ "kiwi": "奇异鸟" }</code>——一本你自己写的翻译书！<code>counts = [0, 0, 0]</code> 也会变成更聪明的 <code>{"石头": 2, "布": 1}</code>。还要当 <b>AI 侦探</b>：AI 有时候会一本正经地编造，你能抓住它吗？</span><span class="en">🔮 <b>Next week:</b> dictionaries <code>{ "kiwi": "奇异鸟" }</code> — a translation book you write yourself! <code>counts = [0, 0, 0]</code> becomes the smarter <code>{"石头": 2, "布": 1}</code>. And you'll be an <b>AI detective</b>: AI sometimes makes things up with a straight face. Can you catch it?</span></div>
