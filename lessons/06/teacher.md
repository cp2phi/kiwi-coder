---
title: 第 6 课 · 教案
title_en: Lesson 6 · Teacher plan
lesson: "06"
tab: teacher
---

# 👩‍🏫 第 6 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 两件事。① 语法：会用 `while`、计数器 `+= 1`、`and / or / not`、`while True + break`（停车暗号），能用**两个条件**管一个 while 并在循环后判断「是哪个原因停的」；加餐：旗子变量 `while not launched`。并且**亲手经历一次死循环并自己停下来**。② 概念：能用自己的话说出「写规则的程序」和「从例子学的 AI」有什么不同，以及「例子不好 AI 就学歪」。这是整个课程里最重要的 AI 概念课。

**今天的铁律：** 让他写死循环，不要拦。点红色 ■ 的那一刻比任何讲解都管用。概念部分**多问少讲**：「为什么它把狗猜成猫？」「企鹅怎么办？」「写得完吗？」

<div class="box box-tip"><span class="box-title">📈 本课难度已上调（约 +30%）</span>
① 热身改成「行星之旅」：复习第 5 课的 <code>in</code> / <code>append</code>，并引出「for 保证不了 → 需要 while」；<br>
② 第一个猜一猜要跟踪 <code>n = n - 3</code> 的每一圈；改一改里要<b>自己写</b>往上数的 while 和行星 while；<br>
③ while True + break 换成「太空日志」（停车暗号 + 列表 + 写满 5 页再 break）；<br>
④ 猜数字 2.0 改成 <code>while guess != secret and tries &lt; 6</code>，循环后的 if/else <b>自己写</b>；<br>
⑤ 新增「加餐」：旗子变量 + 把比较结果存进变量（<code>rain = ... == 1</code>），火箭等发射窗口；<br>
⑥ 动物猜猜猜的蝙蝠规则从填空变成<b>自己写 2 行</b>；新增 🏆「太空知识闯关」（3 条命，自己设计）；<br>
⑦ 作业：🥉 必须认出狗 / 蝙蝠 / 企鹅（要自己想新问题和规则顺序）；🥈 给两个 AI 打分（正确率）；🥇 「问题树」聪明侦探。作业里去掉了 while 画画。
</div>

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-6">
  <li>自己把 <a href="../learn/">学一学</a> 跑一遍，特别试一下删掉 <code>n = n - 1</code> 后点 ■ 停下是否正常。</li>
  <li>准备 10 张动物卡（手写纸条就行）：猫、狗、tūī、kiwi、鲨鱼、金鱼、马、企鹅、蝙蝠、海龟。企鹅和蝙蝠是「陷阱卡」。</li>
  <li><b>Teachable Machine</b>：<b>课前老师自己把「好模型」训练好、留着标签页不关</b>（课上不现场拍 40 张，太慢）。课上孩子只做「坏模型」。提前用 <a href="https://teachablemachine.withgoogle.com/train/image" target="_blank" rel="noopener">图片项目</a> 自己做一遍「好模型」和「坏模型」（坏模型：一类只拍 3 张且都在角落）。确认摄像头权限、网速。如果没有摄像头，用「Upload」上传手机照片也可以。</li>
  <li>想好一个和孩子兴趣相关的 AI 偏见例子（比如：只用白天照片训练的「认路」AI，晚上就不行了）。</li>
  <li>打开 <a href="{{ '/games/reader/' | relative_url }}">🔮 读心术</a>，看看第 1 关。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>行星之旅。先问「range(3) 的时候 visited 最多几个？」再运行。他加 4 颗行星，改 range(10) 跑几次——「10 次够不够？要几次才<b>保证</b>？」（说不准 → 引出 while）</td><td>上节课的 <code>in</code> 还记得吗</td></tr>
