---
title: 第 10 课 · 教案
title_en: Lesson 10 · Teacher plan
lesson: "10"
tab: teacher
---

# 👩‍🏫 第 10 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子从三个太空项目里**自己**选定一个，写出一页任务计划书（必做 3 个、加分 2 个、至少 5 个小步骤、至少 1 个要测的 assert），理解「计划 → 写 → 测 → 修 → 发布」的循环，并且明白「把规则写成纯函数 → 用 assert 测它」这个做法。

**今天的铁律：** 老师**不替孩子做决定**。他选哪个任务、要什么加分功能，哪怕你觉得太简单或太难，先让他讲理由。你的工作是帮他**拆小**、帮他**看清每个选项要做什么**，不是帮他选。

**关于 SpaceX / Elon Musk 的话题：** 孩子很可能会兴奋地聊起来。顺着他的兴趣聊**工程**：助推器怎么回收、为什么要测试很多次、失败了怎么改。学一学里写到的事实（2002 年创办、2015 年底第一次成功着陆、2024 年 10 月发射塔机械臂接住 Super Heavy）都是公开、确定的；其他细节不确定就说「我们一起查一下」，不要即兴补充。对人物本身不评价，把话题拉回「工程师怎么解决问题」。

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-10">
  <li>把 <code>_config.yml</code> 的 <code>current_lesson</code> 改成 <code>10</code>（首页地图会高亮本周这一课）。</li>
  <li>自己跑一遍 <a href="../learn/">学一学</a>：热身、cargo.py（试一下「卸第 9 件」）、tests.py（看清楚最后那个 assert 是故意写错的）。</li>
  <li><b>三个骨架每个亲手玩 3 分钟</b>（键盘游戏要先点画布）：🚀 试着让助推器停在半空、☄️ 一直按 ← 看飞船飞出去、🛰️ 运行 2–3 次，看 GO / NO-GO 是随机的。按两次空格，火箭会加速得特别快——这是骨架故意留的 bug（必做 2 要修）。</li>
  <li>打开 <a href="{{ '/lessons/11/teacher/' | relative_url }}">第 11 课教案</a>最下面的三个「参考答案 v1」各运行一次，知道「做完长什么样」。</li>
  <li>准备一张纸的计划书（网页表格和纸都可以，有的孩子写纸上更顺）。</li>
  <li>回看孩子前 9 周的作品墙，挑 2 个他最得意的——课上提醒他「你已经会这些了」。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>火箭资料库。先让他<b>猜</b>最后一行打印什么，再运行。让他自己想办法只改一行修好（<code>.lower().strip()</code>）。</td><td>能不能想到第 8 课的字符串方法？</td></tr>
