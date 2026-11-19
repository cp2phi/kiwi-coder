---
title: 第 7 课 · 教案
title_en: Lesson 7 · Teacher plan
lesson: "07"
tab: teacher
---

# 👩‍🏫 第 7 课教案：把代码打包（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子能**照着一句说明自己写出**带参数、会 return 的函数，并在循环和 if 里使用它；能说出「def 是教，调用是表演」「参数是递进去的东西」「return 是交回来」「函数里的变量是它自己的」。进阶：默认值、招式里喊招式、交回列表。

**今天的铁律：** 这是第二阶段「一起做」的第 3 课。今天 `___` 很少，大部分是 ✍️「照说明自己写」——老师**不碰键盘**；孩子卡住先问「小词典里有没有？」再让他看 💡 提示。今天的两个核心感受：「**改一处，全部都变**」和「**大问题 = 小招式拼起来**」。

<div class="box box-tip"><span class="box-title">📈 这一课比原版难了大约 30–40%</span>
老师反馈第 1–3 课偏简单，所以这一课：① 热身只有 1 个空 + 1 行要自己补；② 例 2 / 例 3 / 例 4 的改一改从「改数字」变成「照说明写一个招式」（<code>row</code>、<code>is_even</code>、<code>smallest</code>）；③ 新增两道<b>追踪题</b>（bigger 嵌套调用、boost 的本地变量）；④ 新增进阶例 5「发射控制中心」：交回 True / False 放进 if、默认值、交回列表；⑤ 小镇不再填空，<code>street(n, y)</code> 自己写；⑥ 挑战 5 条规则；作业 🥇 要设计「规划 + 绘制」两个函数。<br>
<b>如果孩子吃力</b>：见下面「时间不够 / 太难时怎么砍」——进阶例 5 和 smallest 是第一批可以砍的。
</div>

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-7">
  <li>自己把 <a href="../learn/">学一学</a> 从头跑一遍，特别是：热身少掉的那一行、例 4 的 5 行输出、scope 的 3 个数、例 5 的输出、例 6 自己写一次 street。</li>
  <li>先自己做一遍两道追踪题（bigger、boost），想好怎么用「先里面再外面」「两个不同的盒子」讲。</li>
  <li>打开 <a href="{{ '/games/robot/' | relative_url }}">💎 宝石机器人</a>，确认第 5 关以后确实需要函数（第 5–6 关的检查要求定义 grab_row / go）——今天课上不一定玩，作为回家选做。</li>
  <li>检查第 6 课作业是否已交（<a href="{{ '/gallery/' | relative_url }}">作品墙</a>），在 <a href="{{ '/feedback/' | relative_url }}">老师的话</a> 写好反馈——开课先花 2 分钟聊反馈。</li>
  <li>准备一句「生活中的函数」比喻：点餐（「大份、辣」是参数；不说就是「默认中份」= 默认值）、遥控器按钮（按一下表演一次）、发射前检查清单（每一项一个 True / False）。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>💌 反馈 + 热身</td><td>聊上周作业反馈（夸过程）。热身：要求写 <code>len(colours)</code> 而不是 5，再自己发现少了 <code>count += 1</code>。问：「不补会怎样？」</td><td>能不能自己找出少的那一行？会用 len 吗？</td></tr>
