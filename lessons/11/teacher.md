---
title: 第 11 课 · 教案
title_en: Lesson 11 · Teacher plan
lesson: "11"
tab: teacher
---

# 👩‍🏫 第 11 课教案（给老师 / 家长）

<p class="en box box-tip">This page is for the teacher and is in Chinese only.</p>

**目标：** 孩子把第 10 课的计划做成**能跑的 v1**，并且在过程中**自己**用四招排错。今天没有新语法，有的是「独立」。

**今天的铁律：顾问模式。** 老师**不碰键盘、不给代码、不说「应该这样写」**。只做三件事：反问、指方向（去看第几课 / 词典 / 笔记本）、在他真的卡死 5 分钟以上时给「下一个最小步骤」。

<div class="box box-rule"><b>只许问的三句话：</b>「报错说了什么？」「你觉得是哪一行？」「你怎么验证你的猜想？」——三句话轮着问，大多数 bug 他自己能找到。</div>

---

## 📋 课前准备

<ul class="quests" data-key="teacher-prep-11">
  <li>打开作品墙，确认 <code>week10-plan</code> 在那里；读一遍他的计划，心里把功能 1/2/3 按「最小可跑」重新排序（上课时不要替他排，用问题引导）。</li>
  <li>自己把 <a href="../learn/">学一学</a> 的 4 个排错例子和 3 个事件例子跑一遍（约 10 分钟）。键盘例子记得<b>先点画布</b>。</li>
  <li>看一遍下面「参考答案」里他选的那种项目的功能 1 怎么写——不是为了给他，而是为了知道他离「能跑」还有几步。</li>
  <li>准备一只小黄鸭（或任何玩偶）放在桌上，真的有用。</li>
  <li>计时器：每 15 分钟响一次 = 存档时间。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–5</b></td><td>🔁 热身</td><td>三个 bug。让他<b>读出红框</b>再动手。「电脑一次只报一个错」这句话让他自己说出来。</td><td>他看到红字的第一反应是读还是乱改？</td></tr>
<tr><td><b>5–15</b></td><td>🧰 四招</td><td>每招 2 分钟：print 侦探让他自己加 print 看 total；读报错用那张表；小黄鸭真的念出来（你当鸭子，只点头）；二分法真的注释掉一半。</td><td>哪一招他最喜欢？以后卡住就先提醒那一招。</td></tr>
<tr><td><b>15–22</b></td><td>⌨️ 事件</td><td>只跑方向键和掉落星星两个例子（点击的留给他自己玩）。重点一句：「<b>函数名不加括号</b> = 把函数交给屏幕等着用」。做猜一猜。</td><td>他能说出 tick() 为什么会一直跑吗？</td></tr>
<tr><td><b>22–55</b></td><td>🏗️ 制作</td><td><b>40 分钟（含存档）。</b>按开工清单：计划 → 骨架贴进作业画板 → 功能 1 → 测 → 存 → 功能 2 …<br>你坐在旁边做自己的事（真的），每 10 分钟问一句「现在在做哪个功能？」。<br>15、30、45 分钟各存一次。</td><td>见下面的「卡住了的教练脚本」。记录他每个功能花了多久。</td></tr>
<tr><td><b>55–60</b></td><td>📓 收尾</td><td>存最后一版。笔记本 3 行（最难的 bug 一定要写）。看一眼作业页：这周作业就是把它做完 + 找真人来玩。</td><td>他能用自己的话说出今天用了哪一招排错吗？</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>功能 1 能跑并存档</b> &gt; 四招里的 print 侦探 + 读报错 &gt; 方向键例子 &gt; 其他。四招可以只讲两招，剩下的作业周自己看。宁可功能 1 做得很小很丑，也要有「从头运行没有红字」的那一刻。
</div>

---

## 🧑‍🏫 卡住了的教练脚本（卡住 &gt; 5 分钟才用）

