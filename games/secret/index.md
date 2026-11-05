---
title: 密码破译
title_en: Secret Code
playground: true
---

# 🔐 <span class="zh">密码破译</span><span class="en">Secret Code</span>

<p class="zh">每一关都藏着一个密码。你的任务：<b>改代码</b>，让程序打印出<b>一模一样</b>的密码（大小写、空格、换行都要一样）。运行后画板会把<b>你的输出</b>和<b>需要的输出</b>放在一起对比，看看差在哪里。关卡越往后，需要的魔法越多：变量 → 字符串 → 循环 → 列表。</p>
<p class="en">Every level hides a secret. Your job: <b>change the code</b> so the program prints the secret <b>exactly</b> (capitals, spaces and line breaks all count). After you run it, the playground shows <b>your output</b> next to the <b>wanted output</b> so you can spot the difference. Later levels need more magic: variables → strings → loops → lists.</p>

<div class="levels-bar">
  <a href="#lv1" data-badge-id="secret-1">1</a><a href="#lv2" data-badge-id="secret-2">2</a><a href="#lv3" data-badge-id="secret-3">3</a><a href="#lv4" data-badge-id="secret-4">4</a><a href="#lv5" data-badge-id="secret-5">5</a><a href="#lv6" data-badge-id="secret-6">6</a>
</div>

<div class="level-head" id="lv1" data-badge-id="secret-1"><span class="lv"><span class="zh">第 1 关</span><span class="en">Level 1</span></span><b><span class="zh">一字不差</span><span class="en">Exactly right</span></b><span class="pill">📘 <span class="zh">需要第 1 课</span><span class="en">Needs Lesson 1</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">让程序打印：<code>KIA ORA</code>（毛利语「你好」）</span><span class="en">Make the program print: <code>KIA ORA</code> (Māori for "hello")</span></div>
<div class="playground" data-src="{{ '/games/secret/code/level1-start.py' | relative_url }}" data-title="🔐 第 1 关" data-title-en="🔐 Level 1" data-save="secret-1" data-draft="secret-1" data-rows="6" data-canvas="no" data-expect="KIA ORA" data-badge="secret-1"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">运行一下，看看左右两边哪里不一样。大写和小写，电脑觉得是<b>不同的字</b>。</span><span class="en">Run it and compare the two sides. To a computer, capital and small letters are <b>different</b>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">引号里的字会<b>原封不动</b>地打印出来。所以引号里写什么，就出来什么。</span><span class="en">Whatever is inside the quotes is printed <b>exactly as written</b>.</span></details>

<div class="level-head" id="lv2" data-badge-id="secret-2"><span class="lv"><span class="zh">第 2 关</span><span class="en">Level 2</span></span><b><span class="zh">变量</span><span class="en">Variables</span></b><span class="pill">📘 <span class="zh">需要第 2 课</span><span class="en">Needs Lesson 2</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">只用变量 <code>word</code> 和 <code>number</code>（不要直接打 kiwi），打印两行：<code>kiwi kiwi</code> 和 <code>I have 3 kiwis</code></span><span class="en">Using only the variables <code>word</code> and <code>number</code> (don't type kiwi yourself), print two lines: <code>kiwi kiwi</code> and <code>I have 3 kiwis</code></span></div>
<div class="cmds small">
  <div class="cmd"><code>print(a, b)</code><span><span class="zh">打印两个东西，中间自动加空格</span><span class="en">Print two things with a space between</span></span></div>
  <div class="cmd"><code>print(f"I am {age}")</code><span><span class="zh">f 字符串：把变量塞进句子</span><span class="en">f-string: put a variable inside a sentence</span></span></div>
</div>
<div class="playground" data-src="{{ '/games/secret/code/level2-start.py' | relative_url }}" data-title="🔐 第 2 关" data-title-en="🔐 Level 2" data-save="secret-2" data-draft="secret-2" data-rows="8" data-canvas="no" data-expect="kiwi kiwi\nI have 3 kiwis" data-badge="secret-2"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh"><code>print(word, word)</code> 会打印两次，中间有一个空格。</span><span class="en"><code>print(word, word)</code> prints it twice with a space in between.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">第二行用 f 字符串：<code>print(f"I have {number} kiwis")</code>——注意引号前面的小 <code>f</code> 和花括号 <code>{ }</code>。</span><span class="en">Second line with an f-string: <code>print(f"I have {number} kiwis")</code> — note the little <code>f</code> before the quote and the curly braces <code>{ }</code>.</span></details>