<tr><td><b>5–12</b></td><td>🔄 五步循环</td><td>读 SpaceX 那个框（让他读，你听）。重点一句：<b>失败不是结束，是数据</b>。问：「助推器第一次没落稳，工程师下一步做什么？」——和我们看到红字以后做的一样。做 quiz「网站怎么发布」。</td><td>他以前是不是以为「报错 = 我不行」</td></tr>
<tr><td><b>12–22</b></td><td>👓 读代码</td><td>cargo.py：先<b>不运行</b>，用三步读法说出 4 个函数、主循环、两个列表。做 quiz（900 kg 会怎样）。再运行按 quests 操作。最后「卸第 9 件」——引出测试。</td><td>读代码时是从上往下扫 def，还是一行一行啃？</td></tr>
<tr><td><b>22–32</b></td><td>🧪 测试</td><td>先讲「纯函数」那个框（1 分钟，用计算器按钮比喻）。tests.py：猜一猜 → 运行 → 读 AssertionError → 发现<b>测试本身写错了</b>。然后把 <code>&lt;=</code> 改成 <code>&lt;</code>：只有「刚好在边上」那个测试抓得到——这就是<b>边界测试</b>。</td><td>看到报错先读消息还是先叫老师？能说出「函数错还是测试错」吗？</td></tr>
<tr><td><b>32–40</b></td><td>🚀 试飞 + 选</td><td>三个骨架<b>各试飞 2 分钟</b>（你计时）。看对比表。用下面「怎么帮他选」的三个问题，<b>听他说理由</b>。</td><td>他在哪个骨架上停留最久、最想改？</td></tr>
<tr><td><b>40–55</b></td><td>📄 计划书</td><td>先看他选的那个「例子计划书」（1 分钟），然后<b>关掉它</b>，填表格，用自己的话写。老师只问问题（见策划指导）。拼到 ⭐⭐⭐⭐⭐ → 复制到画板 → 运行 → 存 <code>week10-plan</code>。时间够：在骨架里找所有 TODO。</td><td>必做功能是否都「能运行看到」？加分功能是不是他自己真想要的？</td></tr>
<tr><td><b>55–60</b></td><td>📓 收尾</td><td>让他<b>像任务简报一样</b>把计划讲给家人听（讲不清楚的地方就是计划不清楚的地方）。看作业页。笔记本写「我选的任务是」「小步骤」。</td><td>能否不看屏幕说出 3 个必做功能</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>选任务 + 计划书</b> &gt; tests.py（至少做到「测试也会错」和边界测试）&gt; cargo.py 读代码 &gt; 五步循环 &gt; 热身。计划书没填完可以回家填（它就是作业 🥉）。读代码的 quests 后两项可以跳过；试飞可以压缩成每个 1 分钟。
</div>

---

## 🧭 怎么帮他选任务（不替他选）

**先问三个问题，让他自己答：**

1. 「三个里，做完以后你<b>最想给谁玩</b>？他会玩哪个？」
2. 「你喜欢<b>手快</b>（☄️）、<b>手稳</b>（🚀）还是<b>动脑指挥</b>（🛰️）？」
3. 「试飞的时候，哪个你<b>最想马上改点什么</b>？改什么？」——能说出具体要改什么的那个，通常就是对的选择。

**给你自己看的对比（不要念给他听，用来判断他选完后哪里会卡）：**

| | 🚀 助推器回家 | ☄️ 陨石大躲避 | 🛰️ 任务控制中心 |
|---|---|---|---|
| 新概念 | 「速度」变量：重力改速度、速度改位置（第 11 课 thrust.py 会讲） | 一个<b>列表里装海龟</b>，for 一起移动 | 字典 + input + <b>两个</b>心跳（倒数、飞行）|
| 必做的难点 | 必做 1 要 <code>global fuel</code>；必做 3 要 <code>and</code> | 必做 2 要改 <code>tick()</code> 的结尾：命没了就不再 ontimer | 必做 2 的倒数是一个新的 ontimer 函数 + 防止按两次 |
| 卡住的样子 | 物理数字调不好（太难 / 太简单）→ 这本身就是「测试 → 调参」，鼓励 | 撞上后陨石不回去 → 每一拍都扣命，命瞬间变负数 | 倒数和飞行同时开始；分离日志打印几十次（没用「只一次」的变量）|
| 适合 | 喜欢 SpaceX 回收助推器、愿意反复调手感 | 想最快玩起来；比较像接水果，信心最足 | 喜欢发射直播、GO / NO-GO、看日志；打字不怕多 |
| 代码量（v1） | ~120 行 | ~120 行 | ~190 行 |

**他想做自己的点子**（比如「用发射塔机械臂接住 Super Heavy」）：可以，前提是① 从<b>最像的骨架</b>改起（接助推器 = 🚀 骨架 + 一个会左右移动的「机械臂」目标）；② 他能说出 3 个「运行能看到」的必做功能；③ 至少有 1 个能测的纯函数。三条做不到就先做三选一，把点子写进「下一个项目」。