<tr><td><b>5–15</b></td><td>✨ def + 参数</td><td>先讲比喻。<b>先做猜一猜</b>：画几个正方形？运行例 1。关键一问：「def 那几行运行的时候海龟动了吗？」<br>改一改：for 5 次 + 自己算 72 度；<b>只改 def 里的 80</b>——大声说「改一处，全变」。<br>例 2：目标「一个比一个大」——让他自己发现要换成 <code>for i in range(len(colours))</code>。</td><td>他能分清「教」和「喊」吗？会不会忘记冒号 / 缩进？例 2 是自己想到用 i，还是要看提示 2？</td></tr>
<tr><td><b>15–28</b></td><td>🏘️ 街 + return + 追踪</td><td>例 3：做 x 的猜一猜 → 运行 → 加 colour 参数 → ✍️ 自己写 <code>row(y, n)</code>（招式里喊招式）。<br>例 4：<b>先做 bigger 的猜一猜</b>，再在纸上写 5 行输出，运行对答案。✍️ <code>is_even</code>（必做），<code>smallest</code>（时间够再做）。<br>boost 追踪题：先猜再运行，讲「两个不同的盒子」。</td><td>return 和 print 分得清吗？嵌套调用能「先里面再外面」吗？</td></tr>
<tr><td><b>28–38</b></td><td>🚀 发射控制中心（进阶）</td><td>读 code-walk 的 3 行，做 <code>countdown()</code> 默认值的猜一猜。运行。改 wind / fuel 让发射推迟（两个不同原因）。✍️ <code>crew_ok</code> 加进 go_for_launch。<code>step=1</code> 留给能力强时做。</td><td>他是否理解「交回 True / False 就能放进 if」？加参数时记得两头都加吗？</td></tr>
<tr><td><b>38–52</b></td><td>🏙️ 火箭小镇 + 挑战</td><td>例 6：<b>没有填空</b>，照说明写 street。看 rocket 的 <code>size=120</code> 默认值。然后挑战：5 条规则。<b>老师手放背后</b>，只问「这个东西能不能变成一个招式？」「哪个招式会交回东西？」</td><td>他会主动把重复代码变函数吗？参数命名有意义吗？5 条规则做到几条？</td></tr>
<tr><td><b>52–56</b></td><td>🤖 和 AI 一起</td><td>把挑战里重复最多的几行贴给 AI，用页面上的问法（含「默认值」）。贴回来运行——跑得起来吗？找一行看不懂的追问。</td><td>他会检验 AI 的代码还是直接信？</td></tr>
<tr><td><b>56–60</b></td><td>📓 收尾</td><td>作品存到作品墙。笔记本 3 行。看作业页：🥉 是屋顶 + random_colour + street（4 个 TODO）。宝石机器人回家选做。预告下周迷你项目。</td><td>能用自己的话说出 def / 参数 / return / 默认值吗？</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够 / 太难时怎么砍</span>
优先级：<b>例 1 + 改一改</b> &gt; <b>例 2 参数</b> &gt; <b>例 3 + row</b> &gt; <b>例 4 return + is_even</b> &gt; boost 追踪题 &gt; 例 6 小镇（自己写 street）&gt; 挑战 &gt; 例 5 发射控制 &gt; smallest &gt; AI。<br>
<b>孩子吃力时：</b>① 例 5 整个跳过（默认值作业 🥈 会再遇到，第 8 课 judge() 也会用到 return True/False 的思路）；② smallest、step=1、crew_ok 都是可选；③ 例 6 的 street 允许先看提示 1 和 2；④ 挑战规则降到 3 条（≥3 个招式、≥1 个参数、for 循环）。<br>
<b>孩子很快时：</b>让他把例 4 的 smallest 用「招式里喊招式」写第二种方法；挑战里加一个交回列表的招式（比如 <code>star_positions(n)</code> 交回 n 个随机坐标）。
</div>

---

## 🗣️ 好用的话术

- 「这几行是在<b>教</b>还是在<b>喊</b>？」（每次看到 def 和调用都问）
- 「你改了一个数字，几个正方形变了？为什么？」
- 「这个东西你画了几遍？能不能变成一个招式？」
- 「return 交回来的东西去哪了？你看得见吗？」
- 「先算里面的，再算外面的——里面那个交回了什么？」（嵌套调用）
- 「函数里的 fuel 和外面的 fuel 是同一个盒子吗？」
- 「参数要两头加：def 那头加了，喊的那头加了吗？」
- 「不递这个参数的时候，你希望它是多少？那就是默认值。」

## 🐞 常见卡点和应对

| 卡点 | 表现 | 怎么办 |
|---|---|---|
| 忘记冒号 | `SyntaxError` 在 def 那行 | 让他读报错，画板会提示「最后要有冒号」 |
| 缩进不一致 | `IndentationError` | 问「哪几行属于这个招式？」让他用 4 个空格对齐 |
| 教了没喊 | 运行什么都没画 | 「你教了它，喊了吗？」 |
| 参数数量不对 | `TypeError: ... missing` | 「def 要几个？你给了几个？」 |
| 以为 return 会显示 | 「怎么没东西？」 | 加 print 包住：`print(double(5))` |
| return 后面还写代码 | 那几行永远不跑 | 「return 之后招式就结束了」 |
| 在函数外用函数里的变量 | `NameError` | 回到 boost 追踪题那句话 |
| 默认值写在前面 | `def f(size=50, x):` 报 SyntaxError | 「有默认值的参数要排在最后」 |
| street 里忘了喊 house | 什么都没画 | 「street 自己会画吗？它要喊谁？」 |

---

## ✅ 参考答案

<details class="hint"><summary>热身 warmup.py</summary><pre>while count &lt; len(colours):
    t.color(colours[count])
    t.circle(30 + count * 15)
    count = count + 1      # 少掉的那一行（count += 1 也对）</pre></details>

<details class="hint"><summary>例 1 改一改 / 例 2 一个比一个大</summary><pre>for i in range(5):
    square()
    t.left(72)             # 360 ÷ 5

# 例 2
for i in range(len(colours)):
    square(30 + i * 10, colours[i])
    t.penup()
    t.forward(80 + i * 10)   # 只写 forward(80) 后面的会重叠一点，也可以接受
    t.pendown()</pre></details>

<details class="hint"><summary>例 3 row(y, n)</summary><pre>def row(y, n):
    for i in range(n):
        house(-250 + i * 120, y, 80)

row(-150, 5)
row(20, 3)</pre></details>

<details class="hint"><summary>例 4 输出 + is_even + smallest</summary><pre>10
120
True
80 不大 / 80 is not big
12 14

