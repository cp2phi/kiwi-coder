---
title: 第 11 课 · 教案
title_en: Lesson 11 · Teacher plan
lesson: "11"
tab: teacher
playground: true
---

# 👩‍🏫 第 11 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子把第 10 课选的太空任务做成**能跑的 v1**（3 个必做功能 + 测试全绿），并且在过程中**自己**用四招排错，学会「报错在 A，bug 可能在 B」。今天没有新语法，有的是「独立」。

**今天的铁律：顾问模式。** 老师**不碰键盘、不给代码、不说「应该这样写」**。只做三件事：反问、指方向（去看第几课 / 词典 / 笔记本 / 开工步骤第几步）、在他真的卡死 5 分钟以上时给「下一个最小步骤」。

<div class="box box-rule"><b>只许问的三句话：</b>「报错说了什么？」「你觉得是哪一行？」「你怎么验证你的猜想？」——三句话轮着问，大多数 bug 他自己能找到。</div>

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-11">
  <li>把 <code>_config.yml</code> 的 <code>current_lesson</code> 改成 <code>11</code>（首页地图会高亮本周这一课）。</li>
  <li>打开作品墙，确认 <code>week10-plan</code>（和 <code>week10-skeleton</code>，如果他做了 🥈）在那里；读一遍他的计划，对照<a href="../learn/#build">学一学的开工步骤</a>，心里估计他今天能做到第几步。</li>
  <li>自己把学一学的 4 个排错例子（含「顺着报错往回找」）和 3 个事件例子跑一遍（约 10 分钟）。键盘例子记得<b>先点画布</b>。</li>
  <li>在本页最下面把<b>他选的那个任务的参考答案 v1</b>玩一遍、读一遍。不是为了给他，而是为了知道「做完」长什么样、他离它还有几步。</li>
  <li>准备一只小黄鸭（或任何玩偶）放在桌上，真的有用。</li>
  <li>计时器：制作环节每 10 分钟响一次 = 存档时间（共 3 次）。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>三个 bug。让他<b>读出红框</b>再动手。「电脑一次只报一个错」这句话让他自己说出来。</td><td>他看到红字的第一反应是读还是乱改？</td></tr>
<tr><td><b>5–17</b></td><td>🧰 四招</td><td>print 侦探 2 分钟（他自己加 print 看 fuel）；读报错 2 分钟（用那张表）；<b>进阶：顺着报错往回找 3 分钟</b>——问「红的这行在哪个函数里？speed 是谁交进来的？」；小黄鸭 2 分钟（你当鸭子，只点头）；二分法 3 分钟（真的注释掉一半）。顺口提一句「游戏卡住没红字 → tick 里加编号 print」。</td><td>哪一招他最喜欢？以后卡住就先提醒那一招。能不能说出「报错在 A，bug 在 B」？</td></tr>
<tr><td><b>17–25</b></td><td>⌨️ 事件</td><td>方向键（做猜一猜：为什么不加括号）→ 掉落陨石（第 3 个 quest：删掉 ontimer 那行，游戏就停——这是 GAME OVER 的秘密）→ 重力 + 点火（猜一猜：按一次 ↑ 不会马上往上）。global 只跑一下，删掉那行看 UnboundLocalError。点击例子跳过。</td><td>他能说出 tick() 为什么会一直跑、怎么让它停吗？</td></tr>
<tr><td><b>25–55</b></td><td>🏗️ 制作</td><td><b>30 分钟（含存档）。</b>打开作业画板（第 10 课的骨架会自动在里面）→ 打开学一学「开工」里<b>他那个任务</b>的步骤 → 一步一步做，每步运行。<br>你坐在旁边做自己的事（真的），每 10 分钟问一句「现在在第几步？」。<br>制作开始后第 10、20、30 分钟各存一次（大约是课上第 35、45、55 分钟）。</td><td>见下面的「卡住了的教练脚本」和「三个任务的常见坑」。记录每个必做功能花了多久。</td></tr>
<tr><td><b>55–60</b></td><td>📓 收尾</td><td>存最后一版。笔记本 3 行（最难的 bug 一定要写，写用了哪一招）。看一眼作业页：这周作业就是把 v1 做完 + 找真人试飞。</td><td>他能用自己的话说出今天用了哪一招排错吗？</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>必做 1 能跑并存档</b> &gt; print 侦探 + 读报错（含往回找）&gt; 重力 + 点火（选 🚀 / 🛰️ 的话）或 方向键（选 ☄️ 的话）&gt; 其他。四招可以只讲两招，剩下的作业周自己看。宁可必做 1 做得很小很丑，也要有「从头运行没有红字」的那一刻。
</div>