**他三个都想做**：「先做一个，做完再说」——另外两个写进第 12 课的「下一个项目清单」。🛰️ 的加分功能「一级飞回来降落」正好能把 🚀 合进去，可以作为远期目标。

**他选了你觉得太简单的**：不要加难度；让他把加分写满，做完必做自然会想做加分。<br>**他选了你觉得太难的**：不劝退；在计划书里把必做 3 的范围写小（比如 🛰️ 的分离先「只记日志，不做掉落动画」）。

---

## 🗺️ 策划指导：怎么帮他拆，而不是替他选

**只问问题，不给答案：**

- 「如果只能做**一个**功能，是哪个？」（→ 必做 1）「然后呢？」（→ 必做 2、3）
- 「这个功能，你**运行的时候能看到**吗？」（看不到的不算一步）
- 「这一步你觉得要几分钟？超过 10 分钟就再拆。」
- 「这一步要用到第几课的东西？翻一下小词典。」
- 「哪个规则能写成纯函数？你会用什么数字测它？有没有一个<b>刚好在边上</b>的数字？」
- 「卡住了你打算先问谁？」（→ 四步法；AI 那一栏只写「提示」类问题）

### 计划书评分表（给自己用，不打分给孩子）

| 项目 | 好的样子 |
|---|---|
| 做什么 | 一句话说清，家人能听懂 |
| 必做 3 个 | 每个运行时都能看到；和骨架里的 3 个 TODO 对得上（或者他有理由换） |
| 加分 2 个 | 是他自己真想要的，不是照抄例子 |
| 小步骤 ≥ 5 | 每步 10 分钟；第一步是「骨架跑起来 + 读懂 tick()」；有「删掉测试前的 # → 红 → 写函数 → 绿」这种步骤 |
| 要测的纯函数 | 至少 1 个 assert，最好有 1 个边界测试 |
| 问 AI | 只写「提示」类问题，没有「帮我写整个游戏」 |

## 🗣️ 好用的话术

- 「SpaceX 的助推器摔了好几次才落稳。你今天看到几次红字？每一次都是数据。」
- 「这个 assert 在检查什么？它失败了——是函数错了，还是测试错了？」
- 「读代码先找 def——这段代码的『目录』是什么？」
- 「这条规则能不能写成一个纯函数？那就能测了。」
- 「小一点，但做完。」（今天可以说三遍。）
- 夸过程：「你自己把『做着陆游戏』拆成了 7 步，这就是工程师的本事。」

## 🧱 常见卡点

| 卡点 | 应对 |
|---|---|
| 想做「真实的 SpaceX 模拟器」级别的大项目 | 不否定。问「最简单能玩的版本是什么？」大点子写进「加分」和「下一个项目」 |
| 键盘骨架按键没反应 | 先点一下画布（画板会提示）；🛰️ 要先在输入框回答完问题，再点画布按空格 |
| 🛰️ 一直 SCRUB 发射不了 | 骨架里 <code>all_systems_go</code> 还没写，所以现在<b>永远能发射</b>；写好以后大约一半的时候会 SCRUB，再运行一次 = 「明天再试」，这是设计好的 |
| 不明白 assert 报错 | 读消息：逗号后面那句话就是写测试的人留的提示 |
| 分不清「纯函数」 | 问：「这个函数里有海龟、print 或 input 吗？没有 → 纯函数。」 |
| 计划书写了「做出游戏」当一步 | 「运行的时候能看到什么？」拆到能看到为止 |
| 想让 AI 直接写整个项目 | 回到第 9 课的约定；AI 只做头脑风暴和提示 |

## ✅ 参考答案

