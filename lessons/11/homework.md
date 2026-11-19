---
title: 第 11 课 · 作业
title_en: Lesson 11 · Homework
lesson: "11"
tab: homework
playground: true
---

# 🏠 <span class="zh">第 11 课作业：完成任务 v1</span><span class="en">Lesson 11 homework: finish mission v1</span>

<p><span class="zh">这周的作业就是<b>你的太空任务</b>。不用新学什么，就是：做 → 测 → 修 → 存。</span><span class="en">This week's homework is <b>your space mission</b>. Nothing new to learn — just build → test → fix → save.</span> <span class="pill">⏱ <span class="zh">大约 60 分钟，可以分几次</span><span class="en">about 60 minutes, in a few sittings</span></span> <span class="pill pill-brand">📅 <span class="zh">下节课前交</span><span class="en">due before next lesson</span></span></p>

<div class="hw-status" data-file="week11-project.py"></div>

## 🎖️ <span class="zh">三个等级</span><span class="en">Three levels</span>

<div class="levels">
  <div class="level"><div class="medal">🥉</div><div>
    <h3><span class="zh">必做：3 个必做功能都能跑，测试全绿</span><span class="en">Must do: all 3 must-haves run, all tests green</span></h3>
    <p><span class="zh">按<a href="../learn/#build">开工步骤</a>把<b>必做 1、2、3</b> 都做出来。从头运行<b>没有红字</b>；<code>test()</code> 里<b>没有「睡着的测试」</b>了（所有 <code>#</code> 都删掉了），而且全部通过；再加 <b>1 个你自己的边界测试</b>。可以在 <code>test()</code> 最后加一行 <code>print("✅ 测试通过")</code>，一眼就能看到。不漂亮没关系，<b>能跑</b>就是胜利。</span><span class="en">Follow the <a href="../learn/#build">build steps</a> to make <b>must-haves 1, 2 and 3</b>. Run from scratch with <b>no red text</b>; <code>test()</code> has <b>no "sleeping tests"</b> left (every <code>#</code> removed) and all pass; plus <b>1 edge test of your own</b>. Add <code>print("✅ tests passed")</code> as the last line of <code>test()</code> so you can see it. Pretty doesn't matter; <b>running</b> is the win.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥈</div><div>
    <h3><span class="zh">加分：一个加分功能 + 不怕乱按</span><span class="en">Bonus: one nice-to-have + survives button-mashing</span></h3>
    <p><span class="zh">做一个计划里的 ⭐ 加分功能。然后按<a href="../learn/#tests">测试清单</a>故意弄坏它：乱按键、按 100 次、输入「abc」、直接回车……程序不能崩，结果要合理。</span><span class="en">Add one ⭐ nice-to-have from your plan. Then try to break it with the <a href="../learn/#tests">test checklist</a>: mash keys, press 100 times, type "abc", hit Enter on nothing… it must not crash, and the result must make sense.</span></p>
  </div></div>
  <div class="level"><div class="medal">🥇</div><div>
    <h3><span class="zh">挑战：找一个真人来试飞</span><span class="en">Challenge: get a real person to test-fly it</span></h3>
    <p><span class="zh">让家人或朋友玩 3 分钟，<b>不要解释</b>，只看。他们卡在哪里？太难还是太简单？找到一个问题，修好它（可能只是改一个设置数字！），在代码最上面的注释里写：「XX 发现了 ___，我把 ___ 改成了 ___」。这就是真正的「试飞 → 改进」。</span><span class="en">Let a family member or friend play for 3 minutes, <b>don't explain</b>, just watch. Where do they get stuck? Too hard or too easy? Find one problem and fix it (maybe just one settings number!), then write in the top comment: "XX found ___, I changed ___ to ___". That's a real "test flight → improve".</span></p>
  </div></div>
</div>

## 🧪 <span class="zh">作业画板</span><span class="en">Homework playground</span>

<p class="muted"><span class="zh">这个画板和第 10 课作业画板 2 是<b>同一份草稿</b>：在同一台电脑上，你上周的骨架已经在下面了——接着写！（没看到？按画板里的提示，从作品墙的 <code>week10-skeleton</code> 复制过来。）新的 <code>assert</code> 加进骨架里<b>已经有的</b> <code>test()</code>，它在主程序前面运行。</span><span class="en">This playground shares <b>one draft</b> with Lesson 10's homework playground 2: on the same computer, last week's skeleton is already below — carry on! (Not there? Follow the note in the playground and copy <code>week10-skeleton</code> from the Gallery.) Add new <code>assert</code>s to the skeleton's <b>existing</b> <code>test()</code>, which runs before the main program.</span></p>

<div class="playground" data-src="{{ '/lessons/11/code/homework.py' | relative_url }}" data-title="🛠️ 我的任务 v1" data-title-en="🛠️ My mission v1" data-save="week11-project" data-draft="project" data-rows="22" data-images></div>