def is_even(n):
    return n % 2 == 0          # 写成 if … return True else return False 也对

# 方法 1
def smallest(a, b, c):
    if a &lt;= b and a &lt;= c:
        return a
    if b &lt;= c:
        return b
    return c

# 方法 2：招式里喊招式
def smaller(a, b):
    if a &lt; b:
        return a
    return b

def smallest(a, b, c):
    return smaller(smaller(a, b), c)
# 测试：2 3 1</pre></details>

<details class="hint"><summary>boost 追踪题</summary>fuel: 3、x: 7、y: 15。<code>boost(3)</code>：里面的 fuel = 6，交回 7；<code>boost(7)</code>：14 + 1 = 15。外面的 fuel 没变。</details>

<details class="hint"><summary>例 5 发射控制中心</summary><pre>输出：True / False / [3, 2, 1] / 10 / 5 ... 到 1 ... / 🚀 点火！
推迟：wind = 30 或更大；或 fuel = 89 或更小。

def crew_ok(crew):
    return crew &gt;= 1 and crew &lt;= 4

def go_for_launch(fuel, wind, crew):
    return fuel_ok(fuel) and wind_ok(wind) and crew_ok(crew)
# 下面喊的地方：go_for_launch(95, 12, 4) 等，都要多递一个数

def countdown(start=10, step=1):
    numbers = []
    n = start
    while n &gt; 0:
        numbers.append(n)
        n -= step
    return numbers
# countdown(10, 2) → [10, 8, 6, 4, 2]；countdown(3) → [3, 2, 1]</pre></details>

<details class="hint"><summary>例 6 火箭小镇 street</summary><pre>def street(n, y):
    for i in range(n):
        house(-280 + i * 100, y, 70, colours[i % len(colours)])

street(4, -150)
street(3, 0)</pre></details>

<details class="hint"><summary>作业 🥉🥈🥇 完整参考</summary><pre>colours = ["tomato", "gold", "lightgreen", "skyblue", "plum"]

def house(x, y, size, colour):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    # 🥉 屋顶
    t.penup()
    t.goto(x, y + size)
    t.pendown()
    t.fillcolor("firebrick")
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def random_colour():                      # 🥉
    return random.choice(colours)

def street(n, y):                         # 🥉
    for i in range(n):
        house(-280 + i * 130, y, 90, random_colour())

def rocket(x, y, size=80):                # 🥈 机身 + 机头（尾翼见学一学例 6）
    w = size / 3
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y + size)
    t.goto(x, y + size)
    t.goto(x, y)
    t.end_fill()
    t.penup()
    t.goto(x, y + size)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.goto(x + w, y + size)
    t.goto(x + w / 2, y + size + w)
    t.goto(x, y + size)
    t.end_fill()

def sky(is_night):                        # 🥈
    if is_night:
        turtle.bgcolor("midnightblue")
        t.penup()
        t.goto(220, 200)
        t.dot(60, "lightyellow")
        for i in range(20):
            t.goto(random.randint(-300, 300), random.randint(50, 280))
            t.dot(4, "white")
    else:
        turtle.bgcolor("skyblue")
        t.penup()
        t.goto(220, 200)
        t.dot(70, "gold")

def tree(x, y):                           # 🥇 用到（可抄学一学例 6）
    t.penup()
    t.goto(x + 20, y)
    t.pendown()
    t.color("saddlebrown")
    t.left(90)
    t.forward(40)
    t.right(90)
    t.color("green")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.color("black")

def plan_city(n):                         # 🥇
    plan = []
    rockets = 0
    for i in range(n):
        building = random.choice(["house", "tree", "rocket"])
        if building == "rocket" and rockets == 1:
            building = "house"
        if building == "rocket":
            rockets += 1
        plan.append(building)
    return plan

def draw_city(plan):                      # 🥇
    x = -300
    for building in plan:
        if building == "house":
            house(x, -150, 70, random_colour())
        elif building == "tree":
            tree(x, -150)
        elif building == "rocket":
            rocket(x + 20, -150)
        x = x + 100

sky(True)
street(4, 0)
plan = plan_city(6)
print(plan)
draw_city(plan)</pre>
🥇 的评价重点不是画得多好看，而是：plan_city 真的<b>交回</b>列表（不是在里面直接画）、draw_city 用 if / elif 分派、「最多 1 个火箭」的规则运行 5 次都成立。</details>

---

## 📝 观察记录

| 问题 | 记录 |
|---|---|
| 能不能照一句说明自己写出函数（row / is_even / street）？ | |
| 两道追踪题（bigger、boost）猜对了吗？ | |
| 进阶例 5 做到哪里？默认值听懂了吗？ | |
| 今天的报错他第一反应是什么（读 / 问 / 乱改）？ | |
| AI 的代码他检验了吗？ | |
| 难度感受：太难 / 刚好 / 还能更难？ | |
| 作业等级预估（🥉🥈🥇） | |