<details class="hint"><summary>热身：火箭资料库</summary><code>return rockets.get(name.lower().strip(), "❓ …")</code>。<code>"Saturn V"</code> 查不到是因为字典的键是小写的 <code>"saturn v"</code>，字典查找大小写敏感。</details>
<details class="hint"><summary>cargo.py 的 quests</summary>4 个函数：total（算总重）、show（显示清单）、load（装货，太重就拒绝）、unload（卸货）。<code>total()</code> 被 <code>show</code> 和 <code>load</code> 用到。装好自动显示：在 <code>load</code> 的 <code>else</code> 里、<code>print("✅ …")</code> 之后加 <code>show()</code>（放在 if 外面也行，那样太重时也会显示）。「卸第 9 件」→ <code>pop(8)</code> 越界 → IndexError（第 32 行）。</details>
<details class="hint"><summary>tests.py</summary>最后一个 assert 本身写错：应该是 <code>keep_inside(300) == 270</code>。函数是对的。把 <code>speed &lt;= 2</code> 改成 <code>speed &lt; 2</code> 后，第一个抓到的是第 3 个 assert <code>is_safe_landing(2, 40) == True</code>（边界测试）；前两个测试都不在边上，抓不到。自己的测试示例：<code>assert all_systems_go({"a": "GO", "b": "GO", "c": "NO-GO"}) == False</code>；<code>assert keep_inside(270) == 270</code>、<code>assert keep_inside(-270) == -270</code>。</details>
<details class="hint"><summary>作业 🥈：三个任务的必做功能 1</summary>
<b>🚀 燃料：</b>
<pre>def engine():
    global vy, fuel
    if fuel > 0:
        vy = vy + THRUST
        fuel = use_fuel(fuel)</pre>
<code>show_hud()</code> 的 f-string 里加 <code>燃料 fuel {fuel}</code>。常见坑：只写了 <code>global vy</code>，改 fuel 时报 UnboundLocalError（第 11 课的 global 小魔法会讲）。
<br><b>☄️ keep_inside：</b>
<pre>def keep_inside(x):
    if x > EDGE:
        return EDGE
    elif x &lt; -EDGE:
        return -EDGE
    return x</pre>
再把 <code>go_left / go_right</code> 改成 <code>ship.setx(keep_inside(ship.xcor() - SHIP_STEP))</code>。
<br><b>🛰️ all_systems_go：</b>
<pre>def all_systems_go(checks):
    for system in checks:
        if checks[system] != "GO":
            return False
    return True</pre>
常见坑：把 <code>return True</code> 也缩进到 for 里面 → 只看了第一个系统就返回了。删掉 <code>#</code> 后的第二个测试正好能抓到这个错误（如果 NO-GO 不在第一个）——可以让他自己发现。</details>
<details class="hint"><summary>作业 🥇：边界测试的例子</summary>🚀 <code>assert use_fuel(1) == 0</code>、<code>assert is_safe_landing(MAX_SPEED, PAD_HALF) == True</code>；☄️ <code>assert keep_inside(EDGE) == EDGE</code>、<code>assert hit(0, 0, 24, 0) == True</code>（24 &lt; 25）；🛰️ <code>assert poll({"fuel": 95, "wind": 30, "engines": 9})["燃料 fuel"] == "GO"</code>（95 刚好够）。</details>

## 📝 为第 11 课做准备

- 确认孩子选的骨架<b>贴进了第 10 课作业画板 2</b>（draft 会自动记在他的电脑上；第 11 课作业画板用的是同一个 draft，下周打开第 11 课作业页就能接着写）。存档名用 <code>week10-skeleton</code>，第 11 课存 <code>week11-project</code> 时不会撞名。
- 把计划书打印一份放在桌上，第 11 课每做完一步就打一个勾。
- 第 11 课老师的台词只有三句：「计划书上下一步是什么？」「报错说了什么？」「你打算先问谁？」

## 📝 观察记录

| 项目 | 记录 |
|---|---|
| 选的任务 / 理由（他自己的原话） | |
| 必做 3 个功能 / 加分 2 个 | |
| 小步骤数量 / 是否每步可见 | |
| 他想到的 assert（有没有边界测试） | |
| 读代码时的习惯（扫 def 还是逐行？） | |
| 对 AssertionError 的反应 | |