<details class="hint"><summary><span class="zh">💡 卡住了，不知道先做什么？</span><span class="en">💡 Stuck, don't know what to do first?</span></summary><span class="zh">打开<a href="../learn/#build">开工步骤</a>里你那个任务，找到第一个还没打勾的步骤，把它<b>再拆小</b>：比如「侧推」→ 先只做「按 → 往右推」：一个函数 + 一行 <code>onkey</code>。跑通了再加 ←。<b>每次只加 3 行就运行一次。</b></span><span class="en">Open your mission in the <a href="../learn/#build">build steps</a>, find the first unticked step and <b>split it smaller</b>: e.g. "side thrusters" → just "→ pushes right" first: one function + one <code>onkey</code> line. Works? Add ←. <b>Add 3 lines, run, repeat.</b></span></details>
<details class="hint"><summary><span class="zh">💡 报错了怎么办？游戏卡住了怎么办？</span><span class="en">💡 Got an error? The game froze?</span></summary><span class="zh">四步法！① 读红框，看第几行、什么种类（<a href="../learn/#toolbox">第 11 课的表</a>），再问「这个值从哪来？」② 翻<a href="{{ '/notebook/' | relative_url }}">笔记本</a> ③ 点红框里的「复制问 AI 要提示的话」④ 下节课问老师，<b>先把报错抄下来</b>。游戏卡住没有红字：在 <code>tick()</code>（或 <code>fly()</code>）里加编号的侦探 print。</span><span class="en">The 4 steps! ① Read the red box: which line, which kind (<a href="../learn/#toolbox">Lesson 11's table</a>), then ask "where did this value come from?" ② check your <a href="{{ '/notebook/' | relative_url }}">notebook</a> ③ click "copy a hint-please message for AI" in the red box ④ ask the teacher next lesson — <b>write the error down first</b>. Frozen game with no red text: add numbered detective prints inside <code>tick()</code> (or <code>fly()</code>).</span></details>
<details class="hint"><summary><span class="zh">💡 我自己的边界测试写什么？</span><span class="en">💡 What's my own edge test?</span></summary><span class="zh">找你的纯函数里的 <code>&lt;</code>、<code>&lt;=</code>、<code>&gt;</code>，用<b>刚好等于</b>那个数的值去测：🚀 <code>is_safe_landing(MAX_SPEED, PAD_HALF)</code>；☄️ <code>keep_inside(EDGE)</code>、<code>hit(0, 0, 25, 0)</code>（25 不小于 25，所以是 False！）；🛰️ <code>stage_for(SEPARATION)</code>。</span><span class="en">Find the <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code> in your pure functions and test with a value <b>exactly equal</b> to that number: 🚀 <code>is_safe_landing(MAX_SPEED, PAD_HALF)</code>; ☄️ <code>keep_inside(EDGE)</code>, <code>hit(0, 0, 25, 0)</code> (25 isn't less than 25, so it's False!); 🛰️ <code>stage_for(SEPARATION)</code>.</span></details>

## 📤 <span class="zh">怎么交</span><span class="en">How to hand it in</span>

<ol class="steps">
  <li><span class="zh">在作业画板点 <b>📤 存到作品墙</b>，文件名用 <code>week11-project</code>，在 GitHub 页面点 <b>Commit changes</b>。（中途也要存！名字已存在就加 <code>-v2</code>。）</span><span class="en">Click <b>📤 Save to Gallery</b>, name it <code>week11-project</code>, click <b>Commit changes</b> on GitHub. (Save along the way too! If the name exists, add <code>-v2</code>.)</span></li>
  <li><span class="zh">在 <a href="{{ '/notebook/' | relative_url }}">📓 笔记本</a> 第 11 课写 3 行：做到了什么 / 最难的 bug / 怎么解决的（用了哪一招）。</span><span class="en">Write 3 lines under Lesson 11 in your <a href="{{ '/notebook/' | relative_url }}">📓 notebook</a>: what got done / hardest bug / how I fixed it (which trick).</span></li>
  <li><span class="zh">想想下周的「发射直播」邀请谁来看。</span><span class="en">Think about who to invite to next week's "launch broadcast".</span></li>
</ol>

<div class="box box-think"><span class="zh">🔮 <b>下周预告：发射日！</b>你的任务会变成<b>网上的一个页面</b>，有链接，谁都能打开玩。部署前我们会像任务控制中心一样做一次 GO / NO-GO 检查。把家人叫来当观众吧。</span><span class="en">🔮 <b>Next week: launch day!</b> Your mission becomes <b>a page on the web</b> with a link anyone can open and play. Before deploying we'll do a GO / NO-GO poll just like mission control. Invite your family to be the audience.</span></div>