1. **「停一下，告诉我你现在想让它做什么？」**（一句话）
2. **「它现在实际做了什么？」**（让他指着屏幕说）
3. **「这两件事之间，差在哪一行？」** → 不知道 → **「用哪一招能知道？」**（print 侦探 / 二分法）
4. 还不行 → 给**下一个最小步骤**，不给代码：「先让它打印出 x 的值」「先只做按 → 往右」「把这个功能先注释掉，让其他的跑起来」。
5. 真的是知识缺口（比如不知道 global）→ **指方向**：「第 11 课的小魔法那一段」「词典第 7 课」。让他自己读。
6. 最后手段：你在**另一个**画板里写一个 3 行的、**和他的问题不同但同类**的例子，让他看了自己迁移。

**不要做的：** 接过鼠标；说「应该是 ==」；一口气指出三个问题。一次一个。

## 🗣️ 好用的话术

- 「你猜它会打印什么？」（运行前）
- 「这个红字里，哪个词你认识？」
- 「刚才那一招叫什么？写进笔记本。」
- 「存了吗？」（每 15 分钟）
- 夸过程：「你刚才是自己用 print 找到的，这就是程序员的做法。」

## 🏁 什么叫「做完了」（给孩子的标准，也给你）

- 从「↺ 还原」后的空白开始，粘贴最新版，**运行一次没有红字**
- 计划里的 3 个功能，每个都能演示一下
- `test()` 打印 ✅
- 作品墙上有 `week11-project`
- 笔记本有「最难的 bug」

没做完也算：**能跑的 1 个功能 + 存档了** 就是本周的及格线。作业周补剩下的。

---

## 🔑 参考答案（功能 1 示例，只给老师看）

<details class="hint"><summary>🎮 游戏骨架：功能 1「海龟能左右动」</summary>
<pre>import turtle
screen = turtle.Screen()
player = turtle.Turtle()
player.shape("turtle")
player.penup()
player.goto(0, -250)
player.speed(0)

def left():
    player.setx(player.xcor() - 20)

def right():
    player.setx(player.xcor() + 20)

screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()</pre>
常见坑：忘了 <code>listen()</code>；函数名后加了括号；没 <code>penup()</code> 所以留下线；运行后没点画布。
</details>

<details class="hint"><summary>📱 App 骨架：功能 1「问一个问题并判断对错」</summary>
<pre>questions = {"kia ora": "你好", "whānau": "家人"}
score = 0
for word in questions:
    answer = input(f"{word} 是什么意思？")
    if answer.strip() == questions[word]:
        print("对了！")
        score = score + 1
    else:
        print("不对，是", questions[word])
print("得分", score)

def test():
    assert questions["kia ora"] == "你好"
    print("✅ 测试通过")
test()</pre>
常见坑：<code>input</code> 返回的是文字，比较数字要 <code>int()</code>；<code>.strip()</code> 去空格；字典的键拼错 → KeyError。
</details>

<details class="hint"><summary>🎨 互动艺术骨架：功能 1「点哪里画一朵花」</summary>
<pre>import turtle, random
screen = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.speed(0)

def flower(x, y):
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(["red", "gold", "violet"]))
    for i in range(6):
        t.circle(20)
        t.left(60)
    t.penup()

screen.onclick(flower)</pre>
常见坑：<code>onclick</code> 的函数必须接 <code>x, y</code> 两个参数；忘了 <code>penup()</code> 会从上一朵拖线过来。
</details>

<details class="hint"><summary>🧮 记分：UnboundLocalError</summary>
函数里写 <code>score = score + 1</code> 会报 <code>UnboundLocalError</code>（网页画板可能显示为 NameError）。解法：函数第一行 <code>global score</code>。这是本周最常见的 bug，让他自己从第 11 课「小魔法」找到。
</details>

---

## 📝 观察记录

| 项目 | 记录 |
|---|---|
| 功能 1 / 2 / 3 各花了几分钟 | |
| 他自己用了哪几招排错 | |
| 卡住最久的 bug 是什么、谁解决的 | |
| 我忍住没给代码的次数 😄 | |
| 下周展示前还差什么 | |