<tr><td><b>5–15</b></td><td>🚀 while</td><td>公交车比喻 1 分钟。猜一猜 <code>n = n - 3</code>：<b>先在纸上一圈一圈写 n</b>，再运行验证。<br><b>关键 3 分钟：</b>删掉 <code>n = n - 1</code>，看刷屏，<b>自己</b>点 ■。问：「什么时候 n &gt; 0 会变成 False？」<br>✍️ 自己写往上数；回到热身改成 <code>while len(visited) &lt; 8</code>（可以留作业时间）。</td><td>死循环时的第一反应是慌还是找按钮？</td></tr>
<tr><td><b>15–20</b></td><td>♾️ 太空日志</td><td>while True + break：写 3 条日志再 end。删掉 break 试一次。✍️ 写满 5 页就 break（问他放 append 前还是后——都能跑，但放前面会多问一次、把第 6 条白白丢掉，让他自己试出来）。</td><td>能说出「end 是停车暗号」吗</td></tr>
<tr><td><b>20–28</b></td><td>🔐 and / or / not + 猜数字 2.0</td><td>两个真值猜一猜（第 2 个是 <code>not rain</code>，要一块一块算）。秘密基地的门试 4 种输入、and 改 or。<br>猜数字 2.0：先做 tries 的猜一猜，再<b>自己写</b>循环后的 if/else。</td><td>and 和 or 会不会混；能不能说出「循环停了有两个原因」</td></tr>
<tr><td><b>28–33</b></td><td>🚩 加餐：发射窗口</td><td>运行 3 次，比较天数。指着 <code>rain = random.randint(1, 4) == 1</code>：「这个盒子里装的是什么？」（True / False）。时间够就加 scrubs 计数器。</td><td>他能不能接受「True / False 也是一种值」</td></tr>
<tr><td><b>33–38</b></td><td>✂️ 不插电</td><td>动物卡游戏。他当「AI」，写 3 条规则分「鸟 / 不是鸟」，你出卡他按规则答。<b>然后出企鹅和蝙蝠。</b>规则错了→改规则。<br>💬「写得完吗？世界上有多少种动物？」</td><td>他有没有自己说出「规则永远写不完」</td></tr>
<tr><td><b>38–46</b></td><td>🕵️ 规则版 AI</td><td>运行动物猜猜猜，<b>自己写</b>蝙蝠规则（2 行）。想一只狗→被猜成猫→「为什么？」→加第 4 个问题「会汪汪叫吗」+ 一条规则（放在猫前面）。</td><td>能不能自己想到要加新问题，而不只是加 elif</td></tr>
<tr><td><b>46–55</b></td><td>📸 Teachable Machine</td><td>① 好模型：打开老师<b>课前训练好的</b>那个，孩子测试 1 分钟。② 坏模型（孩子自己做）：拳头只拍 3 张且全在左上角。测试：拳头放中间→它可能说「手掌」。<br>💬「它学到的规律可能是什么？」「这叫数据偏见。」</td><td>他能不能说出「例子少 / 例子偏 → 学歪」。这句话要写进笔记本</td></tr>
<tr><td><b>55–60</b></td><td>📓 收尾</td><td>作业页：🥉 要认出狗、蝙蝠、企鹅（要想新问题）；🥈 给两个 AI 打分。笔记本 3 行 + 「规则 vs 数据」1 行。读心术第 1 关留作家庭任务。</td><td>用自己的话复述「规则 vs 学习」</td></tr>
</table>
</div>

<p>例 5 海龟画到边上（选做）和 🏆 太空知识闯关留给快的孩子 / 回家。</p>

<div class="box box-warn"><span class="box-title">⏰ 时间不够 / 孩子吃力时怎么砍</span>
优先级：<b>while + 死循环体验</b> &gt; <b>动物猜猜猜 + 不插电</b> &gt; <b>Teachable Machine 坏模型</b> &gt; and/or/not + 猜数字 2.0 &gt; 太空日志 &gt; 🚩 发射窗口 &gt; 海龟 while &gt; 挑战。<br>
<b>如果孩子明显吃力：</b>① 发射窗口只运行、只问「rain 里装的是什么」，不写代码；② 太空日志只运行 + 删 break，不做「写满 5 页」；③ 猜数字 2.0 直接给提示，看他敲；④ 作业告诉他 🥉 先做狗和蝙蝠，企鹅算加分。<br>
<b>如果孩子很快：</b>课上做 🏆 太空知识闯关，并挑战「不重复」那一步（while 条件要再加 <code>len(questions) &gt; 0</code>）。<br>
Teachable Machine 网络不好时：只做「坏模型」部分，用上传照片；或者口头讨论「如果只给它 3 张图会怎样」。</div>

---

## 🗣️ 好用的话术

- 「别慌，红色按钮在哪？」（死循环时只说这一句）
- 「**什么时候**条件会变成 False？」（每个 while 都问）
- 「and 是『而且』，or 是『或者』——你要的是哪个？」
- 「它为什么把狗猜成猫？是它笨，还是**我们**没告诉它？」
- 「这个模型学到的规律可能是什么？我们怎么知道？」（引出：很难知道 AI 学了什么）
- 夸过程：「你自己发现要加新问题，而不是只加规则——这就是在设计程序。」