<div class="level-head" id="lv3" data-badge-id="secret-3"><span class="lv"><span class="zh">第 3 关</span><span class="en">Level 3</span></span><b><span class="zh">倒过来</span><span class="en">Backwards</span></b><span class="pill">📘 <span class="zh">需要第 2 课</span><span class="en">Needs Lesson 2</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh"><code>secret</code> 是倒着写的。把它倒回来、变成大写，打印 <code>KIWI</code>。不能直接打 KIWI 哦！</span><span class="en"><code>secret</code> is written backwards. Reverse it, make it uppercase and print <code>KIWI</code>. No typing KIWI yourself!</span></div>
<div class="cmds small">
  <div class="cmd"><code>word.upper()</code><span><span class="zh">全部变大写</span><span class="en">All capitals</span></span></div>
  <div class="cmd"><code>word.lower()</code><span><span class="zh">全部变小写</span><span class="en">All lowercase</span></span></div>
  <div class="cmd"><code>word[::-1]</code><span><span class="zh">倒过来（魔法咒语，照抄就行）</span><span class="en">Reversed (a magic spell — just copy it)</span></span></div>
  <div class="cmd"><code>len(word)</code><span><span class="zh">有几个字母</span><span class="en">How many letters</span></span></div>
</div>
<div class="playground" data-src="{{ '/games/secret/code/level3-start.py' | relative_url }}" data-title="🔐 第 3 关" data-title-en="🔐 Level 3" data-save="secret-3" data-draft="secret-3" data-rows="7" data-canvas="no" data-expect="KIWI" data-badge="secret-3"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">先试 <code>print(secret[::-1])</code>，看看出来什么。</span><span class="en">Try <code>print(secret[::-1])</code> first and see what comes out.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">魔法可以连着用：<code>secret[::-1].upper()</code>。</span><span class="en">Spells can be chained: <code>secret[::-1].upper()</code>.</span></details>

<div class="level-head" id="lv4" data-badge-id="secret-4"><span class="lv"><span class="zh">第 4 关</span><span class="en">Level 4</span></span><b><span class="zh">一行一个字母</span><span class="en">One letter per line</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">把 <code>word</code> 的每个字母各打印一行，最后打印 <code>4 letters</code>（用 <code>len</code> 数，不要自己写 4）</span><span class="en">Print each letter of <code>word</code> on its own line, then print <code>4 letters</code> (count with <code>len</code>, don't type the 4)</span></div>
<div class="cmds small">
  <div class="cmd"><code>for c in word:</code><span><span class="zh">对 word 里的每个字母 c 做一次（下面要缩进）</span><span class="en">Do this once for each letter c in word (indent the lines below)</span></span></div>