---

## 🧑‍🏫 卡住了的教练脚本（卡住 &gt; 5 分钟才用）

1. **「停一下，告诉我你现在想让它做什么？」**（一句话）
2. **「它现在实际做了什么？」**（让他指着屏幕说）
3. **「这两件事之间，差在哪一行？」** → 不知道 → **「用哪一招能知道？」**（print 侦探 / 二分法）
4. 还不行 → 给**下一个最小步骤**，不给代码：「先让它打印出 fuel 的值」「先只做按 → 往右」「把这个功能先注释掉，让其他的跑起来」「看开工步骤第 5 步的那句话」。
5. 真的是知识缺口（比如不知道 global）→ **指方向**：「第 11 课的小魔法那一段」「词典第 7 课」。让他自己读。
6. 最后手段：你在**另一个**画板里写一个 3 行的、**和他的问题不同但同类**的例子，让他看了自己迁移。

**不要做的：** 接过鼠标；说「应该是 ==」；一口气指出三个问题。一次一个。

## 🧱 三个任务的常见坑

| 任务 | 现象 | 原因 → 引导他怎么找 |
|---|---|---|
| 🚀 | 改燃料时报 UnboundLocalError | <code>engine()</code> 只写了 <code>global vy</code>。→「报错说哪个名字？你告诉电脑它是外面的了吗？」 |
| 🚀 | 侧推按了没反应 | 忘了写 <code>onkey</code>，或者 <code>onkey</code> 里的函数名拼错 / 加了括号。→「按 ← 的时候，电脑会叫哪个函数？」 |
| 🚀 | 怎么都落不稳 / 太容易 | 不是 bug，是<b>调参</b>。鼓励他改 <code>GRAVITY</code>、<code>THRUST</code>、<code>START_FUEL</code>，每次只改一个，玩一次——这就是「试飞 → 改进」。提示：快到船再点火最省油 |
| 🚀 | 测试 <code>is_safe_landing(1, 80)</code> 失败 | 只检查了速度，忘了 drift。→「这个测试想说什么？你的 return 里有 drift 吗？」 |
| ☄️ | 撞一下命就变成负数 | 撞上后没有把陨石送回上面，每一拍都再扣一次。→ print 侦探：在扣命那行 print lives |
| ☄️ | GAME OVER 写出来了，陨石还在掉 | <code>ontimer</code> 还在 if 外面。→ 回想例 2 第 3 个 quest |
| ☄️ | <code>speed_for(1000)</code> 测试失败 | 没写上限，或者先 return 了。→ 用小黄鸭念一遍函数 |
| 🛰️ | 测试 <code>all_systems_go(... NO-GO)</code> 失败 | <code>return True</code> 缩进在 for 里 → 只看了第一个。→ print 侦探：在 for 里 print system |
| 🛰️ | 倒数和飞行同时开始 / 倒数一下子就到 0 | 在倒数函数里用 for 循环 print（没有用 ontimer），或在 <code>launch()</code> 里倒数后又直接 <code>fly()</code>。→「每 0.5 秒叫一次的是哪个函数？」 |
| 🛰️ | 「一二级分离」日志打印了几十次 | 每一拍都 log 了。→「什么时候算『刚刚』分离？需要记住什么？」（stage 变量）|
| 🛰️ | SCRUB 了还是能按空格发射 | <code>onkey</code> 写在 if 外面 |
| 全部 | 删掉 <code>#</code> 后 IndentationError | 把前面的 4 个空格也删了。→ 读表里 IndentationError 那一行 |

## 🗣️ 好用的话术

- 「你猜它会打印什么？」（运行前）
- 「这个红字里，哪个词你认识？」
- 「红的这一行在哪个函数里？这个值是谁交给它的？」
- 「测试变红了——太好了，说明它在工作。现在让它变绿。」
- 「存了吗？」（制作时每 10 分钟）
- 夸过程：「你刚才是自己用 print 找到的，这就是工程师的做法。」

## 🏁 什么叫「做完了」（给孩子的标准，也给你）