## 🧱 常见卡点

| 卡点 | 怎么办 |
|---|---|
| 死循环刷屏，不知道怎么办 | 指一下红色 ■。然后让他自己说出少了哪一行 |
| `while` 后面忘记冒号 / 缩进 | 和 for 一样——「for 是怎么写的？」 |
| `tries += 1` 看不懂 | 让他把它改写成 `tries = tries + 1`，两种都认得就行 |
| `and` / `or` 混用 | 回到真值表猜一猜；用「而且 / 或者」翻译一遍 |
| 两个条件的 while 停了，不知道谁赢 | 「停下来有几种可能？」→ 循环外面再 `if guess == secret` |
| `while not launched` 读不懂 | 翻译成中文：「只要**还没**发射」；再问「什么时候 launched 变 True？」 |
| `rain = random.randint(1, 4) == 1` 看不懂 | 先在画板里 `print(3 == 1)`、`print(1 == 1)`，看 True / False 也能打印、也能放进盒子 |
| 日志 / 测验的 break 写在 if 外面 | 第一条就停了——「break 是谁的手下？」让他数缩进 |
| 回答 `Yes`（大写）程序不认 | 这是真实的 bug！先让他发现，告诉他第 8 课会学 `.lower()` 解决 |
| 填空写了 `yes` 没引号 | 报错「不认识 yes」→ 引号 |
| Teachable Machine 坏模型居然没学坏 | 也行：说「这次运气好；例子只有 3 张，换个光线再试」，或者让拳头的 3 张图都带一个明显的背景物 |

---

## ✅ 参考答案

<details class="hint"><summary>倒计时：从 1 数到 10 / 行星 while</summary><pre>n = 1
while n &lt;= 10:
    print(n)
    n = n + 1

# 热身改成 while：一定去遍 8 颗
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
visited = []
flights = 0
while len(visited) &lt; 8:
    p = random.choice(planets)
    flights += 1
    if p in visited:
        print(f"🔁 {p} 去过了")
    else:
        visited.append(p)
        print(f"🚀 飞往 {p}")
print(f"飞了 {flights} 次才去遍 8 颗行星")</pre></details>
<details class="hint"><summary>太空日志：写满 5 页</summary><pre>while True:
    entry = input("📝 ...")
    if entry == "end":
        break
    log.append(entry)
    if len(log) == 5:
        print("📕 本子写满了")
        break</pre>（放在 append 后面：写完第 5 条马上说「写满了」。放在前面的话，也记 5 条，但要等你写第 6 条才发现写满，第 6 条被白白丢掉——让孩子自己试出来）</details>
<details class="hint"><summary>秘密基地：小朋友规则</summary><pre>elif password != "kiwi" and age &lt; 6:
    print("👶 小朋友，去找爸爸妈妈")
else:
    print("❌ 密码错误")</pre></details>
<details class="hint"><summary>猜数字 2.0：循环后的 if / else</summary><pre>if guess == secret:
    print(f"🎉 答对了！用了 {tries} 次")
    if tries &lt;= 3:
        print("🏆 太神了")
else:
    print(f"😢 机会用完了，答案是 {secret}")</pre>把 <code>and</code> 改成 <code>or</code> 以后，只要「还没猜对」就一直是 True，6 次的限制就没用了。</details>
<details class="hint"><summary>🚩 发射窗口：scrubs + 温度 + 最多 10 天</summary><pre>launched = False
day = 0
scrubs = 0
while not launched and day &lt; 10:
    day += 1
    wind = random.randint(0, 60)
    rain = random.randint(1, 4) == 1
    temp = random.randint(-5, 30)
    print(f"第 {day} 天: 风 {wind}, 雨 {rain}, 温度 {temp}")
    if wind &lt; 30 and not rain and temp &gt;= 0:
        print("   ✅ GO!")
        launched = True
    else:
        print("   ⛔ NO GO")
        scrubs += 1
if launched:
    print(f"🚀 第 {day} 天发射，推迟了 {scrubs} 次")
else:
    print("😢 10 天都没发射成，任务取消")</pre></details>
<details class="hint"><summary>动物猜猜猜：蝙蝠 + 狗</summary><pre>bark = input("它会汪汪叫吗？Does it bark? (yes/no) ")

if water == "yes":
    print("🦈 是鲨鱼 shark？")