</div>
<div class="playground" data-src="{{ '/games/secret/code/level4-start.py' | relative_url }}" data-title="🔐 第 4 关" data-title-en="🔐 Level 4" data-save="secret-4" data-draft="secret-4" data-rows="8" data-canvas="no" data-expect="K\nO\nR\nU\n4 letters" data-badge="secret-4"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">循环可以走过一个词的每个字母，就像走过 <code>range(4)</code> 的每个数字一样：<code>for c in word:</code> 然后缩进 <code>print(c)</code>。</span><span class="en">A loop can walk through every letter of a word, just like the numbers of <code>range(4)</code>: <code>for c in word:</code> then an indented <code>print(c)</code>.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">最后一行<b>不要缩进</b>（它不在循环里）：<code>print(len(word), "letters")</code>。</span><span class="en">The last line is <b>not indented</b> (it's outside the loop): <code>print(len(word), "letters")</code>.</span></details>

<div class="level-head" id="lv5" data-badge-id="secret-5"><span class="lv"><span class="zh">第 5 关</span><span class="en">Level 5</span></span><b><span class="zh">拼图</span><span class="en">Puzzle pieces</span></b><span class="pill">📘 <span class="zh">需要第 5 课</span><span class="en">Needs Lesson 5</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">密码的字母被打乱放进了列表 <code>pieces</code>。正确顺序是第 <b>1、3、2、0</b> 格。把它们拼成一行：<code>KORU</code></span><span class="en">The letters are scrambled in the list <code>pieces</code>. The right order is index <b>1, 3, 2, 0</b>. Join them into one line: <code>KORU</code></span></div>
<div class="cmds small">
  <div class="cmd"><code>pieces[0]</code><span><span class="zh">列表的第 0 格（第一格是 0 不是 1！）</span><span class="en">Item 0 of the list (the first one is 0, not 1!)</span></span></div>
  <div class="cmd"><code>"a" + "b"</code><span><span class="zh">把两段文字接起来 → "ab"</span><span class="en">Join two pieces of text → "ab"</span></span></div>
</div>
<div class="playground" data-src="{{ '/games/secret/code/level5-start.py' | relative_url }}" data-title="🔐 第 5 关" data-title-en="🔐 Level 5" data-save="secret-5" data-draft="secret-5" data-rows="7" data-canvas="no" data-expect="KORU" data-badge="secret-5"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">先试 <code>print(pieces[1])</code>，是不是 K？</span><span class="en">Try <code>print(pieces[1])</code> first — is it K?</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">用 <code>+</code> 把四格接起来放进一个 print 里：<code>pieces[1] + pieces[3] + …</code></span><span class="en">Use <code>+</code> to join the four items inside one print: <code>pieces[1] + pieces[3] + …</code></span></details>

<div class="level-head" id="lv6" data-badge-id="secret-6"><span class="lv"><span class="zh">第 6 关</span><span class="en">Level 6</span></span><b><span class="zh">凯撒密码</span><span class="en">Caesar cipher</span></b><span class="pill">📘 <span class="zh">需要第 3 课</span><span class="en">Needs Lesson 3</span></span><span class="done-mark">⭐</span></div>
<div class="goal">🎯 <span class="zh">两千年前的罗马将军凯撒就是这样写密信的：每个字母往前推 1 个（a→b，k→l）。<code>secret</code> 被推过了，你把每个字母<b>退回 1 个</b>，拼成词打印出来。</span><span class="en">Julius Caesar wrote secret letters this way 2000 years ago: shift every letter forward by 1 (a→b, k→l). <code>secret</code> has been shifted — move every letter <b>back by 1</b>, join them and print the word.</span></div>
<div class="cmds small">
  <div class="cmd"><code>ord("a")</code><span><span class="zh">字母变成它的号码 → 97</span><span class="en">Letter → its number → 97</span></span></div>
  <div class="cmd"><code>chr(98)</code><span><span class="zh">号码变回字母 → "b"</span><span class="en">Number → letter → "b"</span></span></div>
  <div class="cmd"><code>result = result + c</code><span><span class="zh">把字母 c 接到 result 后面</span><span class="en">Stick letter c onto the end of result</span></span></div>
</div>
<div class="playground" data-src="{{ '/games/secret/code/level6-start.py' | relative_url }}" data-title="🔐 第 6 关" data-title-en="🔐 Level 6" data-save="secret-6" data-draft="secret-6" data-rows="9" data-canvas="no" data-expect="kiwi" data-badge="secret-6"></div>
<details class="hint"><summary>💡 <span class="zh">提示 1</span><span class="en">Hint 1</span></summary><span class="zh">一个字母退 1 格：<code>chr(ord(c) - 1)</code>。先用 <code>print(chr(ord("l") - 1))</code> 试试。</span><span class="en">One letter back by 1: <code>chr(ord(c) - 1)</code>. Try <code>print(chr(ord("l") - 1))</code> first.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 2</span><span class="en">Hint 2</span></summary><span class="zh">先做一个空袋子 <code>result = ""</code>，然后 <code>for c in secret:</code> 里每次把退好的字母接到袋子后面，循环结束再 <code>print(result)</code>。</span><span class="en">Start with an empty bag <code>result = ""</code>, then inside <code>for c in secret:</code> add each shifted letter to the bag, and <code>print(result)</code> after the loop.</span></details>
<details class="hint"><summary>💡 <span class="zh">提示 3（差不多是答案了）</span><span class="en">Hint 3 (almost the answer)</span></summary><pre>result = ""
for c in secret:
    result = result + chr(ord(c) - 1)
print(result)</pre></details>

<div class="box box-think"><span class="box-title"><span class="zh">🧠 六关都过了？</span><span class="en">🧠 Beaten all six?</span></span>
<span class="zh">自己发明一个密码：在 <a href="{{ '/playground/' | relative_url }}">画板</a> 里把一句话往前推 3 个字母（<code>chr(ord(c) + 3)</code>），存到作品墙，让老师或朋友来破译！</span>
<span class="en">Invent your own code: in the <a href="{{ '/playground/' | relative_url }}">Playground</a>, shift a sentence forward by 3 letters (<code>chr(ord(c) + 3)</code>), save it to the Gallery and challenge your teacher or a friend to crack it!</span></div>

<p style="text-align:center;margin-top:2em"><a class="pg-btn run" style="text-decoration:none" href="{{ '/games/' | relative_url }}">🎮 <span class="zh">回到游戏板块</span><span class="en">Back to Games</span></a></p>