- 从「↺ 还原」后的空白开始，粘贴最新版，**运行一次没有红字**
- 计划里的 3 个必做功能，每个都能演示一下
- `test()` 里没有「睡着的测试」，全部通过 + 1 个他自己的边界测试（可以在 `test()` 最后加 `print("✅ 测试通过")`）
- 作品墙上有 `week11-project`
- 笔记本有「最难的 bug」

没做完也算：**必做 1 能跑 + 存档了** 就是本周的及格线。作业周补剩下的。

---

## 🔑 参考答案：学一学里的例子

<details class="hint"><summary>热身 / print 侦探 / 读报错</summary>热身：<code>range(3):</code> 加冒号；<code>rokcet</code> → <code>rocket</code>；<code>if fuel == 3:</code>。print 侦探：侦探 print 显示 70、75、80——每一圈都从 100 重新减；改成 <code>fuel = fuel - burn</code>。读报错：第 9 行 <code>stages[3]</code>，IndexError，只有 0–2。</details>
<details class="hint"><summary>顺着报错往回找（traceback2.py）</summary>红框标在第 8 行（函数 <code>is_safe_landing</code> 里面），TypeError：文字和数字不能比较大小。侦探 print 显示 speed 是 <code>&lt;class 'str'&gt;</code>。往回找：第 12 行把 speed 交进函数，speed 来自第 11 行的 <code>input()</code>。在第 11 行修：<code>speed = int(input(…))</code>。<b>函数本身没错</b>——这是今天最值得他说出来的一句话。</details>
<details class="hint"><summary>小黄鸭 / 二分法</summary>小黄鸭：两句话放反了。两种修法：① 交换两个 print；② 把条件改成 <code>if speed &lt;= MAX_SPEED:</code>。速度 2 时应该是「安全」——如果他把条件改成 <code>speed &lt; MAX_SPEED</code> 就错了，正好复习边界测试。二分法：注释掉第 3、4 部分后倒三角还在 → 注释掉第 2 部分后剩下的都对 → bug 在第 2 部分：两个 <code>t.right(120)</code> 都改成 <code>t.left(120)</code>。</details>
<details class="hint"><summary>事件例子的 quests</summary>掉落陨石：删掉 <code>screen.ontimer(tick, BEAT)</code> 后陨石只动一下就停——没人再叫 tick 了。重力 + 点火：<code>GRAVITY = -0.05</code> 时什么都不按也越飞越快（往上），这就是 🛰️ 的 <code>ACCEL</code>。global：删掉后报 <code>UnboundLocalError: local variable 'fuel' referenced before assignment</code>。</details>

## 🔑 参考答案 v1（只给老师看，可以直接玩）

<p>下面三个画板是三个任务「3 个必做功能都做好」的样子，每个都是在第 10 课骨架上改出来的（改的地方就是骨架里的 TODO）。<b>不要给孩子看</b>；用来对照他的进度、准备提问。键盘游戏先点画布。</p>

### 🚀 助推器回家 v1

<div class="playground" data-src="{{ '/lessons/11/code/teacher-booster.py' | relative_url }}" data-title="🚀 参考答案：助推器回家" data-title-en="🚀 Reference: Booster landing" data-save="teacher-booster" data-rows="12"></div>

<details class="hint"><summary>关键改动（对照骨架的 TODO）</summary>
<pre>def is_safe_landing(speed, drift):
    return speed &lt;= MAX_SPEED and drift &lt;= PAD_HALF

def engine():
    global vy, fuel
    if fuel > 0:
        vy = vy + THRUST
        fuel = use_fuel(fuel)

def go_left():
    global vx
    vx = vx - SIDE          # SIDE = 0.3，新加的设置

# touchdown() 里：
    if is_safe_landing(speed, drift):
        hud.color("lime")
        hud.write("🎉 着陆成功 Landed!", ...)
    else:
        booster.color("red")
        hud.color("red")
        hud.write("💥 坠毁 Crashed!", ...)</pre>
加分功能思路：🔥 火焰 = 再做一只橙色 triangle 海龟，<code>setheading(270)</code>，点火时 <code>goto</code> 到助推器下面并 <code>showturtle()</code>，几拍后 <code>hideturtle()</code>；🌬️ 侧风 = <code>tick()</code> 里 <code>vx = vx + random.choice([-0.02, 0, 0.02])</code>；🌕 月球模式 = <code>GRAVITIES = {"地球": 0.05, "月球": 0.01}</code> + 开头 <code>input</code> 选一个。
</details>