elif fur == "yes" and bark == "yes":
    print("🐶 是狗 dog？")
elif fur == "yes" and fly == "no":
    print("🐱 是猫 cat？")
elif fur == "yes" and fly == "yes":
    print("🦇 是蝙蝠 bat？")
...</pre>（狗的规则要放在猫前面）</details>
<details class="hint"><summary>🏆 太空知识闯关（不重复版）</summary><pre>while lives &gt; 0 and len(questions) &gt; 0:
    i = random.randint(0, len(questions) - 1)
    q = questions.pop(i)
    a = answers.pop(i)
    answer = input(q + " ")
    if answer == a:
        score += 1
        print(f"✅ 对！{score} 分")
    else:
        lives -= 1
        print(f"❌ 答案是 {a}，还剩 {lives} 条命")

if lives &gt; 0:
    print(f"🏆 通关！{score} 分")
else:
    print(f"💥 没命了，{score} 分")</pre>简单版：<code>while lives &gt; 0 and score &lt; 5:</code>，不 pop，直接用 <code>questions[i]</code> / <code>answers[i]</code>（会重复出题）。<br>题目里的太空知识（水星最近、木星最大、8 颗行星、火星是红色星球、土星光环最大最亮）都是公认事实。</details>
<details class="hint"><summary>作业 🥉 + 🥈：6 种动物 + 打分</summary><pre>while again == "yes":
    fur = input("它有毛吗？")
    fly = input("它会飞吗？")
    water = input("它住在水里吗？")
    bark = input("它会汪汪叫吗？")
    swim = input("它会游泳吗？")

    if fur == "no" and fly == "no" and swim == "yes":
        print("🐧 是企鹅 penguin？")
    elif water == "yes":
        print("🦈 是鲨鱼 shark？")
    elif fur == "yes" and bark == "yes":
        print("🐶 是狗 dog？")
    elif fur == "yes" and fly == "no":
        print("🐱 是猫 cat？")
    elif fur == "yes" and fly == "yes":
        print("🦇 是蝙蝠 bat？")
    elif fur == "no" and fly == "yes":
        print("🐦 是 tūī？")
    elif fur == "no" and fly == "no":
        print("🥝 是奇异鸟 kiwi？")
    else:
        print("🤷 我不知道")

    ok = input("我猜对了吗？(yes/no) ")
    rounds += 1
    if ok == "yes":
        right += 1
    again = input("再玩一次？")

print(f"规则 AI 猜对了 {right} / {rounds} 局")
if right == rounds:
    print("🏆 完美侦探")</pre>孩子的问题和顺序可以完全不同，只要 6 种动物都能猜对就算过。企鹅放最前面是因为孩子可能对「住在水里吗」答 yes。</details>
<details class="hint"><summary>作业 🥇：问题树（聪明侦探）</summary><pre>asked = 0
fur = input("它有毛吗？")
asked += 1
if fur == "yes":
    bark = input("它会汪汪叫吗？")
    asked += 1
    if bark == "yes":
        print("🐶 狗")
    else:
        fly = input("它会飞吗？")
        asked += 1
        if fly == "yes":
            print("🦇 蝙蝠")
        else:
            print("🐱 猫")
else:
    water = input("它住在水里吗？")
    asked += 1
    if water == "yes":
        print("🦈 鲨鱼")
    else:
        fly = input("它会飞吗？")
        asked += 1
        if fly == "yes":
            print("🐦 tūī")
        else:
            swim = input("它会游泳吗？")
            asked += 1
            if swim == "yes":
                print("🐧 企鹅")
            else:
                print("🥝 奇异鸟")
print(f"这次只问了 {asked} 个问题")</pre>可以和孩子聊：这棵「问题树」就是「决策树」，一种真正的机器学习方法会自己从例子里长出这样的树（只点到为止）。</details>

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 死循环时他做了什么？几秒钟找到 ■？ | |
| 他能说出「什么时候条件变 False」吗？ |
| n − 3 的猜一猜：他是在纸上跟踪的，还是猜的？ |
| 猜数字 2.0：他能说出「循环停了有两个原因」吗？ | |
| 不插电：企鹅 / 蝙蝠出来时他怎么改规则？ | |
| 他用自己的话怎么说「规则 vs 从数据学」？（原话记下来，第 12 课回顾用） | |
| Teachable Machine 坏模型学到了什么「规律」？他猜的是？ | |
| 下节课要复习什么？ | |
