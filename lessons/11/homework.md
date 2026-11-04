---
title: 第 11 课 · 作业
title_en: Lesson 11 · Homework
lesson: "11"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 11 课作业：把项目做完</span><span class="en">Lesson 11 homework: finish the project</span>

<p><span class="zh">这周的作业就是<b>你的项目</b>。不用新学什么，就是：做 → 测 → 修 → 存。</span><span class="en">This week's homework is <b>your project</b>. Nothing new to learn — just build → test → fix → save.</span> <span class="pill">⏱ <span class="zh">大约 60 分钟，可以分几次</span><span class="en">about 60 minutes, in a few sittings</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week11-project.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：3 个功能都能跑</span><span class="en">Must do: all 3 features run</span></h3>
    <p><span class="zh">计划里的 <b>功能 1、2、3</b> 都做出来，从头运行<b>没有红字</b>，<code>test()</code> 打印「✅ 测试通过」。不漂亮没关系，<b>能跑</b>就是胜利。</span><span class="en">Build <b>features 1, 2 and 3</b> from your plan, run from scratch with <b>no red text</b>, and <code>test()</code> prints "✅". Pretty doesn't matter; <b>running</b> is the win.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：一个加分功能 + 不怕乱输入</span><span class="en">Bonus: one bonus feature + survives silly input</span></h3>
    <p><span class="zh">做一个计划里的 ⭐ 加分功能。然后按<a href="../learn/#tests">测试清单</a>故意弄坏它：输入「abc」、按 100 次键、直接回车……程序不能崩。</span><span class="en">Add one ⭐ bonus feature from your plan. Then try to break it with the <a href="../learn/#tests">test checklist</a>: type "abc", press a key 100 times, hit Enter on nothing… it must not crash.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：找一个真人来玩</span><span class="en">Challenge: get a real person to play</span></h3>
    <p><span class="zh">让家人或朋友玩 3 分钟，<b>不要解释</b>，只看。他们卡在哪里？找到一个问题，修好它，在代码最上面的注释里写：「XX 发现了 ___，我把 ___ 改成了 ___」。</span><span class="en">Let a family member or friend play for 3 minutes, <b>don't explain</b>, just watch. Where do they get stuck? Find one problem, fix it, and write in the top comment: "XX found ___, I changed ___ to ___".</span></p>
  </div></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">写的代码会自动记在这台电脑上。把第 10 课的骨架或 <code>week10-plan</code> 里的代码粘贴进来。</span><span class="en">Your code is saved on this computer automatically. Paste in the skeleton from Lesson 10 or your <code>week10-plan</code> code.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/homework.py' | relative_url }}" data-title="🛠️ 我的项目 v1" data-title-en="🛠️ My project v1" data-save="week11-project" data-draft="l11-homework" data-rows="22" data-images></div>

<details class="hint"><summary><span class="zh">💡 卡住了，不知道先做什么？</span><span class="en">💡 Stuck, don't know what to do first?</span></summary><span class="zh">把功能 1 再拆小：「海龟能左右动」→ 先只做「按 → 往右走」，一行 <code>onkey</code> + 一个函数。跑通了再加 ←。<b>每次只加 3 行就运行一次。</b></span><span class="en">Split feature 1 smaller: "turtle moves left/right" → first just "press → moves right": one <code>onkey</code> + one function. Works? Add ←. <b>Add 3 lines, run, repeat.</b></span></details>
<details class="hint"><summary><span class="zh">💡 报错了怎么办？</span><span class="en">💡 Got an error?</span></summary><span class="zh">四步法！① 读红框，看第几行、什么种类（<a href="../learn/#toolbox">第 11 课的表</a>）② 翻<a href="{{ '/notebook/' | relative_url }}">笔记本</a> ③ 点红框里的「复制问 AI 要提示的话」④ 下节课问老师，<b>先把报错截图或抄下来</b>。</span><span class="en">The 4 steps! ① Read the red box: which line, which kind (<a href="../learn/#toolbox">Lesson 11's table</a>) ② check your <a href="{{ '/notebook/' | relative_url }}">notebook</a> ③ click "copy a hint-please message for AI" in the red box ④ ask the teacher next lesson — <b>write the error down first</b>.</span></details>
<details class="hint"><summary><span class="zh">💡 test() 里写什么？</span><span class="en">💡 What goes in test()?</span></summary><span class="zh">检查你的函数算得对不对。比如翻译 app：<code>assert translate("kia ora") == "你好"</code>；游戏：<code>assert hit(0, 0, 0, 10) == True</code>（两个东西距离 10 算碰到）。一个 assert 就够 🥉。</span><span class="en">Check your functions give the right answer. Translator app: <code>assert translate("kia ora") == "hello"</code>; game: <code>assert hit(0, 0, 0, 10) == True</code> (distance 10 counts as a hit). One assert is enough for 🥉.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week11-project</code>，在 GitHub 页面点 <b>Commit changes</b>。（中途也要存！名字已存在就加 <code>-v2</code>。）</span><span class="en">Click <b>📤 Save to Gallery</b>, name it <code>week11-project</code>, click <b>Commit changes</b> on GitHub. (Save along the way too! If the name exists, add <code>-v2</code>.)</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 第 11 课写 3 行：做到了什么 / 最难的 bug / 怎么解决的。</span><span class="en">Write 3 lines under Lesson 11 in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what got done / hardest bug / how I fixed it.</span></li>
  <li><span class="zh">想想下周给谁展示。</span><span class="en">Think about who you'll show it to next week.</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：展示日 + 部署上线！</b>你的项目会变成<b>网上的一个页面</b>，有链接，谁都能打开玩。把家人叫来当观众吧。</span><span class="en">🔮 <b>Next week: show day + going live!</b> Your project becomes <b>a page on the web</b> with a link anyone can open and play. Invite your family to be the audience.</span></div>