### ☄️ 陨石大躲避 v1

<div class="playground" data-src="{{ '/lessons/11/code/teacher-asteroids.py' | relative_url }}" data-title="☄️ 参考答案：陨石大躲避" data-title-en="☄️ Reference: Asteroid dodger" data-save="teacher-asteroids" data-rows="12"></div>

<details class="hint"><summary>关键改动（对照骨架的 TODO）</summary>
<pre>def keep_inside(x):
    if x > EDGE:
        return EDGE
    elif x &lt; -EDGE:
        return -EDGE
    return x

def speed_for(score):
    speed = START_SPEED + score / 10
    if speed > MAX_SPEED:
        return MAX_SPEED
    return speed

# tick() 里（global score, lives）：
        if hit(ship.xcor(), ship.ycor(), rock.xcor(), rock.ycor()):
            lives = lives - 1
            rock.goto(random.randint(-EDGE, EDGE), random.randint(300, 450))
    show_hud()
    if lives > 0:
        screen.ontimer(tick, 50)
    else:
        hud.write("GAME OVER ...", ...)</pre>
加分功能思路：🔋 燃料电池 = 再做一个金色 circle 海龟，和陨石一样往下掉，<code>hit</code> 到飞船就 <code>score += 5</code> 并送回上面；❤️ = <code>f"{'❤️' * lives}"</code>；🛡️ 护盾 = <code>shield = True</code> + <code>screen.ontimer(shield_off, 3000)</code>，撞上时 <code>if not shield:</code> 才扣命。
</details>

### 🛰️ 任务控制中心 v1

<div class="playground" data-src="{{ '/lessons/11/code/teacher-mission.py' | relative_url }}" data-title="🛰️ 参考答案：任务控制中心" data-title-en="🛰️ Reference: Mission control" data-save="teacher-mission" data-rows="12"></div>

<details class="hint"><summary>关键改动（对照骨架的 TODO）</summary>
<pre>def all_systems_go(checks):
    for system in checks:
        if checks[system] != "GO":
            return False
    return True             # 在 for 外面！

def stage_for(height):
    if height &lt; SEPARATION:
        return 1
    return 2

def countdown():            # 新函数；count = 10、launched = False、big 海龟是新加的
    global count
    big.clear()
    if count > 0:
        big.write(f"T-{count}", align="center", font=("Arial", 40, "bold"))
        count = count - 1
        screen.ontimer(countdown, 500)
    else:
        big.write("LIFTOFF!", ...)
        screen.ontimer(big.clear, 1500)
        log_event("点火，起飞！Liftoff!")
        fly()

def launch():
    global launched
    if launched:
        return
    launched = True
    countdown()

# fly() 的爬升部分（global 里加 stage）：
        if stage_for(rocket.ycor()) == 2 and stage == 1:
            stage = 2
            log_event("一二级分离 stage separation")
        if stage == 1:
            booster.goto(rocket.xcor(), rocket.ycor() - 20)
# fly() 最后、ontimer 之前：
    if stage == 2 and booster.ycor() > -320:
        booster.sety(booster.ycor() - 4)

# 主程序最后：
if all_systems_go(checks):
    screen.onkey(launch, "space")
    screen.listen()
else:
    log_event("🛑 推迟发射 SCRUB")</pre>
大约一半的运行会 SCRUB（传感器是随机的），这是设计好的。加分功能思路：🔁 明天再试 = 把检查放进 <code>while not all_systems_go(checks):</code>，每次 <code>input("明天再试？")</code> 后重新 <code>poll(read_sensors())</code>；🛑 中止 = <code>onkey(abort, "a")</code>，<code>abort()</code> 里设一个变量让 <code>fly()</code> 不再 ontimer；🌍 圈数 = 入轨后数 <code>fly()</code> 被叫了几次，每 180 次（2° × 180 = 360°）是一圈。
</details>

---

## 📝 观察记录

| 项目 | 记录 |
|---|---|
| 他的任务 / 做到开工步骤第几步 | |
| 必做 1 / 2 / 3 各花了几分钟 | |
| 他自己用了哪几招排错（有没有「往回找」） | |
| 卡住最久的 bug 是什么、谁解决的 | |
| 他自己写的边界测试 | |
| 我忍住没给代码的次数 😄 | |
| 下周展示前还差什么 | |
